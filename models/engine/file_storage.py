#!/usr/bin/python3
"""Defines the FileStorage class module."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine for managing object instances.

    This class provides an abstracted interface for storing and retrieving
    object instances. It allows objects to be serialized and deserialized
    from a JSON file, enabling data persistence after different program runs.

    Attributes:
        __file_path (str): The Json file path used to store data.
        __objects (dict): A dictionary that holds instantiated objects.

    """
    __file_path = "data.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of instantiated objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in objects the obj with key <obj class name>.id."""
        uniq_key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[uniq_key] = obj

    def save(self):
        """Serializes objects to the JSON file."""
        obj_dict = FileStorage.__objects
        serialized_objs = {}
        for obj in obj_dict.keys():
            instance = obj_dict[obj]
            serialized_objs[obj] = instance.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserializes the JSON file to objects."""
        try:
            with open(FileStorage.__file_path, "r") as file:
                obj_dict = json.load(file)
                for val in obj_dict.values():
                    class_name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(class_name)(**val))

        except FileNotFoundError:
            return
