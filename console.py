#!/usr/bin/python3
"""Console module"""
import cmd
import models
import shlex
import sys
import json
import os
import re


class HelloWorld(cmd.Cmd):
    """
        Simple command processor example.
    """
    intro = '\nWelcome to the airbnb comsole.'
    intro += ' Type help or ? to list commands.\n'
    prompt = '(hbtn) '
    file = None

    def do_count(self, line):
        """count: Count the number of instances of a class"""
        print("hello")

    def do_all(self, line):
        """all: Show all instances"""
        print("hello")

    def do_destroy(self, line):
        """destroy: Destroy an instance"""
        print("hello")

    def do_show(self, line):
        """show: Show an instance"""
        print("hello")

    def do_create(self, line):
        """create: Create an instance"""
        print("hello")

    def do_update(self, line):
        """update: Update an instance"""
        print("hello")

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
        pass


if __name__ == '__main__':
    """Main function"""
    HelloWorld().cmdloop()
