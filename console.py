#!/usr/bin/python3
"""Writing line-oriented command interpreters"""
import cmd
import json
import sys
from models import *
from models import storage
import re


class HBNBcommand(cmd.Cmd):

    """Creating a simple line-oriented commands"""
    prompt = '(hbnb) '

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
        """Usage:create<class_name>,Function:creates an instance of a class"""
        if line != "" and line is not None:
            if line not in storage.classes():
                print("** class doesn't exist **")
            else:
                # Create an instance of the given class
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
        if len(args) == 0 or args[0] == '' or args[0] is None:
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
        if len(args) == 0 or args[0] == '' or args[0] is None:
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

    def do_all(self, line):
        """Prints all string representation of all instances.
        """
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, line):
        '''Usage: 1. update <class name> <id> <attribute> <value> | \
        2. <class name>.update(<id> <attribute> <value>) \
        3. update <clas name> <id> <dictionary> \
        4. <class name>.update(<id> <dictionary>) \
        Function: Updates the instance of the class
        '''

        if line == "" or line is None:
            print("** class name missing**")
            return

        regex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        matched = re.search(regex, line)
        classname = matched.group(1)
        uid = matched.group(2)
        attribute = matched.group(3)
        value = matched.group(4)
        if not matched:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class name doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "().()".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("*** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save

    def precmd(self, line):
        # make the app work non-interactively
        if not sys.stdin.isatty():
            print()

        checks = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if checks:
            class_name = checks.group(1)
            command = checks.group(2)
            args = checks.group(3)

            if args is None:
                line = f"{command} {class_name}"
                return ''
            else:
                # print(args)
                args_checks = re.search(r"^\"([^\"]*)\"(?:, (.*))?$", args)
                # print(args_checks.group(1), args_checks.group(2))
                instance_id = args_checks[1]

                if args_checks.group(2) is None:
                    line = f"{command} {class_name} {instance_id}"
                else:
                    attribute_part = args_checks.group(2)
                    # print(attribute_part)
                    line = f"{command} {class_name} {instance_id} \
{attribute_part}"
                return ''

        return cmd.Cmd.precmd(self, line)
        # return ''


if __name__ == '__main__':
    HBNBcommand().cmdloop()
