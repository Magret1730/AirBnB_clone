#!/usr/bin/python3
"""Test cases for Review module"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review"""
    def test_instance_creation(self):
        """Test if you can create an instance of the Review class"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_attributes(self):
        """
        Test if the Review class has the 'place_id', 'user_id', and
        'text' attributes
        """
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_default_attributes(self):
        """
        Test if the 'place_id' and 'user_id' attributes have default values of
        an empty string
        and if 'text' has a default value of an empty string as well
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attribute_assignment(self):
        """
        Test if you can assign values to the 'place_id', 'user_id', and
        'text' attributes
        """
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Great place to stay!"
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Great place to stay!")

    def test_to_dict_method(self):
        """
        Test if the to_dict method returns a dictionary with the expected
        keys and values
        """
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Great place to stay!"
        review_dict = review.to_dict()
        expected_dict = {
                         '__class__': 'Review',
                         'id': review.id,
                         'created_at': review.created_at.isoformat(),
                         'updated_at': review.updated_at.isoformat(),
                         'place_id': '123',
                         'user_id': '456',
                         'text': 'Great place to stay!'
                         }
        self.assertDictEqual(review_dict, expected_dict)

    def test_from_dict_method(self):
        """
        Test if you can create an instance of the Review class
        from a dictionary
        """
        data = {
                '__class__': 'Review',
                'id': '12345',
                'created_at': '2023-09-15T12:00:00.000000',
                'updated_at': '2023-09-15T13:00:00.000000',
                'place_id': '789',
                'user_id': '101',
                'text': 'Enjoyed my stay!'
               }
        review = FileStorage.create_obj_by_class_name(data['__class__'],
                                                      **data)
        self.assertIsInstance(review, Review)
        self.assertEqual(review.id, '12345')
        self.assertEqual(review.place_id, '789')
        self.assertEqual(review.user_id, '101')
        self.assertEqual(review.text, 'Enjoyed my stay!')


if __name__ == '__main__':
    unittest.main()
