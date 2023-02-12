#!/usr/bin/python3
"""storage module"""
import json
import uuid


class FileStorage:
    """FileStorage class"""
    __objects = {}
    __file_path = "MyJsonFile.json"

    def __init(self):
        """__init__ method"""
        pass

    def save(self):
        with open(self.__file_path, mode='w', encoding='utf8') as myObj:
            to_dict = self.__dict__
            toJson = json.dumps(to_dict)
            myObj.write(toJson)

    def all(self):
        """method all"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def reload(self):
        """method reload"""
        try:
            with open(self.__file_path, mode='r', encoding='utf8') as myObj:
                fromJson = json.loads(myObj)
                for key, value in fromJson.items():
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
