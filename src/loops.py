def filterNumbers(myList):
    print('--filtering numbers from your list...')
    numbers = []
    for l in myList:
        if type(l) == int:
            numbers.append(l)
    return numbers

def filterWords(myList):
    print('getting words from your list...')
    letters = []
    for i in myList:
        if type(i) == str:
            letters.append(i)
    if len(letters) > 0:
        print(letters)
    else:
        print('there were no letters found')

def countBackwards(number):
    print("I'll count backwards from your number to zero")
    counter = number
    numbers = []
    while counter > -1:
        numbers.append(counter)
        counter -= 1
    print('here it is: {}'.format(numbers))

def getTotal(myList):
    print("I'll get the total the numbers on your list")
    numbers = filterNumbers(myList)
    total = 0
    for i in numbers:
        total += i
    print(total)

def filterOddNumbers(myList):
    print('getting the odd numbers')
    l = filterNumbers(myList)
    odds = []
    for i in l:
        if i % 2 != 0:
            odds.append(i)
    print(odds)

def filterEvenNumbers(myList):
    print('getting the even numbers')
    l = filterNumbers(myList)
    evens = []
    for i in l:
        if i % 2 == 0:
            evens.append(i)
    print(evens)

def getDuplicates(myList):
    print('getting the duplicate values from your list...')
    soFar = {}
    for i in myList:
        if i in soFar:
            soFar[i] += 1
        else:
            soFar[i] = 1
    duplicates = [x for x in soFar if soFar[x] > 1]
    print(duplicates)



myList = [1,'hello',2,'there',3,4,5,6]
myNumbers = ['foo', 'bar', 'yanny', 'yanny', 'laurel']

print(filterNumbers(myList))
filterWords(myList)
countBackwards(20)
getTotal(myList)
filterOddNumbers(myList)
filterEvenNumbers(myList)
getDuplicates(myNumbers)
