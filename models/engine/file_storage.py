#!/usr/bin/python3
"""File storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        serialized_obj = {key: obj.to_dict()
                          for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, mode='w', encoding='UTF8')as f:
            json.dump(serialized_obj, f)

    @staticmethod
    def create_obj_by_class_name(class_name, **kwargs):
        """
        Dynamically create an object based on the class name and
        initialize it with the provided attributes.
        """
        class_mapping = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }
        if class_name in class_mapping:
            obj_class = class_mapping[class_name]
            obj = obj_class(**kwargs)
            return obj
        else:
            raise ValueError(
                    "Class '{}' not found in class_mapping").format(class_name)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode='r') as f:
                data = json.load(f)
                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    obj = FileStorage.create_obj_by_class_name(class_name,
                                                               **obj_data)
                    FileStorage.__objects[key] = obj
        except IOError:
            pass
