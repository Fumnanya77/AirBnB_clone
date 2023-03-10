#!/usr/bin/python3
"""Module that saves the objects"""
import json
from os import path

class FileStorage:
    """

    This is a class that serialises an object to a json file and
    deserialisies a json file to an object

    """
    __file_path = "file.path"
    __objects = {}

    def all(self):
        """returns a dictionary of all the objects"""
        return FileStorage.__object
    
    def new(self, obj):
        """
        Sets an object in the __object dictionary with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__,obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes the __object to the json file"""
        serialized_objs = {}
        for key, value in FileStorage.__object.items():
            serialized_objs[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """Deserializes a json file to __object"""
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                deserialized_obj = json.load(f)
            for key, value in deserialized_obj.items():
                class_name, obj_id = key.split('.')
                print(type(value))
                obj = eval(class_name)(**obj_dict)
                self.__objects[key] = obj
            return FileStorage.__object
