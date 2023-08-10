#!/usr/bin/python3
"""This module defines unittests for the 'models/state.py'.

Unittest classes:
    -TestStateInstantiation: Testing for instantiation of the State class.
    -TestStateSave: Testing for the 'save' method of the State class.
    -TestStateToDict: Testing for the 'To_dict' method of the State class.
"""
import unittest
import os
from datetime import datetime
from time import sleep
import models
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests for instantiation of the State class."""

    def test_state_instantiation_no_args(self):
        """Test that a state instance is created with no args."""
        self.assertEqual(State, type(State()))

    def test_state_new_instance_stored(self):
        """
        Test that a newly created State instance is stored
        in the objects dictionary.
        """
        self.assertIn(State(), models.storage.all().values())

    def test_state_id_is_public_str(self):
        """Test if the id attribute of a state instance is a string."""
        self.assertEqual(str, type(State().id))

    def test_created_at_is_datetime(self):
        """
        Test if the created_at attribute of a State instance
        is an instance of datetime.
        """
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_datetime(self):
        """
        Test if the updated_at attribute of a State instance
        is an instance of datetime.
        """
        self.assertEqual(datetime, type(State().updated_at))

    def test_two_states_is_unique_id(self):
        """Test if two State instances have unique id."""
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_two_states_created_at(self):
        """
        Test if two State instances have different 'created_at' timestamps.
        """
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertNotEqual(state1.created_at, state2.created_at)

    def test_two_states_updated_at(self):
        """
        Test if two State instances have different 'updated_at' timestamps.
        """
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertNotEqual(state1.updated_at, state2.updated_at)

    def test_state_name_is_public_cls_attr(self):
        """
        Test if the name attribute of a state instance
        is a public class attribute.
        """
        state = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state.__dict__)

    def test_state_no_args(self):
        """Test that positional arguments are unused."""
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_state_instantiation_with_kwargs(self):
        """
        Test if a State instance can be created with keyword arguments.
        """
        timestamp = datetime.now()
        dt_format = timestamp.isoformat()
        dt_obj = datetime.fromisoformat(dt_format)
        state = State(id="0123", created_at=dt_format, updated_at=dt_format)
        self.assertEqual(state.id, "0123")
        self.assertEqual(state.created_at, dt_obj)
        self.assertEqual(state.updated_at, dt_obj)

    def test_state_instantiation_with_none_kwargs(self):
        """
        Test if a State instance can be created with None keyword arguments.
        """
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_state_str_representation(self):
        """Test the str representation of a State instance."""
        timestamp = datetime.now()
        dt_repr = repr(timestamp)
        state = State()
        state.id = "0123"
        state.created_at = state.updated_at = timestamp
        state_str = state.__str__()
        self.assertIn("[State] (0123)", state_str)
        self.assertIn("'id': '0123'", state_str)
        self.assertIn("'created_at': " + dt_repr, state_str)
        self.assertIn("'updated_at': " + dt_repr, state_str)


class TestState_save_method(unittest.TestCase):
    """Unittests for the 'save' method of the State class."""

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
        state = State()
        sleep(0.05)
        test_updated_at = state.updated_at
        state.save()
        self.assertLess(test_updated_at, state.updated_at)

    def test_save_method_two_update(self):
        """
        Test that the 'save' method updates the updated_at attribute.
        """
        state = State()
        sleep(0.05)
        test_updated_at = state.updated_at
        state.save()
        test2_updated_at = state.updated_at
        self.assertLess(test_updated_at, state.updated_at)
        sleep(0.05)
        state.save()
        self.assertLess(test2_updated_at, state.updated_at)

    def test_save_method_with_arg(self):
        """
        Test if 'save' method raises a TypeError when called with an arg.
        """
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)

    def test_save_method_update_file(self):
        """Test if the `save` method updates the file."""
        state = State()
        state.save()
        state_id = "State." + state.id
        with open("data.json", "r") as file:
            self.assertIn(state_id, file.read())


class TestState_to_dict(unittest.TestCase):
    """Unittests for 'to_dict' method of the State class."""

    def test_to_dict_method_type(self):
        """
        Test if the return value of the `to_dict` method is a dictionary.
        """
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_method_correct_keys(self):
        """
        Test if the return value of the `to_dict` method is a dictionary.
        with the correct keys.
        """
        state = State()
        self.assertIn("id", state.to_dict())
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())
        self.assertIn("__class__", state.to_dict())

    def test_to_dict_method_added_attributes(self):
        """
        Test if the 'to_dict' method includes added attributes
        in the dictionary.
        """
        state = State()
        state.region = "Silicon Valley"
        state.rank = 21
        self.assertEqual("Silicon Valley", state.region)
        self.assertIn("rank", state.to_dict())

    def test_to_dict_method_with_arg(self):
        """
        Test if the 'save' method raises a TypeError when called with args.
        """
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)

    def test_to_dict_method_datetime_attr_are_strs(self):
        """
        Test if the 'to_dict' method datetime attributes
        are strings in the dictionary.
        """
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(str, type(state_dict["id"]))
        self.assertEqual(str, type(state_dict["created_at"]))
        self.assertEqual(str, type(state_dict["updated_at"]))

    def test_to_dict_method_output(self):
        """Test the 'to_dict' method output."""
        timestamp = datetime.now()
        state = State()
        state.id = "0123"
        state.created_at = state.updated_at = timestamp
        test_to_dict = {
            'id': '0123',
            '__class__': 'State',
            'created_at': timestamp.isoformat(),
            'updated_at': timestamp.isoformat(),
        }
        self.assertDictEqual(state.to_dict(), test_to_dict)

    def test_to_dict_method_no_dunder_dict(self):
        """
        Test if the 'to_dict' does not return the internal
        attribute dictionary.
        """
        state = State()
        self.assertNotEqual(state.to_dict(), state.__dict__)


if __name__ == "__main__":
    unittest.main()
