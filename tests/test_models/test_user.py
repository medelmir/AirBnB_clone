#!/usr/bin/python3
"""This module defines unittests for the 'models/user.py'.

Unittest classes:
    -TestUserInstantiation: Testing for instantiation of the User class.
    -TestUserSave: Testing for 'Save' method of the User class.
    -TestUserToDict: Testing for 'to_dict' method of the User class.
"""
import unittest
import os
from datetime import datetime
from time import sleep
import models
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests for instantiation of the User class."""
    def test_user_instantiation_no_args(self):
        """Test that a user instance is created with no args"""
        self.assertEqual(User, type(User()))

    def test_user_newinstance_stored(self):
        """
        Test that a newly created User instance
        is stored in the objects dictionary.
        """
        self.assertIn(User(), models.storage.all().values())

    def test_user_id_is_public_str(self):
        """Test if the id attribute of a user instance is a string."""
        self.assertEqual(str, type(User().id))

    def test_created_at_is_datetime(self):
        """
        Test if the created_at attribute of a User instance
        is instances of the datetime.
        """
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_datetime(self):
        """
        Test if the updated_at attribute of a User instance
        is instances of the datetime.
        """
        self.assertEqual(datetime, type(User().updated_at))

    def test_user_email_is_str(self):
        """Test if the email attribute of a user instance is a string."""
        self.assertEqual(str, type(User.email))

    def test_user_password_is_str(self):
        """Test if the password attribute of a user instance is a string."""
        self.assertEqual(str, type(User.password))

    def test_user_firstname_is_str(self):
        """Test if the first name attribute of a user instance is a string."""
        self.assertEqual(str, type(User.first_name))

    def test_user_lastname_is_str(self):
        """Test if the last name attribute of a user instance is a string."""
        self.assertEqual(str, type(User.last_name))

    def test_two_users_is_unique_id(self):
        """Test if two user instances have unique id."""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_two_users_created_at(self):
        """
        Test if two user instances have different 'created_at' timestamps.
        """
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.created_at, user2.created_at)

    def test_two_users_updated_at(self):
        """
        Test if two user instances have different 'updated_at' timestamps.
        """
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.updated_at, user2.updated_at)

    def test_user_no_args(self):
        """
        Test that the positional arguments are unused.
        """
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_user_instantiation_with_kwargs(self):
        """
        Test if a User instance can be created with keyword arguments.
        """
        timestamp = datetime.now()
        dt_format = timestamp.isoformat()
        dt_obj = datetime.fromisoformat(dt_format)
        user = User(id="0123", created_at=dt_format, updated_at=dt_format)
        self.assertEqual(user.id, "0123")
        self.assertEqual(user.created_at, dt_obj)
        self.assertEqual(user.updated_at, dt_obj)

    def test_user_instantiation_with_nonekwargs(self):
        """
        Test if a User instance can be created with None keyword arguments.
        """
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_user_str_representation(self):
        """Test the str representation of a User instance."""
        timestamp = datetime.now()
        dt_repr = repr(timestamp)
        user = User()
        user.id = "0123"
        user.created_at = user.updated_at = timestamp
        user_str = user.__str__()
        self.assertIn("[User] (0123)", user_str)
        self.assertIn("'id': '0123'", user_str)
        self.assertIn("'created_at': " + dt_repr, user_str)
        self.assertIn("'updated_at': " + dt_repr, user_str)


class TestUser_save_method(unittest.TestCase):
    """Unittests for the 'save' method of the User class."""

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

    def tearDown(self):
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

    def test_save_method_one_update(self):
        """
        Test that the 'save' method updates the updated_at attribute.
        """
        user = User()
        sleep(0.05)
        test_updated_at = user.updated_at
        user.save()
        self.assertLess(test_updated_at, user.updated_at)

    def test_save_method_two_update(self):
        """
        Test that the 'save' method updates the updated_at attribute.
        """
        user = User()
        sleep(0.05)
        test_updated_at = user.updated_at
        user.save()
        test2_updated_at = user.updated_at
        self.assertLess(test_updated_at, user.updated_at)
        sleep(0.05)
        user.save()
        self.assertLess(test2_updated_at, user.updated_at)

    def test_save_method_with_arg(self):
        """
        Test if 'save' method raises a TypeError when called with an arg.
        """
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_method_update_file(self):
        """Test if the `save` method updates the file."""
        user = User()
        user.save()
        user_id = "User." + user.id
        with open("data.json", "r") as file:
            self.assertIn(user_id, file.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests for 'to_dict' method of the User class."""

    def test_to_dict_method_type(self):
        """
        Test if the return value of the `to_dict` method is a dictionary.
        """
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_method_correct_keys(self):
        """
        Test if the return value of the `to_dict` method is a dictionary.
        with the correct keys.
        """
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_to_dict_method_added_attributes(self):
        """
        Test if the 'to_dict' method includes added attributes
        in the dictionary.
        """
        user = User()
        user.nick_name = "python"
        user.weight = 60
        self.assertEqual("python", user.nick_name)
        self.assertIn("weight", user.to_dict())

    def test_to_dict_method_with_arg(self):
        """
        Test if the 'save' method raises a TypeError when called with args.
        """
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)

    def test_to_dict_method_datetime_attr_are_strs(self):
        """
        Test if the 'to_dict' method datetime attributes
        are strings in the dictionary.
        """
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(str, type(user_dict["id"]))
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_method_output(self):
        """Test the 'to_dict' method output."""
        timestamp = datetime.now()
        user = User()
        user.id = "0123"
        user.created_at = user.updated_at = timestamp
        test_to_dict = {
            'id': '0123',
            '__class__': 'User',
            'created_at': timestamp.isoformat(),
            'updated_at': timestamp.isoformat(),
        }
        self.assertDictEqual(user.to_dict(), test_to_dict)

    def test_to_dict_method_no_dunder_dict(self):
        """
        Test if the 'to_dict' does not return the internal
        attribute dictionary.
        """
        user = User()
        self.assertNotEqual(user.to_dict(), user.__dict__)


if __name__ == "__main__":
    unittest.main()
