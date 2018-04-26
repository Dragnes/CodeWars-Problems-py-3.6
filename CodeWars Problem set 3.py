# Codewars Problem set 3


# 44) example: Not Jaden-Cased: "How can mirrors be real if our eyes aren't real."
#              Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real."
#              convert from Not Jaden-Cased to Jaden-Cased

string = "how can mirrors be real if our eyes aren't real."
def toJadenCase(string):
  capitalized_words = [word.capitalize() for word in string.split(" ")]
  return (" ".join(capitalized_words))
print(toJadenCase(string))

string = "how can mirrors be real if our eyes aren't real."
def toJadenCase(string):
    words = string.split(" ")   # initializing words to split string as a list --> ['how', 'can', 'mirrors', 'be', 'real', 'if', 'our', 'eyes', 'aren't, 'real']
    jaden_cased = []   # initializing jaden_cased to be an empty list
    for word in words:   # words = string.split() = ['how', 'can', 'mirrors', 'be', 'real',... ], for 'How' in words
        title_cased = word[0].upper() + word[1:]   # title_cased = (word[0].upper() = 'H') + (word[1:] = 'ow')
        jaden_cased.append(title_cased)   # append title_cased to our initialized empty jaden_cased list, then repeat this for all word in words
    return (" ".join(jaden_cased))   # return jaden_cased list joined together as a string with a space between each indices in the list
print(toJadenCase(string))

string = "how can mirrors be real if our eyes aren't real."
def toJadenCase(string):
    words = []
    st = string.split()
    for i in st:
        il = list(i)
        il[0] = il[0].upper()
        words.append(''.join(il))
    return (' '.join(words))
print(toJadenCase(string))

string = "How can mirrors be real if our eyes aren't real."
def toJadenCase(string):        
    return (" ".join(word.capitalize() for word in string.split()))
print(toJadenCase(string))


# 45) Write a function that returns the sum of all the multiples of 3 or 5 below a given integer.

number = 10
def solution(num):    
    sum = 0   # initializing sum to be 0
    for i in range(num):   # range(10) = [0,1,2,3,4,5,6,7,8,9] --> so for i in [0,1,2,3,4,5,6,7,8,9] which equals 0, then 1, then 2, loops till the last index 9
        if (i % 3 == 0) or (i % 5 == 0):   # if the index i is [(i % 3 == 0) = i divisible by 3 with 0 remainder] or [(i % 5 == 0) = i divisible by 5 with 0 remainder]
            sum += i   # increment the initialized sum by adding the i'th indices which are divisible by 3 or 5
    return(sum)   # return the sum when looping is finished for all i in range(10)
print(solution(number))

number = 10
def solution(num):
    multiple1 = 3   # initializing multiple1 to be 3
    multiple2 = 5   # initializing multiple2 to be 5
    sum = 0   # initializing sum to be 0
    for i in range(1, num):   # range(1, num) = range(1,10) = [1,2,3,4,5,6,7,8,9]
        if (i % multiple1 == 0) or (i % multiple2 == 0):   # # if the index i is [(i % 3 == 0) = i divisible by 3 with 0 remainder] or [(i % 5 == 0) = i divisible by 5 with 0 remainder] 
            sum += i   # increment the initialized sum by adding the i'th indices which are divisible by 3 or 5
    return(sum)   # return the sum when looping is finished for all i in range(1, 10)
print(solution(number))

number = 10000000000
def solution(num):
    return (sum(x for x in range(num) if (x % 3 == 0) or (x % 5 == 0)))
print(solution(number))


# 46) Write a function that takes in a positive parameter num and returns its multiplicative persistence.
#     Which is the number of times you must multiply the digits in num until you reach a single digit.
#     ex: persistence(999) => 4 steps;  Because (9*9*9 = 729) = 1, (7*2*9 = 126) = 2, (1*2*6 = 12) = 3, and finally (1*2 = 2) = 4

number = 999
def persistence(num):
    num = str(num)   # num is string of num which is "999"
    count = 0   # initializing count to be 0
    while len(num) > 1:   # len(num) = len("999") = 3: so while the condition 3 > 1 is true:
        total = 1   # initializing total = 1 instead of t = 0 because we will multiply numbers to total
        for i in num:   # i1 = '9', i2 = '9', i3 = '9'
            total *= int(i)   # multiply i1 to the initialized total then setting that equal to total, then multiply i2 to total, then multiply i3 to total incrementally
        num = str(total)   # str(total) = '9*9*9' = '729', setting num = '729'
        count += 1   # increment count by adding 1, previously was 0. Going back to while loop till condition becomes false
    return(count)   # return the final count until the while loop became false
print(persistence(number))

