import math
from functools import reduce
"""
def circle_data(radius = None,area = None):
    if radius == None and area == None:
        return 'At least 1 value is required'
    elif radius != None and area != None:
        return 'Only 1 parameter is required'
    if radius != None:
        return(f'Radius: {radius}, Diameter: {radius * 2}, Circumference: {radius * 2 * math.pi}, Area, {radius * radius * math.pi} ')
    else:
        radius_1 = math.sqrt((area/math.pi))
        return(f'Radius: {radius_1}, Diameter: {2 * radius_1}, Circumference: {radius_1 * 2 * math.pi}')




y = circle_data(6)
print(y)
"""


"""
def check_true(*args):
    for i in args:
        if bool(i) == False:
            return False
    return True

y = check_true(6,7,8,9,)
print(y)

"""

"""
d1 = {}
int_list = []
float_list = []
str_list = []
bool_list = []
def group_types(**kwargs):
    for i in kwargs:
        key_value = kwargs.get(i)
        if type(key_value) == int:

            int_list.append(key_value)
        elif type(key_value) == float:

            float_list.append(key_value)

        elif type(key_value) == str:

            str_list.append(key_value)
        elif type(key_value) == bool:

            bool_list.append(key_value)

    d1['Ints'] = int_list
    d1['Float'] = float_list
    d1['Str'] = str_list
    d1['Bool'] = bool_list

    return d1

x = group_types( a= 1,b = 1,c = True,d = 0.7,e = False, f = "Hello", g = 0)

print(x)

"""

"""
from collections import ChainMap
def subject_dict(**kwargs):
    m_list = []
    p_list = []
    c_list = []
    for key,value in kwargs.items():
        m,p,c = value
        m_list.append({key:m})
        p_list.append({key:p})
        c_list.append({key:c})

    return {"Maths":dict(ChainMap(*m_list)), "Physics": ChainMap(*p_list), "Chemistry":ChainMap(*c_list)}


x = subject_dict(Ram = [97,90,89], Anand = [78,99,82], Jon = [98,67,81])

print(x)
"""
#Args and Kwargs combined together
"""
def my_function(*args,**kwargs):
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,value)

y = my_function(10,11,12,13,14,a=0, f='hello')
"""

"""
def add_1(x):
    return x+1
print(add_1(5))
#Lambda Functions - anonymous function

y = lambda x:x+1
print(y(10))
print(y)
print(type(y))
z = add_1
print(type(z))
"""

"""
y = lambda x: x*x

print(y(10))

"""
"""
def my_func(*args):
    l1 = [i * i for i in args]
    return l1

print(my_func(3,5,6,7,8,9))


y = lambda x,y: x+y
print(y(3,5))
"""
#1
"""
1. Write a lambda function that will take 2 integers as parameters and return the largest of the two
Input 10,5
Output: 10
"""
"""
y = lambda x,z: max(x,z)

print(y(10,5))
"""

#2
"""
2. Write a lambda function that will return "E" when even number is passed and "O" when odd number is passed
Input: 8
Output: E
Input: 7
Output: O
"""
"""
y = lambda x: 'E' if x % 2 == 0 else 'O'

print(y(10))
"""

#3
"""
3. Write a lambda function that takes unlimited integers as parameters and return a list that contains the square
of each parameter
Input: 2,3,4
Output: [4, 9, 16]
"""
"""
y = lambda *args: [i * i for i in args]


print(y(3,5,6,7,8,9))

"""

#4
"""
4. Write a lambda function that takes unlimited arguments and returns a list of even numbers
Input: 1,2,3,4,5
Output: [2, 4]
"""


"""
y = lambda *args: [i for i in args if i % 2 == 0]


print(y(1,2,3,4,5,6,7))
"""

#5

'''
5. Write a lambda function that takes unlimited arguments and unlimited keyword arguments and returns the total
number of arguments passed
Input: 2,3,4,a=10,b=12 
Output: 5
'''

"""
y = lambda *args, **kwargs: len(args) + len(kwargs)

print(y(2,3,4,a=10,b=12, d=22))
"""

# map, filter, reduce
# map will take 1 or more iterable and process all of the elements that you have given in your mao funtion.


# map syntax(<function> *iterable(s)

