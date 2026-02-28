import unittest
from unittest.mock import patch

from lib.gewechat.api.login_api import LoginApi


class TestLoginApi(unittest.TestCase):
    @patch("lib.gewechat.api.login_api.post_json")
    def test_get_qr_omits_empty_app_id(self, mock_post_json):
        mock_post_json.return_value = {"ret": 200, "data": {}}
        api = LoginApi("http://127.0.0.1:2531/v2/api", "token")

        api.get_qr("")

        mock_post_json.assert_called_once_with(
            "http://127.0.0.1:2531/v2/api",
            "/login/getLoginQrCode",
            "token",
            {},
        )

    @patch("lib.gewechat.api.login_api.post_json")
    def test_get_qr_omits_blank_app_id(self, mock_post_json):
        mock_post_json.return_value = {"ret": 200, "data": {}}
        api = LoginApi("http://127.0.0.1:2531/v2/api", "token")

        api.get_qr("   ")

        mock_post_json.assert_called_once_with(
            "http://127.0.0.1:2531/v2/api",
            "/login/getLoginQrCode",
            "token",
            {},
        )

    @patch("lib.gewechat.api.login_api.post_json")
    def test_get_qr_omits_none_app_id(self, mock_post_json):
        mock_post_json.return_value = {"ret": 200, "data": {}}
        api = LoginApi("http://127.0.0.1:2531/v2/api", "token")

        api.get_qr(None)

        mock_post_json.assert_called_once_with(
            "http://127.0.0.1:2531/v2/api",
            "/login/getLoginQrCode",
            "token",
            {},
        )

    @patch("lib.gewechat.api.login_api.post_json")
    def test_get_qr_keeps_non_empty_app_id(self, mock_post_json):
        mock_post_json.return_value = {"ret": 200, "data": {}}
        api = LoginApi("http://127.0.0.1:2531/v2/api", "token")

        api.get_qr("wx_xxx")

        mock_post_json.assert_called_once_with(
            "http://127.0.0.1:2531/v2/api",
            "/login/getLoginQrCode",
            "token",
            {"appId": "wx_xxx"},
        )


if __name__ == "__main__":
    unittest.main()
