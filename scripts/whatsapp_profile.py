#!/usr/bin/env python3

import argparse
import os
import re
import socket
import sys
from pathlib import Path


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
    try:
        target.mkdir(mode=0o700)
    except FileExistsError as error:
        raise ProfileError(f"Profile already exists: {name}") from error
    return target


def select_profile(
    bridge_dir: Path, name: str, bridge_running=port_8080_in_use
) -> Path:
    if bridge_running():
        raise ProfileError("Stop the WhatsApp bridge before switching profiles")
    target = profile_path(bridge_dir, name)
    if not target.is_dir():
        raise ProfileError(f"Unknown profile: {name}")
    write_active_profile(bridge_dir, name)
    return target


def migrate_legacy_store(
    bridge_dir: Path, name: str, bridge_running=port_8080_in_use
) -> Path:
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
    target.chmod(0o700)
    write_active_profile(bridge_dir, name)
    return target


def current_profile(bridge_dir: Path) -> str:
    active_file = bridge_dir / ".active-profile"
    try:
        name = active_file.read_text(encoding="utf-8").strip()
    except FileNotFoundError as error:
        raise ProfileError("No active profile selected") from error
    target = profile_path(bridge_dir, name)
    if not target.is_dir():
        raise ProfileError(f"Active profile does not exist: {name}")
    return name


def list_profiles(bridge_dir: Path) -> list[str]:
    profiles_dir = bridge_dir / "profiles"
    if not profiles_dir.is_dir():
        return []
    return sorted(path.name for path in profiles_dir.iterdir() if path.is_dir())


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage local WhatsApp profiles")
    subcommands = parser.add_subparsers(dest="command", required=True)
    for command in ("create", "use", "migrate"):
        command_parser = subcommands.add_parser(command)
        command_parser.add_argument("name")
    subcommands.add_parser("current")
    subcommands.add_parser("list")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    bridge_dir = Path(__file__).resolve().parents[1] / "whatsapp-bridge"
    try:
        if args.command == "create":
            path = create_profile(bridge_dir, args.name)
            print(f"Created profile {args.name}: {path}")
        elif args.command == "use":
            select_profile(bridge_dir, args.name)
            print(f"Active profile: {args.name}")
        elif args.command == "migrate":
            path = migrate_legacy_store(bridge_dir, args.name)
            print(f"Migrated legacy store to profile {args.name}: {path}")
        elif args.command == "current":
            print(current_profile(bridge_dir))
        else:
            active = None
            try:
                active = current_profile(bridge_dir)
            except ProfileError:
                pass
            for name in list_profiles(bridge_dir):
                marker = "*" if name == active else " "
                print(f"{marker} {name}")
    except (OSError, ProfileError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
