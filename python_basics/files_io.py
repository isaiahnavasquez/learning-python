import json
import os

def save_as_json(data, file_name):
    """checks if object or list, then saves"""
    path_file = generate_path(file_name)
    with open(path_file, 'w+') as f:
        json.dump(data, f)

def save_as_csv(data, file_name):
    """should save a list only"""


def save_as_string(data, file_name):
    pass

def retrieve_list(file_name):
    """opens json with list, then returns reg list"""
    pass

def retrieve_object(file_name):
    """opens json with object, then returns reg object"""
    pass

def retrieve_csv(file_name):
    """opens csv then returns as a list"""
    pass

def generate_path(file_name):
    """
    check and create the directory for the app
    returns the file_name to be used
    """
    if os.path.exists('/files'):
        os.mkdir('files')
    return 'files/{}'.format(file_name)

obj = {
    'name': 'Isaiah Jan',
    'age': 52
}

save_as_json(obj, 'output.txt')
