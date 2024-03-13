"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""


class Counter:
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Allocate memory and return a reference to a new Person object"""
        if cls._instance:
            return cls._instance
        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.__count = 0

    def __str__(self):
        return f"{self.__count}"

    @property
    def count(self):
        """Count property"""
        return self.__count

    def increment(self):
        """Add 1 and return the new count"""
        return self.__count + 1
