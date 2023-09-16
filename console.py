#!/usr/bin/python3
"""Console for the HBNB project"""
import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import re


class HBNBCommand(cmd.Cmd):
    """Console with cmd module"""
    prompt = "(hbnb) "
    CLASSES = ["BaseModel",
               "User",
               "State",
               "City",
               "Amenity",
               "Place",
               "Review"
               ]

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        # print(line)
        args = line.split(" ")
        # if len(args) == 1:
        if line == "":
            print("** class name missing **")
        elif line not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            if len(args) > 1:
                attr_str = " ".join(args[1:])
                try:
                    new_instance = self.create_obj_by_class_name(class_name,
                                                                 attr_str)
                    new_instance.save()
                    print(new_instance.id)
                except Exception as e:
                    print("** invalid attribute format: {}".format(e))
            else:
                new_instance = self.create_obj_by_class_name(class_name)
                new_instance.save()
                print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id
         Usage: show BaseModel <id>
        and
        retrieve an instance based on its ID
        Usage: <class name>.show(<id>).
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        # print(args)
        if args[0] in HBNBCommand.CLASSES:
            self.do_show0(line)
        else:
            self.do_show1(line)

    @staticmethod
    def do_show0(line):
        """
        Prints the string representation of an instance based
        on the class name and id
        Usage: show BaseModel <id>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in HBNBCommand.CLASSES:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                # instance_key = f"{class_name}.{obj_id}"
                instance_key = "{}.{}".format(class_name, obj_id)
                objs = storage.all()
                if instance_key not in objs:
                    print("** no instance found **")
                else:
                    obj = objs[instance_key]
                    print(obj)

    @staticmethod
    def do_show1(line):
        """
        retrieve an instance based on its ID
        Usage: <class name>.show(<id>).
        """
        args = line.split(".")
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
            return
        obj_id = args[1][5:-1]
        obj_id = obj_id.strip('"')
        # print(obj_id)
        objs = storage.all()
        instance_key = "{}.{}".format(class_name, obj_id)
        if instance_key in objs:
            print(objs[instance_key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        Usuage: destroy BaseModel <id>
        and
        destroy an instance based on his ID
        Usage: <class name>.destroy(<id>)
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        # print(args)
        if args[0] in HBNBCommand.CLASSES:
            self.do_destroy0(line)
        else:
            self.do_destroy1(line)

    @staticmethod
    def do_destroy0(line):
        """
        Deletes an instance based on the class name and id
        Usuage: destroy BaseModel <id>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        objs = storage.all()
        # instance_key = f"{class_name}.{obj_id}"
        instance_key = class_name + "." + obj_id
        if instance_key not in objs:
            print("** no instance found **")
            return

        del objs[instance_key]
        storage.save()

    @staticmethod
    def do_destroy1(line):
        """
        destroy an instance based on his ID
        Usage: <class name>.destroy(<id>)
        """
        args = line.split(".")
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
            return
        id_str = args[1][8:-1]
        id_str = id_str.strip('"')
        objs = storage.all()
        instance_key = "{}.{}".format(class_name, id_str)
        if instance_key in objs:
            del objs[instance_key]
        else:
            print("** no instance found **")
        storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on the class name
        """
        objs = storage.all()
        args = line.split()

        if not args:
            instance_list = [str(obj) for obj in objs.values()]
        else:
            class_name = args[0]
            if class_name not in HBNBCommand.CLASSES:
                print("** class doesn't exist **")
                return

            instance_list = [str(objs[obj])
                             for obj in objs
                             if obj.startswith(class_name + '.')]

        formatted_output = "[" + ", ".join(['"' + instance + '"'
                                            for instance in instance_list]) \
            + "]"
        print(formatted_output)

    def create_obj_by_class_name(self, class_name, attr_str=""):
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
            obj = obj_class(**eval("{" + attr_str + "}"))
            return obj
        else:
            raise ValueError(
                "Class '{}' not found in class_mapping".format(class_name))

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        and
        update an instance based on his ID
        Usage: <class name>.update(<id>, <attribute name>, <attribute value>)
        and
        Updates an instance based on the class name and id using a dictionary
        Usage: <class name>.update(<id>, <dictionary representation>)
        """
        args = line.split()
        print(args[0])
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in HBNBCommand.CLASSES:
            self.do_update0(line)
        """class_name = args[0]
        if class_name not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
            return"""
        if re.match(r'(\w+)\.update\("([\w-]+)", "([\w_]+)", "([\w\s]+)"\)',
                    line):
            self.do_update1(line)
        if re.match(r'(\w+)\.update\("([\w-]+)", \{.*\}\)$', line):
            self.do_update_dic(line)

    @staticmethod
    def do_update0(line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        print(args)
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        objs = storage.all()
        instance_key = "{}.{}".format(class_name, obj_id)
        # print(instance_key)

        if instance_key not in objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = " ".join(args[3:])
        obj = objs[instance_key]
        if attribute_name in ['id', 'created_at', 'updated_at']:
            print("** cannot update id, created_at, or updated_at **")
            return
        if attribute_name in obj.__dict__:
            attr_type = type(obj.__dict__[attribute_name])
            try:
                new_value = attr_type(attribute_value)
            except ValueError:
                print("** invalid value type **")
                return
        attribute_value = attribute_value.strip('"')
        setattr(obj, attribute_name, attribute_value)
        storage.save()

    @staticmethod
    def do_update1(line):
        """
        Update an instance based on its ID
        Usage: <class name>.update(<id>, <attribute name>, <attribute value>)
        """
        args = line.split(".")
        # print(args)
        if len(args) < 2:
            print("** class name and method missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
            return

        # Extract the method and parameters
        method_args = args[1].strip('()').split(',')
        if len(method_args) != 3:
            print("** invalid method parameters **")
            return

        # Extract ID, attribute name, and attribute value
        instance_id_quotes = method_args[0].strip()
        instance_id = instance_id_quotes.split('"')[1]
        attribute_name_quotes = method_args[1].strip()
        attribute_name = attribute_name_quotes.strip('"')
        attribute_value_quotes = method_args[2].strip()
        attribute_value = attribute_value_quotes.strip('"')

        objs = storage.all()
        instance_key = "{}.{}".format(class_name, instance_id)

        if instance_key in objs:
            obj = objs[instance_key]
            setattr(obj, attribute_name, attribute_value)
            storage.save()
        else:
            print("** no instance found **")

    @staticmethod
    def do_update_dic(line):
        """
        Updates an instance based on the class name and id using a dictionary
        Usage: <class name>.update(<id>, <dictionary representation>)
        """
        args = line.split()
        pattern = r'(\w+)\.update\("([\w-]+)",'
        match = re.search(pattern, str(args))
        class_name = match.group(1)
        obj_id = match.group(2)
        if class_name not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
            return

        objs = storage.all()
        instance_key = "{}.{}".format(class_name, obj_id)

        if instance_key not in objs:
            print("** no instance found **")
            return

        try:
            dictionary_rep = " ".join(args[1:])
            # print(dictionary_rep)
            dictionary_rep = dictionary_rep.strip(')')
            # print(dictionary_rep)
            update_dict = eval(dictionary_rep)
            # print(update_dict)
            if not isinstance(update_dict, dict):
                raise ValueError("Invalid dictionary representations")

            obj = objs[instance_key]

            for key, value in update_dict.items():
                if key not in ['id', 'created_at', 'updated_at']:
                    setattr(obj, key, value)
            storage.save()
        except Exception as e:
            print("** invalid dictionary representation: {}".format(e))

    def do_count(self, line):
        """
        retrieve the number of instances of a class
        Usage: <class name>.count().
        """
        class_name = line.split('.')[0]
        objs = storage.all()
        count = 0
        for obj in objs.values():
            if class_name == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, line):
        """Default command"""
        args = line.split('.')
        if args[0] in self.CLASSES:
            command = args[1]
            if command.startswith("update(") and command.endswith(")"):
                self.do_update(args[0] + '.' + command)
            if command.startswith("destroy(") and command.endswith(")"):
                self.do_destroy(args[0] + '.' + command)
            if command.startswith("show(") and command.endswith(")"):
                self.do_show(args[0] + '.' + command)
            if command == "count()":
                self.do_count(args[0])
            if command == "all()":
                self.do_all(args[0])
        else:
            print("*** Unknown syntax: {}".format(line))

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Used when empty line is used as arg"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
