#!/usr/bin/python3
"""Module that saves the objects"""
import json
from os import path


class FileStorage:
    """ The File Storage `Class`

    This is a class that serialises an object to a json file and
    deserialisies a json file to an object
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns a dictionary of all the objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets a `new` object in a dictionary

        Sets an object in the __object dictionary with key <obj class name>.id
        Args:
            obj(object): an instance of a `class`
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
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
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """Reloads the stored objects from the json file"""
        if not path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            serialized_objects =json.load(f)

        deserialized_objects = {}

        for obj_id, serialized_obj in serialized_objects.items():
            class_name = serialized_obj['__class__']
            if class_name in self.classes():
                obj_class = self.classes()[class_name]
            else:
                continue

            deserialized_obj = obj_class(**serialized_obj)
            deserialized_objects[obj_id] = deserialized_obj

        FileStorage.__objects = deserialized_objects
