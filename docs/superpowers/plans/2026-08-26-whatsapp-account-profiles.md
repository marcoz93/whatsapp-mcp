# WhatsApp Account Profiles Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Keep multiple WhatsApp accounts in isolated local profiles while exposing exactly one identified account to the bridge and MCP at a time.

**Architecture:** A stdlib Python selector owns the single `.active-profile` file and migrates or selects profile directories. Go and Python independently validate that file, derive their database paths from it, identify every MCP result, and reject sends whose `expected_profile` differs from the active profile.

**Tech Stack:** Go 1.26, Python 3.11 stdlib, FastMCP, SQLite, `unittest`, Go `testing`.

---

## File map

- Create `scripts/whatsapp_profile.py`: local profile creation, migration, selection and inspection.
- Create `tests/test_whatsapp_profile.py`: selector behavior using temporary directories.
- Create `whatsapp-bridge/profile.go`: validated active-profile resolution for Go.
- Create `whatsapp-bridge/profile_test.go`: Go profile path and validation checks.
- Modify `whatsapp-bridge/main.go`: use the active profile for session, messages, media, account identity and send guard.
- Create `whatsapp-mcp-server/profile.py`: validated active-profile resolution for Python.
- Create `whatsapp-mcp-server/test_profile.py`: MCP-side profile resolution and response checks.
- Modify `whatsapp-mcp-server/whatsapp.py`: dynamic database path, account endpoint and expected-profile payloads.
- Modify `whatsapp-mcp-server/main.py`: active-account tool, profile envelope and required send guard.
- Modify `.gitignore`: exclude all local profile state.
- Modify `README.md`: document profile operation and recovery.

### Task 1: Profile selector

**Files:**
- Create: `scripts/whatsapp_profile.py`
- Create: `tests/test_whatsapp_profile.py`

- [ ] **Step 1: Write failing selector tests**

Cover invalid names, explicit creation, selection without silent creation, refusal while port `8080` is active, and migration of the legacy `store` directory:

```python
class ProfileTests(unittest.TestCase):
    def test_create_and_select(self):
        root = Path(self.temp_dir.name)
        create_profile(root, "pessoal")
        select_profile(root, "pessoal", bridge_running=lambda: False)
        self.assertEqual((root / ".active-profile").read_text(), "pessoal\n")

    def test_select_rejects_unknown_profile(self):
        with self.assertRaises(ProfileError):
            select_profile(Path(self.temp_dir.name), "ausente", bridge_running=lambda: False)

    def test_migrate_moves_legacy_store(self):
        root = Path(self.temp_dir.name)
        (root / "store").mkdir()
        (root / "store" / "messages.db").write_bytes(b"db")
        migrate_legacy_store(root, "empresa", bridge_running=lambda: False)
        self.assertEqual((root / "profiles/empresa/messages.db").read_bytes(), b"db")
        self.assertFalse((root / "store").exists())
```

- [ ] **Step 2: Run tests and verify failure**

Run: `python3 -m unittest tests/test_whatsapp_profile.py -v`

Expected: import failure because `scripts.whatsapp_profile` does not exist.

- [ ] **Step 3: Implement the stdlib selector**

Implement these stable entry points:

