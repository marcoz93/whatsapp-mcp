import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


BRIDGE_DIR = Path(__file__).resolve().parent.parent / "whatsapp-bridge"
PROFILE_RE = re.compile(r"^[a-z0-9][a-z0-9_-]*$")


class ProfileError(RuntimeError):
    pass


class ProfileMismatch(ProfileError):
    pass


@dataclass(frozen=True)
class ActiveProfile:
    name: str
    store_dir: Path

    @property
    def messages_db(self) -> Path:
        return self.store_dir / "messages.db"


def load_active_profile(bridge_dir: Path = BRIDGE_DIR) -> ActiveProfile:
    active_file = bridge_dir / ".active-profile"
    try:
        name = active_file.read_text(encoding="utf-8").strip()
    except FileNotFoundError as error:
        raise ProfileError("No active WhatsApp profile selected") from error
    if not PROFILE_RE.fullmatch(name):
        raise ProfileError(f"Invalid active profile: {name!r}")

    store_dir = bridge_dir / "profiles" / name
    if not store_dir.is_dir():
        raise ProfileError(f"Active profile does not exist: {name}")
    return ActiveProfile(name=name, store_dir=store_dir)


def profiled(profile: str, data: Any) -> dict[str, Any]:
    return {"account_profile": profile, "data": data}


def require_expected_profile(expected: str, active: str) -> None:
    if not expected:
        raise ProfileMismatch(
            f"expected_profile is required; active profile is {active!r}"
        )
    if expected != active:
        raise ProfileMismatch(
            f"Expected profile {expected!r}, active profile is {active!r}"
        )
