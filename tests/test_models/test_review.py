#!/usr/bin/python3
"""This module defines unittests for the 'models/review.py'.

Unittest classes:
    -TestReviewInstantiation: Testing for instantiation of the Review class.
    -TestReviewSave: Testing for the 'save' method of the Review class.
    -TestReviewToDict: Testing for the 'To_dict' method of the Review class.
"""
import unittest
import os
from datetime import datetime
from time import sleep
import models
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests for instantiation of the Review class."""

    def test_review_instantiation_no_args(self):
        """Test that a review instance is created with no args."""
        self.assertEqual(Review, type(Review()))

    def test_review_new_instance_stored(self):
        """
        Test that a newly created Review instance is stored
        in the objects dictionary.
        """
        self.assertIn(Review(), models.storage.all().values())

    def test_review_id_is_public_str(self):
        """Test if the id attribute of a review instance is a string."""
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_datetime(self):
        """
        Test if the created_at attribute of a Review instance
        is an instance of datetime.
        """
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_datetime(self):
        """
        Test if the updated_at attribute of a Review instance
        is an instance of datetime.
        """
        self.assertEqual(datetime, type(Review().updated_at))

    def test_two_reviews_is_unique_id(self):
        """Test if two Review instances have unique id."""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_two_reviews_created_at(self):
        """
        Test if two Review instances have different 'created_at' timestamps.
        """
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertNotEqual(review1.created_at, review2.created_at)

    def test_two_reviews_updated_at(self):
        """
        Test if two Review instances have different 'updated_at' timestamps.
        """
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertNotEqual(review1.updated_at, review2.updated_at)

    def test_review_place_id_is_public_cls_attr(self):
        """
        Test if the place id attribute of a review instance
        is a public class attribute.
        """
        review = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(review))
        self.assertNotIn("place_id", review.__dict__)

    def test_review_user_id_is_public_cls_attr(self):
        """
        Test if the user id attribute of a review instance
        is a public class attribute.
        """
        review = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(review))
        self.assertNotIn("user_id", review.__dict__)

    def test_review_text_is_public_cls_attr(self):
        """
        Test if the text attribute of a review instance
        is a public class attribute.
        """
        review = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(review))
        self.assertNotIn("text", review.__dict__)

    def test_review_no_args(self):
        """Test that positional arguments are unused."""
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def test_review_instantiation_with_kwargs(self):
        """
        Test if a Review instance can be created with keyword arguments.
        """
        timestamp = datetime.now()
        dt_format = timestamp.isoformat()
        dt_obj = datetime.fromisoformat(dt_format)
        review = Review(id="0123", created_at=dt_format, updated_at=dt_format)
        self.assertEqual(review.id, "0123")
        self.assertEqual(review.created_at, dt_obj)
        self.assertEqual(review.updated_at, dt_obj)

    def test_review_instantiation_with_none_kwargs(self):
        """
        Test if a Review instance can be created with None keyword arguments.
        """
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_review_str_representation(self):
        """Test the str representation of a Review instance."""
        timestamp = datetime.now()
        dt_repr = repr(timestamp)
        review = Review()
        review.id = "0123"
        review.created_at = review.updated_at = timestamp
        review_str = review.__str__()
        self.assertIn("[Review] (0123)", review_str)
        self.assertIn("'id': '0123'", review_str)
        self.assertIn("'created_at': " + dt_repr, review_str)
        self.assertIn("'updated_at': " + dt_repr, review_str)


class TestReview_save_method(unittest.TestCase):
    """Unittests for the 'save' method of the Review class."""

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
        review = Review()
        sleep(0.05)
        test_updated_at = review.updated_at
        review.save()
        self.assertLess(test_updated_at, review.updated_at)

    def test_save_method_two_update(self):
        """
        Test that the 'save' method updates the updated_at attribute.
        """
        review = Review()
        sleep(0.05)
        test_updated_at = review.updated_at
        review.save()
        test2_updated_at = review.updated_at
        self.assertLess(test_updated_at, review.updated_at)
        sleep(0.05)
        review.save()
        self.assertLess(test2_updated_at, review.updated_at)

    def test_save_method_with_arg(self):
        """
        Test if 'save' method raises a TypeError when called with an arg.
        """
        review = Review()
        with self.assertRaises(TypeError):
            review.save(None)

    def test_save_method_update_file(self):
        """Test if the `save` method updates the file."""
        review = Review()
        review.save()
        review_id = "Review." + review.id
        with open("data.json", "r") as file:
            self.assertIn(review_id, file.read())


class TestReview_to_dict(unittest.TestCase):
    """Unittests for 'to_dict' method of the Review class."""

    def test_to_dict_method_type(self):
        """
        Test if the return value of the `to_dict` method is a dictionary.
        """
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_method_correct_keys(self):
        """
        Test if the return value of the `to_dict` method is a dictionary.
        with the correct keys.
        """
        review = Review()
        self.assertIn("id", review.to_dict())
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())
        self.assertIn("__class__", review.to_dict())

    def test_to_dict_method_added_attributes(self):
        """
        Test if the 'to_dict' method includes added attributes
        in the dictionary.
        """
        review = Review()
        review.user_name = "Python"
        review.stars = 5
        self.assertEqual("Python", review.user_name)
        self.assertIn("stars", review.to_dict())

    def test_to_dict_method_with_arg(self):
        """
        Test if the 'save' method raises a TypeError when called with args.
        """
        review = Review()
        with self.assertRaises(TypeError):
            review.to_dict(None)

    def test_to_dict_method_datetime_attr_are_strs(self):
        """
        Test if the 'to_dict' method datetime attributes
        are strings in the dictionary.
        """
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(str, type(review_dict["id"]))
        self.assertEqual(str, type(review_dict["created_at"]))
        self.assertEqual(str, type(review_dict["updated_at"]))

    def test_to_dict_method_output(self):
        """Test the 'to_dict' method output."""
        timestamp = datetime.now()
        review = Review()
        review.id = "0123"
        review.created_at = review.updated_at = timestamp
        test_to_dict = {
            'id': '0123',
            '__class__': 'Review',
            'created_at': timestamp.isoformat(),
            'updated_at': timestamp.isoformat(),
        }
        self.assertDictEqual(review.to_dict(), test_to_dict)

    def test_to_dict_method_no_dunder_dict(self):
        """
        Test if the 'to_dict' does not return the internal
        attribute dictionary.
        """
        review = Review()
        self.assertNotEqual(review.to_dict(), review.__dict__)


if __name__ == "__main__":
    unittest.main()
