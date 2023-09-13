#!/usr/bin/python3
"""A Module inherited from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """A User Module"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
