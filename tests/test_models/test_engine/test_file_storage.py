#!/usr/bin/python3
"""Test Cases for the `FileStorage` class"""
import unittest
import sys
sys.path.insert(0, '../../..')
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test Cases on the `FileSorage` `class`"""

    def setUp(self):
        """Default object for all testing methods"""
        self.file_obj = FileStorage()
        self.base_obj = BaseModel()

    def test_cls_objects(self):
        """Tests the class objects"""
        self.assertTrue(self.file_obj._FileStorage__file_path)
        self.assertTrue(self.file_obj._FileStorage__objects)
        self.assertIsInstance(self.file_obj._FileStorage__objects, dict)

    def test_all(self):
        """Test that `all` returns a dictionary"""
        all_obj = FileStorage.all(self)
        self.assertIsInstance(all_obj, dict)
        self.assertTrue(all_obj)
        self.assertEqual(all_obj, self.file_obj._FileStorage__objects)

    def test_new(self):
        """Test that `new` object is an instance of a class"""
#        new_obj = FileStorage.new(self, self.base_obj)
#        self.assertTrue(new_obj)
#        self.assertEqual(self.file_obj.key, "BaseModel"+"."+self.base_obj.id)

    def test_save(self):
        """Test the `save` method of the class"""
#        self.assertIsInstance(self.file_obj.save().serialized_obj, dict)

    def test_reload(self):
        """Test the `reload` method"""


if __name__ == '__main__':
    unittest.main()
