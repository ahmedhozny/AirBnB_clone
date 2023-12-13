#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
import re

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    __all_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
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
        elif args[0] not in HBNBCommand.__all_classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, args):
        """
        Usage: show <class> <id> or <class name>.show(<id>).
        Shows a string representation of instance and print its id.
        """
        args = args.split()
        objects_dict = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__all_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objects_dict:
            print("** no instance found **")
        else:
            print(objects_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, args):
        """
        Usage: destroy <class> <id> or <class name>.destroy(<id>)
        Deletes an instance based on the class name and id.
        """
        args = args.split()
        objects_dict = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__all_classes:
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
        Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """
        args = args.split()
        if len(args) > 0 and args[0] not in HBNBCommand.__all_classes:
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
            or <class name>.update(<id>, <attribute name>, <attribute value>)
        Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        curly_braces = (args.find("{"), args.find("}"))
        temp = ""
        if curly_braces != (-1, -1) and curly_braces[0] < curly_braces[1]:
            temp = args[curly_braces[0]: curly_braces[1] + 1]
            args = args[:curly_braces[0]]

        args = args.split()
        if temp != "":
            args.insert(2, temp)
        objects_dict = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__all_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objects_dict:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            try:
                eval(args[2])
            except NameError:
                print("** value missing **")
        elif len(args) == 4:
            obj = objects_dict["{}.{}".format(args[0], args[1])]
            class_dict = obj.__dict__
            if args[2] in class_dict.keys():
                val_type = type(class_dict[args[2]])
                class_dict[args[2]] = val_type(args[3])
            else:
                class_dict[args[2]] = args[3]
            storage.save()
        elif type(eval(args[2])) == dict:
            obj = objects_dict["{}.{}".format(args[0], args[1])]
            class_dict = obj.__dict__
            for k, v in eval(args[2]).items():
                if (k in class_dict.keys() and
                        type(class_dict[k]) in {str, int, float}):
                    class_dict[k] = type(class_dict[k])(v)
                else:
                    class_dict[k] = v
            storage.save()

    def do_count(self, args):
        """
        Usage: count <class> or <class>.count()
        Counts the number of instances of a class.
        """
        args = args.split()
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == args[0]:
                count += 1
        print(count)

    def default(self, args):
        """Function called when a command given might be invalid"""
        commands = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }

        if '.' in args and '(' in args and ')' in args:
            cls = args.split('.')
            cnd = cls[1].split('(')
            arg = cnd[1].split(')')[0]
            curly_braces = (arg.find("{"), args.find("}"))
            temp = ""
            if curly_braces != (-1, -1) and curly_braces[0] < curly_braces[1]:
                temp = arg[curly_braces[0]: curly_braces[1] + 1]
                arg = arg[:curly_braces[0]]
            arg = arg.replace(",", "").replace("\"", "") + temp
            if cnd[0] in commands.keys():
                return commands[cnd[0]]("{} {}".format(cls[0], arg))
        print("*** Unknown syntax: {}".format(args))
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
