#!/usr/bin/python3
"""Test cases for Place module"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for Place"""
    def test_instance_creation(self):
        """Test if you can create an instance of the Place class"""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_attributes(self):
        """Test if the Place class has all the expected attributes"""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

    def test_default_attributes(self):
        """Test if the numeric attributes have default values of 0"""
        place = Place()
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)

    def test_attribute_assignment(self):
        """Test if you can assign values to the attributes"""
        place = Place()
        place.city_id = "123"
        place.user_id = "456"
        place.name = "Cozy Cottage"
        place.description = "A charming cottage by the beach"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 34.0567
        place.longitude = -118.2421
        place.amenity_ids = ["amenity1", "amenity2"]

        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Cozy Cottage")
        self.assertEqual(place.description, "A charming cottage by the beach")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 34.0567)
        self.assertEqual(place.longitude, -118.2421)
        self.assertEqual(place.amenity_ids, ["amenity1", "amenity2"])

    def test_to_dict_method(self):
        """
        Test if the to_dict method returns a dictionary with
        the expected keys and values
        """
        place = Place()
        place.city_id = "123"
        place.user_id = "456"
        place.name = "Cozy Cottage"
        place.description = "A charming cottage by the beach"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 34.0567
        place.longitude = -118.2421
        place.amenity_ids = ["amenity1", "amenity2"]

        place_dict = place.to_dict()
        expected_dict = {
                         '__class__': 'Place',
                         'id': place.id,
                         'created_at': place.created_at.isoformat(),
                         'updated_at': place.updated_at.isoformat(),
                         'city_id': '123',
                         'user_id': '456',
                         'name': 'Cozy Cottage',
                         'description': 'A charming cottage by the beach',
                         'number_rooms': 2,
                         'number_bathrooms': 1,
                         'max_guest': 4,
                         'price_by_night': 100,
                         'latitude': 34.0567,
                         'longitude': -118.2421,
                         'amenity_ids': ["amenity1", "amenity2"]
                        }
        self.assertDictEqual(place_dict, expected_dict)

    def test_from_dict_method(self):
        """Test if you can create an instance of the
        Place class from a dictionary
        """
        data = {
                '__class__': 'Place',
                'id': '12345',
                'created_at': '2023-09-15T12:00:00.000000',
                'updated_at': '2023-09-15T13:00:00.000000',
                'city_id': '789',
                'user_id': '101',
                'name': 'Beach House',
                'description': 'A beautiful beachfront house',
                'number_rooms': 3,
                'number_bathrooms': 2,
                'max_guest': 6,
                'price_by_night': 200,
                'latitude': 34.1234,
                'longitude': -118.5678,
                'amenity_ids': ["amenity3", "amenity4"]
               }
        place = FileStorage.create_obj_by_class_name(data['__class__'],
                                                     **data)
        self.assertIsInstance(place, Place)
        self.assertEqual(place.id, '12345')
        self.assertEqual(place.city_id, '789')
        self.assertEqual(place.user_id, '101')
        self.assertEqual(place.name, 'Beach House')
        self.assertEqual(place.description, 'A beautiful beachfront house')
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 200)
        self.assertEqual(place.latitude, 34.1234)
        self.assertEqual(place.longitude, -118.5678)
        self.assertEqual(place.amenity_ids, ["amenity3", "amenity4"])


if __name__ == '__main__':
    unittest.main()
