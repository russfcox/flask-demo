import json
import unittest

from app.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Tests for the App."""

    def test_users(self):
        """Ensure the / route behaves correctly."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
