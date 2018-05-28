from . import salary

class Payslip(salary.Salary):
    """Simple functions for payslip system"""

    def __init__(self, employee, hourly_rate):
        salary.Salary.__init__(self, hourly_rate)
        # an instance of class Employee
        self.employee = employee

    def dump_payslip(self, days, absences):
        pay = salary.Salary.salary_from_days(self, days)
        output = {
            'employee': self.employee.dump_employee(),
            'salary': pay
        }
        return output
