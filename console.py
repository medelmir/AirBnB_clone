#!/usr/bin/python3
"""cmd module"""

import cmd
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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

    def do_create(self, arg):
        """Create a new instance of a class"""
        if not arg:
            print("** class name missing **")
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            new_instance = globals()[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            if obj_key in storage.all():
                print(storage.all()[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            if obj_key in storage.all():
                del storage.all()[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances"""
        args = arg.split()
        if not args:
            obj_list = []
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
        elif args[0] not in globals():
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if type(obj).__name__ == args[0]:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj_key = args[0] + "." + args[1]
            if obj_key in storage.all():
                setattr(storage.all()[obj_key], args[2], args[3])
                storage.all()[obj_key].save()
            else:
                print("** no instance found **")

    def default(self, line):
        """Custom handling of <class name>.all()"""
        parts = line.split('.')
        if len(parts) == 2 and parts[1] == "all()":
            class_name = parts[0]
            if class_name in globals():
                obj_list = []
                for obj in storage.all().values():
                    if type(obj).__name__ == class_name:
                        obj_list.append(str(obj))
                print(obj_list)
            else:
                print("** class doesn't exist **")
        elif len(parts) == 2 and parts[1] == "count()":
            class_name = parts[0]
            if class_name in globals():
                obj_count = 0
                for obj in storage.all().values():
                    if type(obj).__name__ == class_name:
                        obj_count += 1
                print(obj_count)
        elif len(parts) == 2 and parts[1].startswith("show("):
            class_name = parts[0]
            if class_name in globals():
                obj_id = parts[1][6:-2]
                obj_key = class_name + "." + obj_id
                if obj_key in storage.all():
                    print(storage.all()[obj_key])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(parts) == 2 and parts[1].startswith("destroy("):
            class_name = parts[0]
            if class_name in globals():
                obj_id = parts[1][9:-2]
                obj_key = class_name + "." + obj_id
                if obj_key in storage.all():
                    del storage.all()[obj_key]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(parts) == 2 and parts[1].startswith("update("):
            class_name = parts[0]
            if class_name in globals():
                update_args = parts[1][7:-1].split(',')
                if len(update_args) >= 3:
                    obj_id = update_args[0].strip()[1:-1]
                    obj_key = class_name + "." + obj_id
                    if obj_key in storage.all():
                        attribute_name = update_args[1].strip()[1:-1]
                        attribute_value = update_args[2].strip()[1:-1]
                        setattr(storage.all()[obj_key],
                                attribute_name, attribute_value)
                        storage.all()[obj_key].save()
                    else:
                        print("** no instance found **")
                else:
                    print("** invalid update syntax **")
            else:
                print("** class doesn't exist **")
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