#examples
"""
num_list = [1,2,3,4,5]

def square_num(n):
    square_list = [i ** 2 for i in n]
    return square_list

#print(square_num(num_list))



def sq_num(n):
    return n * n


y = map(sq_num, num_list)
"""

#print(list(y))

# map and lambda

#z = print(list(map(lambda n: n*n, num_list)))


#city_list = ["new york", "chicago", "san francisco", "dallas", "austin"]


#print(list(map(lambda city_name:city_name.title(), city_list)))

#print(list(map(lambda city_reverse: city_reverse[::-1], city_list)))


#radii_list = [1,2,3,4,5]

#print(list(map(lambda radius: round(2 * math.pi * radius, 5) , radii_list)))

#l_list = [7,10,4,3]

#w_list = [8,6,10,12]

"""
def perimeter(l,w):
    perimeters = []
    for i,j in zip(l,w):
        perimeters.append(i * 2 + j * 2)
    return perimeters

print(perimeter(l_list,w_list))
"""
"""
z = map(lambda l,w: l * 2 + w * 2,l_list, w_list )

print(list(z))
"""

# 1. Marks of some students in Maths, Physics and Chemistry are given as three lists. Write a function that would
# return the average marks as rounded integer.
# Input: get_average([75,83,92,65,98], [63,82,69,92,81], [57,98,93,62,76])
# Output: Average: [65, 88, 85, 73, 85]
"""
m = [75,83,92,65,98]
p = [63,82,69,92,81]
c = [57,98,93,62,76]


z = map(lambda m,p,c: round((m + p + c) / 3),m,p,c)

print(list(z))
"""

# 2. Take input of radii as unlimited parameter and provide diameter, circumference and area as a list of tuples.
# Round the result to 3 decimal places
# Input: get_dac(5,10,15,20,25)
# Output: [(10, 31.416, 78.54), (20, 62.832, 314.159), (30, 94.248, 706.858), (40, 125.664, 1256.637), (50, 157.08, 1963.495)]

"""
def get_dac(*args):
    z = map(lambda radii: (round(radii * 2,3), round(2 * math.pi * radii,3), round(math.pi * radii * radii,3)),args)
    return z


print(list(get_dac(5,10,15,20,25)))
"""



#3. Jack goes and buys some items from the grocery store. The items he purchased and the price are given here
#Item #, Name, Qty, Price/item
#768, Apple, 10, 0.65
#890, Orange, 5, 0.90
#199, Lemon, 6, 0.25
#200, Milk, 2, 3.25

"""
grocery_items = [[768, "Apple", 10, 0.65],[890, "Orange", 5, 0.90],[199, "Lemon", 6, 0.25],[200, "Milk", 2, 3.25]]


z = map(lambda x: (x[1], x[2] * x[3]),grocery_items)

print(list(z))
"""






#4. Write a function that will convert all the numbers passed as string parameter to integers and return it as a list
#Input convert_to_int("10", "5", "3", "7", "6", "4", "78")
#Output: [10,5,3,7,6,4,78]

"""
list_string = ["10","5","3","7","6","4","78"]


convert_to_int = map(lambda x: int(x),list_string)

print(list(convert_to_int))
"""

#5. Write a function that will take unlimited angles as arguments and return a list of tuples containing the
#sine, cosine and tangent values of those angles.
#Input: get_trig_values(15,30)
#Output: [(0.6502878401571169, -0.7596879128588212, -0.8559934009085189), (-0.9880316240928618, 0.15425144988758405, -6.4053311966462765)]
#Use math module

"""
l1 = [15,30]

get_trig_values = map(lambda x: f'({math.sin(x)}, {math.cos(x)}, {math.tan(x)})',l1)


print(list(get_trig_values))
"""




#Filter and reduce

#filter syntax goes like this: filter(<function>,*iterable)
#This function should only return only a bool which means it will put true or false


#l1 = [1,2,3,4,5,6,7,8,9]
"""
def even(l):
    l2 = [i for i in l if i % 2 == 0]
    return l2

print(even(l1))


def even(n):
    if n % 2 == 0:
        return 1
    else:
        return 1

print(even(4))
"""


#x = filter(even, l1)

