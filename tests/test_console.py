#!/usr/bin/python3
"""Test cases for console module"""
from console import HBNBCommand
from io import StringIO
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from unittest.mock import patch
import unittest


class TestConsole(unittest.TestCase):
    """Test cases for console"""
    def test_execute_basic_commands(self):
        """
        Test that the console can execute basic commands without errors
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue().strip()
            self.assertNotEqual(output, "")

    def test_create_commands(self):
        """
        Test the create command for each class.
        """
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                   "Review"]
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {class_name}")
                output = f.getvalue().strip()
                self.assertNotEqual(output, "")

    def test_show_commands(self):
        """
        Test the show command for each class.
        """
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                   "Review"]
        obj_id = "12345"
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"show {class_name} {obj_id}")
                output = f.getvalue().strip()
                self.assertNotEqual(output, "")

    def test_destroy_commands(self):
        """
        Test the destroy command for each class.
        """
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                   "Review"]
        obj_id = "12345"
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"destroy {class_name} {obj_id}")
                output = f.getvalue().strip()
                self.assertNotEqual(output, "")

    def test_all_commands(self):
        """
        Test the all command for each class.
        """
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                   "Review"]
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"all {class_name}")
                output = f.getvalue().strip()
                self.assertNotEqual(output, "")

    def test_update_commands(self):
        """
        Test the update command for each class.
        """
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                   "Review"]
        obj_id = "12345"
        attribute_name = "name"
        attribute_value = "New Value"
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"update {class_name} {obj_id}\
                    {attribute_name} '{attribute_value}'")
                output = f.getvalue().strip()
                self.assertNotEqual(output, "")

    def test_count_commands(self):
        """
        Test the count command for each class.
        """
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                   "Review"]
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"{class_name}.count()")
                output = f.getvalue().strip()
                self.assertNotEqual(output, "")

    def test_quit_and_eof_commands(self):
        """
        Test the quit and EOF commands for exiting the console.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_invalid_command(self):
        """"
        Test for an invalid command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("invalid_command")
            output = f.getvalue().strip()
            self.assertEqual(output, "*** Unknown syntax: invalid_command")

    def test_missing_class_name_create(self):
        """
        Test for missing class name in the create command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_invalid_class_name_create(self):
        """
        Test for providing an invalid class name in the create command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create InvalidClass")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_missing_object_id_show(self):
        """
        Test for missing object ID in the show command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_invalid_object_id_show(self):
        """
        Test for providing an invalid object ID in the show command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel InvalidID")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_missing_class_name_destroy(self):
        """
        Test for missing class name in the destroy command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_invalid_class_name_destroy(self):
        """
        Test for providing an invalid class name in the destroy command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy InvalidClass 12345")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_missing_object_id_destroy(self):
        """
        Test for missing object ID in the destroy command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_invalid_object_id_destroy(self):
        """
        Test for providing an invalid object ID in the destroy command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel InvalidID")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    """def test_invalid_object_id_update(self):
        Test for providing an invalid object ID in the update command.
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel \
                                 InvalidID attribute_name 'value'")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")"""

    def test_empty_line_input(self):
        """
        Test for an empty line as input, which should be ignored.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            output = f.getvalue().strip()
            self.assertEqual(output, "")


if __name__ == '__main__':
    unittest.main()
