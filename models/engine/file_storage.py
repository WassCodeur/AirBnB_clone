#!/usr/bin/python3
"""storage module"""
import json
import uuid
import models
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class"""
    __objects = {}
    __file_path = "MyJsonFile.json"

    def __init(self):
        """__init__ method"""
        pass

    def save(self):
        """Save data to JSON file"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def all(self):
        """method all"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def reload(self):
        """method reload"""
        try:
            with open(self.__file_path, mode='r', encoding='utf8') as myObj:
                fromJson = json.loads(myObj)
                for key, value in fromJson.items():
                    self.__objects[key] = value
        except FileNotFoundError:
            pass


test = FileStorage()
test.save()
print(test.all())