#print(list(x))
"""
z = filter(lambda x: x % 2 == 0, l1)

print(list(z))
"""

"""
l_string = ["Hello","Bob","Luck","Madam"]

z = filter(lambda x: x.lower()[::-1] == x.lower(),l_string)

print(list(z))
"""

"""
l_city = ["Austin","San Fransisco", "Los Angeles", "Dallas"]

z = filter(lambda x: " " not in x, l_city)

print(list(z))
"""

#reduce syntax reduce(<function>, sequence)
#reduce function must take 2 arguments

#l1 = [10,20,30]

"""
def add(x,y):
    return x+y


z = reduce(add,l1,5)

print(z)
"""
"""
z = reduce(lambda x,y: x+y,l1)



print(z)
"""


# 1. Write a function to count the number of vowels in a list of strings and return that list
# Input: count_vowels("Hello", "World", "Dinosaur", "Affirmation", "Adament")
# Output: [2, 1, 4, 5, 3]

"""
def vowel_count(str):
    num_vowel = 0
    for i in str:
        if i.lower() in "aeiou":
            num_vowel += 1
    return num_vowel


word_list = ["Hello", "World", "Dinosaur", "Affirmation", "Adament"]

vowels = {}
for str in word_list:
    vowels[str] = vowel_count(str)

print(vowels)
"""



#6. Find the minimum and maximum value in a list using reduce() function.
"""
l1 = [1,2,3,4,5,6,7,8]

z = reduce(lambda x,y: f'{min(l1)},{max(l1)}',l1)



print(z)
"""

#2. Write a function that will take an input of numbers and return only the numbers that are prime

"""
l1 = [1,2,3,4,81,31]

def prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return number > 1

def filter_primes(l_num):
    return list(filter(prime,l_num))

print(filter_primes(l1))
"""

#5. Given a list of strings return the list of strings that cotains all vowels and not more than twice.
"""
l_string = ["hello","mighty","world","aeiou"]

z = filter(lambda x: 'a' in x.lower() and 'e' in x.lower() and 'i' in x.lower() and 'o' in x.lower() and 'u' in x.lower() and x.count('a') <= 2 and x.count('e') <= 2 and x.count('i') <= 2 and x.count('o') <= 2 and x.count('u') <= 2,l_string)


print(list(z))
"""


"""
l1 = [5,4,32,7,5,9]
def small(x,y):
    if x < y:
        return x
    else:
        return y



z = reduce(small,l1)
print(z)
"""



#reduce only takes 2 values
#function will be called len(iterable)-1
"""
count = 0

def f(x,y):

    global count
    count = count + 1
    print(f'{x},{y}, function f is called {count} times')
    return x + y


l = [1,2,3,4,5,6,7,8]

z = reduce(f,l)

print(z)
"""

"""
my_list = ["my","name","is","Visvesh"]


def string(x,y):
    z = x + y
    return z[:len(z) // 2]

y = reduce(string,my_list)

print(y)
"""


# 4. Write a program to find if the two strings passed are Anagram.
# Note: An anagram of a string, is just another string formed using the same letters (case in-sensitive)
# Eg: "ostta" is anagram of "Toast"
# Input: is_anagram("boast", "aobss")
# Output False

"""
def anagram(word1,word2):
    if sorted(word1) == sorted(word2):
        return 'The strings are anagrams.'
    else:
        return 'The strings are not anagrams.'

#print(anagram("ostta","toast"))




z = lambda x,y: sorted(x) == sorted(y)


print(z("ostta","toast"))

"""


# 1. Write a function that will calculate the number of occurrences of even number when unlimited numbers are
# passed as parameters. Use reduce() to solve this problem
# Input: noc(10,12,15,13,18,21,100,102)
# Output: 5


#l1 = [10,12,15,13,18,21,100,102]

# def even(x,y):
#     if y % 2 == 0:
#         x += 1
#
#     return x
#
#
# z = reduce(even,l1,0)
#
#
# print(z)

#z = reduce(lambda x,y: x + 1 if y % 2 == 0 else x,l1,0)


#print(z)
# 2. Calculate the number of boys and number of girls in a given list of dictionary that contains the name of the
# student and their gender.
# class_list = [{'name': 'John', 'gender': 'B'}, {'name': 'Jill', 'gender': 'G'}, {'name': 'Nicole', 'gender': 'G'}]
# Input: b_g_count(class_list)
# Output: {'Boys': 1, 'Girls': 2}