```python
PROFILE_RE = re.compile(r"^[a-z0-9][a-z0-9_-]*$")

class ProfileError(RuntimeError):
    pass

def profile_path(bridge_dir: Path, name: str) -> Path:
    if not PROFILE_RE.fullmatch(name):
        raise ProfileError(f"Invalid profile name: {name!r}")
    return bridge_dir / "profiles" / name

def port_8080_in_use() -> bool:
    with socket.socket() as sock:
        return sock.connect_ex(("127.0.0.1", 8080)) == 0

def write_active_profile(bridge_dir: Path, name: str) -> None:
    temporary = bridge_dir / ".active-profile.tmp"
    temporary.write_text(f"{name}\n", encoding="utf-8")
    temporary.chmod(0o600)
    os.replace(temporary, bridge_dir / ".active-profile")

def create_profile(bridge_dir: Path, name: str) -> Path:
    target = profile_path(bridge_dir, name)
    target.parent.mkdir(mode=0o700, exist_ok=True)
    target.mkdir(mode=0o700)
    return target

def select_profile(bridge_dir: Path, name: str, bridge_running=port_8080_in_use) -> Path:
    if bridge_running():
        raise ProfileError("Stop the WhatsApp bridge before switching profiles")
    target = profile_path(bridge_dir, name)
    if not target.is_dir():
        raise ProfileError(f"Unknown profile: {name}")
    write_active_profile(bridge_dir, name)
    return target

def migrate_legacy_store(bridge_dir: Path, name: str, bridge_running=port_8080_in_use) -> Path:
    if bridge_running():
        raise ProfileError("Stop the WhatsApp bridge before migrating")
    legacy = bridge_dir / "store"
    if not legacy.is_dir():
        raise ProfileError("Legacy store does not exist")
    target = profile_path(bridge_dir, name)
    target.parent.mkdir(mode=0o700, exist_ok=True)
    if target.exists():
        raise ProfileError(f"Profile already exists: {name}")
    legacy.rename(target)
    write_active_profile(bridge_dir, name)
    return target

def current_profile(bridge_dir: Path) -> str:
    name = (bridge_dir / ".active-profile").read_text(encoding="utf-8").strip()
    profile_path(bridge_dir, name)
    return name
```

Use `Path.mkdir(mode=0o700)`, write `.active-profile` through a temporary sibling followed by `os.replace`, refuse unknown profiles, and provide `create`, `use`, `current`, `list`, and `migrate` argparse commands. Resolve `bridge_dir` as `<repo>/whatsapp-bridge` in the CLI.

- [ ] **Step 4: Run selector tests**

Run: `python3 -m unittest tests/test_whatsapp_profile.py -v`

Expected: all selector tests pass.

- [ ] **Step 5: Commit selector**

```bash
git add scripts/whatsapp_profile.py tests/test_whatsapp_profile.py
git commit -m "Add WhatsApp profile selector"
```

### Task 2: Profile-aware Go storage

**Files:**
- Create: `whatsapp-bridge/profile.go`
- Create: `whatsapp-bridge/profile_test.go`
- Modify: `whatsapp-bridge/main.go`

- [ ] **Step 1: Write failing Go tests**

```go
func TestLoadActiveProfile(t *testing.T) {
    dir := t.TempDir()
    os.MkdirAll(filepath.Join(dir, "profiles", "empresa"), 0700)
    os.WriteFile(filepath.Join(dir, ".active-profile"), []byte("empresa\n"), 0600)
    profile, err := loadActiveProfile(dir)
    if err != nil || profile.Name != "empresa" {
        t.Fatalf("profile=%+v err=%v", profile, err)
    }
}

func TestLoadActiveProfileRejectsTraversal(t *testing.T) {
    dir := t.TempDir()
    os.WriteFile(filepath.Join(dir, ".active-profile"), []byte("../empresa\n"), 0600)
    if _, err := loadActiveProfile(dir); err == nil {
        t.Fatal("expected invalid profile error")
    }
}
```

- [ ] **Step 2: Run tests and verify failure**

Run: `cd whatsapp-bridge && go test ./...`

Expected: compilation fails because `loadActiveProfile` is undefined.

- [ ] **Step 3: Implement profile resolution**

Create:

