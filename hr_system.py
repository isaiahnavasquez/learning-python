from human_resource.employee import Employee
from human_resource.payslip import Payslip

def add_employee():
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    age = input('Age: ')
    job = input('Job Description: ')
    emp_started = input('Employment Started: ')
    employee = Employee(first_name, last_name, age, job, emp_started)
    pretty_print(employee.dump_employee())
    generate_payslip(employee)

def generate_payslip(employee):
    hourly_rate = int(input('Hourly rate: '))
    days_worked = int(input('Days worked: '))
    absences = int(input('Days Absent: '))

    payslip = Payslip(employee, hourly_rate)
    pay = payslip.dump_payslip(days_worked, absences)
    pretty_print(pay)

def pretty_print(iterable):
    for x, y in zip(iterable.keys(), iterable.values()):
        print(x + ':')
        if type(y) == dict:
            for i in y:
                print('  -' + i)
        else:
            print('  -' + str(y))

options = {
    'a': add_employee,
}

if __name__ == '__main__':
    while True:
        option = input('Options: \n'\
                        + 'a: Generate Payslip\n')
        if option != 'x':
            invoker = options[option]
            invoker()
        else:
            break
