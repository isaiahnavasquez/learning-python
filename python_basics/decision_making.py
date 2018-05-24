def is_similar(num1, num2):
    print('are both numbers similar? {}, {}'.format(num1, num2))
    if num1 == num2:
        print(True)
    else:
        print(False)

def is_bigger(num1, num2):
    print('Which is larger? {}, {}'.format(num1, num2))
    if num1 > num2:
        print(num1)
    elif num1 < num2:
        print(num2)
    else:
        print('both are the same')

def is_smaller(num1, num2):
    print('Which is smaller? {}, {}'.format(num1, num2))
    if num1 < num2:
        print(num1)
    elif num1 > num2:
        print(num2)
    else:
        print('both are the same')

def is_string(value):
    print('is {} a string?'.format(value))
    if type(value) == str:
        print(True)
    else:
        print(False)

def is_number(value):
    print('is {} a number?'.format(value))
    if type(value) == int:
        print(True)
    else:
        print(False)

def is_list(my_list):
    print('is {} a list?'.format(my_list))
    if type(my_list) == list:
        print(True)
    else:
        print(False)

def is_dict(my_dict):
    print('is {} a dict?'.format(my_dict))
    if type(my_dict) == dict:
        print(True)
    else:
        print(False)

def is_in_my_list(value, my_list):
    print('does {} contains the value: {}?'.format(my_list, value))
    if value in my_list:
        print(True)
    else:
        print(False)

def is_even(value):
    print('is {} an even number?'.format(value))
    if value % 2 == 0:
        print('yes')
    else:
        print('no')

def is_odd(value):
    print('is {} an odd number?'.format(value))
    if value % 2 == 0:
        print('no')
    else:
        print('yes')

a = 5
b = 2
my_string = 'Hello'
my_number = 1
my_list = [1,2,3,4,5]
my_dict = {'name': 'John','surname': 'Doe'}

# is_similar(a, b)
# is_bigger(a, b)
# is_smaller(a, b)
# is_string(my_string)
# is_number(my_number)
# is_list(my_list)
# is_dict(my_dict)
# is_even(a)
# is_odd(a)
