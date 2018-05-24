def filter_numbers(myList):
    print('--filtering numbers from your list...')
    numbers = []
    for l in myList:
        if type(l) == int:
            numbers.append(l)
    return numbers

def filter_words(myList):
    print('getting words from your list...')
    letters = []
    for i in myList:
        if type(i) == str:
            letters.append(i)
    if len(letters) > 0:
        print(letters)
    else:
        print('there were no letters found')

def count_backwards(number):
    print("I'll count backwards from your number to zero")
    counter = number
    numbers = []
    while counter > -1:
        numbers.append(counter)
        counter -= 1
    print('here it is: {}'.format(numbers))

def get_total(myList):
    print("I'll get the total the numbers on your list")
    numbers = filter_numbers(myList)
    total = 0
    for i in numbers:
        total += i
    print(total)

def filter_odd_numbers(myList):
    print('getting the odd numbers')
    l = filter_numbers(myList)
    odds = []
    for i in l:
        if i % 2 != 0:
            odds.append(i)
    print(odds)

def filter_even_numbers(myList):
    print('getting the even numbers')
    l = filter_numbers(myList)
    evens = []
    for i in l:
        if i % 2 == 0:
            evens.append(i)
    print(evens)

def get_duplicates(myList):
    print('getting the duplicate values from your list...')
    soFar = {}
    for i in myList:
        if i in soFar:
            soFar[i] += 1
        else:
            soFar[i] = 1
    duplicates = [x for x in soFar if soFar[x] > 1]
    print(duplicates)

def get_squares(myList):
    print('Getting the squares of each number in your list')
    l = filter_numbers(myList)
    squares = []
    for i in l:
        squares.append(i ** 2)
    print(squares)

def bust_fake_numbers(myList):
    print('finding the fake numbers')
    fakes = []
    for i in myList:
        if type(i) != int:
            fakes.append(i)
    print(fakes)

def find_dominant(myList):
    print('printing all the numbers that repeat the most')
    dominants = {}
    for i in myList:
        if i in dominants:
            dominants[i] += 1
        else:
            dominants[i] = 1
    print('dominant count: {}'.format(max(dominants.values())))
    max_count = max(dominants.values())
    dominant = [k for k, v in dominants.items() if dominants[k] == max_count]
    print(dominant)


nums = [1,4,2,3,1,1,2,4,5,2,1,4,5,6,4]
fakeNumbers = [1,'2','3',4,'5',6,7]
myList = [1,'hello',2,'there',3,4,5,6]
myNumbers = ['foo', 'bar', 'yanny', 'yanny', 'laurel']

# print(filter_numbers(myList))
# filter_words(myList)
# count_backwards(20)
# get_total(myList)
# filter_odd_numbers(myList)
# filter_even_numbers(myList)
# get_duplicates(myNumbers)
# get_squares(myList)
# bust_fake_numbers(fakeNumbers)
# find_dominant(nums)
