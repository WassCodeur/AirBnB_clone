#!/usr/bin/python3
"""This module contains the BaseModel class"""
import uuid
from datetime import datetime
import time
# import models


class BaseModel:
    """
        This class defines all common attributes/
        methods for other classes
    """
    def  __init__(self, *args, **kwargs):
         """init method"""
         self.id = str(uuid.uuid4())
         self.created_at = datetime.now()
         self.updated_at = datetime.now()
         if len(kwargs) > 0:
             for key , value in kwargs.items():
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "created_at":
                    self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    setattr(self, key, value)
        
                

         

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """to_dict method"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def __str__(self):
        """str method"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)



my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)