#!/usr/bin/python3
"""
Module: base
"""
import json
import os
import csv


class Base:
    """
    Base Class
    nb: number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialize attributes
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns JSON string representation of list_dictionaries.
        """
        if list_dictionaries and len(list_dictionaries) is not 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        """
        list_dicts = []

        if list_objs is not None:
            for n in list_objs:
                list_dicts.append(cls.to_dictionary(n))

        file_name = "{}.json".format(cls.__name__)
        with open(file_name, 'w') as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.
        """
        if json_string is not None and len(json_string) != '':
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        """
        if cls.__name__ is 'Rectangle':
            dummy = cls(2, 1)
        elif cls.__name__ is 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.
        """
        lst = []
        list_dicts = []
        file_name = '{}.json'.format(cls.__name__)

        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                list_dicts = cls.from_json_string(file.read())
                for n in list_dicts:
                    lst.append(cls.create(**n))
        return lst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes csv
        """
        file_name = cls.__name__ + ".csv"
        with open(file_name, mode='w', newline='') as file:
            if list_objs is not None:
                wr = csv.writer(file)
                if cls.__name__ is "Rectangle":
                    for o in list_objs:
                        wr.writerow([o.id, o.width, o.height, o.x, o.y])
                elif cls.__name__ is "Square":
                    for o in list_objs:
                        wr.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes csv
        """
        file_name = cls.__name__ + '.csv'
        obj = []
        try:
            with open(file_name, mode='r', newline='') as file:
                rd = csv.reader(file)
                for arg in r:
                    if cls.__name__ is "Rectangle":
                        d = {"id": int(arg[0]),
                             "width": int(arg[1]),
                             "height": int(arg[2]),
                             "x": int(arg[3]),
                             "y": int(arg[4])}
                    if cls.__name__ is "Square":
                        d = {"id": int(arg[0]),
                             "size": int(arg[1]),
                             "x": int(arg[2]),
                             "y": int(arg[3])}
                    o = cls.create(**d)
                    obj.append(o)
        except:
            pass
        return obj
