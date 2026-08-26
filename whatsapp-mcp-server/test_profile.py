import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from account_profile import (
    ActiveProfile,
    ProfileError,
    ProfileMismatch,
    load_active_profile,
    profiled,
    require_expected_profile,
)
from main import get_active_account as mcp_get_active_account
from main import search_contacts as mcp_search_contacts
from main import send_message as mcp_send_message
from whatsapp import get_active_account, send_message


class ActiveProfileTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.bridge_dir = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_load_active_profile_returns_its_messages_database(self):
        store_dir = self.bridge_dir / "profiles" / "empresa"
        store_dir.mkdir(parents=True)
        (self.bridge_dir / ".active-profile").write_text(
            "empresa\n", encoding="utf-8"
        )

        profile = load_active_profile(self.bridge_dir)

        self.assertEqual(profile.name, "empresa")
        self.assertEqual(profile.store_dir, store_dir)
        self.assertEqual(profile.messages_db, store_dir / "messages.db")

    def test_load_active_profile_rejects_traversal(self):
        (self.bridge_dir / ".active-profile").write_text(
            "../empresa\n", encoding="utf-8"
        )

        with self.assertRaisesRegex(ProfileError, "Invalid active profile"):
            load_active_profile(self.bridge_dir)

    def test_profiled_result_names_its_source(self):
        self.assertEqual(
            profiled("empresa", ["resultado"]),
            {"account_profile": "empresa", "data": ["resultado"]},
        )

    def test_expected_profile_must_match(self):
        require_expected_profile("empresa", "empresa")

        with self.assertRaisesRegex(ProfileMismatch, "active profile is 'empresa'"):
            require_expected_profile("pessoal", "empresa")
        with self.assertRaisesRegex(ProfileMismatch, "expected_profile is required"):
            require_expected_profile("", "empresa")

    @patch("whatsapp.requests.post")
    def test_send_message_forwards_expected_profile(self, post):
        response = Mock(status_code=200)
        response.json.return_value = {"success": True, "message": "sent"}
        post.return_value = response

        success, message = send_message("5511999999999", "Olá", "empresa")

        self.assertTrue(success)
        self.assertEqual(message, "sent")
        self.assertEqual(
            post.call_args.kwargs["json"]["expected_profile"], "empresa"
        )

    @patch("whatsapp.requests.get")
    def test_get_active_account_reads_bridge_identity(self, get):
        response = Mock(status_code=200)
        response.json.return_value = {
            "profile": "empresa",
            "jid": "device@s.whatsapp.net",
        }
        get.return_value = response

        self.assertEqual(get_active_account()["profile"], "empresa")

    @patch("main.load_active_profile")
    @patch("main.whatsapp_search_contacts")
    def test_mcp_read_result_identifies_profile(self, search_contacts, active):
        active.return_value = ActiveProfile("empresa", Path("/profiles/empresa"))
        search_contacts.return_value = ["contato"]

        self.assertEqual(
            mcp_search_contacts("nome"),
            {"account_profile": "empresa", "data": ["contato"]},
        )

    @patch("main.load_active_profile")
    @patch("main.whatsapp_send_message")
    def test_mcp_send_rejects_wrong_profile(self, send, active):
        active.return_value = ActiveProfile("empresa", Path("/profiles/empresa"))

        result = mcp_send_message("5511999999999", "Olá", "pessoal")

        self.assertFalse(result["success"])
        self.assertEqual(result["account_profile"], "empresa")
        send.assert_not_called()

    @patch("main.load_active_profile")
    def test_invalid_send_still_identifies_profile(self, active):
        active.return_value = ActiveProfile("empresa", Path("/profiles/empresa"))

        result = mcp_send_message("", "Olá", "empresa")

        self.assertFalse(result["success"])
        self.assertEqual(result["account_profile"], "empresa")

    @patch("main.whatsapp_get_active_account")
    @patch("main.load_active_profile")
    def test_mcp_account_identity_matches_selected_profile(self, active, account):
        active.return_value = ActiveProfile("empresa", Path("/profiles/empresa"))
        account.return_value = {"profile": "empresa", "jid": "device@s.whatsapp.net"}

        self.assertEqual(mcp_get_active_account()["profile"], "empresa")


if __name__ == "__main__":
    unittest.main()
