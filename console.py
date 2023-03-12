#!/usr/bin/python3
"""Writing line-oriented command interpreters"""
import cmd
import json
import sys
from models import *
from models import storage


class HBNBcommand(cmd.Cmd):
    """Creating a simple line-oriented commands"""
    prompt = '(hbnb) '

    def do_create(self, line):
        """Create new instances of `BaseModel` and store in JSON file"""
        if line == "":
            print("** class name missing **")
        elif line not in dir(base_model):
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
    
    def do_create(self, line):
        """Usage: create <class_name>, Function: creates an instance of a class"""
        if line != "" or line is not None:
            if line not in storage.classes():
                print("** class doesn't exist **")
            else:
                #Create an instance of the given class
                new_obj = storage.classes()[line]()
                new_obj.save()
                print(new_obj.id)
        else:
            print("** class name missing **")
    
    def do_show(self, line):
        """Usage: show <class_name> <id>
           Funtion: shows object at that id
        """
        args = line.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance_id = args[1]
            class_name = args[0]
            key = f"{class_name}.{instance_id}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Usage: destroy <class_name> <id>
           Funtion: deletes object at that id
        """
        args = line.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance_id = args[1]
            class_name = args[0]
            key = f"{class_name}.{instance_id}"
            if key in storage.all():
                del (storage.all()[key])
                storage.save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBcommand().cmdloop()
