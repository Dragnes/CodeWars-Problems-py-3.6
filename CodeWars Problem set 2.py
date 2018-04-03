# CodeWars Problem set 2


# 26) Fake Binary: Given a string of digits, replace any digit below 5 with '0' 
#                  and any digit 5 and above with '1'. Return the resulting string. 
string = "4591052873"
def fake_binary(s):
    str = ""
    for num in s:
        if int(num) < 5:
            str = str + "0"
        else:
            str = str + "1"
    return (str)
print(fake_binary(string))

string = "4591052873"
def fake_binary(s):
    return("".join("0" if int(num) < 5 else "1" for num in s))
print(fake_binary(string))


# 27) Write a function that does the following
#  "abcd"---->"A-Bb-Ccc-Dddd"
#  "RqaEzty"---->"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#  "cwAt"---->"C-Ww-Aaa-Tttt"
string = "abcd"
def accum(s):
    output = ''
    for i in range(len(s)):
        output += (s[i] * (i+1)) + '-'
    return(output.title()[:-1])
print(accum(string))

string = 'RqaEzty'
def accum(s):
    output = ''
    for i, c in enumerate(s):
        output += c.upper() + (c.lower() * i) + '-'
    return(output[:-1])
print(accum(string))

string = 'cwAt'
def accum(s):
    return('-'.join(c.upper() + c.lower() * i for i,c in enumerate(s)))
print(accum(string))


# 28) Reverse words in a string

string = "Hello World!"
def reverse(s):
    a = s.split(' ')       # split
    a.reverse()            # reverse
    a = ' '.join(a)        # join
    return a
print(reverse(string))

string = "Hello World."
def reverse(s):
    return(' '.join(s.split(' ')[::-1]))
print(reverse(string))


# 29) Square (n) sum
#   [1, 2, 2] ---> [1, 4, 4] ---> 9

lst = [1, 2, 2]
def square_sum(num):
    return(sum(n**2 for n in num))
print(square_sum(lst))

lst = [1, 2, 2]
def square_sum(num):
    output = 0
    for n in num:
        output += n**2
    return(output)
print(square_sum(lst))


# 30) Count by X: given two arguments creat a function that return a list of len(n)
#                 with multiples of (x)    i.e. count_by(1, 5) ---> [1, 2, 3, 4, 5]

x = 2
n = 10
def count_by(x, n):
    return [x * i for i in range(1, n + 1)]
print(count_by(x, n))

x = 2
n = 10
def count_by(x, n):
    count = []
    for i in range(1, n+1):
        count.append(x * i)
    return (count)
print(count_by(x, n))


# 31) Power of 2
# explained better by example: n = 0  ==> [1]           # [2^0]
#                              n = 1  ==> [1, 2]        # [2^0, 2^1]
#                              n = 2  ==> [1, 2, 4]     # [2^0, 2^1, 2^2]

n = 1
def power_of_two(n):
    return[2**x for x in range(n+1)]
print(power_of_two(n))

n = 5
def power_of_two(n):
    output = []
    for x in range(n + 1):
        output.append(2**x)
    return(output)
print(power_of_two(n))


# 32) # Think of a way to store the languages as a database (eg an object). The languages are listed below so you can copy and paste!
#       Write a 'welcome' function that takes a parameter 'language' (always a string), and returns a greeting - if you have it in your database. 
#       It should default to English if the language is not in the database, or in the event of an invalid input.

data_base = {'english': 'Welcome',
'czech': 'Vitejte',
'danish': 'Velkomst',
'dutch': 'Welkom',
'estonian': 'Tere tulemast',
'finnish': 'Tervetuloa',
'flemish': 'Welgekomen',
'french': 'Bienvenue',
'german': 'Willkommen',
'irish': 'Failte',
'italian': 'Benvenuto',
'latvian': 'Gaidits',
'lithuanian': 'Laukiamas',
'polish': 'Witamy',
'spanish': 'Bienvenido',
'swedish': 'Valkommen',
'welsh': 'Croeso'}
def greet(language):
    return(data_base.get(language, "Welcome"))
print(greet(data_base('czech', "Welcome")))


# 33) Remove exclamation marks from a given string.

string1 = 'Hello World!'
def remove_exclamation_marks(s):
    return(s.replace('!', ''))
print(remove_exclamation_marks(string1))

string2 = 'Hello! World!!'
def remove_exclamation_marks(s):
    return(''.join([x for x in s if x != '!']))
print(remove_exclamation_marks(string2))

string3 = 'Hello,! World!.!'
def remove_exclamation_marks(s):
    x = s.replace('!', '')
    return (x)
print(remove_exclamation_marks(string3))


# 34 Remove the last exclamation mark from a given string.

string1 = "!Hi!"
def remove(s):
    if s.endswith("!"):
        s = s[:-1] 
    return (s)
print(remove(string1))

string2 = "Hi! Hi!!"
def remove(s):
    return(s[:-1] if s.endswith("!") else s)
print(remove(string2))


# 35) When provided with a number between 0-9, return it in words.

number = 3
def switch_it_up(num):
    if num == 0:
        return("Zero")
    elif num == 1:
        return("One")
    elif num == 2:
        return("Two")
    elif num == 3:
        return("Three")
    elif num == 4:
        return("Four")
    elif num == 5:
        return("Five")
    elif num == 6:
        return("Six")
    elif num == 7:
        return("Seven")
    elif num == 8:
        return("Eight")
    else:
        return("Nine")