"""
class_list = [{'name': 'John', 'gender': 'B'}, {'name': 'Jill', 'gender': 'G'}, {'name': 'Nicole', 'gender': 'G'}]

def gender1(x,y):
    if y['gender'] == 'B':
        x['Boys'] += 1
    if y['gender'] == 'G':
        x['Girls'] += 1

    return x


z = reduce(gender1,class_list,{'Boys':0,'Girls':0})

print(z)
"""


# 3. Calculate the total price of the invoice passed as a list of items along with quantity and unit price
# invoice_list = [{'item':'Apple', 'qty': 10, 'unit_price': 0.65}, {'item':'Orange', 'qty': 20, 'unit_price': 0.35}
# ,{'item':'Banana', 'qty': 100, 'unit_price': 0.15},{'item':'Water Melon', 'qty': 3, 'unit_price': 2.25}]
# Input: invoice_total(invoice_list)
# Output: 35.25


"""
invoice_list = [{'item':'Apple', 'qty': 10, 'unit_price': 0.65}, {'item':'Orange', 'qty': 20, 'unit_price': 0.35},{'item':'Banana', 'qty': 100, 'unit_price': 0.15},{'item':'Water Melon', 'qty': 3, 'unit_price': 2.25}]


def invoice_total(x,y):
    total = x + y['qty'] * y['unit_price']

    return total
z = reduce(invoice_total,invoice_list,0)


print(z)
"""
# 4. Find the factorial of a number
# Input fact(5)
# Output: 120

"""
n = 5

factorial = reduce(lambda x,y: x*y, range(2,n+1))


print(factorial)
"""

# 5. Calculate the number movies in each year
# movie_list = [{'name':'movie 1', 'year',2001}, {'name':'movie 2', 'year',2003}, {'name':'movie 3', 'year',2001},
# {'name':'movie 4', 'year',2002}, {'name':'movie 5', 'year',2002}, {'name':'movie 6', 'year',2002}]
# Output: {2001:2, 2002:3, 2003:1}
"""
movie_list = [{'name':'movie 1', 'year':2001}, {'name':'movie 2', 'year':2003}, {'name':'movie 3', 'year':2001},{'name':'movie 4', 'year':2002}, {'name':'movie 5', 'year':2002}, {'name':'movie 6', 'year':2002}]

def movies(x,y):
    if y['year'] == 2001:
        x[2001] += 1
    if y['year'] == 2002:
        x[2002] += 1
    if y['year'] == 2003:
        x[2003] += 1

    return x

z = reduce(movies,movie_list,{2001:0, 2002:0, 2003:0})

print(z)
"""
"""
g_name = "Visvesh"
print(f'Global, before calling print_name {g_name}')

def print_name(my_name):
    my_name = my_name + "x"
    print(f'Local:{my_name}')
    return my_name
#don't change the global variable in a local area

z = print_name(g_name)
print(f'Global, after calling print_name {z}')

"""

# 1. Use map to check if a list of words are in order.
# Note: A word is considered in order, if the alphabets in a word are all in ascending order.
# Eg: allow (In order, l comes after a, o comes after l and w comes after o]
# Eg: same [Not in order, a comes after s, also e comes after m]

"""
word_list = ["hello","same","all","zo"]

def word_order(x):
    if ''.join(sorted(x)) == x:
        return "In order"
    else:
        return "Not in order"

z = map(word_order,word_list)



print(list(z))
"""


# 2. Given a dictionary in a grocery shop, update the price list after a discount of 10%
# for all the items that has "a" in it.
# Eg: {'Apple': 2.50, 'Cherry': 4.35, 'Lemon': 2.85, 'Mango': 1.5}
# Now the discount to be calculated only for "Apple" and "Mango" since only those two items contain "a" in it.



"""
grocery_list = {'Apple': 2.50, 'Cherry': 4.35, 'Lemon': 2.85, 'Mango': 1.5}

def discount(x):
    percent = 0.1 * grocery_list[x]
    if 'a' in x or 'A' in x:
        return x,grocery_list[x] - percent
    else:
        return x,grocery_list[x]


z = map(discount,grocery_list)

print(dict(z))
"""






