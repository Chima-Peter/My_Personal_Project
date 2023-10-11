#!/usr/bin/env python3
"""
This module contains the BaseModel class
"""
import datetime
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
