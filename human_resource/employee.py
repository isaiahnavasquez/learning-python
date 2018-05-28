from . import person

class Employee(person.Person):
    """Simple employee functions and job description"""

    def __init__(self, first_name, last_name, age, job, emp_started):
        person.Person.__init__(self, first_name, last_name, age)
        self.job = job
        self.emp_started = emp_started

    def dump_employee(self):
        """returns an object definition of this employee instance"""
        output = {
            'bio_data': person.Person.dump_person(self),
            'job': self.job,
            'emp_started': self.emp_started
        }
        return output
