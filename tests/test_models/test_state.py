#!/usr/bin/python3
"""Test cases for State module"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State"""
    def test_instance_creation(self):
        """
        Test to check that you can create an instance of the State class
        and verify that it inherits from BaseModel.
        """
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertIsInstance(state, State)

    def test_default_name_attribute(self):
        """
        Test to ensure that the State class has the name attribute
        and that it's an empty string by default.
        """
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_name_assignment(self):
        """
        Test to verify that you can assign a value to the name attribute
        and retrieve it correctly.
        """
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_to_dict_method(self):
        """
        Test to check that the to_dict method returns a dictionary
        with the expected keys and values.
        """
        state = State()
        state.name = "New York"
        state_dict = state.to_dict()
        expected_dict = {
                         '__class__': 'State',
                         'id': state.id,
                         'created_at': state.created_at.isoformat(),
                         'updated_at': state.updated_at.isoformat(),
                         'name': 'New York'
                        }
        self.assertDictEqual(state_dict, expected_dict)

    def test_from_dict_method(self):
        """
        Test: Ensure that you can create an instance of the State
        class from a dictionary.
        """
        data = {
                '__class__': 'State',
                'id': '12345',
                'created_at': '2023-09-15T12:00:00.000000',
                'updated_at': '2023-09-15T13:00:00.000000',
                'name': 'Florida'
               }
        state = FileStorage.create_obj_by_class_name(data['__class__'], **data)
        self.assertIsInstance(state, State)
        self.assertEqual(state.id, '12345')
        self.assertEqual(state.name, 'Florida')


if __name__ == '__main__':
    unittest.main()