number = 999
def persistence(num):
    if str(num) == 1:   # if number is a one digit number return 0
        return 0
    count = 0   # initializing count to be 0
    while len(str(num)) > 1:   # len(str(num)) = len(str(999)) = len("999") = 3: while the condition 3 > 1 is true
        total = 1   # initialize total to be 1
        for i in str(num):   # i1 = '9', i2 = '9', i3 = '9'
            total *= int(i)   # increment by multiply i1 to the initialized total then setting that equal to total, then multiply i2 to total, then multiply i3 to total incrementally
        num = total    # str(total) = 9*9*9 = 729, setting num = 729
        count += 1   # increment count by 1, previously was 0. Going back to while loop till condition becomes false
    return (count)   # return the final count until the while loop became false
print(persistence(number))



# 47) The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
#     Write a functioni that returns the 'outlier' N.

arr1 = [2, 4, 0, 100, 4, 11, 2602, 36]
arr2 = [160, 3, 1719, 19, 11, 13, -21]
def find_outlier(arr):
    if arr[0] % 2 != arr[1] % 2:   # for odd array with an even outlier
        return (arr[0] if arr[2] % 2 == arr[1] % 2 else arr[1])
    for i in arr:   # for even array with odd outlier
        if i % 2 != arr[0] % 2:
            return (i)
print(find_outlier(arr1))
print(find_outlier(arr2))

arr1 = [2, 4, 0, 100, 4, 11, 2602, 36]
arr2 = [160, 3, 1719, 19, 11, 13, -21]
def find_outlier(arr):
    odds = [x for x in arr if x % 2 != 0]
    evens = [x for x in arr if x % 2 == 0]
    return(odds[0] if len(odds) < len(evens) else evens[0])
print(find_outlier(arr1))
print(find_outlier(arr2))


# 48)  Given n, take the sum of the digits of n. If that value has two digits, continue reducing in this way until a single-digit number is produced.
#      ex: 942 --> 9+4+2 = 15 --> 1+5 = 6

'''
Method 1's
'''
number = 942
def digital_root(n):
    n = str(n)   # initializing n to be str(n)
    sum = 0   # initializing sum to be 0
    for a in n:   # for a in (str(n)='942') = '9'
        sum+= int(a)   # increment sum by the each int(a) in n 
    n = sum   # return the sum from previous line as n
    if n < 10:   # if n (which is the sum) is less 10, then
        return(n)   # return n
    else:   # otherwise
        return(digital_root(n))   # return digital_root of n (which is the sum) until n is less than 10. So I think a while loop can be used for this problem.
print(digital_root(number))

number = 942
def digital_root(n):
    n = sum(int(x) for x in str(n))   # n is the sum of all int(indices = x) of x in string of n
    if n < 10:   # if n from previous line is less than 10, then
        return(n)   # return n
    return(digital_root(n))   # 'else' return(digital_root) till n is less than 10
print(digital_root(number))

number = 942
def digital_root(n):
    n = sum(int(x) for x in str(n))    # n is the sum of all int(indices = x) of x in string of n
    if n > 10:   # if n from previous line is greater than 10, then
        return(digital_root(n))   # return digital_root on n
    return(n)   # 'else' return n which is less than 10
print(digital_root(number))

'''
Method 2's
'''
number = 942
def digital_root(n):
    n = str(n)   # initializing n to be str(n)
    sum = 0   # initializing sum to be 0
    for a in n:   # for a in (str(n)='942') = '9'
        sum+= int(a)   # increment sum by the each int(a) in n 
    n = sum   # return the sum from previous line as n
    while n < 10:   # if n (which is the sum) less than 10, then
        return(n)   # return n
    else:
        return(digital_root(n))   # else return digital_root of n (which is the sum) until n is less than 10
print(digital_root(number))

number = 942
def digital_root(n):
    n = sum(int(x) for x in str(n))   # n is the sum of all int(indices = x) of x in string of n
    while n < 10:   # while n from the previous line is less than 10, then
        return(n)   # return n
    return(digital_root(n))   # return digital_root of n (which is the sum) until n is less than 10
print(digital_root(number))

num = 942
def digital_root(n):
    n = sum(int(x) for x in str(n))   # n is the sum of all int(indices = x) of x in string of n
    while n > 10:   # while n (the sum) from previous line is greater than 10, then
        return(digital_root(n))   # return digital_root on n (the sum)
    return(n)   # 'else' return n which is less than 10
print(digital_root(number))
# or the code above written simpler
num = 942
def digital_root(n):
    while n > 10:
        n = sum(int(x) for x in str(n))
    return(n)
print(digital_root(number))


# 49) Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.
#     in other words: Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
''' Exampls
dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
'''