print(switch_it_up(number))

number = 7
def switch_it_up(n):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]
print(switch_it_up(number))

number = 4
def switch_it_up(number):
    dict = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    0: "Zero"}
    
    return(dict.get(number))
print(switch_it_up(number))


# 36) -If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".
#     -If he doesn't get 10 hoops, return the string "Keep at it until you get it".

n = int(input('How many did you do Alex? '))
def hoopCount(n):
    if n > 9:
        return ('Great, now move on to tricks.')
    else:
        return ('Keep at it until you get it.')
print(hoopCount(n))

n = 5
def hoopCount(n):
    if n >= 10:
        return 'Great, now move on to tricks'
    else:
        return 'Keep at it until you get it'
print(hoopCount(n))

n = 11
def hoopCount(n):
    return ("Keep at it until you get it" if n<10 else "Great, now move on to tricks")
print(hoopCount(n))


# 37) Create a function which answers the question "Are you playing banjo?".
#     If your name starts with the letter "R" or lower case "r", you are playing banjo!

name = "Rob"
def areYouPlayingBanjo(name):
    if  name[0] == "R" or name [0] == 'r':
        return(name + " plays banjo")
    else:
        return(name + " does not play banjo")
print(areYouPlayingBanjo(name))

name = "rob"
def areYouPlayingBanjo(name):
    if name[0].upper() == 'R':       # or .lower to convert name[0] into 'r'
        return(name + ' plays banjo')
    else:
        return(name + ' does not play banjo')
print(areYouPlayingBanjo(name))

# 38) Write a function that returns a reversed sequence list for a given n from n to 1
#     ex: n = 5 -----> [5, 4, 3, 2, 1]

n = 5
def reverse_seq(n):
    a = list(reversed(range(n+1)))
    return (a[:-1])
print(reverse_seq(n))

n = 7
def reverseseq(n):
    return (list(range(n, 0, -1)))
print(reverse_seq(n))


# 39) Write a function that returns a sequenced list for a given n from 1 to n
#     ex: n = 5 -----> [1, 2, 3, 4, 5]

n = 5
def monkey_count(n):
    return(list(range(1, n+1)))
print(monkey_count(n))

n = 7
def monkey_count(n):
    lst = []
    for i in range(1, n+1):
        lst.append(i)
    return(lst)
print(monkey_count(n))


# 40) Reverse(123)---->(321)

n = 123
def reverse(n):
    x=0
    d=0
    while n > 0:
        d = n % 10
        x= x * 10 + d
        n = n // 10
    return (x)
print(reverse(n))

n = '456'
def reverse(s):
    return int(str(n[::-1]))
print(reverse(n))


# 41) Return the middle characther of a string.
#     if string length is odd return the middle character.
#     if string length is even return the middle two characters.

string = "AbCdefGHIjk"
def get_middle(s):
    i,j = divmod(len(s),2)
    if not j:
        return(s[i-1:i+1])
    else:
        return(s[i])
print(get_middle(string))

string = "AbCdeffGHIjk"
def get_middle(s):
    i,j = divmod(len(s),2)
    return(s[i-(1 if not j else 0): i+1])
print(get_middle(string))


# 42) In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
#    ex: DNA_strand ("ATTGC") # return "TAACG"

DNA = "CGCTCGTCTAGGGATGACCCCGT"
def DNA_strand(dna):
    char = list(dna)
    opposite = []
    for i in char:
        if i == "A":
            opposite.append("T")
        elif i == "T":
            opposite.append("A")
        elif i == "C":
            opposite.append("G")
        else:
            opposite.append("C")
    return (''.join(opposite))
print(DNA_strand(DNA))

DNA = "CGCTCGTCTAGGGATGACCCCGT"
def DNA_strand(dna):
    reference = { "A":"T",
                  "T":"A",
                  "C":"G",
                  "G":"C"
                  }
    return ("".join([reference[x] for x in dna]))
print(DNA_strand(DNA))

DNA = "CGCTCGTCTAGGGATGACCCCGT"
reference = {"A":"T",
             "T":"A",
             "C":"G",
             "G":"C"
             }
def DNA_strand(dna):
    return(''.join([reference[x] for x in dna]))
print(DNA_strand(DNA))

DNA = "CGCTCGTCTAGGGATGACCCCGT"
def DNA_strand(dna):
    return(dna.translate(str.maketrans('ATCG', 'TAGC')))
print(DNA_strand(DNA))


# 43)  A function that can take any non-negative integer as an argument and return its digits in descending order.
#      ex: 423897234 -----> 987443322

num = 423897234
def Descending_Order(num):
    num_list = []
    for i in range(len(str(num))):
        num_list.append(str(num)[i])
    sorted_list = sorted(num_list, reverse = True)
    sorted_str = ''.join(sorted_list)
    return(int(sorted_str))
print(Descending_Order(num))

num = 423897234
def Descending_Order(num):
    return(int(''.join(sorted(str(num), reverse = True))))
print(Descending_Order(num))

num = 423897234
def Descending_Order(num):
    return (int(''.join(sorted(list(str(num)), reverse=True))))
print(Descending_Order(num))

num = 423897234
def Descending_Order(num):
    return int(''.join(sorted(str(num))[::-1]))
print(Descending_Order(num))

num = 423897234
def Descending_Order(num):
    s = str(num)
#   s = list(s)        not really needed
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    return int(s)
print(Descending_Order(num))





