#!/usr/bin/python3
"""Test cases for FileStorage module"""
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases"""

    def setUp(self):
        """Create an instance of FileStorage"""
        self.storage = FileStorage()

    def tearDown(self):
        """Reset the __objects dictionary after each test"""
        FileStorage._FileStorage__objects = {}

    def test_file_path_attribute(self):
        """Test if __file_path attribute is set to the correct value"""
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_objects_attribute_empty(self):
        """Test if __objects attribute is an empty dictionary initially"""
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__objects, {})

    def test_objects_attribute_manipulation(self):
        """Test if __objects attribute stores objects correctly"""
        storage = FileStorage()
        # Add an object to __objects
        storage._FileStorage__objects["TestModel.123"] = "test_object"
        self.assertEqual(storage._FileStorage__objects["TestModel.123"],
                         "test_object")

    def test_all_method(self):
        """Test if all() method returns the __objects dictionary"""
        self.assertEqual(self.storage.all(), FileStorage._FileStorage__objects)

    def test_new_method(self):
        """Test if new() method correctly adds an object to __objects"""
        model = BaseModel()
        self.storage.new(model)
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertEqual(FileStorage._FileStorage__objects[key], model)

    def test_save_method(self):
        """Test if save() method correctly serializes objects to file"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as f:
            data = json.load(f)
            key = "{}.{}".format(model.__class__.__name__, model.id)
            self.assertEqual(data[key]['id'], model.id)

    def test_reload_method(self):
        """Test if reload() method correctly deserializes objects from file"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertEqual(self.storage.all()[key].id, model.id)

    def test_create_obj_by_class_name_method(self):
        """
        Test if create_obj_by_class_name() method correctly creates an object
        """
        class_name = 'BaseModel'
        obj_data = {'id': '123', 'name': 'test'}
        obj = self.storage.create_obj_by_class_name(class_name, **obj_data)
        self.assertIsInstance(obj, BaseModel)
        self.assertEqual(obj.id, '123')
        self.assertEqual(obj.name, 'test')


if __name__ == '__main__':
    unittest.main()
