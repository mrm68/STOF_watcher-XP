# config_handler.py

from abc import ABC
from typing import Optional
import json


class i_config_handler(ABC):
    def _read_config(self):
        """responsible for extracting crawl config from json file"""
        pass

    def _read_parse_constants(self):
        """responsible for extracting element parsing cnstants"""
        pass

    def get_crawl_config(self):
        """responsible for returning crawl config from json file"""
        pass

    def get_parse_config(self):
        """responsible for returning element parsing cnstants"""
        pass


class config_handler(i_config_handler):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def _read_config(self, file_path: Optional[str] = "configs.json"):
        with open(file_path, 'r') as f:
            config_data = json.load(f)
        if "Constants" in config_data:
            result = config_handler(**config_data["Constants"])
            print(vars(result))
            return result

    def _read_parse_constants(self, file_path: Optional[str] = "configs.json"):
        with open(file_path, 'r') as f:
            constant_data = json.load(f)
        if "ParsConstants" in constant_data:
            result = config_handler(**constant_data["ParsConstants"])
            print(vars(result))
            return result

    def get_crawl_config(self, file_path: Optional[str] = "configs.json"):
        return self._read_config()

    def get_parse_config(self, file_path: Optional[str] = "configs.json"):
        return self._read_parse_constants()
