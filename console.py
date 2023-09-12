#!/usr/bin/python3
"""Console for the HBNB project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Console with cmd module"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Used when empty line is used as arg"""
        pass

    def do_EOF(self, line):
        """EOF to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not line:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.__objects:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        instance_key = f"{class_name} {obj_id}"

        if instance_key not in self.__objects:
            print("** no instance found **")
            return

        obj = self.__objects[instance_key]
        print(str(obj))

    def destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.__objects:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        instance_key = f"{class_name} {obj_id}"

        if instance_key not in self.__objects:
            print("** no instance found **")
            return

        del self.__objects[instance_key]
        self.save()

        def all(self, line):
            """
            Prints all string representation of all instances based
            or not on the class name
            """
            args = line.split()
            if args and args[0] not in self.__objects:
                print("** class doesn't exist **")
                return

            instance_list = []
            if args:
                class_name = args[0]
                instance_list = [str(obj) for key, obj in self.__objects.items()
                                if key.startswith(class_name + '.')]
            else:
                instance_list = [str(obj) for obj in self.__objects.values()]

            for rep in instance_list:
                print(rep)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
