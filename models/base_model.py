#!/usr/bin/python3
"""Script that used to create the base class"""

import uuid
from datetime import datetime

class BaseModel:
    """Base class for other classes"""
    def __init__(self, *args, **kwargs):
        """
          Initialising the id and updated time of instances
        """
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
          Makes the attribute as strings
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
          Saves changes made to the objects
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
