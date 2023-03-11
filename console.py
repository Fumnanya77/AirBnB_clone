#!/usr/bin/python3
"""Writing line-oriented command interpreters"""
import cmd
import json
import sys
from models import base_model
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBcommand(cmd.Cmd):
    """Creating a simple line-oriented commands"""
    prompt = '(hbnb) '

    def do_create(self, line):
        """Create new instances of `BaseModel` and store in JSON file"""
        if line == "":
            print("** class name missing **")
        elif not line in dir(base_model):
            print("** class doesn\'t exist **")
        elif line in dir(base_model):
            print(line)
            obj = FileStorage.new(self, json.loads(line))
            print(obj)
            obj = FileStorage.save(self)
            print(obj)
            print(obj.id)

    def do_EOF(self, line):
        """End of file to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Enable Carriage-return when an empty line is called"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

if __name__ == '__main__':
    HBNBcommand().cmdloop()
