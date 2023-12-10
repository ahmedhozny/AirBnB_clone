#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    __all_classes = {
        "BaseModel",
        "User",
    }

    def do_quit(self, args):
        """Exits the program."""
        return True

    def do_EOF(self, args):
        """Exits on EOF."""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, args):
        """
        Usage: create <class>
        Create a new class instance and print its id.
        """
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] in HBNBCommand.__all_classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, args):
        """
        Usage: show <class> <id>
        Shows a string representation of instance and print its id.
        """
        args = args.split()
        objects_dict = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] in HBNBCommand.__all_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objects_dict:
            print("** no instance found **")
        else:
            print(objects_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, args):
        """
        Usage: destroy <class> <id>
        Deletes an instance based on the class name and id.
        """
        args = args.split()
        objects_dict = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] in HBNBCommand.__all_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objects_dict:
            print("** no instance found **")
        else:
            del objects_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, args):
        """
        Usage: all or all <class>
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """
        args = args.split()
        if len(args) > 0 and args[0] in HBNBCommand.__all_classes:
            print("** class doesn't exist **")
        else:
            objects_list = []
            for obj in storage.all().values():
                if (len(args) < 1
                        or (len(args) > 0
                            and args[0] == obj.__class__.__name__)):
                    objects_list.append(str(obj))
            print(objects_list)

    def do_update(self, args):
        """
        Usage: Usage: update <class> <id> <attribute_name> <attribute_value>
        Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        args = args.split()
        objects_dict = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] in HBNBCommand.__all_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objects_dict:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj = objects_dict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__dict__.keys():
                val_type = type(obj.__dict__[args[2]])
                obj.__dict__[args[2]] = val_type(args[3])
            else:
                obj.__dict__[args[2]] = args[3]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
