# Codewars Problem set 5


# 66) Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1)
#     Your function productFib takes an integer (prod) and returns an array:
#     [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
#     depending on the language if F(n) * F(n+1) = prod.
#     If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return
#     [F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
#     F(m) being the smallest one such as F(m) * F(m+1) > prod.

#     ex: productFib(714) # should return [21, 34, true], 
#         since F(8) = 21, F(9) = 34 and 714 = 21 * 34

n = 714
def productFib(prod):
    a = 0   # initializing a = 0
    b = 1   # initializing b = 1
    while prod > a * b:   # while prod is less than the product of a*b
        a, b = b, a + b   # a = b, b = a+b --> a=1, b=1+1=2, then a=2, b=2+1=3, then a=3, b=3+2=5...
    return [a, b, prod == a * b]   # return a list consist [a, b, a*b while == product]
print(productFib(n))


# 67) Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
#     ex: pig_it('Pig latin is cool') # igPay atinlay siay oolcay

text = 'Pig latin is cool !'
def pig_it(text):
    result = []   # initializing result to be an empty list
    for i in text.split():  # text.split()=[Pig', 'latin', 'is', 'cool', '!'], so for i in [Pig', 'latin', 'is', 'cool', '!'], i1='Pig', i2='latin'...
        if i not in '!?.':   # if i not in '!?.', then
            result.append(i[1:] + i[0] + 'ay')   # i[1:]='ig', i[0]=P, so append concatenated strings (i[1:] + i[0] + 'ay') to our empty list result
        else:
            result.append(i)   # otherwise, append i to result
    return(' '.join(result))   # return result by joining result with a space between each of its indices
print(pig_it(text))

text = 'Pig latin is cool !'
def pig_it(text):
    result = []   # initializing result to be an empty list
    for i in text.split():   # text.split()=[Pig', 'latin', 'is', 'cool', '!'], so for i in [Pig', 'latin', 'is', 'cool', '!'], i1='Pig', i2='latin'...
        if i.isalpha():   # if i is alphabet, then
            result.append(i[1:] + i[0] + 'ay')   # i[1:]='ig', i[0]=P, so append concatenated strings (i[1:] + i[0] + 'ay') to our empty list result
        else:
            result.append(i)   # otherwise, append i to result
    return(' '.join(result))   # return result by joining result with a space between each of its indices
print(pig_it(text))

text = 'pig latin !'
def pig_it(text):
    result = []   # initializing result to be an empty list
    text = text.split()   # text = text.split() = [Pig', 'latin', 'is', 'cool', '!']
    for i in text:   # for i in [Pig', 'latin', 'is', 'cool', '!'], i1='Pig', i2='latin'...
        if i.isalpha():   # if i is alphabet, then
            result.append(i[1:] + i[0] + 'ay')   # i[1:]='ig', i[0]=P, so append concatenated strings (i[1:] + i[0] + 'ay') to our empty list result 
        else:
            result.append(i)   # otherwise, append i to result
    return(' '.join(result))   # # return result by joining result with a space between each of its indices
print(pig_it(text))

text = 'pig latin !'
def pig_it(text):
    return " ".join([ i[1:] + i[0] + "ay" if i.isalpha() else i for i in text.split(" ") ])
print(pig_it(text))


#  68) The name of the person who drinks the n-th can of cola.
#      The cans are numbered starting from 1. "Sheldon", "Leonard", "Penny", "Rajesh", "Howard". In that order precisely the friends are in the queue initially.
#      ex: whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52)=="Penny"
#      ex: whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951)=="Leonard"

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
r = 52
def whoIsNext(names, r):
    while r > len(names):   # while r is greater than len(names)
        r = (r - len(names) + 1) >> 1   # r - len(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]) + 1 = 52 - 5 + 1 = 48. set r = 48 shifted right by 1 in binary
    return(names[r - 1])   # return index of names[r-1]
print(whoIsNext(names, r))


# 69) Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
#      The maximum time never exceeds 359999 (99:59:59)

s = 359999
def make_readable(seconds):
    hr = seconds//3600
    seconds = seconds % 3600
    m = seconds//60
    seconds = seconds % 60
    return('{:02d}'.format(hr) + ':' + '{:02d}'.format(m) + ':' + '{:02d}'.format(seconds))
