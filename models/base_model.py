#!/usr/bin/env Python3
"""An AIRBNB console package"""
import uuid
import datetime


class BaseModel:
    """
    Class BaseModel that defines all common attributes
    methods for other classes
    """

    def __init__(self, id, created_at, updated_at):
        """Constructor."""
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        prints: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance:
        """
        d = {}
        d.update(self.__dict__)
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