```go
type AccountProfile struct {
    Name     string
    StoreDir string
}

var profileNamePattern = regexp.MustCompile(`^[a-z0-9][a-z0-9_-]*$`)

func loadActiveProfile(bridgeDir string) (AccountProfile, error) {
    raw, err := os.ReadFile(filepath.Join(bridgeDir, ".active-profile"))
    if err != nil {
        return AccountProfile{}, fmt.Errorf("read active profile: %w", err)
    }
    name := strings.TrimSpace(string(raw))
    if !profileNamePattern.MatchString(name) {
        return AccountProfile{}, fmt.Errorf("invalid active profile %q", name)
    }
    storeDir, err := filepath.Abs(filepath.Join(bridgeDir, "profiles", name))
    if err != nil {
        return AccountProfile{}, fmt.Errorf("resolve profile path: %w", err)
    }
    info, err := os.Stat(storeDir)
    if err != nil || !info.IsDir() {
        return AccountProfile{}, fmt.Errorf("profile directory does not exist: %s", name)
    }
    return AccountProfile{Name: name, StoreDir: storeDir}, nil
}

func (p AccountProfile) SessionDB() string { return filepath.Join(p.StoreDir, "whatsapp.db") }
func (p AccountProfile) MessagesDB() string { return filepath.Join(p.StoreDir, "messages.db") }
```

Trim the file, validate with `^[a-z0-9][a-z0-9_-]*$`, require the selected directory to exist, and return absolute paths.

- [ ] **Step 4: Route session, message and media storage through the profile**

Change `NewMessageStore()` to `NewMessageStore(storeDir string)`, add `storeDir string` to `MessageStore`, replace both hardcoded SQLite paths, and replace the hardcoded media directory with `filepath.Join(messageStore.storeDir, strings.ReplaceAll(chatJID, ":", "_"))`. In `main`, load the profile before opening either database and log the active profile name.

- [ ] **Step 5: Run and format Go tests**

Run: `cd whatsapp-bridge && gofmt -w profile.go profile_test.go main.go && go test ./...`

Expected: all Go tests pass.

- [ ] **Step 6: Commit Go isolation**

```bash
git add whatsapp-bridge/main.go whatsapp-bridge/profile.go whatsapp-bridge/profile_test.go
git commit -m "Isolate WhatsApp bridge storage by profile"
```

### Task 3: Identity and send protection across REST and MCP

**Files:**
- Modify: `whatsapp-bridge/main.go`
- Create: `whatsapp-mcp-server/profile.py`
- Create: `whatsapp-mcp-server/test_profile.py`
- Modify: `whatsapp-mcp-server/whatsapp.py`
- Modify: `whatsapp-mcp-server/main.py`

- [ ] **Step 1: Write profile and send-guard tests**

Python tests must assert that active-profile resolution returns the selected `messages.db`, response envelopes include `account_profile`, and a mismatched expected profile is rejected before HTTP is called:

```python
def test_profiled_result(self):
    self.assertEqual(profiled("empresa", ["x"]), {
        "account_profile": "empresa",
        "data": ["x"],
    })

def test_expected_profile_must_match(self):
    with self.assertRaises(ProfileMismatch):
        require_expected_profile("pessoal", "empresa")
```

Add a Go test for the bridge guard:

```go
func TestExpectedProfileMismatch(t *testing.T) {
    if err := validateExpectedProfile("pessoal", "empresa"); err == nil {
        t.Fatal("expected mismatch")
    }
}
```

- [ ] **Step 2: Run tests and verify failure**

Run: `python3 -m unittest discover -s whatsapp-mcp-server -p 'test_*.py' -v && (cd whatsapp-bridge && go test ./...)`

Expected: failures for missing profile helpers and guard.

- [ ] **Step 3: Add bridge identity and guard**

Extend `SendMessageRequest` with `ExpectedProfile string \`json:"expected_profile"\``. Before sending, require exact equality with the active profile and return HTTP `409 Conflict` on mismatch. Add `GET /api/account` returning the string fields `profile`, `jid`, `push_name`, and `business_name` from the selected profile and `client.Store`.

Pass `AccountProfile` into `startRESTServer` so the handler cannot infer a different profile.

- [ ] **Step 4: Make the MCP profile-aware**

In `profile.py`, read `whatsapp-bridge/.active-profile` with the same validation and derive `profiles/<name>/messages.db`. In `whatsapp.py`, replace `MESSAGES_DB_PATH` with `messages_db_path()` and add `get_active_account()` plus `expected_profile` to all three send payloads.

