#!/usr/bin/env python3
"""
Module containing unittest for base_model module
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Class to test BaseModel
    """
    def test_init(self):
        """
        Testing the initailisation
        """
        first = BaseModel()
        second = BaseModel()
        self.assertNotEqual(first.id, second.id)
        self.assertEqual(type(first.updated_at), datetime)
        self.assertEqual(type(first.created_at), datetime)

    def test_save(self):
        """
        Testing save() method
        """
        first = BaseModel()
        prev_first_updated_at = first.updated_at
        first.save()
        self.assertNotEqual(prev_first_updated_at, first.updated_at)

    def test_to_dict(self):
        """
        Testing the to_dict() method
        """
        first = BaseModel()
        my_model = first.to_dict()
        self.assertIn("__class__", my_model)
        self.assertEqual(type(my_model["created_at"]), str)
        self.assertEqual(type(my_model["updated_at"]), str)

if __name__ == "__main__":
    unittest.main()
