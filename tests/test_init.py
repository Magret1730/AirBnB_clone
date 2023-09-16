#!/usr/bin/python3
"""init module"""
import unittest
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from models import storage
from models import __init__


class TestInit(unittest.TestCase):
    """Test cases for init """
    def test_file_storage_instance(self):
        """Test that a FileStorage instance is created"""
        self.assertIsInstance(storage, FileStorage)


if __name__ == '__main__':
    unittest.main()
