#!/usr/bin/python3
"""cmd module"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit cmd"""
        return True

    def do_EOF(self, arg):
        """EOF cmd"""
        return True

    def emptyline(self):
        """emptyline cmd"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

