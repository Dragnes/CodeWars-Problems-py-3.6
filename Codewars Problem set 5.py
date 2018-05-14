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