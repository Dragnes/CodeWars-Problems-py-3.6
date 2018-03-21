# CodeWar Problems


# 1) Change a string's cases from Upperto Lower or vice versa.
string = 'ASDF asdf'
def alternative_case(string):
    return(string.swapcase())
print(alternative_case(string))


# 2) Given an array, find the int that appears an odd number of times.
a = [20,1,-1,2,-2,3,3,3,5,1,2,4,20,4,-1,-2,5]
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2!=0:
            return(i)
print(find_it(a))


# 3) Smash the following:
# words = ['hello', 'world', 'this', 'is', 'great']
# to 'hello world ths is great'
words = ['hello', 'world', 'this', 'is', 'great']
def smash(words):
    return(" ".join(words))
print(smash(words))


# 4) Define a method that will sum the indices of an array
a = [20,1,-1,2,-2,3,3,3,5,1,2,4,20,4,-1,-2,5]
def sum_array(array):
    return(sum(array))
print(sum_array(a))

a = [20,1,-1,2,-2,3,3,3,5,1,2,4,20,4,-1,-2,5]
def sum_array(array):
    sum = 0
    for i in array:
        sum += i
    return(sum)
print(sum_array(a))


# 5) Reverse the string value passed into it: i.e. 'world'  --->  'dlrow'
string = ['world', 'dlrow']
def reverse(str):
    return (str[::-1])
print(reverse(string))

def reverse(string):
    string = string[::-1]
    return (string)
print(reverse(string))

string = 'world'
def reverse(s):
    s = list(s)
    s.reverse()
    return("".join(s))
print(reverse(string))


# 6) Reverse the string as follows: '123' ---> ['321', '21', '1']
# and 'abcde' ---> ['edcba', 'dcba', 'cda', 'ba', 'a']
string1 = '123'
string2 = 'abcde'
def reverse_slice(string):
    lst = []
    string = string[::-1]
    for s in range(len(string)):
        lst.append(string[s:])
    return(lst)
print(reverse_slice(string1))

def reverse_slice(s):
    return([s[-i::-1] for i in range(1, len(s) + 1)])
print(reverse_slice(string1))


# 7) Odd or Even?
Number = '11111111111111111'
def odd_or_even(num):
    num = int(num)
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(odd_or_even(Number))

Number = 11111111111111111
def odd_or_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(odd_or_even(Number))
    
Number = 22222222222222222
def odd_or_even(num):
    return('Even' if num % 2 == 0 else 'odd')
print(odd_or_even(Number))

Number = 33333333333333333
def odd_or_even(num):
    if num % 2 != 0:
        return "Odd"
    else:
        return "Even"
print(odd_or_even(Number))

Number = 44444444444444444
def odd_or_even(num):
    if num % 2 ==1:
        return "Odd"
    else:
        return "Even"
print(odd_or_even(Number))


# 8) Write a function that will put a dash between odd numbers.
Number = '9234751973461827569275623794610874735629'
def insert_dash(num):
    num = str(num)
    ans = ''
    for i in range(len(num)-1):
        ans += num[i]
        if int(num[i]) % 2 == 1 and int(num[i+1]) % 2 == 1:
            ans += '-'
    ans += num[-1]
    return(ans)
print(insert_dash(Number))

Number = '9234751973461827569275623794610874735629'
def is_odd(a):
    a = int(a)
    if a % 2 == 0:
        return (False)
    else:
        return (True)
def insert_dash(num):
    num = str(num)
    num = list(num)
    for i in range(1, len(num)-1):
        if(is_odd(num[i]) and is_odd(num[i+1])):
            num[i] = str('-' + num [i])
    return (''.join(num))
print(insert_dash(Number))
    # Code below is similar to code above with consideration of different range
Number = '9234751973461827569275623794610874735629'
def is_odd(a):
    a = int(a)
    if a % 2 == 0:
        return (False)
    else:
        return (True)
def insert_dash(num):
    num = str(num)
    num = list(num)
    for i in range(1, len(num)):
        if(is_odd(num[i]) and is_odd(num[i-1])):
            num[i] = str('-' + num [i])
    return (''.join(num))
print(insert_dash(Number))


# 9) Sum all the positive integers in an array
array = [1, -2, 3, -4, 5, -6, 7]
def positive_sum(arr):
    sum = 0
    for a in arr:
        if a > 0:
            sum += a
    return (sum)
print(positive_sum(array))

array = [1, -2, 3, -4, 5, -6, 7]
def positive_sum(arr): 
    return(sum(a for a in arr if a>0))
print(positive_sum(array))


# 10) Write a function which repeats a given string n number of times.
string = 'acdc'
def repeat_str(n, s):
    n = int(n)
    s = str(s)
    return (n * s)
print(repeat_str(3, string))

string = 'acdc'
def repeat_str(n, string):
    return (n * string)
print(repeat_str(3, string))


