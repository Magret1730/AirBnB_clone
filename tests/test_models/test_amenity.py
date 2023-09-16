#!/usr/bin/python3
"""Test cases for Amenity module"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity


class TestState(unittest.TestCase):
    """Test cases for Amenity"""
    def test_instance_creation(self):
        """Test if you can create an instance of the Amenity class"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_attributes(self):
        """Test if the Amenity class has the 'name' attribute"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))

    def test_default_name_attribute(self):
        """
        Test if the 'name' attribute has a default value of
        an empty string
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_name_assignment(self):
        """Test if you can assign a value to the 'name' attribute"""
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_to_dict_method(self):
        """
        Test if the to_dict method returns a dictionary
        with the expected keys and values
        """
        amenity = Amenity()
        amenity.name = "Gym"
        amenity_dict = amenity.to_dict()
        expected_dict = {
            '__class__': 'Amenity',
            'id': amenity.id,
            'created_at': amenity.created_at.isoformat(),
            'updated_at': amenity.updated_at.isoformat(),
            'name': 'Gym'
        }
        self.assertDictEqual(amenity_dict, expected_dict)

    def test_from_dict_method(self):
        """
        Test if you can create an instance of the Amenity
        class from a dictionary
        """
        data = {
                '__class__': 'Amenity',
                'id': '12345',
                'created_at': '2023-09-15T12:00:00.000000',
                'updated_at': '2023-09-15T13:00:00.000000',
                'name': 'Spa'
               }
        amenity = FileStorage.create_obj_by_class_name(data['__class__'],
                                                       **data)
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.id, '12345')
        self.assertEqual(amenity.name, 'Spa')


if __name__ == '__main__':
    unittest.main()
