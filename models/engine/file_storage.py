#!/usr/bin/python3
"""Module that saves the objects"""
import json

class FileStorage:
    """

    This is a class that serialises an object to a json file and
    deserialisies a json file to an object

    """
    __file_path = "file.path"
    __object = {}

    def all(self):
        """returns a dictionary of all the objects"""
        return FileStorage.__object
    
    def new(self, obj):
        """
        Sets an object in the __object dictionary with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__object[key] = obj


