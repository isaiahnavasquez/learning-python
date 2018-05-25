import random

def get_name():
    try:
        print(s)
    except NameError as e:
        print(e)
    finally:
        print('catching is done')

def import_something():
    try:
        import something
    except ImportError as e:
        print(e)
    finally:
        print('catching is done')

def divide(num_1, num_2):
    try:
        total = num_1/num_2
    except ZeroDivisionError as e:
        print('error: {}: {}/{}'.format(e, num_1, num_2))
    else:
        print('no errors, total: ' + str(int(total)))
    finally:
        print('catching is done')

def convert_to_float(val):
    try:
        output = float(val)
    except ValueError as e:
        print('error: cannot convert \'{}\' to float'.format(val))
    else:
        print('conversion done: {}'.format(output))
    finally:
        print('catching is done')

def get_key(key):
    try:
        data = {'name': 'Scarlet Johansson'}
        output = data[key]
    except KeyError as e:
        print('cannot get value, key \'{}\' does not exist'.format(key))
    else:
        print('reference success, value is: {}'.format(output))

def get_letter(string, i):
    try:
        output = string[i]
    except IndexError as e:
        print('index {} does not exist in {}'.format(i, string))
    else:
        print('the letter is: ' + output)

def number_play(num):
    ai_num = random.choice(range(1,11))
    try:
        assert (ai_num == num), 'Guess did not match.'
    except AssertionError as e:
        print(e)
        print('The number is: ' + str(ai_num))
    else:
        print('Congrats! You guessed it right.')

def get_attribute():
    try:
        i = []
        total = i.total
    except AttributeError as e:
        print(e)

def get_file(file_name):
    try:
        with open(file_name, 'r+') as f:
            print(f.readline())
    except FileNotFoundError as e:
        print(e)
    else:
        print('file found')

def non_existing():
    try:
        print(i)
    except NameError as e:
        print(e)


# get_name()
# import_something()
# divide(1,0)
# divide(1,1)
# convert_to_float('10.')
# get_key('name')
# get_key('age')
# get_letter('salmon', 6)
# get_letter('salmon', 1)
# number_play(6)
# get_attribute()
# get_file('hello.txt')
# get_file('files/hello.txt')
non_existing()
