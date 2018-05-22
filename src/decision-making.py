def isSimilar(num1, num2):
    print('are both numbers similar? {}, {}'.format(num1, num2))
    if num1 == num2:
        print(True)
    else:
        print(False)

def isBigger(num1, num2):
    print('Which is larger? {}, {}'.format(num1, num2))
    if num1 > num2:
        print(num1)
    elif num1 < num2:
        print(num2)
    else:
        print('both are the same')

def isSmaller(num1, num2):
    print('Which is smaller? {}, {}'.format(num1, num2))
    if num1 < num2:
        print(num1)
    elif num1 > num2:
        print(num2)
    else:
        print('both are the same')

def isString(value):
    print('is {} a string?'.format(value))
    if type(value) == str:
        print(True)
    else:
        print(False)

def isNumber(value):
    print('is {} a number?'.format(value))
    if type(value) == int:
        print(True)
    else:
        print(False)

def isList(mylist):
    print('is {} a list?'.format(myList))
    if type(myList) == list:
        print(True)
    else:
        print(False)

def isDict(myDict):
    print('is {} a dict?'.format(myDict))
    if type(myDict) == dict:
        print(True)
    else:
        print(False)

def isInMyList(value, myList):
    print('does {} contains the value: {}?'.format(myList, value))
    if value in myList:
        print(True)
    else:
        print(False)

def isEven(value):
    print('is {} an even number?'.format(value))
    if value % 2 == 0:
        print('yes')
    else:
        print('no')

def isOdd(value):
    print('is {} an odd number?'.format(value))
    if value % 2 == 0:
        print('no')
    else:
        print('yes')

a = 5
b = 2
myString = 'Hello'
myNumber = 1
myList = [1,2,3,4,5]
myDict = {'name': 'John','surname': 'Doe'}

isSimilar(a, b)
isBigger(a, b)
isSmaller(a, b)
isString(myString)
isNumber(myNumber)
isList(myList)
isDict(myDict)
isEven(a)
isOdd(a)
