#!/usr/bin/python3
"""This module defines unittests for the 'models/amenity.py'.

Unittest classes:
    -TestAmenityInstantiation: Testing for instantiation of the Amenity cls.
    -TestAmenitySave: Testing for the 'save' method of the Amenity cls.
    -TestAmenityToDict: Testing for the 'To_dict' method of the Amenity cls.
"""
import unittest
import os
from datetime import datetime
from time import sleep
import models
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for instantiation of the Amenity class."""

    def test_amenity_instantiation_no_args(self):
        """Test that a amenity instance is created with no args."""
        self.assertEqual(Amenity, type(Amenity()))

    def test_amenity_new_instance_stored(self):
        """
        Test that a newly created Amenity instance is stored
        in the objects dictionary.
        """
        self.assertIn(Amenity(), models.storage.all().values())

    def test_amenity_id_is_public_str(self):
        """Test if the id attribute of a amenity instance is a string."""
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_datetime(self):
        """
        Test if the created_at attribute of a Amenity instance
        is an instance of datetime.
        """
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_datetime(self):
        """
        Test if the updated_at attribute of a Amenity instance
        is an instance of datetime.
        """
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_two_amenitys_is_unique_id(self):
        """Test if two Amenity instances have unique id."""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_two_amenitys_created_at(self):
        """
        Test if two Amenity instances have different 'created_at' timestamps.
        """
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.created_at, amenity2.created_at)

    def test_two_amenitys_updated_at(self):
        """
        Test if two Amenity instances have different 'updated_at' timestamps.
        """
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.updated_at, amenity2.updated_at)

    def test_amenity_name_is_public_cls_attr(self):
        """
        Test if the name attribute of a amenity instance
        is a public class attribute.
        """
        amenity = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(amenity))
        self.assertNotIn("name", amenity.__dict__)

    def test_amenity_no_args(self):
        """Test that positional arguments are unused."""
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

    def test_amenity_instantiation_with_kwargs(self):
        """
        Test if a Amenity instance can be created with keyword arguments.
        """
        timestamp = datetime.now()
        dt_format = timestamp.isoformat()
        dt_obj = datetime.fromisoformat(dt_format)
        amenity = Amenity(id="0123", created_at=dt_format,
                          updated_at=dt_format)
        self.assertEqual(amenity.id, "0123")
        self.assertEqual(amenity.created_at, dt_obj)
        self.assertEqual(amenity.updated_at, dt_obj)

    def test_amenity_instantiation_with_none_kwargs(self):
        """
        Test if a Amenity instance can be created with None keyword arguments.
        """
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_amenity_str_representation(self):
        """Test the str representation of a Amenity instance."""
        timestamp = datetime.now()
        dt_repr = repr(timestamp)
        amenity = Amenity()
        amenity.id = "0123"
        amenity.created_at = amenity.updated_at = timestamp
        amenity_str = amenity.__str__()
        self.assertIn("[Amenity] (0123)", amenity_str)
        self.assertIn("'id': '0123'", amenity_str)
        self.assertIn("'created_at': " + dt_repr, amenity_str)
        self.assertIn("'updated_at': " + dt_repr, amenity_str)


class TestAmenity_save_method(unittest.TestCase):
    """Unittests for the 'save' method of the Amenity class."""

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
        amenity = Amenity()
        sleep(0.05)
        test_updated_at = amenity.updated_at
        amenity.save()
        self.assertLess(test_updated_at, amenity.updated_at)

    def test_save_method_two_update(self):
        """
        Test that the 'save' method updates the updated_at attribute.
        """
        amenity = Amenity()
        sleep(0.05)
        test_updated_at = amenity.updated_at
        amenity.save()
        test2_updated_at = amenity.updated_at
        self.assertLess(test_updated_at, amenity.updated_at)
        sleep(0.05)
        amenity.save()
        self.assertLess(test2_updated_at, amenity.updated_at)

    def test_save_method_with_arg(self):
        """
        Test if 'save' method raises a TypeError when called with an arg.
        """
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.save(None)

    def test_save_method_update_file(self):
        """Test if the `save` method updates the file."""
        amenity = Amenity()
        amenity.save()
        amenity_id = "Amenity." + amenity.id
        with open("data.json", "r") as file:
            self.assertIn(amenity_id, file.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for 'to_dict' method of the Amenity class."""

    def test_to_dict_method_type(self):
        """
        Test if the return value of the `to_dict` method is a dictionary.
        """
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_method_correct_keys(self):
        """
        Test if the return value of the `to_dict` method is a dictionary.
        with the correct keys.
        """
        amenity = Amenity()
        self.assertIn("id", amenity.to_dict())
        self.assertIn("created_at", amenity.to_dict())
        self.assertIn("updated_at", amenity.to_dict())
        self.assertIn("__class__", amenity.to_dict())

    def test_to_dict_method_added_attributes(self):
        """
        Test if the 'to_dict' method includes added attributes
        in the dictionary.
        """
        amenity = Amenity()
        amenity.facilities = "golf courses"
        amenity.rooms = 20
        self.assertEqual("golf courses", amenity.facilities)
        self.assertIn("rooms", amenity.to_dict())

    def test_to_dict_method_with_arg(self):
        """
        Test if the 'save' method raises a TypeError when called with args.
        """
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.to_dict(None)

    def test_to_dict_method_datetime_attr_are_strs(self):
        """
        Test if the 'to_dict' method datetime attributes
        are strings in the dictionary.
        """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(str, type(amenity_dict["id"]))
        self.assertEqual(str, type(amenity_dict["created_at"]))
        self.assertEqual(str, type(amenity_dict["updated_at"]))

    def test_to_dict_method_output(self):
        """Test the 'to_dict' method output."""
        timestamp = datetime.now()
        amenity = Amenity()
        amenity.id = "0123"
        amenity.created_at = amenity.updated_at = timestamp
        test_to_dict = {
            'id': '0123',
            '__class__': 'Amenity',
            'created_at': timestamp.isoformat(),
            'updated_at': timestamp.isoformat(),
        }
        self.assertDictEqual(amenity.to_dict(), test_to_dict)

    def test_to_dict_method_no_dunder_dict(self):
        """
        Test if the 'to_dict' does not return the internal
        attribute dictionary.
        """
        amenity = Amenity()
        self.assertNotEqual(amenity.to_dict(), amenity.__dict__)


if __name__ == "__main__":
    unittest.main()
