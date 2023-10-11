#!/usr/bin/env python3
"""
This module contains the BaseModel class
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    The class thatb defines all common attributes/methods for other classes
    """

    def __init__(self):
        """
        Initialisation of the class with attributes
            id
            created_at
            updated_at
        """
        self.id = uuid.uuid4()
        self.id = str(self.id)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns user-readable string to stdout
        """
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """
        updates the attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary of all keys/values of __dict__ of the instance
        """
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__dict__["__class__"] = "BaseModel"
        return self.__dict__
