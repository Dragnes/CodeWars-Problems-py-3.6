# Codewars Problem set 4


# 55) Write a function takes sequence as an argument and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
#    ex: unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
#        unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
#        unique_in_order([1,2,2,3,3])       == [1,2,3]

string = 'AAAABBbBCCDAABbbBB'
def unique_in_order(iterable):
    ordered = []   # initializing ordered to be an empty list
    previous = None   # initializing previous to be None
    for i in iterable:   # for i'th index in 'AAAABBbBCCDAABbbBB'
        if i != previous:   # if i does't equal to previous
            ordered.append(i)   # append i'th index from iterable to ordered
            previous = i   # now initializing previous to be i and looping throuogh every i in iterable
    return (ordered)   # return ordered
print(unique_in_order(string))         
            
iterable = 'AAAABBbBCCDAABbbBB'
def unique_in_order(iterable):
    ordered = []   # initializing ordered to be an empty list
    for i in iterable:  # for i'th index in 'AAAABBbBCCDAABbbBB'
        if len(ordered) == 0 or i != ordered[-1]:   # if len(ordered) = 0 (for initialized ordered) or i doesn't equal ordered[-1] = last element in ordered, then
            ordered.append(i)   # append i'th index from iterable to initialized list called ordered
    return(ordered)   # return ordered
print(unique_in_order(iterable))         

iterable = [1,2,2,3,3]
def unique_in_order(iterable):
    ordered = []   # initializing ordered to be an empty list
    for i in iterable:   # for i'th index in 'AAAABBbBCCDAABbbBB'
        if ordered == []:   # if ordered is an empty list
            ordered.append(i)   # append i'th index from iterable to ordered
        if i != ordered[-1]:   # if i doesn't equal to last index in ordered, then
            ordered.append(i)   # append i'th index from iterable to ordered
    return(ordered)   # return ordered
print(unique_in_order(iterable))


# 56) Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities.
#    "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
            
a1 = [35, 95, 44, 59]
a2 = [1225, 9025, 1936, 3481]
def comp(array1, array2):
    if array1 == None or array2 == None:
        return(False)
    for i in array1:   # for i'th element in array1
        if i * i not in array2:   # if square of i not in array 2, then
            return(False)   # return false
    for i in array2:   # for i'th element in array1
        if i ** 0.5 not in array1:   # if squar root of i not in array 1, then
            return(False)   # return false
    return(True)   # otherwise return true
print(comp(a1, a2))

a1 = [35, 95, 44, 59]
a2 = [1225, 9025, 1936, 3481]
def comp(array1, array2):
    array1.sort()   # sort array1
    array2.sort()   # sort array2
    for i in range(len(array1)):   # len(array1) = 4, range(4) = [0,1,2,3], for i in [0,1,2,3] 
        if array1[i] ** 2 != array2[i]:   # if i'th element of array1 squared doesn't equal to i'th element of array2, then
            return(False)   # return false
    return(True)   # otherwise return true
print(comp(a1, a2))

a1 = [35, 95, 44, 59]
a2 = [1225, 9025, 1936, 3481]
def comp(array1, array2):
    try:
        return(sorted(i**2 for i in array1)) == sorted(array2)   # return true if the sorted array1 of i**2 for all i'th element in array1 is equal to the sorted array2 
    except:
        return(False)
print(comp(a1, a2))


# 57) Given an array containing hashes of names
#     Return a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
#     ex: namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
#         returns 'Bart, Lisa & Maggie'
#     ex: namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
#         returns 'Bart & Lisa'
#     ex: namelist([ {'name': 'Bart'} ])
#         returns 'Bart'
#     ex: namelist([])
#         returns ''

names = ([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}])
def namelist(names):
    Name = []   # initializing Name to be an empty list
    for i in names:   # for i'th element in names, i1 = {'name': 'Bart'}, i2 = {'name': 'Lisa'}, i3 = {'name': 'Maggie'}, ...
        Name.append(i.get('name'))   # i1.get('name') = Bart, i2.get('name') = Lisa, ... append Bart, Lisa, Maggie to initialized list Names
        #Name.append(''.join(i.values()))   is another way to do it
    if len(Name) == 0 :   # len(Name) = len(['Bart', 'Lisa', 'Maggie']) = 3. if len(Name) == 0, then
        return ("")   # then return empty string
    if len(Name) == 1:   # if len(Name) == 1, i.e. Name = ['Bart'] then
        return (Name[0])   # return (Name[0] = ['Bart']) = 'Bart'
    if len(Name) == 2:   # if len(Name) == 2, i.e. Name = ['Bart', 'Lisa'] then
        return (' & '.join(Name))   # return Name joined with ' & '
    else:   # if len(Name) >= 3, Name = ['Bart', 'Lisa', 'Maggie']
        One = Name[0: len(Name) - 2]   # Name[0:len(Name)-2] = Name[0: 3-2] = Name[0: 1] = ['Bart']. initializing One to be ['Bart']
        Two = Name[len(Name) - 2: len(Name)]   # Name[len(Name)-2 : len(Name)] = Name[3-2 : 3] = Name[1: 3] = ['Lisa', 'Maggie']. initializing Two to be ['Lisa', 'Maggie']
        p1 = ', '.join(One)   # initializing p1 to be joind with a ', ' to one. i.e. "Bart, "
        p2 = ' & '.join(Two)   # initializing p2 to be joind with a ' & ' to Two. i.e. "Lisa & Maggie"
        p = [p1, p2]   # p = [p1, p2] = ["Bart, ", "Lisa & Maggie"]
        return (', '.join(p))   # return p joind with ', '
