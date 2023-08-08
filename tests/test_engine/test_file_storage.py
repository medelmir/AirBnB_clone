#!/usr/bin/python3
"""This module defines unittests for the 'models/engine/file_storage.py'

Unittest classes:
    - TestFileStorageInstantiation:
    Tests for the instantiation of the FileStorage class.
    - TestFileStorageMethods:
    Tests for the methods within the FileStorage class.
"""
import unittest
import os
import json
from datetime import datetime
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for instantiation of the FileStorage class."""
    def test_FileStorage_instantiation_no_args(self):
        """Test if the FileStorage is correctly instantiated with no args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        """
        Test if FileStorage raises a TypeError when instantiated with args.
        """
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        """Test if the file_path attribute is a private string."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_is_private_dict(self):
        """Test if the file_path attribute is a private dictionary."""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initialization(self):
        """
        Test if the models.storage variable is an instance of FileStorage.
        """
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests/testcase for testing the FileStorage class methods."""

    @classmethod
    def setUp(self):
        """
        Setup method to prepare the environment and resources needed for
        the testcases in the class to execute.
        Renames 'data.json' to 'temp' for testing purposes.
        """
        try:
            os.rename("data.json", "temp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        """
        Cleanup executed after all testing methods in this class are done.
        Removes temp files and resets attributes for the next testing.
        """
        try:
            os.remove("data.json")
        except IOError:
            pass
        try:
            os.rename("temp", "data.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all_method_return_dict(self):
        """Test if 'all' method returns a dictionary"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_method_with_args(self):
        """
        Test if 'all' method raises a TypeError when called with an arg.
        """
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_method(self):
        """
        Test if the 'new' method adds an instance to the storage dictionary.
        """
        base = BaseModel()
        models.storage.new(base)
        self.assertIn("BaseModel." + base.id, models.storage.all().keys())
        self.assertIn(base, models.storage.all().values())

    def test_new_method_with_args(self):
        """
        Test if the 'new' method raises a TypeError
        when called with invalid arguments.
        """
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_method_with_none(self):
        """
        Test if the 'new' method raises an AttributeError.
        when called with None as an argument.
        """
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_method(self):
        """
        Test if the 'save' method correctly saves an instance to the file.
        """
        base = BaseModel()
        models.storage.new(base)
        models.storage.save()
        saved = ""
        with open("data.json", 'r') as file:
            saved = file.read()
            self.assertIn("BaseModel." + base.id, saved)

    def test_save_method_with_arg(self):
        """
        Test if the 'save' method raises a TypeError when called with args.
        """
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_method(self):
        """
        Test if the 'reload' method correctly loads objects from the file.
        """
        base = BaseModel()
        models.storage.new(base)
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base.id, objs)

    def test_reload_method_with_arg(self):
        """
        Test if the 'reload' method raises a TypeError when called with args.
        """
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
