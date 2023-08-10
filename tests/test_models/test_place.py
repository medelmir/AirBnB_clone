#!/usr/bin/python3
"""This module defines unittests for the 'models/place.py'.

Unittest classes:
    -TestPlaceInstantiation: Testing for instantiation of the place class.
    -TestPlaceSave: Testing for the 'save' method of the place class.
    -TestPlaceToDict: Testing for the 'To_dict' method of the place class.
"""
import unittest
import os
from datetime import datetime
from time import sleep
import models
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for instantiation of the Place class."""

    def test_place_instantiation_no_args(self):
        """Test that a place instance is created with no args."""
        self.assertEqual(Place, type(Place()))

    def test_place_new_instance_stored(self):
        """
        Test that a newly created Place instance is stored
        in the objects dictionary.
        """
        self.assertIn(Place(), models.storage.all().values())

    def test_place_id_is_public_str(self):
        """Test if the id attribute of a place instance is a string."""
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_datetime(self):
        """
        Test if the created_at attribute of a Place instance
        is an instance of datetime.
        """
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_datetime(self):
        """
        Test if the updated_at attribute of a Place instance
        is an instance of datetime.
        """
        self.assertEqual(datetime, type(Place().updated_at))

    def test_two_places_is_unique_id(self):
        """Test if two Place instances have unique id."""
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_two_places_created_at(self):
        """
        Test if two Place instances have different 'created_at' timestamps.
        """
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertNotEqual(place1.created_at, place2.created_at)

    def test_two_places_updated_at(self):
        """
        Test if two Place instances have different 'updated_at' timestamps.
        """
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertNotEqual(place1.updated_at, place2.updated_at)

    def test_place_name_is_public_cls_attr(self):
        """
        Test if the name attribute of a place instance
        is a public class attribute.
        """
        place = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(place))
        self.assertNotIn("name", place.__dict__)

    def test_user_id_is_public_cls_attr(self):
        """
        Test if the user id attribute of a place instance
        is a public class attribute.
        """
        place = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(place))
        self.assertNotIn("user_id", place.__dict__)

    def test_city_id_is_public_cls_attr(self):
        """
        Test if the city id attribute of a place instance
        is a public class attribute.
        """
        place = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(place))
        self.assertNotIn("city_id", place.__dict__)

    def test_description_is_public_cls_attr(self):
        """
        Test if the description attribute of a place instance
        is a public class attribute.
        """
        place = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(place))
        self.assertNotIn("description", place.__dict__)

    def test_num_rooms_is_public_cls_attr(self):
        """
        Test if the number rooms attribute of a place instance
        is a public class attribute.
        """
        place = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(place))
        self.assertNotIn("number_rooms", place.__dict__)

    def test_max_guest_is_public_cls_attr(self):
        """
        Test if the max guest attribute of a place instance
        is a public class attribute.
        """
        place = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(place))
        self.assertNotIn("max_guest", place.__dict__)

    def test_price_by_night_is_public_cls_attr(self):
        """
        Test if the price_by_night attribute of a place instance
        is a public class attribute.
        """
        place = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(place))
        self.assertNotIn("price_by_night", place.__dict__)

    def test_latitude_is_public_cls_attr(self):
        """
        Test if the latitude attribute of a place instance
        is a public class attribute.
        """
        place = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(place))
        self.assertNotIn("latitude", place.__dict__)

    def test_longitude_is_public_cls_attr(self):
        """
        Test if the longitude attribute of a place instance
        is a public class attribute.
        """
        place = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(place))
        self.assertNotIn("longitude", place.__dict__)

    def test_amenity_ids_is_public_cls_attr(self):
        """
        Test if the amenity ids attribute of a place instance
        is a public class attribute.
        """
        place = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(place))
        self.assertNotIn("amenity_ids", place.__dict__)

    def test_place_no_args(self):
        """Test that positional arguments are unused."""
        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def test_place_instantiation_with_kwargs(self):
        """
        Test if a Place instance can be created with keyword arguments.
        """
        timestamp = datetime.now()
        dt_format = timestamp.isoformat()
        dt_obj = datetime.fromisoformat(dt_format)
        place = Place(id="0123", created_at=dt_format, updated_at=dt_format)
        self.assertEqual(place.id, "0123")
        self.assertEqual(place.created_at, dt_obj)
        self.assertEqual(place.updated_at, dt_obj)

    def test_place_instantiation_with_none_kwargs(self):
        """
        Test if a Place instance can be created with None keyword arguments.
        """
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_place_str_representation(self):
        """Test the str representation of a Place instance."""
        timestamp = datetime.now()
        dt_repr = repr(timestamp)
        place = Place()
        place.id = "0123"
        place.created_at = place.updated_at = timestamp
        place_str = place.__str__()
        self.assertIn("[Place] (0123)", place_str)
        self.assertIn("'id': '0123'", place_str)
        self.assertIn("'created_at': " + dt_repr, place_str)
        self.assertIn("'updated_at': " + dt_repr, place_str)


class TestPlace_save_method(unittest.TestCase):
    """Unittests for the 'save' method of the Place class."""

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
        place = Place()
        sleep(0.05)
        test_updated_at = place.updated_at
        place.save()
        self.assertLess(test_updated_at, place.updated_at)

    def test_save_method_two_update(self):
        """
        Test that the 'save' method updates the updated_at attribute.
        """
        place = Place()
        sleep(0.05)
        test_updated_at = place.updated_at
        place.save()
        test2_updated_at = place.updated_at
        self.assertLess(test_updated_at, place.updated_at)
        sleep(0.05)
        place.save()
        self.assertLess(test2_updated_at, place.updated_at)

    def test_save_method_with_arg(self):
        """
        Test if 'save' method raises a TypeError when called with an arg.
        """
        place = Place()
        with self.assertRaises(TypeError):
            place.save(None)

    def test_save_method_update_file(self):
        """Test if the `save` method updates the file."""
        place = Place()
        place.save()
        place_id = "Place." + place.id
        with open("data.json", "r") as file:
            self.assertIn(place_id, file.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for 'to_dict' method of the Place class."""

    def test_to_dict_method_type(self):
        """
        Test if the return value of the `to_dict` method is a dictionary.
        """
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_method_correct_keys(self):
        """
        Test if the return value of the `to_dict` method is a dictionary.
        with the correct keys.
        """
        place = Place()
        self.assertIn("id", place.to_dict())
        self.assertIn("created_at", place.to_dict())
        self.assertIn("updated_at", place.to_dict())
        self.assertIn("__class__", place.to_dict())

    def test_to_dict_method_added_attributes(self):
        """
        Test if the 'to_dict' method includes added attributes
        in the dictionary.
        """
        place = Place()
        place.style = "Modern"
        place.bath = 4
        self.assertEqual("Modern", place.style)
        self.assertIn("bath", place.to_dict())

    def test_to_dict_method_with_arg(self):
        """
        Test if the 'save' method raises a TypeError when called with args.
        """
        place = Place()
        with self.assertRaises(TypeError):
            place.to_dict(None)

    def test_to_dict_method_datetime_attr_are_strs(self):
        """
        Test if the 'to_dict' method datetime attributes
        are strings in the dictionary.
        """
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(str, type(place_dict["id"]))
        self.assertEqual(str, type(place_dict["created_at"]))
        self.assertEqual(str, type(place_dict["updated_at"]))

    def test_to_dict_method_output(self):
        """Test the 'to_dict' method output."""
        timestamp = datetime.now()
        place = Place()
        place.id = "0123"
        place.created_at = place.updated_at = timestamp
        test_to_dict = {
            'id': '0123',
            '__class__': 'Place',
            'created_at': timestamp.isoformat(),
            'updated_at': timestamp.isoformat(),
        }
        self.assertDictEqual(place.to_dict(), test_to_dict)

    def test_to_dict_method_no_dunder_dict(self):
        """
        Test if the 'to_dict' does not return the internal
        attribute dictionary.
        """
        place = Place()
        self.assertNotEqual(place.to_dict(), place.__dict__)


if __name__ == "__main__":
    unittest.main()
