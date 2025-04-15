# config_handler.py

from abc import ABC
from typing import Optional
import json


class i_config_handler(ABC):
    @classmethod
    def read_config(cls):
        """responsible for extracting crawl config from json file"""
        pass

    @classmethod
    def read_parse_constants(cls):
        """responsible for extracting element parsing cnstants"""
        pass


class config_handler(i_config_handler):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def read_config(cls, file_path: Optional[str] = "configs.json"):
        with open(file_path, 'r') as f:
            config_data = json.load(f)
        if "Constants" in config_data:
            result = cls(**config_data["Constants"])
            print(vars(result))
            return result

    @classmethod
    def read_parse_constants(cls, file_path: Optional[str] = "configs.json"):
        with open(file_path, 'r') as f:
            constant_data = json.load(f)
        if "ParsConstants" in constant_data:
            result = cls(**constant_data["ParsConstants"])
            print(vars(result))
            return result
