#!/usr/bin/python3
"""Writing line-oriented command interpreters"""
import cmd

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

if __name__ == '__main__':
    HBNBcommand().cmdloop()
