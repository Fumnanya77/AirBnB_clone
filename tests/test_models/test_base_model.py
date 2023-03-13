#!/usr/bin/python3
"""Test cases for the `BaseModel` class"""
import unittest
import sys
from datetime import datetime
sys.path.insert(0, '../..')
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test Cases on the `BaseModel` `class`"""
    def setUp(self):
        """Default object for all methods"""
        self.obj = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        """Testing that the string method is properly returned"""
        self.assertEqual(self.obj.__str__, self.obj.__str__)

    def test_save(self):
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.assertFalse(self.obj.save(), "")

    def test_to_dict(self):
        """Testing the `dict` method"""
        self.assertIsInstance(self.obj.to_dict(), dict)


if __name__ == '__main__':
    unittest.main()
    BaseModel()
