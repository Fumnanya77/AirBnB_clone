#!/usr/bin/python3
"""Module that saves the objects"""
import json
from os import path

class FileStorage:
    """

    This is a class that serialises an object to a json file and
    deserialisies a json file to an object

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns a dictionary of all the objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """
        Sets an object in the __object dictionary with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__,obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes the __object to the json file"""
        serialized_objs = {}
        for key, value in FileStorage.__objects.items():
            serialized_objs[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serialized_objs, f)

    def classes(self):
        """A list of valid classes"""
        from models.base_model import BaseModel
        classes = {"BaseModel": BaseModel}
        return classes

    def reload(self):
       """Reloads the stored objects from the json file"""
       if not path.isfile(FileStorage.__file_path):
           return

       # Load the serialized object from the json file

       with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
           serialized_objects =json.load(f)

       #Create a dictionary to hold the serialized objects
       deserialized_objects = {}

       #iterate over the serialized objects and deserialize them
       for obj_id, serialized_obj in serialized_objects.items():
           class_name = serialized_obj['__class__']

           #Look up the class object from the class name
           if class_name in self.classes():
               obj_class = self.classes()[class_name]
           else:
               #if the class is not define, skip
               continue

           # Make a new object from the serialized representation
           deserialized_obj = obj_class(**serialized_obj)

           #store the deserialized objects in a dictionary
           deserialized_objects[obj_id] = deserialized_obj

       FileStorage.__objects = deserialized_objects
