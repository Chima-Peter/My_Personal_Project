#!/usr/bin/env python3
"""
Module containing the classs FileStorage
"""
import json
from os import path

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
        unique_id = type(obj).__name__ + "." + obj.id
        self.__objects[unique_id] = obj

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r+") as f:
                lines = f.read()
                data = json.loads(lines)
                for key, value in FileStorage.__objects.items():
                    data[key] = value.to_dict()
                json.dump(data, f)
        with open(FileStorage.__file_path, "w+", encoding="utf-8") as f:
            serialised_dict = {}
            for key, value in FileStorage.__objects.items():
                serialised_dict[key] = value.to_dict()
            json.dump(serialised_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                lines = f.read()
                data = json.loads(lines)
                FileStorage.__objects = {}
                for key, value in data.items():
                    class_name, class_id = key.split(".")
                    FileStorage.__objects[key] = value
     
