import unittest
from aviator import BotApp
from selenium import webdriver  # Import Selenium WebDriver

class TestBotApp(unittest.TestCase):

    def setUp(self):
        """Set up the BotApp instance for testing."""
        self.app = BotApp()

    def test_start_bot(self):
        """Test the start_bot method."""
        self.app.username_input.text = "test_user"
        self.app.password_input.text = "test_pass"
        self.app.platform_input.text = "hollywoodbets"
        self.app.start_bot(None)
        self.assertTrue(self.app.running)

    def test_stop_bot(self):
        """Test the stop_bot method."""
        self.app.running = True
        self.app.stop_bot(None)
        self.assertFalse(self.app.running)

    def test_invalid_platform(self):
        """Test handling of invalid platform input."""
        self.app.platform_input.text = "invalid_platform"
        with self.assertRaises(SystemExit):
            self.app.run_bot("test_user", "test_pass", "invalid_platform")

if __name__ == '__main__':
    unittest.main()
