# test_config_handler_happy.py
import unittest
from config_handler import config_handler


class TestConfigHandler(unittest.TestCase):

    def test_read_config(self):
        """Test read_config with real JSON file"""
        print("read_config")
        c_handler = config_handler()
        config = c_handler.get_crawl_config(
            "configs.json")  # Using real file
        self.assertIsNotNone(config)  # Ensure the object is created
        self.assertTrue(hasattr(config, "user_agent"))
        self.assertTrue(hasattr(config, "base_url"))
        self.assertTrue(hasattr(config, "tag"))

    def test_read_parse_constants(self):
        """Test read_parse_constants with real JSON file"""
        print("read_parse_constants")
        c_handler = config_handler()
        constants = c_handler.get_parse_config(
            "configs.json")  # Using real file
        self.assertIsNotNone(constants)  # Ensure the object is created
        self.assertTrue(hasattr(constants, "post_summary"))


if __name__ == "__main__":
    unittest.main()
