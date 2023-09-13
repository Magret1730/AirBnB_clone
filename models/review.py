#!/usr/bin/python3
"""A module for Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class for Review"""
    place_id = ""
    user_id = ""
    text = ""