#y = map(lambda x: print(x,grocery_list[x] - 0.1 * grocery_list[x]) if 'a' in x or 'A' in x else print(x,grocery_list[x]),grocery_list)


#print(list(y))





"""
char_to_dots = {
'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
'6': '-....', '7': '--...', '8': '---..', '9': '----.',
'&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
'-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}
"""

"""
def morse_code(x):
    new_str = ''

    for i in x.upper():
        new_str += char_to_dots.get(i)



    return new_str

print(morse_code("hello"))
"""


"""
l1 = ['dog', 'Cat', 'Dog', 'Cow', 'Train', 'book', 'Book']
def unique_list(n):
    l_lower = [i.lower() for i in n]
    for i in l_lower:
        if l_lower.count(i) > 1:
            l_lower.remove(i)
        else:
            i.upper()
    return l_lower

print(unique_list(l1))
"""
"""
l1 = ['dog', 'Cat', 'Dog', 'cOw', 'tRAin', 'book', 'Book']
def unique_list(n):
    l_lower = [i.lower() for i in n]
    l2 = []
    d1 = {}
    for i in l_lower:
        if d1.get(i) == None:
            d1[i] = 1
        else:
            d1[i] += 1
    for i in d1:
        if d1.get(i) > 1:
            l2.append(i.upper())
        else:
          l2.append(i)



    return l2

print(unique_list(l1))
"""






#2. Write a method to find the LCM of two numbers.
"""

def lcm(num1,num2):
    for i in range(max(num1,num2),(num1 * num2) + 1):
        if i % num1 == 0 and i % num2 == 0:
            return i


print(lcm(4,6))
"""







# 1. Given a dictionary which has unique values, write a function to swap the keys and values and return the new
# dictionary

"""
d1 = {1:"Apple", 2:"Orange", 3:"Banana", 4:"Strawberry"}


def swap_key(dictionary):
    new_dict = {}
    for i in dictionary:
        new_dict[dictionary.get(i)] = i
    return new_dict

print(swap_key(d1))
"""

# 2. Given two strings of equal length that contains only + and/or - in it. Write a function that will take these
# two strings as parameter and return the result of their interaction.
# Eg: charge_discharge("++--+-+", "-+++--+")
# Output: "0+000-+"
# + and + result is +
# - and - result is -
# + and - result is 0

"""
def charge_discharge(str1,str2):
    output = ""
    for i,j in zip(str1,str2):
        if i == '+' and j == '+':
            output += '+'
        elif i == '-' and j == '-':
            output += '-'
        else:
            output += '0'
    return output

print(charge_discharge("++--+-+", "-+++--+"))
"""
# 3. Write a function that take two numbers. Find out how many numbers have to be added or subtracted
# to each one so that the first one is twice that of second.
# Input: add_or_subtract(20, 5)
# Output: 10 (Reason: you add 10 to both numbers, it will become 30, 15 and first number is twice that of second)
# Note: Try for various other numbers and test
"""
def add_or_subtract(num1,num2):
    add = 0

    while num2 * 2 != num1:
        if num1 < num2:
            return "num1 cannot be smaller than num2"
        num1 += 1
        num2 += 1
        add += 1
    return add

print(add_or_subtract(20,5))
"""


#real_add_or_subtract = lambda num1,num2: num1 - (num2 * 2)

#print(real_add_or_subtract(20,5))




# 4. Write a function to test if an integer contains all the numbers from 0-9 at least once in it and return True
# if it contains and return False otherwise

"""
def integer(num):
    str_num = str(num)
    if '0' in str_num and '1' in str_num and '2' in str_num and '3' in str_num and '4' in str_num and '5' in str_num and '6' in str_num and '7' in str_num and '8' in str_num and '9' in str_num:
        return True
    else:
        return False


print(integer(1234567876790))
"""

#5. Given a list of numbers add all the prime numbers and return the output.


"""
num_list = [1,2,3,4,5,6,7,8,9,12]


def prime_add(l1):
    output = 0
    for i in l1:
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break


        else:
            if i == 1:
                output -= 1
            output += i

    return output

print(prime_add(num_list))
"""
















