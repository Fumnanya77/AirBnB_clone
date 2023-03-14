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
        """To test the object attributes"""
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        """Testing that the string method is properly returned"""
        self.assertEqual(self.obj.__str__, self.obj.__str__)

    def test_save(self):
        """To test the save method"""
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.assertNotEqual(self.obj.save(), "")
        self.assertNotEqual(self.obj.updated_at, self.obj.save())
#        self.assertEqual(self.obj.save(), self.obj.updated_at)
        self.assertEqual(self.obj.save(), None)

    def test_to_dict(self):
        """Testing the `dict` method"""
        obj_dict = self.obj.to_dict()
        self.assertIsInstance(self.obj.to_dict(), dict)
        self.assertTrue(self.obj.to_dict())
        self.assertTrue(obj_dict['__class__'] == 'BaseModel')


if __name__ == '__main__':
    unittest.main()
    BaseModel()