# 11) Sum without highest and lowest number.
array = [1, -2, 3, -4, 5, -6, 7]
def sum_array(arr):
    if arr == None or len(arr) <= 2:
        return 0
    else:
        return (sum(arr) - max(arr) - min(arr))
print(sum_array(array))


# 12) Convert number to reversed array of digits.
numbers = 123456
def digitize(num):
    array = []
    num = str(num)
    num = num[::-1]
    for i in range(len(num)):
        array.append(int(num[i]))
    return (array)
print(digitize(numbers))

numbers = 123456
def digitize(n):
    return [int(i) for i in str(n)[::-1]]
print(digitize(numbers))


# 13) Secret message: Funtion that greets specific greeting to Kristy
Name = 'Kristy'
def greet(name):
    if name == 'Kristy':
        return ("Hello my love!")
    else:
        return("Hello " + name + "!")
print(greet(Name))


# 14) Return an array, where the first element is the count of positives numbers
#     and the second element is sum of negative numbers.
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
def count_p_sum_n(array):
    p_count = 0
    n_sum = 0
    if len(array) == 0:
        return []
    for a in array:
        if a > 0:
            p_count += 1
        else:
            a < 0
            n_sum += a
    return[p_count, n_sum]
print(count_p_sum_n(array))


# 15) Find Max and Min values of a list.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
def max_min(arr):
    return(max(arr), min(arr))
print(max_min(list))


# 16) Invert values in a list
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
def invert(lst):
    new_lst = []
    for l in lst:
        new_lst.append(l * -1)
    return (new_lst)
print(invert(arr))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
def invert (arr):
    return([-a for a in arr])
print(invert(arr))


# 17) Rock, Paper, Scissor
p1 = input('Rock, Paper, or Scissors?: ')
p2 = input('Rock, Paper, or Scissors?: ')
def r_p_s(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
        return "Player 1 Wins!"
    else:
        return "Player 2 Wins!"
print(r_p_s(p1, p2))


# 18) Remove the first and the last character from a string.
string = 'abcdefghijklmopqrstuwxyz'
def remove_char(string):
    return((string)[1:-1])
print(remove_char(string))

string = 'abcdefghijklmopqrstuwxyz'
def remove_char(string):
    new_string = string[1:-1]
    return(new_string)
print(remove_char(string))

string = 'abcdefghijklmopqrstuwxyz'
def remove_char(string):
    r = ''
    for i in range(1, len(string)-1):
        r += string[i]
    return r
print(remove_char(string))

string = 'abcdefghijklmopqrstuwxyz'
def remove_char(string):
    return (string[1:-1])
print(remove_char(string))


# 19) Remove spaces in a given string.
string = 'Coding is fun, it just requires time.'
def no_space(s):
    string = s.replace(' ', '')
    return string
print(no_space(string))

string = 'Coding is fun, it just requires time.'
def no_space(s):
    return(s.replace(' ', ''))
print(no_space(string))


# 20) Sum of two lists
lst1 = [2, 4, 6]
lst2 = [1, 3, 5]
def sum_lists(lst1, lst2):
    return (sum(lst1 + lst2))
print(sum_lists(lst1, lst2))


# 21) Convert a number to a string
number = 123456789
def num_to_string(num):
    return str(num)
print(num_to_string(number))


# 22) Convert a string to a number
string = '123456789'
def string_to_num(str):
    return(int(str))
print(string_to_num(string))

# 23) Convert boolean value to a string "Yes" string for true, or a "No" string for false.
string = True
def bool_to_str(bool):
    if bool == True:
        return('Yes')
    else:
        return('No')
print(bool_to_str(string))

string = False
def bool_to_str(bool):
    return('Yes' if bool else 'No')
print(bool_to_str(string))

# 24) To Square to not to Square
lst = [4, 3, 9, 2, 7, 1]
def square_or_square_root(arr):
    output = []
    for a in arr:
        root = a ** (0.5)
        if root.is_integer():
            output.append(root)
        else:
            output.append(a*a)
    return(output)
print(square_or_square_root(lst))

lst = [4, 3, 9, 2, 7, 1]
from math import sqrt
def square_or_square_root(arr):
    return[sqrt(a) if sqrt(a).is_integer() else a*a for a in arr]
print(square_or_square_root(lst))

lst = [4, 3, 9, 2, 7, 1]
import math
def square_or_square_root(arr):
    output = []
    for a in arr:
        n = math.sqrt(a)
        if n % 1 == 0:
            output.append(n)
        else:
            output.append(a*a)
    return output
print(square_or_square_root(lst))


# 25) If bonus is given, multiply the salary by 10

Salary = 50000
bonus = True
def bonus_time(salary, bonus):
    if bonus == True:
        return('$' + str(salary * 10))
    else:
        return('$' + str(salary))
print(bonus_time(Salary, bonus))