print(namelist(names))

names = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
def namelist(names):
    Name = []   # initializing Name to be an empty list
    if len(names) == 0:   # if len(names) == 0, then
        return('')   # return empty string
    else:
        for i in names:   # for i in [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]. i1 = {'name': 'Bart'}, i2 = {'name': 'Lisa'}, i3 = {'name': 'Maggie'}, ...
            Name.append(i.get('name'))   # i1.get('name') = Bart, i2.get('name') = Lisa, ... append Bart, Lisa, Maggie to initialized list Names = ['Bart', 'Lisa', 'Maggie']
            #Name.append(''.join(i.values()))   is another way to do it
        if len(Name) == 1:   # if len(Name) == 1, then
            return(Name[0])   # return 0th element in Name
        else:   # otherwise if len(Name) > 1, then
            return(', '.join(Name[:-1]) + ' & ' + Name[-1])   # return (Name[:-1] = ['Bart', 'Lisa']) + ' & ' + (Name[-1] = Maggie) joind together with ', '
print(namelist(names))


# 58) Given a string, replace every letter with its position in the alphabet.

'''
Method 1: using ASCII ord()
'''
text = 'abc xyz'
def alphabet_position(text):
    output = ''   # initializing output to be an empty string
    for ch in text.lower():   # for each ch in lower case version of the text
        if ch.isalpha():   # if ch is an alphabet
            output += str(ord(ch) - 96 ) + ' '   # str((ord(ch) = numerical designation for character in ASCII)-96) = numerical string value
    output = output.strip()   # rid of extra spaces in output
    return(output)   # return output
print(alphabet_position(text)) 

text = 'abc xyz'
def alphabet_position(text):   # code above written in a different way
    return (' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha()))
print(alphabet_position(text)) 
'''
Method 2
'''
text = 'abc xyz'
def alphabet_position(text):
    alpha = "abcdefghijklmnopqrstuvwxyz"   # initializing alpha to be "abcdefghijklmnopqrstuvwxyz"
    lst = []   # initializing l to be an empty list
    for i in text.lower():   # for each i in lower case version of the text
        if i in alpha:   # if i is in the initialized alpha
            index = alpha.index(i) + 1   # alpah.index(i) is the index position location of i, knowing a = 1, then alpha.index(a) + 1 = 1 which is initialized to index
            lst.append(str(index))   # append the string value of index to initialized list l
    return (" ".join(lst))   # return l joind with a space between each indices
print(alphabet_position(text)) 

text = 'abc XYZ'
def alphabet_position(text):      # code above written in a different way
    alpha = "abcdefghijklmnopqrstuvwxyz"
    return (" ".join([str(alpha.index(i)+1) for i in text.lower() if i.isalpha()]))
print(alphabet_position(text)) 


# 59) Build Tower by the following given argument: number of floors (integer and always greater than 0).
'''
exmple: a tower of 3 floors looks like below
[
  '  *  ', 
  ' *** ', 
  '*****'
]
'''

n = 3
def tower_builder(n_floors):
    floors = []   # initializing floors to be an empty list
    for i in range(n_floors):   # range(n_floors) = range(3) = [0,1,2]. for i in [0,1,2]
        n_floors -= 1   # decrement n_floors by 1 
        floors.append(' ' * n_floors + '*' * (i * 2 + 1) + ' ' * n_floors)  # concatenat strings by multiples of i by appending to an initialized empty list, floors
    return(floors)   # return the list floors
print(tower_builder(n))

n = 3
def tower_builder(n_floors):
    floors = []   # initializing floors to be an empty list
    for i in range(1, n_floors + 1):   # range(1, n_floors + 1) = range(1, 3+1) = range(1, 4) = [1,2,3]. for i in [1,2,3]: i1 = 1, i2 = 2, i3 = 3
        stars = '*' * (i * 2 - 1)   # initializing stars the following way: (i1 * 2 - 1) = (1 * 2 - 1) = 1 multiple of '*' for i1 = '*', 3 multiples of '*' for i2 = '***', 5 multiples of '*' for i3 = '*****'
        spaces = ' ' * (n_floors - i)   # initializing spaces the following way: (n_floors - i1) = (3 - 1) = 2 mltiples of ' ' = '  ', 1 multiples of ' ' = ' ', 0 multiples of ' ' = '' 
        floors.append(spaces + stars + spaces)   # concateneat strings (spaces + stars + spaces) by appending to an initialized empty list, floors
    return(floors)   # return the list floors
print(tower_builder(n))
