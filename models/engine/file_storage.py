#!/usr/bin/env python3
"""
Module containing the classs FileStorage
"""
import json
import os.path


class FileStorage:
    """
    A class FileStorage that serializes instances to a JSON file\
            and deserializes JSON file to instances
    """

    __objects = {}
    __file_path = "file.json"

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        unique_id = type(obj).__name__ + obj.id
        __objects[unique_id] = obj

    def all(self):
        """
        returns the dictionary __objects
        """
        return __objects

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(__file_path, "w", encoding="utf-8") as f:
            json.dumps(__objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.exists(__file_path) = True:
            with open(__file_path, "r", encoding="utf-8") as f:
                __objects = json.load(f)