In `main.py`, add:

```python
class ProfileMismatch(ValueError):
    pass

def profiled(profile: str, data: Any) -> Dict[str, Any]:
    return {"account_profile": profile, "data": data}

def require_expected_profile(expected: str, active: str) -> None:
    if expected != active:
        raise ProfileMismatch(f"Expected profile {expected!r}, active profile is {active!r}")
```

Wrap every read/download result with `profiled`, expose `get_active_account`, and require `expected_profile` in `send_message`, `send_file`, and `send_audio_message`.

- [ ] **Step 5: Run both test suites**

Run: `python3 -m unittest discover -s whatsapp-mcp-server -p 'test_*.py' -v && (cd whatsapp-bridge && gofmt -w main.go profile.go profile_test.go && go test ./...)`

Expected: all Python and Go tests pass.

- [ ] **Step 6: Commit identity guard**

```bash
git add whatsapp-bridge whatsapp-mcp-server
git commit -m "Identify and guard the active WhatsApp profile"
```

### Task 4: Local-state protection and operator documentation

**Files:**
- Modify: `.gitignore`
- Modify: `README.md`

- [ ] **Step 1: Protect local profile data**

Add:

```gitignore
whatsapp-bridge/.active-profile
whatsapp-bridge/profiles/
whatsapp-bridge/store/
```

- [ ] **Step 2: Document commands and safety behavior**

Document `create`, `use`, `current`, `list`, and `migrate`; explain that only one profile syncs at a time, switching requires stopping bridge/MCP, reads identify the active profile, and sends require `expected_profile`.

- [ ] **Step 3: Run full static verification**

Run: `git diff --check && python3 -m unittest discover -s tests -v && python3 -m unittest discover -s whatsapp-mcp-server -p 'test_*.py' -v && (cd whatsapp-bridge && go test ./...)`

Expected: no whitespace errors and all tests pass.

- [ ] **Step 4: Commit docs and ignores**

```bash
git add .gitignore README.md
git commit -m "Document isolated WhatsApp profiles"
```

### Task 5: Reversible migration and second-account pairing

**Files:**
- Move local ignored data: `whatsapp-bridge/store/` → `whatsapp-bridge/profiles/empresa/`
- Create local ignored directory: `whatsapp-bridge/profiles/pessoal/`
- Create local ignored selector: `whatsapp-bridge/.active-profile`

- [ ] **Step 1: Stop the current bridge**

Send `SIGTERM` to the known `go run main.go` parent and compiled child, then verify `lsof whatsapp-bridge/store/whatsapp.db whatsapp-bridge/store/messages.db` returns no holders.

- [ ] **Step 2: Migrate the current account**

Run: `python3 scripts/whatsapp_profile.py migrate empresa`

Expected: `store` is moved, `.active-profile` contains `empresa`, and both databases retain their original sizes and SQLite integrity checks return `ok`.

- [ ] **Step 3: Prove the original profile still works**

Start the bridge with `cd whatsapp-bridge && go run .`, verify `GET /api/account` reports profile `empresa` and the existing JID without displaying a QR, then stop it normally.

- [ ] **Step 4: Create and select the second profile**

Run:

```bash
python3 scripts/whatsapp_profile.py create pessoal
python3 scripts/whatsapp_profile.py use pessoal
python3 scripts/whatsapp_profile.py current
```

Expected: current profile is `pessoal`; `empresa` remains unchanged.

- [ ] **Step 5: Start the new profile for pairing**

Run: `cd whatsapp-bridge && go run .`

Expected: a new QR is displayed. After scanning, `GET /api/account` reports profile `pessoal` and its own JID.

- [ ] **Step 6: Final verification and push**

Verify both profile databases with `PRAGMA integrity_check`, confirm `git status` contains no local profile files, run all tests, push the current branch, and record both commit IDs. Do not send a WhatsApp message as part of verification.
