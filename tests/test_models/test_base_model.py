#!/usr/bin/python3
"""
Test cases for base model module
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for base model module
    """

    def setUp(self):
        """Setup for the test cases"""
        self.base_model = BaseModel()

    """IDs"""
    def test_id_attr(self):
        """Id attribute"""
        self.assertTrue(hasattr(self.base_model, 'id'))

    def test_id_str(self):
        """id is a str"""
        self.assertIsInstance(self.base_model.id, str)

    def test_id_unique(self):
        """uniqueness of the ids"""
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_custom_id(self):
        """assigning id"""
        custom_id = "my_custom_id"
        base_model = BaseModel(id=custom_id)
        self.assertEqual(base_model.id, custom_id)

    """created_at"""
    def test_created_attr(self):
        """if BaseModel() has attr created_at"""
        self.assertTrue(hasattr(self.base_model, 'created_at'))

    def test_created_datetime(self):
        """if datetime is an instance of created_at"""
        self.assertIsInstance(self.base_model.created_at, datetime)

    """updated_at"""
    def test_updated_attr(self):
        """if BaseModel() has attr updated_at"""
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_created_datetime(self):
        """if datetime is an instance of updated_at"""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    """__str__ representation"""
    def test_str_representation(self):
        """__str__ representation"""
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id,
                                                    self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    """save"""
    def test_save_method(self):
        """test for save"""
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    """dict"""
    def test_to_dict(self):
        """instance of dict"""
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)

    def test_dict_class(self):
        """class"""
        model_dict = self.base_model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_dict_created_at(self):
        """created_at an isoformat()"""
        model_dict = self.base_model.to_dict()
        self.assertEqual(model_dict['created_at'],
                         self.base_model.created_at.isoformat())

    def test_dict_updated_at(self):
        """updated_at an isoformat()"""
        model_dict = self.base_model.to_dict()
        self.assertEqual(model_dict['updated_at'],
                         self.base_model.updated_at.isoformat())

    """kwargs"""
    def test_kwargs_initialization(self):
        data = {
                'id': '12345',
                'created_at': '2023-09-15T12:00:00.000000',
                'updated_at': '2023-09-15T13:00:00.000000',
                'custom_attr': 'custom_value'
                }
        model_with_kwargs = BaseModel(**data)
        self.assertEqual(model_with_kwargs.id, '12345')
        self.assertEqual(model_with_kwargs.created_at,
                         datetime(2023, 9, 15, 12, 0))
        self.assertEqual(model_with_kwargs.updated_at,
                         datetime(2023, 9, 15, 13, 0))
        self.assertEqual(model_with_kwargs.custom_attr, 'custom_value')


if __name__ == '__main__':
    unittest.main()
