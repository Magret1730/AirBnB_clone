#!/usr/bin/python3
"""An AIRBNB Package"""
from datetime import datetime
import uuid


class BaseModel:
    """
    Class BaseModel that defines common
    attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value,
                                                '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        if not kwargs:
            from models import storage
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id,
            self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
        'updated_at' with the current datetime.
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance.
        """
        d = dict(self.__dict__)
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return (d)
    
