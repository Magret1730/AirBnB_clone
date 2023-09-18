#!/usr/bin/python3
"""A test module for User"""
import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test cases for User"""
    def setUp(self):
        """setups"""
        self.user = User()
        self.user.email = "test@example.com"
        self.user.password = "password"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

    def test_user_attributes(self):
        """Testing user attributes"""
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_user_inheritance(self):
        """Testinf user inheritance"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str(self):
        """Testing str"""
        user_str = str(self.user)
        self.assertIn("[User] ({})".format(self.user.id), user_str)
        self.assertIn("'email': 'test@example.com'", user_str)
        self.assertIn("'password': 'password'", user_str)
        self.assertIn("'first_name': 'John'", user_str)
        self.assertIn("'last_name': 'Doe'", user_str)

    def test_user_to_dict(self):
        """User to dict"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], "User")
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "password")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")


if __name__ == "__main__":
    unittest.main()
