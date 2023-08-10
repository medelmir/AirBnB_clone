#!/usr/bin/python3
"""This module defines unittests for the 'models/city.py'.

Unittest classes:
    -TestCityInstantiation: Testing for instantiation of the city class.
    -TestCitySave: Testing for the 'save' method of the city class.
    -TestCityToDict: Testing for the 'To_dict' method of the city class.
"""
import unittest
import os
from datetime import datetime
from time import sleep
import models
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for instantiation of the City class."""

    def test_city_instantiation_no_args(self):
        """Test that a city instance is created with no args."""
        self.assertEqual(City, type(City()))

    def test_city_new_instance_stored(self):
        """
        Test that a newly created City instance is stored
        in the objects dictionary.
        """
        self.assertIn(City(), models.storage.all().values())

    def test_city_id_is_public_str(self):
        """Test if the id attribute of a city instance is a string."""
        self.assertEqual(str, type(City().id))

    def test_created_at_is_datetime(self):
        """
        Test if the created_at attribute of a City instance
        is an instance of datetime.
        """
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_datetime(self):
        """
        Test if the updated_at attribute of a City instance
        is an instance of datetime.
        """
        self.assertEqual(datetime, type(City().updated_at))

    def test_two_citys_is_unique_id(self):
        """Test if two City instances have unique id."""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_two_citys_created_at(self):
        """
        Test if two City instances have different 'created_at' timestamps.
        """
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertNotEqual(city1.created_at, city2.created_at)

    def test_two_citys_updated_at(self):
        """
        Test if two City instances have different 'updated_at' timestamps.
        """
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertNotEqual(city1.updated_at, city2.updated_at)

    def test_city_name_is_public_cls_attr(self):
        """
        Test if the name attribute of a city instance
        is a public class attribute.
        """
        city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(city))
        self.assertNotIn("name", city.__dict__)

    def test_city_no_args(self):
        """Test that positional arguments are unused."""
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_city_instantiation_with_kwargs(self):
        """
        Test if a City instance can be created with keyword arguments.
        """
        timestamp = datetime.now()
        dt_format = timestamp.isoformat()
        dt_obj = datetime.fromisoformat(dt_format)
        city = City(id="0123", created_at=dt_format, updated_at=dt_format)
        self.assertEqual(city.id, "0123")
        self.assertEqual(city.created_at, dt_obj)
        self.assertEqual(city.updated_at, dt_obj)

    def test_city_instantiation_with_none_kwargs(self):
        """
        Test if a City instance can be created with None keyword arguments.
        """
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_city_str_representation(self):
        """Test the str representation of a City instance."""
        timestamp = datetime.now()
        dt_repr = repr(timestamp)
        city = City()
        city.id = "0123"
        city.created_at = city.updated_at = timestamp
        city_str = city.__str__()
        self.assertIn("[City] (0123)", city_str)
        self.assertIn("'id': '0123'", city_str)
        self.assertIn("'created_at': " + dt_repr, city_str)
        self.assertIn("'updated_at': " + dt_repr, city_str)


class TestCity_save_method(unittest.TestCase):
    """Unittests for the 'save' method of the City class."""

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
        city = City()
        sleep(0.05)
        test_updated_at = city.updated_at
        city.save()
        self.assertLess(test_updated_at, city.updated_at)

    def test_save_method_two_update(self):
        """
        Test that the 'save' method updates the updated_at attribute.
        """
        city = City()
        sleep(0.05)
        test_updated_at = city.updated_at
        city.save()
        test2_updated_at = city.updated_at
        self.assertLess(test_updated_at, city.updated_at)
        sleep(0.05)
        city.save()
        self.assertLess(test2_updated_at, city.updated_at)

    def test_save_method_with_arg(self):
        """
        Test if 'save' method raises a TypeError when called with an arg.
        """
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

    def test_save_method_update_file(self):
        """Test if the `save` method updates the file."""
        city = City()
        city.save()
        city_id = "City." + city.id
        with open("data.json", "r") as file:
            self.assertIn(city_id, file.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for 'to_dict' method of the City class."""

    def test_to_dict_method_type(self):
        """
        Test if the return value of the `to_dict` method is a dictionary.
        """
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_method_correct_keys(self):
        """
        Test if the return value of the `to_dict` method is a dictionary.
        with the correct keys.
        """
        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())

    def test_to_dict_method_added_attributes(self):
        """
        Test if the 'to_dict' method includes added attributes
        in the dictionary.
        """
        city = City()
        city.region = "Silicon Valley"
        city.rank = 21
        self.assertEqual("Silicon Valley", city.region)
        self.assertIn("rank", city.to_dict())

    def test_to_dict_method_with_arg(self):
        """
        Test if the 'save' method raises a TypeError when called with args.
        """
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)

    def test_to_dict_method_datetime_attr_are_strs(self):
        """
        Test if the 'to_dict' method datetime attributes
        are strings in the dictionary.
        """
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(str, type(city_dict["id"]))
        self.assertEqual(str, type(city_dict["created_at"]))
        self.assertEqual(str, type(city_dict["updated_at"]))

    def test_to_dict_method_output(self):
        """Test the 'to_dict' method output."""
        timestamp = datetime.now()
        city = City()
        city.id = "0123"
        city.created_at = city.updated_at = timestamp
        test_to_dict = {
            'id': '0123',
            '__class__': 'City',
            'created_at': timestamp.isoformat(),
            'updated_at': timestamp.isoformat(),
        }
        self.assertDictEqual(city.to_dict(), test_to_dict)

    def test_to_dict_method_no_dunder_dict(self):
        """
        Test if the 'to_dict' does not return the internal
        attribute dictionary.
        """
        city = City()
        self.assertNotEqual(city.to_dict(), city.__dict__)


if __name__ == "__main__":
    unittest.main()
