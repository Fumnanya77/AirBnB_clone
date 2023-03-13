#!/usr/bin/python3
"""Test Case for the `FileStorage`"""

import unittest
import sys
sys.path.append('../../AirBnB_clone')
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test Cases on the `FileSorage` `class`"""
    def test_all(self):
        """Test that `all` returns a dictionary"""
        all_obj = FileStorage.all(self)
        self.assertIsInstance(all_obj, dict)

    def test_new(self):
        """Test that `new` object is an instance of a class"""
#        self.assertTrue(type(obj in FileSorage.new(self, obj)), object)

    def test_reload(self):
        """Test the `reload` method"""


if __name__ == '__main__':
    unittest.main()
