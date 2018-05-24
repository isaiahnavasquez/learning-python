def censor_string(string):
    # censors = ['#', '$', '@', '%', '!', '&']
    return string[0] + ('*' * (len(string)-1))

def censor_strings(string):
    l = string.split()
    censored = [censor_string(x) for x in l]
    return ' '.join(censored)

def camel_case(string):
    l = string.split()
    camel = l[0].lower()
    tail = [x.title() for x in l]
    del tail[0]
    return camel + ''.join(tail)

def snake_case(string):
    return '_'.join([x.lower() for x in string.split()])

def greetings_generator(name):
    return 'Hello there {}'.format(name)

def greetings_generator_v2(name, age):
    return 'Hello there %s, I believe you are %d years old.' % (name, age)

def find_the_snake(string):
    if string.find('ss') == -1:
        print('snake not found')
    else:
        print('snake found at index: {}'.format(string.find('ss')))

def number_eligible(string):
    print('determines if {} is can be converted to a number'.format(string))
    if string.isnumeric():
        print('yes')
    else:
        print('false')

def swap_case(string):
    # l = []
    # for i in list(string):
    #     if i.isupper():
    #         l.append(i.lower())
    #     elif i.islower():
    #         l.append(i.upper())
    #     elif i.isspace():
    #         l.append(' ')
    # return ''.join(l)
    return ''.join([x.lower() if x.isupper() else x.upper() for x in list(string)])

def lazy_type(string):
    print('remove all vowels in {}'.format(string))
    return ''.join([x if x not in 'aeiou' else '' for x in list(string)]).upper()


print(censor_string('hello'))
print(censor_strings('hello there bitch'))
print(camel_case('google is alphabet'))
print(snake_case('google is alphabet'))
print(greetings_generator('Isaiah'))
print(greetings_generator_v2('Isaiah', 22))
find_the_snake('bessy')
number_eligible('123456')
print(swap_case('hEllO thErE'))
print(lazy_type('california'))
