#!/usr/bin/python3
"""Test cases for City module"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.city import City


class TestState(unittest.TestCase):
    """Test cases for City"""
    def test_instance_creation(self):
        """Test if you can create an instance of the City class"""
        city = City()
        self.assertIsInstance(city, City)

    def test_attributes(self):
        """Test if City class has the 'state_id' and 'name' attributes"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_default_attributes(self):
        """Test if 'state_id' and 'name' attributes have default values"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attribute_assignment(self):
        """Test if you can assign values to 'state_id' and 'name' attributes"""
        city = City()
        city.state_id = "123"
        city.name = "New York"
        self.assertEqual(city.state_id, "123")
        self.assertEqual(city.name, "New York")

    def test_to_dict_method(self):
        """
        Test if the to_dict method returns a dictionary
        with the expected keys and value
        """
        city = City()
        city.state_id = "123"
        city.name = "New York"
        city_dict = city.to_dict()
        expected_dict = {
                        '__class__': 'City',
                        'id': city.id,
                        'created_at': city.created_at.isoformat(),
                        'updated_at': city.updated_at.isoformat(),
                        'state_id': '123',
                        'name': 'New York'
                        }
        self.assertDictEqual(city_dict, expected_dict)

    def test_from_dict_method(self):
        """
        Test if you can create an instance of the
        City class from a dictionary
        """
        data = {
                '__class__': 'City',
                'id': '12345',
                'created_at': '2023-09-15T12:00:00.000000',
                'updated_at': '2023-09-15T13:00:00.000000',
                'state_id': '567',
                'name': 'Los Angeles'
               }
        city = FileStorage.create_obj_by_class_name(data['__class__'],
                                                    **data)
        self.assertIsInstance(city, City)
        self.assertEqual(city.id, '12345')
        self.assertEqual(city.state_id, '567')
        self.assertEqual(city.name, 'Los Angeles')


if __name__ == '__main__':
    unittest.main()
