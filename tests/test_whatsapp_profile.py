import tempfile
import unittest
from pathlib import Path

from scripts.whatsapp_profile import (
    ProfileError,
    create_profile,
    current_profile,
    migrate_legacy_store,
    select_profile,
)


class ProfileTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.bridge_dir = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_create_and_select_profile(self):
        created = create_profile(self.bridge_dir, "pessoal")
        selected = select_profile(
            self.bridge_dir, "pessoal", bridge_running=lambda: False
        )

        self.assertEqual(created, self.bridge_dir / "profiles" / "pessoal")
        self.assertEqual(selected, created)
        self.assertEqual(current_profile(self.bridge_dir), "pessoal")

    def test_invalid_profile_name_is_rejected(self):
        with self.assertRaisesRegex(ProfileError, "Invalid profile name"):
            create_profile(self.bridge_dir, "../empresa")

    def test_unknown_profile_is_not_created_by_selection(self):
        with self.assertRaisesRegex(ProfileError, "Unknown profile"):
            select_profile(
                self.bridge_dir, "ausente", bridge_running=lambda: False
            )

        self.assertFalse((self.bridge_dir / "profiles" / "ausente").exists())

    def test_selection_is_refused_while_bridge_is_running(self):
        create_profile(self.bridge_dir, "empresa")

        with self.assertRaisesRegex(ProfileError, "Stop the WhatsApp bridge"):
            select_profile(
                self.bridge_dir, "empresa", bridge_running=lambda: True
            )

    def test_migration_moves_legacy_store_and_selects_it(self):
        legacy = self.bridge_dir / "store"
        legacy.mkdir()
        (legacy / "messages.db").write_bytes(b"messages")
        (legacy / "whatsapp.db").write_bytes(b"session")

        target = migrate_legacy_store(
            self.bridge_dir, "empresa", bridge_running=lambda: False
        )

        self.assertFalse(legacy.exists())
        self.assertEqual((target / "messages.db").read_bytes(), b"messages")
        self.assertEqual((target / "whatsapp.db").read_bytes(), b"session")
        self.assertEqual(current_profile(self.bridge_dir), "empresa")


if __name__ == "__main__":
    unittest.main()
