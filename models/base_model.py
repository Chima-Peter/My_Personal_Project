#!/usr/bin/env python3
"""
This module contains the BaseModel class
"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """
    The class that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialisation of the class with attributes
            id
            created_at
            updated_at
            args
            kwargs
        """
        self.updated_at = datetime.now()
        if len(kwargs) == 0:
            self.id = uuid.uuid4()
            self.id = str(self.id)
            self.created_at = datetime.now()
            models.storage.new(self)
        else:
            for key in kwargs:
                value = kwargs[key]
                if key != "__class__":
                    if key == "updated_at" or key == "created_at":
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)

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
        models.storage.save()
        

    def to_dict(self):
        """
        returns a dictionary of all keys/values of __dict__ of the instance
        """
        if type(self.created_at) != str:
            self.created_at = self.created_at.isoformat()
        if type(self.updated_at) != str:
            self.updated_at = self.updated_at.isoformat()
        self.__dict__["__class__"] = "BaseModel"
        return self.__dict__