print(make_readable(s))

s = 359999
def make_readable(seconds):
    return('{:02}:{:02}:{:02}'.format(seconds // 3600, (seconds // 60) % 60, seconds % 60))
print(make_readable(s))

s = 359999
def make_readable(seconds):
    hours = seconds // 3600
    m = (seconds % 3600) // 60
    seconds = seconds % 60
    return("{:02}:{:02d}:{:02}".format(hours,m,seconds))
print(make_readable(s))


# 70) Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

s1 = 'cedewaraaossoqqyt'
s2 =  'codewars'
def scramble(s1, s2):
    for c in set(s2):
        if s2.count(c) > s1.count(c):
            return(False)
    return(True)
print(scramble(s1, s2))


# 71) Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
#     ex: move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]

array = [False,1,0,1,2,0,1,3,"a"]
def move_zeros(array):
  result = []   # initializing result to be an empty list
  count = 0   # initializing count to be 0
  for i in array:   # for i in [False,1,0,1,2,0,1,3,"a"]
    if type(i) in (int, float) and i == 0:   # if type if object i in integer, float, and i = 0, then 
      count += 1   # increment count by 1
    else:
      result.append(i)   # otherwise append i to list result
  return(result + [0] * count)   # return the list result + count of 0
print(move_zeros(array))

array = ["a",0,0,"b","c","d",0,1,True,1,0,3,0,1,9,0,0,0,0,9]
def move_zeros(array):
    result = []
    for i in array[::-1]:
        if type(i) in (int, float) and i == 0:   # if type if object i in integer, float, and i = 0, then 
            result.append(0)   # append 0 to result
        else:
            result.insert(0, i)   # otherwise insert i at index 0 to result
    return(result)   # return the list result
print(move_zeros(array))


# 72) Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none.
#     ex: anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

word = 'abba'
words = ['aabb', 'abcd', 'bbaa', 'dada']
def anagrams(word, words):
    result = []   # initializing result to be an empty list
    for i in words:   # for i in ['aabb', 'abcd', 'bbaa', 'dada']
        if sorted(i) == sorted(word):   # if sorted(i)='aabb' == sorted(word) ='aabb', then
            result.append(i)   # append i to result
    return(result)   #   return the list result
print(anagrams(word, words))

word = 'abba'
words = ['aabb', 'abcd', 'bbaa', 'dada']
def anagrams(word, words):
    return([i for i in words if sorted(word) == sorted(i)])
print(anagrams(word, words))


# 73) You need to write regex that will validate a password to make sure it meets the following criteria:
#     at least six characters long
#     contains a lowercase letter
#     contains an uppercase letter
#     contains a number

regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"

regex="^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{6,}$"

from re import compile, VERBOSE

regex = compile("""
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
""", VERBOSE)


# 74) Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer).
#     For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200).
#     Ingredients that are not present in the objects, can be considered as 0.
#     ex: cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
#         must return 2

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
def cakes(recipe, available):
    Max_amount = 999999999999999   # initilizing Max_amount to be a large number
    for i in recipe:   # for i in {"flour": 500, "sugar": 200, "eggs": 1}, i1 = "flour", i2 = "sugar", i3 = "eggs"
        if i not in available:   # if i not in {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}, then
            return (0)   # return 0
        else:
            if Max_amount > available[i]//recipe[i]:   # available[i1] = 1200 and recipe[i] = 500, if Max_amount > 1200//500 is true then,
                Max_amount = available[i]//recipe[i]   # set Max_amount to be integer division of available[i] to recipe[i] (which is not a large number anymore)
    return (Max_amount)   # return Max_amount
print(cakes(recipe, available))

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
def cakes(recipe, available):
    list = []   # initializing list to en an empty list
    for i in recipe:   # for i in {"flour": 500, "sugar": 200, "eggs": 1}, i1 = "flour", i2 = "sugar", i3 = "eggs"
        if i not in available:   # # if i not in {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}, then
            return(0)   # return 0
        elif i in available:   # if i in {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
            list.append(available[i] // recipe[i])   # append integer division of (available[i] to recipe[i]) to the initialized empty list
    return(min(list))   # return the minimum value in list
print(cakes(recipe, available))
