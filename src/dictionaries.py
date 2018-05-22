my_phonebook = {}

def add_contact():
    print('\n')
    contact = input('enter name of contact: ')
    number = input('enter number of contact: ')
    my_phonebook[contact] = [number]
    print('contact saved.')
    while True:
        cont = input('do you still want to add '\
                    + 'more numbers to {}? y/n: '.format(contact))
        if cont == 'y':
            number = input('enter number to add for {}'.format(contact))
            my_phonebook[contact].append(number)
        else:
            break
    print('\n')
    display_phone_book()

def add_phone_number():
    print('\n')
    contact = input('enter name of contact to add: ')
    number = input('enter number of contact: ')
    if contact not in my_phonebook:
        print('{} does not exist, adding as a new contact'.format(contact))
        my_phonebook[contact] = [number]
    else:
        my_phonebook[contact].append(number)
    display_phone_book()

def display_phone_book():
    print('\nYour Phonebook')
    for contact, numbers in my_phonebook.items():
        print(contact)
        for n in numbers:
            print('  --{}'.format(n))
    print('\n')

def delete_contact():
    print('\n')
    contact = input('enter name of contact to delete: ')
    if contact in my_phonebook:
        del my_phonebook[contact]
        print('delete successful')
    else:
        print('user does not exist')
    display_phone_book();

def search_contact():
    print('\n')
    search = input('enter search keyword: ')
    results = []
    for i in my_phonebook.keys():
        if i.find(search) != -1:
            results.append({i: my_phonebook[i]})
    print(results)

def search_phone_number():
    search  = input('enter search number: ')
    results = []
    for contact, numbers in my_phonebook.items():
        for num in numbers:
            if num.find(search) != -1:
                results.append({contact: num})
    print(results)

def no_option_found():
    pass

switcher = {
    'ac': add_contact,
    'ap': add_phone_number,
    'dis': display_phone_book,
    'dc': delete_contact,
    'sc': search_contact,
    'sp': search_phone_number,
}

def main():
    while True:
        print('--Phone Book--')
        print('ac - add contact\n'\
            + 'ap - add phone number\n'\
            + 'dis - display phone book\n'\
            + 'dc - delete contact\n'\
            + 'sc - search contact\n'\
            + 'sp - search phone number\n'\
            + 'del - get the longest item\n'\
            + 'x - exit and delete list')
        option = input('option: ')
        if option != 'x':
            func = switcher.get(option, no_option_found)
            func()
        else:
            break

main()
