import json
import os

def save_as_json(data, file_name):
    path_file = generate_path(file_name)
    with open(path_file, 'w+') as f:
        json.dump(data, f)

def save_as_csv(data, file_name):
    """should save a list only"""
    # checks if a multidimensional array
    path_file = generate_path(file_name)

    if type(data[0]) != list:
        # not multidimensional
        with open(path_file, 'w+') as f:
            for v in data:
                f.write(str(v) + ',\n')

    elif type(data[0]) == list:
        # is multidimensional
        with open(path_file, 'w+') as f:
            for row in data:
                for i, v in enumerate(row):
                    f.write(str(v) + ',')
                f.write('\n')

def save_as_string(data, file_name):
    path_file = generate_path(file_name)
    with open(path_file, 'w') as f:
        f.write(data)

def retrieve_list(file_name):
    """opens json with list, then returns reg list"""
    output = None
    path_file = 'files/' + file_name
    with open(path_file, 'r+') as f:
        output = json.load(f)
    return output

def retrieve_object(file_name):
    """opens json with object, then returns reg object"""
    output = None
    path_file = 'files/' + file_name
    with open(path_file, 'r+') as f:
        output = json.load(f)
    return output

# def retrieve_csv(file_name):
#     """opens csv then returns as a list"""
#     path_file = 'files/' + file_name
#     output = []
#     with open(path_file, 'r+') as f:
#         pass

def generate_path(file_name):
    """
    check and create the directory for the app
    returns the file_name to be used
    """
    if not os.path.isdir('files'):
        os.mkdir('files')
    if os.path.isfile('files/' + file_name):
        replace = input('File {} is existing\n'.format(file_name)
                        + 'enter r to overwrite or '
                        + 'enter a different name: ')
        if replace != 'r':
            file_name = replace
    return 'files/{}'.format(file_name)

obj = {
    'name': 'Isaiah Jan',
    'age': 52,
    'sex': 'none'
}

list_1 = [
    ['Anne', 'Ferraren', 'Lisa'],
    ['Anne', 'Ferraren', 'Lisa'],
    ['Anne', 'Ferraren', 'Lisa'],
]
list_2 = ['Anne', 'Ferraren', 'Lisa']

s = 'Hello there'

# save_as_json(obj, 'my_json.json')
# save_as_json(list_2, 'my_list.json')
# save_as_csv(list_2, 'my_csv_list.csv')
# save_as_csv(list_1, 'my_csv_lists.csv')
# save_as_string(s, 'my_string.txt')
# print(retrieve_list('my_list.json'))
# print(retrieve_object('object.json'))