def dig_pow(n, p):
    num = str(n)   #initializing num to be string of n
    total = 0   # initializing total to be 0
    for i in num:
        total += pow(int(i), p)   # increment total by adding (the power of int(i'th idex of num) to p'th value(given)) to the initialized total
        p += 1   # the given p is incremented by 1
    if total % n == 0:   # if total divided my n with a remainder of 0, then
        return (total // n)   # return total divided by n
    else:
        return -1   # otherwise return -1
print(dig_pow(46288, 3))

n = 46288
p = 3
def dig_pow(n, p):
    num = str(n)
    total = sum([int(num[i]) ** (p + i) for i in range(len(num))])
    return (total / n if (total % n) == 0 else -1)
print(dig_pow(n, p))


# 50) How many different squares are there in a NxN grid?

n = 5
def count_squares(n):
    s = 0   # initializing s to be 0
    for i in range(1, n+1):   # if n = 5 then range(1, n+1) = [1,2,3,4,5], for i in the list
        s += (n-i+1)**2   # incrementing s by adding [(n-i+1)**2] to initial value of s
    return(s)
print(count_squares(n))

n = 5
def count_squares(n):
    return(sum([i * i for i in range(n+1)]))   # for i in range(n+1) (if n = 5, range(n+1) = [0,1,2,3,4]), return sum([0*0, 1*1, 2*2, 3*3, 4*4])
print(count_squares(n))

n = 5
def count_squares(n):
    return(sum([pow(i, 2) for i in range(1, n+1)]))   # different way of writing previous solution: pow(i, 2) = i * i
print(count_squares(n))

n=5
def count_squares(n):
    total = []   # initializing total to be an empty list
    for i in range(n+1):   # if n = 5, range(n+1) = range(6) = [0,1,2,3,4,5]
        total.append(i * i)   # to an empty list, append the squares of i in range(n+1)
    return(sum(total))   # sum all indices of the list total
print(count_squares(n))


# 51) Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed.
#     Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

s = "Could this be a sentence"
def spin_words(sentence):
    arr = sentence.split()   # initializing arr to split sentence as a list: ex: "Could this be a sentence" --> ["Could", "this", "be", "a" "sentence"]
    ans = []   # initializing ans to be an empty list
    for i in arr:   # for i in arr = ["Could", "this", "be", "a" "sentence"]
        if len(i) >= 5:   # if length of string i is greater than or equal to 5, then:
            ans.append(i[::-1])   # append i in reversed order ([::-1]) to once empty list, ans. This line would work also with: ans.append(''.join(list(reversed(i))))
        else:
            ans.append(i)   # append i to an once empty list, ans
    return (' '.join(ans))   # return ans list joined together with space between each of the indices
print(spin_words(s))

s = "Could this be a sentence"
def spin_words(sentence):
    ans = []   # initializing ans to be an empty list
    for i in sentence.split():   # for i in sentence.split() = ["Could", "this", "be", "a" "sentence"]
        if len(i) >= 5:   # if length of string i is greater than or equal to 5, then:
            ans.append(''.join(list(reversed(i))))   # i[::-1] = ''.join(list(reversed(i)))
        else:
            ans.append(i)   # append i to an once empty list, ans
    return (' '.join(ans))   # return ans list joined together with space between each of the indices
print(spin_words(s))

s = "Could this be a sentence"
def spin_words(sentence):
    return (' '.join(i[::-1] if len(i) >= 5 else i for i in sentence.split()))   # sentence.split() = ["Could", "this", "be", "a" "sentence"], for i in sentence.split(), if len(i) >= 5 then return ' '.join(i[::-1]), else return ' '.join(i)
print(spin_words(s))

s = "Could this be a sentence"
def spin_words(sentence):
    return (' '.join(i if len(i) < 5 else i[::-1] for i in sentence.split()))   # similar to code above, besides if len(i)<5
print(spin_words(s))


# 52)  Task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.
#      ex: For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

sentence = "is2 Thi1s T4est 3a"
def order(sentence):
    if len(sentence) == 0:   # if length of sentence = 0, then
        return ("")   # return empty string
    words = {}   # initializing words to be an empty dictionary
    for word in sentence.split():   # sentence.split() = ['is2', 'Thi1s', 'T4est', '3a']--> for words in ['is2', 'Thi1s', 'T4est', '3a']--> 'is2' in ['is2', 'Thi1s', 'T4est', '3a']
        for letter in word:   # for 'i' in 'is2' loop through evry letter in word in ['is2', 'Thi1s', 'T4est', '3a']
            if letter.isdigit():   # if letter is a digit, then
                words[int(letter)]=word   # words[int(letter)=(key)] = word (new value). "appending" to the dictionary words from integer value found by looping each item in sentence.split()
                #   we get a dictionary words = {2:'is2', 1:'Thi1s', 4:'T4est', 3:'3a'}
    result = [words[key] for key in sorted(words.keys())]   # result = list of sorted keys = ['Thi1s', 'is2', '3a', 'T4est']
    return (' '.join(result))   # return result list joined together with space between each of the indices
print(order(sentence))

sentence = "is2 Thi1s T4est 3a"
def order(sentence):
    if not sentence:   # if not sentence = if len(sentence) == 0
        return ("")   # return empty string
    result = []   # initializing result to be an empty list
    for i in range(1, 5):   # for i in range(1, 5)=[1,2,3,4]
        for words in sentence.split():  # sentence.split() = ['is2', 'Thi1s', 'T4est', '3a']--> for words in ['is2', 'Thi1s', 'T4est', '3a']--> 'is2' in ['is2', 'Thi1s', 'T4est', '3a']
            if str(i) in words:   # if i'th index in range(1,5) is a string in item, then
                 result.append(words)   # append words to the initialized list
    return (" ".join(result))   # return result list joined together with space between each of the indices
print(order(sentence))


# 53) Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string.
#     ex: "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
#     ex: "indivisibility" -> 1 # 'i' occurs six times

text = "Indivisibilities"
def duplicate_count(text):
    seen = set()   # initializing seen to be an empty set
    dupes = set()   # initializing dupes to be an empty set
    for i in text:   # for i in "Indivisibilities" 
        i = i.lower()   # initializing i to be lower()
        if i not in seen:   # if i'th indices of text not in the initialized empty set, then
            seen.add(i)   # 'append' i to the set seen by adding i to the set
        else:
            dupes.add(i)   # otherwise, 'append' i to the set dupes by adding i to the set
    return len(dupes)   # return length of the duplicates characters in assembled into set dupes
print(duplicate_count(text))

text = "Indivisibilities"
def duplicate_count(text):
    count = 0   # initializing count to be 0
    text = text.lower()   # initializing text to be lower case of given text
    for i in set(text):   # set(text) = all characters from text in a set
        if text.count(i) > 1:   # text.count(i) = integer value if elements in set text. if text.count(i) > 1, then
            count += 1   # increment count by adding 1
    return (count)   # after finishing the for loop, return count
print(duplicate_count(text))

text = "indivisibility"
def duplicate_count(text):
    text = text.lower()
    count = 0
    dictionary = {}
    for i in range(0,len(text)):
        dictionary[text[i]] = 0
        
    for key in dictionary:
        for i in range(0,len(text)):
            if(key == text[i]):
                dictionary[key] = dictionary[key] + 1
                
    for key in dictionary:
        if(dictionary[key] > 1):
            count = count + 1
    return (count)
print(duplicate_count(text))


# 54) Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. 
#     ex: likes [] // must be "no one likes this"
#     ex: likes ["Peter"] // must be "Peter likes this"
#     ex: likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
#     ex: likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
#     ex: likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"

names = ["Alex", "Jacob", "Mark", "Max"]
def likes(names):
    len_names = len(names)   # len_names = length of names = 4
    if len_names == 0:
        return('no one likes this')
    if len_names == 1:   # if len_names == 1, then
        return(names[0] + ' likes this')   # name[0] = 'Alex'. concatenate name[0] with ' likes this'
    if len_names == 2:   # if len_name == 2, then
        return(names[0] + ' and ' + names[1] + ' like this')   # concatenate name[0], name[1] to string
    if len_names == 3:   # if len_names == 3
        return(names[0] + ', ' + names[1] + ' and ' + names[2] + ' likes this')   # concatenate name[0], name[1], name[2] to string
    else:   # if len_names > 3
        return(names[0] + ', ' + names[1] + ' and ' + str(len_names - 2) + ' others like this')   # concatenate name[0], name[1], (str(len_names - 2) = integer value in a string) to string
print(likes(names))

names = ["Alex", "Jacob", "Mark", "Max"]
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % (names[0])   # %s place holder for string value, value %s holds = name[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])   # first %s is the first place holder for string value of name[0], second %s is the second place holder for string value name[1] 
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)   # third %s is the third place holder for string value of (len(name)-2) = 2
print(likes(names))

names = ["Alex", "Jacob", "Mark", "Max"]
def likes(names):
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
        }
    # created a dictionary d with key and values with placeholders
    length = len(names)
    return (d[min(4, length)].format(*names, others = length - 2))
    # d[min(4, length)] = calls minimum of (4, length) value for the smallest key, ex: if length = 4 call value of key 4
    # * in *names = names[0], names[1],... = all values in names
    # others = len(name) - 2
print(likes(names))
