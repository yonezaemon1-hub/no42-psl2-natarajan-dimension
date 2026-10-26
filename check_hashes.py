#!/usr/bin/env python3
"""Verify the exact packaged inventory, excluding only generated Python caches."""
import hashlib
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent
    manifest = root / "SHA256SUMS"
    listed = set()
    for line in manifest.read_text(encoding="utf-8").splitlines():
        digest, name = line.split("  ", 1)
        rel = Path(name)
        assert not rel.is_absolute() and ".." not in rel.parts
        assert name not in listed
        listed.add(name)
        path = root / rel
        assert path.is_file(), f"Missing: {name}"
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, f"Mismatch: {name}"
    actual = {p.relative_to(root).as_posix() for p in root.rglob("*")
              if p.is_file() and p != manifest and "__pycache__" not in p.parts}
    assert actual == listed, f"Inventory mismatch: {actual ^ listed}"
    print(f"PASS: {len(listed)} files, SHA-256 and exact inventory")


if __name__ == "__main__":
    main()
