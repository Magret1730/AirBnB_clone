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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
