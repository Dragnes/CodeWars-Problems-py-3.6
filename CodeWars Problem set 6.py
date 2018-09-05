# Codewars Problem set 6

# 77) You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.
#     The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
#     You always walk only a single block in a direction and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes
#     (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

def isValidWalk(walk):
    #determine if walk is valid
    x = 0
    y = 0
    for d in walk:
        print (d)
        if d=='n':
            y+=1
        if d=='s':
            y-=1
        if d=='e':
            x+=1;
        if d=='w':
            x-=1
    print ('result:'+str(x)+','+str(y))
    if (x==0 and y==0 and len(walk)==10):
        print ('true')
        return True
 
    else:
        return False

def isValidWalk(walk):
    if (walk.count('n') == walk.count('s') and 
        walk.count('e') == walk.count('w') and
        len(walk) == 10):
            return True
    return False


# 78) You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
#     Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ('')
    longest = index = 0
    for i in range(n - k + 1):
        length = sum([len(s) for s in strarr[i: i + k]])
        if length > longest:
            longest = length
            index = i
    return (''.join(strarr[index: index + k]))
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))

def longest_consec(strarr, k):
    result = ""
    if k > 0 and len(strarr) >= k:
        for i in range(len(strarr) - k + 1):
            s = ''.join(strarr[i:i+k])
            if len(s) > len(result):
                result = s           
    return(result)
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))


# 79) Your task is to construct a building which will be a pile of n cubes.
#     The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.
#     You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?
#     The parameter of the function findNb (find_nb, find-nb, findNb) will be an integer m and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

def find_nb(m):
    if 1 ** 3 == m:
        return 1
    else:
        n = 2
        volume = 1
        while volume < m:
            volume = volume + n ** 3
            if volume == m:
                return n
            else:
                n = n + 1
                continue
        return -1
print(find_nb(26825883955641))

def find_nb(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n**3
        if volume == m:
            return (n)
        n += 1
    return (-1)
print(find_nb(135440716410000))


# 80) Write a function that takes an (unsigned) integer as input, and returns the number of bits that are equal to one in the binary representation of that number.
#     Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def countBits(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total
print(countBits(1234))

def countBits(n):
    n = format(n,'b').zfill(8)
    count = 0
    for i in str(n):
        if int(i):
            count += 1
    return count
print(countBits(1234))
