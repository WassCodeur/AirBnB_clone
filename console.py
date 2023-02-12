#!/usr/bin/python
"""Console module"""
import cmd
import models
import shlex
import sys
import json
import os
import re


class ConsoleAirbnb(cmd.Cmd):
    """
        Simple command processor example.
    """
    intro = '\nWelcome to the airbnb comsole.'
    intro += ' Type help or ? to list commands.\n'
    prompt = '(hbtn) '
    file = None

    def do_count(self, line):
        """count: Count the number of instances of a class"""
        counter = 0
        if line == "":
            print("** class name missing **")
        else:
            for key, value in models.storage.all().items():
                if line in key:
                    counter += 1
            print(counter)

    def do_all(self, obj):
        """all: Show all instances"""
        if obj == "":
            print("** class name missing **")
        else:
            args = shlex.split(obj)
            if args[0] in models.classes:
                for key, value in models.storage.all().items():
                    if args[0] in key:
                        print(value)
            else:
                print("** class doesn't exist **")

    def do_show(self, obj):
        """show: Show an instance"""
        if obj == "":
            print("** class name missing **")
        else:
            args = shlex.split(obj)
            if args[0] in models.classes:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key in models.storage.all():
                        print(models.storage.all()[key])
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_create(self, line):
        """create: Create an instance"""
        if line == "":
            print("** class name missing **")
        else:
            args = shlex.split(line)
            if args[0] in models.classes:
                new = models.classes[args[0]]()
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """update: Update an instance"""
        if line == "":
            print("** class name missing **")
        else:
            args = shlex.split(line)
            if args[0] in models.classes:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key in models.storage.all():
                        if len(args) == 2:
                            print("** attribute name missing **")
                        else:
                            if len(args) == 3:
                                print("** value missing **")
                            else:
                                setattr(models.storage.all()[key], args[2],
                                        args[3])
                                models.storage.all()[key].save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_delete(self, line):
        """delete: Delete an instance"""
        print("hello")

    def do_quit(self, line):
        """quit: Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF: End of file"""
        return True

    def emptyline(self):
        """emptyline: Empty line"""
        print("empty line")


if __name__ == '__main__':
    """Main function"""
    ConsoleAirbnb().cmdloop()
