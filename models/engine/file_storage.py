#!/usr/bin/python3
"""File storage"""
from models.base_model import BaseModel
from models.user import User
import json


class FileStorage:
    """
    serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    def __init__(self, file_path):
        """
        Constructor.
        """
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        (path: __file_path)
        """
        serialized_obj = {key: obj.to_dict()
                          for key, obj in self.__objects.items()}
        with open(self.__file_path, mode='w', encoding='UTF8')as f:
            json.dump(serialized_obj, f)

    def create_obj_by_class_name(self, class_name, **kwargs):
        """
        Dynamically create an object based on the class name and
        initialize it with the provided attributes.
        """
        class_mapping = {
            'BaseModel': BaseModel,
            'User': User
            }
        if class_name in class_mapping:
            obj_class = class_mapping[class_name]
            obj = obj_class(**kwargs)
            return obj
        else:
            raise ValueError(
                    f"Class '{class_name}' not found in class_mapping")

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, mode='r', encoding='UTF8') as f:
                data = json.load(f)
                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    obj = self.create_obj_by_class_name(class_name, **obj_data)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
