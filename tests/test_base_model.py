#!/usr/bin/python3
"""Test cases for the `BaseModel` class"""
import unittest
import sys
from models.base_model import BaseModel
from datetime import datetime
sys.path.append('../../AirBnB_clone')


class TestBaseModel(unittest.TestCase):
    """Test Cases on the `BaseModel` `class`"""
#    def test_init_kwargs(self):
#        """Testing the `kwargs` input"""
#        self.assertIsInstance(BaseModel, dict, "Dictionary only")
#        self.assertIsNotNone(BaseModel)
#        self.assertTrue(len(BaseModel), "Empty dictionary")

    def test_to_dict(self):
        """Testing the `dict` method"""
        obj_dict = BaseModel.to_dict(self)
        self.assertIsInstance(obj_dict, dict)
        self.assertTrue(type(obj_dict[key]), (int, str))


if __name__ == '__main__':
    unittest.main()
