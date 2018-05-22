import random

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
        print('chances: 0')
        print('vovo')

numbers = [1,2,3,4,5,6,7,8,9,10]
guess_the_number(numbers)
