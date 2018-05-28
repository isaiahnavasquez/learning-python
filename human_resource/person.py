class Person:
    """A simple bio data of a person"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def dump_person(self):
        """returns an object definition of this person instance"""
        output = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        return output
