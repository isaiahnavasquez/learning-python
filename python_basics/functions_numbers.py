import random

global_numbers = [1,2,3,4,5,6,7,8,9]
numbers = range(1,11)

def print_sum(*numbers):
    """simple arithmetic operation"""
    print(sum(numbers))

def print_sum_and_return(*numbers):
    """adds and returns"""
    return sum(numbers)

def get_squares(numbers):
    """
    getting the squares of each number
    with the help of an anonymous function
    """
    local_list = numbers
    local_result = []
    for i in local_list:
        r = lambda a: a * a
        local_result.append(r(i))
    # ez: local_result = [x*x for x in local_list]
    return local_result

def incrementor(num):
    return lambda x: x + num

def parse_to_int(not_an_int):
    return int(not_an_int)

def parse_then_square(not_an_int):
    num = int(not_an_int)
    return num*num

def guess_the_number(numbers):
    print("let's play a game...")
    print("I've picked up a number from 1 - 10")
    print("You only have 3 chances")
    my_num = random.choice(numbers)
    chances = 3
    while chances > 0:
        print("What's your guess?")
        guess = int(input())
        if guess == my_num:
            print("Congrats, you guessed it!")
            break
        elif guess > my_num:
            print("Nope, lesser please")
            chances -= 1
        elif guess < my_num:
            print("Nope, larger please")
            chances -= 1
    else:
        print('answer: {}'.format(my_num))
        print('chances: 0 \t #vovo')


# print_sum(1,2,3,4,5,6,7,8,9)
# print(print_sum_and_return(1,2,3,4,5,6,7))
# print(get_squares(global_numbers))
#
# # using lambda
# inc = incrementor(50)
# print(inc(2))
#
# print(parse_then_square('52'))
# print(parse_to_int(3.9))
#
# # let's play a game!
# guess_the_number(numbers)
