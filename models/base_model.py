#!/usr/bin/python3
"""Script that used to create the base class"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """Base class for other classes"""
    def __init__(self, *args, **kwargs):
        """
          Initialising the id and updated time of instances
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'updated_at' or key == 'created_at':
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
          Makes the attribute as strings
        """
        return "[{}] ({}) {}".\
            format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
          Saves changes made to the objects
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
