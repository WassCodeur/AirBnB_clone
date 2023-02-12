#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:00:00 2020
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import pep8
import json
import datetime
import time
class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""
    def test_pep8(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")
    def test_docstring(self):
        """Test docstring"""
        self.assertIsNotNone(BaseModel.__doc__)
    def test_init(self):
        """Test init"""
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
    def test_save(self):
        """Test save"""
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)
    def test_to_dict(self):
        """Test to_dict"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json["__class__"], "BaseModel")
        self.assertEqual(type(my_model_json["created_at"]), str)
        self.assertEqual(type(my_model_json["updated_at"]), str)
        self.assertEqual(my_model_json["name"], "Holberton")
        self.assertEqual(my_model_json["my_number"], 89)
        self.assertEqual(my_model_json["id"], my_model.id)
        self.assertEqual(my_model_json["created_at"], my_model.created_at.isoformat())
        self.assertEqual(my_model_json["updated_at"], my_model.updated_at.isoformat())
    def test_str(self):
        """Test str"""
        my_model = BaseModel()
        string = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(string, str(my_model))
    def test_filestorage(self):
        """Test filestorage"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as file:
            self.assertIn(my_model.id, file.read())
    def test_filestorage_reload(self):
        """Test filestorage reload"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89