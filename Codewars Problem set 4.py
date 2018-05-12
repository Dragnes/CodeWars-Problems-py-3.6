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


# 60) Write a function that creats a pyramid with levels given as an input using nested for loop.
'''
example of nested for loop
for i in range(3):
    print('a')
    for j in range(3):
        print('b')
'''

floors = 4
def pyramids(floors):
    for i in range(floors):
        for j in range(floors - i):
            print(' ', end = '')
        for k in range(0, 2*i+1):
            print('0', end = '')
print(pyramids(floors))


# 61) Given an array of numbers, sort ascending order numbers but even numbers must be on their places.

n = [5, 3, 2, 8, 1, 4]
def sort_array(source_array):
    odds = []   # initializing odds to be an empty list
    answer = []   # initializing answer to be an empty list
    for i in source_array:   # for i in [5, 3, 2, 8, 1, 4]
        if i % 2 == 1:   # if i is odd, then
            odds.append(i)   # append odd i to the initialized list, odds
            answer.append('X')   # append 'X' to to the initialized list, answer
        else:
            answer.append(i)   # if i is not odd, append i to the intialized list, answer
    odds.sort()   # sort the list odds
    for i in odds:   # for i in list odds
        x = answer.index('X')   # initialize x to be the index location in the list answer of 'X'
        answer[x] = i   # replace the index location of 'X' by i
    return(answer)   # return the list answer
print(sort_array(n))

n = [5, 3, 2, 8, 1, 4]
def sort_array(source_array):
    odds = []   # initializing odds to be an empty list
    for i in range(len(source_array)):   # range(len(source_array)) = range(len([5, 3, 2, 8, 1, 4])) = range(6) = [0,1,2,3,4,5]. so for i in [0,1,2,3,4,5], i1 = 0, i2 = 1, i3 = 2, ...
        if source_array[i] % 2 > 0:   # if (source_array[i1] = source_array[0] = 5) is odd
            odds.append(source_array[i])   # append source_array[i1] to initialized list odds
            source_array[i] = 'X'   # replace the index of i which is odd in source_array by 'X'
    odds.sort()   # sort the list odds
    for i in range(len(odds)):   # range(len([1,2,5])) = range(3) = [0,1,2], so for i in range [0,1,2]
        source_array[source_array.index('X')] = odds [i]   # source_array.index('X') = 0, so source_array[0] = odds[i] (odds[i1] = 1, odds[i2] = 3, odds = 5)
    return(source_array)   # return our source_array list
print(sort_array(n))

n = [5, 3, 2, 8, 1, 4]
def sort_array(source_array):
    if source_array == []:   # if input is an empty array
        return[]   # return an empty list
    for i in range(len(source_array)):   # range(len(source_array)) = range(len([5, 3, 2, 8, 1, 4])) = range(6) = [0,1,2,3,4,5], for i in [0,1,2,3,4,5]; i1 = 0, i2 = 1, i3 = 2...
        for j in range(i, len(source_array)):   # for i1: range(i1 index, len(source_array)) = range(0, 6) = [0,1,2,3,4,5], so for j in [0,1,2,3,4,5]. for i2: range(i2 index, len(source_array)) = range(1, 6) = [1,2,3,4,5], so for j in [1,2,3,4,5]...
            if (source_array[i] % 2 == 1 and source_array[j] % 2 == 1) and (source_array[j] < source_array[i]):
                ints = source_array[i]   # initialize ints to be source_array[i]
                source_array[i] = source_array[j]   ## initializ srouce_array[i] to be source_array[j]
                source_array[j] = ints   # now initialize source_array[j] to be ints
    return(source_array)   # return the source_array list
print(sort_array(n))


# 62) Given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.
#     Going to one direction and coming back the opposite direction is a needless effort.
#     ex: ["NORTH", "WEST", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "SOUTH"] ---> ["NORTH", "WEST", 'WEST', 'SOUTH']
#     ex: ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"] ---> ["WEST"]
          
a = ["NORTH", "WEST", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "SOUTH"]
def dirReduc(arr):
    result = []   # initializing result to be an empty list
    pairs = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
      }   # initializing pairs to be the dictionary of keys and values
    for i in arr:   # for i in ["NORTH", "WEST", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "SOUTH"]
        if result and result[-1] == pairs[i]:   # if result(which is empty list) and result[-1](last item in result) is in pairs
            result.pop()   # pop i out of result
        else:
            result.append(i)   # otherwise append i to result
    return(result)   # return the list result
print(dirReduc(a))


# 63) Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

'''
Method 1: search in dict by taking difference
'''
integers = [1, -2, 3, 0, -6, 1]
sum_value = -6
def sum_pairs(ints, s):
    dictionary = {}   # initialize an empty dictionary
    for i in range(len(ints)):   # range(len(ints)) = range(len([1, -2, 3, 0, -6, 1])) = range(6) = [0,1,2,3,4,5], so for i in [0,1,2,3,4,5]
      result = s - ints[i]   # initializing result to be sum_value - ints[i]
      if result in dictionary:   # if result in dictionary, then
          return [result, ints[i]]   # return a list of result, ints[i]
      dictionary[ints[i]] = None   # initialize None as value for i'th key in dictionary
print(sum_pairs(integers, sum_value))

'''
Method 2: search in set by taking difference
'''
integers = [1, -2, 3, 0, -6, 1]
sum_value = -6
def sum_pairs(ints, s):
    sets = set()   # initializing sets to be an empty set()
    for i in ints:   # for i in [1, -2, 3, 0, -6, 1]
        if s - i in sets:   # if difference of s - i in sets, then
            return[s - i, i]   # return a list of s-i, i
        else:
            sets.add(i)   # otherwise insert(add) i to the initialized set
print(sum_pairs(integers, sum_value))

'''
Method 3: search in list by taking difference
'''
integers = [1, -2, 3, 0, -6, 1]
sum_value = -6
def sum_pairs(ints, s):
    arr = []   # initializing arr to be empty set
    for i in range(len(ints)):   # range(len(ints)) = range(len([1, -2, 3, 0, -6, 1])) = range(6) = [0,1,2,3,4,5], for i in [0,1,2,3,4,5]
        result = s - ints[i]   # initialize result to be differnece of s(=-6) - ints[i]
        if result in arr:   # if result in arr
            return[result, ints[i]]   # return a list with result and int[i]
        else:
            arr.append(ints[i])   # otherwise, append int[i] to arr
print(sum_pairs(integers, sum_value))


# 64) The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers.

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def maxSequence(arr):
    max = 0   # initializing max to be zero
    curr = 0   # initializing curr to be zero
    for i in arr:   # for i in [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        if curr > 0:     # if curr > 0, then
            curr += i   # increment curr by i
            if curr < 0:   # if curr < 0, then
                curr = 0   # set curr to be zero
            elif curr > max:   # if curr > max, then
                max = curr   # set max to be curr
        elif i > 0:   # if i > 0, then
            curr += i   # increment curr by i
    return (max)   # return max
print(maxSequence(array))

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def maxSequence(arr):
    max = 0   # initializing max to be zero
    curr = 0   # initializing curr to be zero
    for i in arr:   # for i in [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        curr += i   # # increment curr by i
        if curr < 0:   # if curr < 0, then
            curr = 0   # set curr to be zero
        elif curr > max:   # if curr > max, then
            max = curr   # set max to be curr
    return(max)   # return max
print(maxSequence(array))
