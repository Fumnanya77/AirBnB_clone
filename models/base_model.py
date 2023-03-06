#!/usr/bin/python3
"""Script that used to create the base class"""

import uuid
from datetime import datetime

class BaseModel:
    """Base class for other classes"""
    def __init__(self,*args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':

