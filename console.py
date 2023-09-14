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
        args = line.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.CLASSES:
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
                instance_key = class_name + "." + obj_id
                objs = storage.all()
                if instance_key not in objs:
                    print("** no instance found **")
                else:
                    obj = objs[instance_key]
                    print(obj)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
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
        """
        args = line.split()
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

        if instance_key not in objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** instance id missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        new_value = args[3]
        obj = objs[instance_key]
        if attribute_name in ['id', 'created_at', 'updated_at']:
            print("** cannot update id, created_at, or updated_at **")
            return
        if attribute_name in obj.__dict__:
            attr_type = type(obj.__dict__[attribute_name])
            try:
                new_value = attr_type(new_value)
            except ValueError:
                print("** invalid value type **")
                return

        setattr(obj, attribute_name, new_value)
        storage.save()

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

    def do_show(self, line):
        """
        retrieve an instance based on its ID
        Usage: <class name>.show(<id>).
        """
        args = line.split(".")
        class_name = args[0]
        id_str = args[1][5:-1]
        objs = storage.all()
        instance_key = "{}.{}".format(class_name, id_str)
        if instance_key in objs:
            print(objs[instance_key])
        else:
            print("** no instance found **")

    def default(self, line):
        """Default command"""
        args = line.split('.')
        if args[0] in self.CLASSES:
            command = args[1]
            if command.startswith("show(") and command.endswith(")"):
                self.do_show(args[0] + '.' + command)
            if command == "count()":
                self.do_count(args[0])
            if command == "all()":
                self.do_all(args[0])

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
