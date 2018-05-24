my_list = []

def display_list():
    print('\n--Your List--')
    for i, v in zip(range(len(my_list)), my_list):
        print('{}: {}'.format(i, v))
    print('\n')

def add_item():
    print('----')
    content = input('Input item text: ')
    print('\n')
    my_list.append(content)
    display_list()

def delete_item():
    print('----')
    index = int(input('enter index to delete: '))
    del my_list[index]
    display_list()

def edit_list():
    edit = int(input('enter index to edit: '))
    value = input('enter modified value: ')
    my_list[edit] = value
    display_list()

def search_list():
    search = input('enter keyword to search: ')
    results = {}
    for i, v in zip(range(len(my_list)), my_list):
        if v.find(search) != -1:
            results[i] = v
    print(results)

def search_and_replace():
    search = input('enter keyword to search: ')
    replace = input('enter string to replace: ')
    for i, v in zip(range(len(my_list)), my_list):
        my_list[i] = v.replace(search, replace) #str.replace(old, new)
    display_list()

def get_longest():
    print('\nsmallest item')
    print(max(my_list))
    print('\n')

def get_shortest():
    print('\nsmallest item')
    print(min(my_list))
    print('\n')

def no_option_found():
    print('\nno option found\n')

switcher = {
    'a': add_item,
    'd': delete_item,
    'l': display_list,
    'e': edit_list,
    's': search_list,
    'r': search_and_replace,
    'min': get_shortest,
    'max': get_longest,
}

def main():
    while True:
        print('--welcome to LIST TAKER--')
        print('a - add item\n'\
            + 'd - delete item\n'\
            + 'l - display list\n'\
            + 'e - edit list\n'\
            + 's - search list\n'\
            + 'r - search and replace\n'\
            + 'min - get the shortest item\n'\
            + 'max - get the longest item\n'\
            + 'x - exit and delete list')
        option = input('option: ')
        if option != 'x':
            func = switcher.get(option, no_option_found)
            func()
        else:
            break
