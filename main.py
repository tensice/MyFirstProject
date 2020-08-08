  

"""
print(87 * 34)
# This is a comment!!!!
print(120)
print('45 * 63 = ' + str(45 * 63))
print(15/3)
print(5 + 3 + 1 * 9 / 5 + 4 - 8) 
print(4 + 2 * 8)
print('Sun' + 'flower')
print('''eat
food''')
"""
"""
first_name = input('Type your first name\n')
last_name = input('Type your last name\n')
address = input('Type your address\n')
zipcode = input('Type your zipcode\n')
birth_year = input('Type your birth year\n')
age = 2020 - int(birth_year)
print(f'Name: {first_name} {last_name}')

print(f'Address:{address}')
print(f'Zipcode:{zipcode}')
print(f'Age: {age}')
"""
"""a = 20 
b = 3
print(a / b)
print(a // b)
"""
"""
minutes = input('Enter minutes\n')
hours = int(minutes) // 60
mins = int(minutes) % 60
print(f'Hours:{hours}')
print(f'Minutes:{mins}')
"""
"""
farenheit = int(input('Enter temperature in farenheit\n'))
celsius = (farenheit - 32) * 5/9
print(f' {farenheit} farenheit is {celsius} celsius')
"""
"""
celsius = int(input('Enter temperature in celsius\n'))
farenheit = (celsius * 9/5) + 32
print(f' {celsius} celsius is {farenheit} farenheit')
"""
"""
area = int(input('Enter area\n'))
radius = area / 3.14 
print(f' Radius is {radius}')
"""


"""
side1 = int(input('Enter side 1\n'))
side2 = int(input('Enter side 2\n'))
area = side1 * side2
print(f'Area of the rectangle is {area}')
"""
"""
angle1 = int(input('Enter angle 1\n'))
angle2 = int(input('Enter angle 2\n'))
angle3 = 180 - angle1 - angle2
print(f'The third angle is {angle3}')
"""
"""
x = input('Enter your name: ')
print(f'Welcome Mr.{x}')

print(4 % 3)
"""

"""
x = 10
y = 15

print(x != y)

#if Statement
x = int(input('Enter x:'))
y = int(input('Enter y:'))
if x > y:
  print(f'x - y = {x-y}')
elif y > x:
  print(f'y - x = {y-x}')

Age = int(input('Enter in an age:\n'))
"""
#if Age < 4:
  #print('You are  toddler')
#elif Age < 13: print('Child') elif Age < 18: print('Teenager')  else: print('Adult')
"""
"""
#Age = int(input("Type your child's age:")) if Age<4 : print("Toddler") elif Age < 13 : print("Child") elif Age < 18: print("Teenager") else: print("Adult") 

"""
"""
#weight = input('Weight in kg or pounds')
#if weight == 'kg':
  #print('In kg')
  #print('Weight in pounds is {weight * 2.2 ')
"""
yay = 'Hello World'
i = 0

print(yay[i])
i += 1
print(f'yay[i]')
"""
"""
Number = int(input('Type a number\n'))
if Number % 2 == 0 :
  print('Number is even')
else:
    print('Number is odd')
"""
"""
num = int(input('Type a number\n'))
if num % 5 == 0 :
  print('Number is divisible by 5')
else :
  print('Number is not divisible by 5')
"""
"""
for x in range(101):
  print(x)
    """
"""
num = int(input('Type a number\n'))
n = num - 1
factorial = num

if num == 0:
  factorial = 1
while n > 1:
  factorial = factorial * n
  n = n - 1
print(f'The factorial of {num} is {factorial}')
"""
"""
f = 1
for i in range(2, num + 1):
  f = f * i
print (f)
"""
"""
while True :
  ans = 'N/A'
  num1 = int(input('Type a number\n'))
  num2 = int(input('Type another number\n'))
  operation = input('Type an operation\n')
  if num2 == 0 and operation == '/':
    print('Cannot divide by zero. Try another number')
  else:
    if operation == '+' :
      ans = num1 + num2
    elif operation == '-':
      ans = num1 - num2
    elif operation == '*':
      ans = num1 * num2
    elif operation == '/':
      ans = num1 / num2
    elif operation == 'q':
      break

    else:
      print(f'{operation} is invalid')
    print(f'The result is {ans}')
"""
"""
fan_on = False
while True:
  command = input('Type a command. On, Off, or Quit\n')
  command = command.lower()
  if command == 'on':
    if fan_on:
      print('Fan is already on')
    else:
      print('Fan is turning on')
    fan_on = True
  elif command == 'off':
    if fan_on:
      print('Fan is turning off')
    else:
      print('Fan is already off')
    fan_on = False
  elif command == 'quit':
    break
  else:
    print(f'{command} is invalid')
"""
"""
while True:
  name = input('Type your name\n')
  name = name.capitalize()
  score = -1
  while score > 100 or score < 0:
    score = int(input('Type your score\n'))
  if score > 94 and score < 101:
    print(f'{name} got an A+')
  elif score > 89 and score < 95:
    print(f'{name} got an A')
  elif score > 84 and score < 90:
    print(f'{name} got a B+')
  elif score > 79 and score < 85:
    print(f'{name} got a B')
  elif score > 74 and score < 80:
    print(f'{name} got a C+')
  elif score > 69 and score < 75:
    print(f'{name} got a C')
  elif score > 64 and score < 70:
    print(f'{name} got a D+')
  elif score > 59 and score < 65:
    print(f'{name} got a D')
  elif score > 54 and score < 60:
    print(f'{name} got an E+')
  elif score > 49 and score < 55:
    print(f'{name} got an E')
  elif score < 50 and score > -1:
    print('You failed')
  elif score > 100 or score < 0:
    print(f'{score} is invalid')
"""
"""
while True:
  name = input('Type your name\n')
  subject = 0
  while subject != 'math' and subject != 'science' and subject != 'language arts' and subject != 'history':
    subject = input('Type your favorite subject. Math,science, language arts, or history\n')
  subject = subject.lower()
  if subject == 'science':
    print(f'Me too {name}!')
  elif subject == 'language arts':
    print('Oh, I do not really like language arts')
  elif subject == 'math':
    print('I like math too!')
  elif subject == 'history':
    print('I kind of like history')
  else:
    print('invalid subject')

"""
"""
while True:
  number = int(input('Type a number\n'))
  if number % 3 == 0 and number % 5 == 0:
    print('Fizz Buzz')
  elif number % 5 == 0:
    print('Buzz')
  elif number % 3 == 0:
    print('Fizz')
  else:
    print('Oops')
"""


"""
fibonacci_count = int(input('Type how many fibonacci sequence numbers you want:'))
if fibonacci_count > 0 and fibonacci_count < 2:
  print('0')

"""

"""
#num_str = input('Enter a number\n')
num_str = '2004'
digit_count = len(num_str) - 1
num = int(num_str)
output = ''
for i in num_str:
  tmp = str(int(i) * (10 ** digit_count))
  if tmp != '0':
    #print(f'Tmp value is: {tmp}')
    output = output + tmp + ' + '
    #print(f'Output is {output}')
  digit_count -= 1
  print (output[:-3])
"""

"""
num_str = input('Enetr a number')
digit_count = 
"""



"""
x = 10
if x > 0:
  pass
else:
  print('x is less than zero')
print(x)
"""
"""
number = int(input('Enter a number\n'))
for i in range(2, number):
  if number % i == 0:
    is_prime = False
    break
else:
  is_prime = True


if is_prime:
  print(f'{number} is prime')
else:
  print(f'{number} is not prime')
"""
"""
countries = ['India', 'USA', 'Canada','Australia', 'South Africa']
countries.sort(key = lambda x:len(x))
print(countries[0])
"""
'''
smallest_country = ''
min_length = 100
for i in countries:
  if len(i) < min_length:
    min_length = len(i)
    smallest_country = i
    print(f'{smallest_country}')
'''








"""
countries = ['India', 'USA', 'Canada', 'Australia', 'South Africa']
temperatures = [100.2,96.8,85.3,73.8,102.3]
smallest_country = ''
min_length = 100

hot_temp = 0
hot_country = ''
cold_temp = 1000
cold_country = ''

for index, temp in enumerate(temperatures):
  if temp > hot_temp:
    hot_temp = temp
    hot_country = countries[index]
if temp < cold_temp:
  cold_temp = temp
  cold_country = countries[index]

print(f'The hottest country is {hot_country} and its temperature today is {hot_temp}')
print(f'The coldest country is {cold_country} and its temperature today is {cold_temp}') 
"""
"""
fruits = {'apple', 'banana', 'cherry'}

x = fruits.
print(x)
print(fruits)
"""
"""
side1 = int(input('Enter the first side length\n'))
side2 = int(input('Enter the second side length\n'))
side3 = int(input('Enter the third side length\n'))
if side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
  print('Cannot form a triangle')
else:
  print('A triangle can be formed')
  """
"""
max_prime_count = int(input('Type how many prime numbers you want\n'))
prime_count = 0
num = 2
while prime_count < max_prime_count:
  for i in range(2, num):
    if num % i == 0:
      break
  else:
    prime_count += 1
    print(f'{prime_count} - {num}')
  num += 1
"""


"""
for i in range(2, 2):
  print('Hello')
else:
  print('World')
"""
"""
student = {'name': 'Ramesh', 'age':40, 'languages' : ['Python', 'Java']}
print(student.get (name))


max average
tuple
dictionary
items    
"""

"""
palindrome = input('Type a word or number')
if (len(palindrome) == 1):
  print('Input needs to be more than one character')
else:
  reverse_str = palidrome[::-1]
  if palindrome == reverse_str:
    print(f'{palindrome} is a palindrome)
  else:
    print(f'{palindrome} is not a palindrome')
    """
"""
lines = int(input('Type how many lines of Pascals Triangle you want\n'))

if lines >= 1:
  print('1')

l2 = [1,1]

l3 = []

for index, i in enumerate(l2):
  print(index, i)
print(l3)
"""
"""
list1 = []
while True:
  num = input('Type a number or character\n')
  if num == '-1':
    break
  if num.isdigit():
    ints = int(num)
    list1.append(ints)

  if num.isalpha():
    ints = str(num)
    list1.append(ints)

    
print(list1)
"""
"""
x = {'fruit': 'apple','name': 'jack'}
print(x.get(name))
"""
"""
def greeting(name):
  print(f'Hello welcome to python class Mr.{name}')  

greeting('Jack')
greeting('Rob')
"""
"""
def addition(a, b):
  print(a + b)
addition(10, 5)
"""
"""
def count_even_and_odd_numbers(my_list):
  count = 0
  for i in my_list:
    pass
    count += 1
    return even, odd




list1 = [2, 1, 2, 3, 4, 10]
list2 = [2, 2, 0]
list3 = [1, 3, 5, 2, 4, 6, 8, 14, 18]
print(f'Value of list1 is: {count_even_numbers(list1)}')
print(f'Value of list2 is: {count_even_numbers(list2)}')
print(f'Value of list3 is: {count_even_numbers(list3)}') 
"""
'''
def program1():
  list1 = [3,4,8,7,5,6,2,45,2,33,5]
  list1.sort()
  

  x = len(list1)
  print(f'{x} is the length of the list')

  min_num = list1[0]
  print(f'{min_num} is the min num')

  max_num = list1[x-1]
  print(f'{max_num} is the max num')

  difference = max_num - min_num
  print(f'{difference} is the difference')
program1()
'''
"""
program1a():
  list2 = [3,4,8,7,5,6,9]
  mini = min(list2)
  print(mini)
  maximum = max(list2)
  print(maximum)
  dif = maximum - mini
  print(dif)


program2():
  list3 = [3,2,5,9,4,6]
  x = len(list3)
  total = 0
  pos = 0

  for i in range(x-1):
    print(pos)
    if list3[pos] == 9:
      print(pos)
      pos += 2
      print(i)
    elif list3[pos] != 9:
      total += list3[pos]
      pos += 1

  print(total)

def program3a():
  list3 = [3,2,10,9,4,6,3,5,2,3,6,8,10,2,3,4,5,6,5,7]
  x = len(list3)
  total = 0
  pos = 0


  for i in range(x-1):
    if list3[pos] == 10:
      pos += 5
    
    elif list3[pos] != 10:
      total += list3[pos]
      pos += 1
      #print (pos)
      #print(total)
      if pos == x:
        break

  print(total)

"""
"""
def program3b():
  list3 = [1,2,3,10,4,5,6,10,9,2]
  x = len(list3)
  total = 0
  pos = 0

  while pos <= x:
    if list3[pos] == 10:
      while 
      pos += 6
    else:
      total += list3[pos]
      pos +=1
      if pos == x:
        break

  print(total)

program3b()
"""
"""
def my_func(list1):
  sum = 0
  for i in list1:
    sum += 1
  return sum - list1[0] - list1[-1]

list1 = [2,5,3,7,9,4,7,3]
print(my_func(list1))
"""
"""
def fight_evens_odds(list_of_values):
  odd_sum = 0
  even_sum = 0
  for i in list_of_values:
    if i % 2 == 0:
      even_sum += i
    else:
      odd_sum += i
      if odd_sum > even_sum:
        return "Odd Wins!" 
      elif odd_sum < even_sum:
        return "Even Wins!"
      else:
        return "Tie!"
list1 = [1, 2, 3, 4, 5, 6, 3]
print(fight_evens_odds(list1)) 
"""
"""
def my_func():
  n = int(input('Type a number\n'))
  if n >= 90 and n <= 110 or n >= 190 and n <= 210:
    print('True')
  else:
    print('False')
my_func()
"""

"""
def my_armstrong(num):
  total = 0
  num_str = str(num)
  power = len(num_str)
  for i in num_str:
    x = int(i)
    total += x ** power
  if num == total:
    return True
  else:
    return False



"""
"""
num = (input('Type a number\n'))


if my_armstrong(num):
  print(f'{num} is an armstrong number')
else:
  print(f'{num} is not an armstrong number')
  

for i in range(10000):
  if my_armstrong(i):
    print(i)
"""
"""
def sep_even_odd(my_list):
  even_list = []
  odd_list = []
  for i in my_list:
    if i % 2 == 0:
      even_list.append(i)
    else:
      odd_list.append(i)
  return even_list,odd_list

main_list = [2,7,4,8,3,9]
even,odd = sep_even_odd(main_list)
print(even)
print(odd)
"""
"""
def sep_float_int(my_list):
  float_list = []
  int_list = []
  for i in my_list:
    if type(i) == float:
      float_list.append(i)
    else:
      int_list.append(i)
  return float_list,int_list

main_list = [3,3.5,87.6,83,9.8,7]
float1,int1 = sep_float_int(main_list)
print(float1)
print(int1)
"""
"""
def sep_all_type(my_list):
  string_list = []
  boolean_list = []
  float_list = []
  int_list = []
  for i in my_list:
    if type(i) == str:
      string_list.append(i)
    elif type(i) == bool:
      boolean_list.append(i)
    elif type(i) == float:
      float_list.append(i)
    else:
      int_list.append(i)
  return string_list,boolean_list,float_list,int_list

main_list = [3,87.9,True,1,'yay','ok', 7, 9.3]
string1,boolean1,float1,int1 = sep_all_type(main_list)
print(string1)
print(boolean1)
print(float1)
print(int1)
"""
"""
help('class')
"""
"""
import utils
n = 10
print(f'Factorial of {n} is {utils.factorial(n)}')
"""
"""
def form_triangle(side1,side2,side3):
 if side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
  print('Cannot form a triangle')
 else:
   print('A triangle can be formed')


side1 = int(input('Enter the first side length\n'))
side2 = int(input('Enter the second side length\n'))
side3 = int(input('Enter the third side length\n'))
form_triangle(side1,side2,side3)
"""
"""
import datetime


d = datetime.datetime.today()





x = input('What do you want? m, d, h, s, mm\n')
if x == 'y':
  print(d.year)
elif x == 'm':
  print(d.month)
elif x == 'd':
  print(d.day)
elif x == 'h':
  print(d.hour)
elif x == 's':
  print(d.second)
elif x == 'mm':
  print(d.microsecond)
else:
  print('Invalid input')
"""
"""
d1 = datetime.date(year = 2020, month = 6, day = 1)
d2 = datetime.date(year = 2020, month = 7, day = 1)
diff = d2 - d1
print(type(diff))
"""
"""
def days_until_christmas():
  christmas_day = datetime.date(year = 2020, month = 12, day = 25)
  today = datetime.date.today()
  totdays.days

print(f'It is {days_until_christmas()} days until christmas ')
"""
"""
def new_date():
  td = datetime.timedelta(days = 150, hours = 5, minutes = 40)
  today = datetime.datetime.now()
  print(today)
  nd = today + td
  return nd


nd = new_date()
print(f'Adding 150 days, 5 hours, 40 mins')
prit(nd)
print(nd.strftime("%dth %B %Y, %H hour, %M minutes %S seconds"))
print(str_nd)

def my_birthday():
  bday = datetime.date(2007,5,2)
  return bday

bday = my_birthday()

bday_str = bday.strftime("My birthday is %B %Y")


seconds = t.time()
print(seconds)
"""
"""
import datetime

while True:
  print(datetime.datetime.now())
  t.sleep(1)
"""
"""
def check_num():
  num = int(input('Type a number\n'))
  if num > 0:
    print(f'{num} is a positive number')
  elif num < 0:
    print(f'{num} is a negative number')
  elif num == 0:
    print(f'{num} is zero')
  else:
    print(f'{num} is an invalid input')
check_num()
"""
"""
def fan_on():
  fan_on = False
  while True:
    command = input('Type a command. On, Off, or Quit\n')
    command = command.lower()
    if command == 'on':
      if fan_on:
        print('Fan is already on')
      else:
        print('Fan is turning on')
      fan_on = True
    elif command == 'off':
      if fan_on:
        print('Fan is turning off')
      else:
        print('Fan is already off')
      fan_on = False
    elif command == 'quit':
      break
    else:
      print(f'{command} is invalid')

fan_on()
"""

"""
num = int(input('Enter a number\n'))
line_level = 1
i = 1
up = ''
while i < num + 2:
    x = 1
    print(f'{up}')
    up = ''
    while x <= i:
        up = up + f'{i}'
        x += 1
    else:
        i += 1
"""
"""
num = int(input('Enter a number\n'))
line_level = 1
i = 1
up = ''
while i < num + 2:
    x = 1
    print(f'{up}')
    up = ''
    while x <= i:
        up = up + f'{line_level}'
        x += 1
        line_level += 1
    else:
        i += 1
"""
"""
num = int(input('Enter a number\n'))
print(f'The factors of {num} are:')
for i in range(1, num + 1):
  if num % i == 0:
    print(i)
"""
"""
list1 = []
for i in range(1,100):
  if i % 7 == 0:
    list1.append(i)
print(list1)

list2 = [i for i in range(1,100) if i % 7 == 0]
print(list2)

list3 = [i ** 2 for i in range(1,21) if i % 2 == 0 ]
print(list3)
cities = ['Austin', 'Round Rock', 'Dallas', 'San Antonio', 'San Francisco']
list4 = [city for city in cities if not city.isalpha()]
print(list4)
list5 = [i for i in range(1,100) if i % 2 == 0]
print(list5)

list6 = [i for i in range(1,1000) if i % 7 == 0]
print(list6)
"""
"""
list7 = [i ** 2 for i in range(1,100) if i % 2 == 1]
print(list7)
"""
"""
v = 'aeiou'
vowels = ['a','e','i','o','u']
human_string = input('Type in a string\n')
vowel_remove = [i for i in human_string if i not in v]
str1 = ''
x = str1.join(vowel_remove)
print(x)
"""
"""
num = int(input('Type a number\n'))
factors = [i for i in range(1, num + 1) if num % i == 0]
print(factors)
"""
"""
items = {1:'Jack',2:'Jon',3:None}
blank_remove = {i:items.get(i) for i in items if items.get(i) is not None}
print(blank_remove)
"""




"""
human_string = input('Type a string\n')
character_count = {}
for i in human_string:
  h = i.lower()
  if h in character_count:
    character_count[h] += 1
  else:
    character_count[h] = 1

print(character_count)
"""

"""
human_string = input('Type a string\n')
character_count = {i:character_count for i in human_string if i in character_count[i] }
"""





"""
def my_func():
  str1 = ''
  for i in range(1,11):
    x = i ** 2
    str1 += f'{x}-'
  return str1
  
  
x = my_func()
x = x.replace('-', ',')
print(x[:-1])
"""


"""
def sep_even_odd():
  even_list = []
  odd_list = []
  for i in main_list:
    if i % 2 == 0:
      even_list.append(i)
    else:
      odd_list.append(i)
  return even_list,odd_list

main_list = [2,7,4,8,3,9]
even,odd = sep_even_odd()
print(even)
print(odd)
"""
"""
str1 = input('Enter a string\n')

def swapcase1():
  str3 = ''
  for i in str1:
    str2 = str1.swapcase()
    str3 += f'{str2}: This is with the characters case swapped'
    return str3
x = swapcase1()
print(x)
"""
"""
import math
num = int(input('Type a number\n'))
def prime_factor(num):
  str1 = ''
  num2 = num
  while num % 2 == 0: 
    str1 += '2 * '
    num = num / 2
  for i in range(3,int(math.sqrt(num2))+1 , 2):
    while num % i == 0: 
      str1 += f'{i} * ' 
      num = num / i
  if num > 2: 
    str1 += f'{num}'
  str2 = str1
  return str2
x = prime_factor(num)
print(f'The prime factors of {num} are {x}')
"""
"""
chemistry = [3,5,6,8,2,3,4,3,4,5,3]
pyshics = [7,2,3,3,5,7,3,4,3,5,7]
math = [8,2,10,4,3,2,3,1,6,8,9]
average = []
y = len(chemistry)
def average_func():
  for i in range(0,y):
    student_total = chemistry[i] + pyshics[i] + math[i]
    i += 1
    average.append(student_total / 3)
  return average

x = average_func()
print(x)

"""

"""
import random
print('Rolling...')
x = random.randint(1,6)
print(f'You got a {x}')
"""

"""
human_string = input('Enter a string\n')
word_count = 1

for i in human_string:
  if i == ' ':
    word_count += 1


character_count = {}
for i in human_string:
  if i in character_count:
    character_count[i]
  else:
    character_count[i] = 1

x = sum(character_count.values())
print(character_count)
print(f'{x} unique characters')
print(f'{word_count} words')
"""
"""
def add(*x):
  print(x)
  sum = 0
  for i in x:
    sum += i
  return sum

print(add(1,2,3,4,5))
"""
"""
def my_func(**kwargs):
  print(kwargs)
  for key,value in kwargs.items():
    print(key,value)

my_func(a = 1, b = 2, c = 3, d = 4)
"""
"""
def city_temp(cites,temps):
  #dict1 = {}
  #for index, i in enumerate(cities):
    #dict1[i] = temps[index]
  return dict1
cities = ['Austin','Bostin','New York City']
temp = [98,75,76]
print(city_temp())
"""
"""
def name_age(f,l,a):
  my_dict = {first+ ' ' +last:age for first,last,age in zip(f,l,a)}
  return my_dict

first = ['bob','jack', 'jill']
last = ['smith','lily','billy']
age = [50,60,30]
my_dict = {}
print(name_age(first,last,age))
"""
"""
import itertools

l1 = 'yeet'
p = itertools.permutations(l1)

print(list(p))
"""
"""
def type_func(x,y,z):

  x = str(5)
  y = []
  z = {}
  def type_func(x,y,z):
    print(type(x))
    print(type(y))
    print(type(z))

  type_func(x,y,z)
"""

human_input = input('Type random characters\n')
special_characters = ['!','@','#','$','%','^','*','()']
upper_case = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']
lower_case = ['abcdefghijklmnopqrstuvwxyz']
length = len(human_input)
for i in human_input:
  if i in upper_case:
    if i in lower_case:
      if i in special_characters:
        if length >= 8 and length <= 15:
          print('yes')
        else:
          print('no')

"""
nums = [[8,1,3,5],[9,5,7,3],[9,7,4,9,7]]
def my_func(nums1):
  for i in nums1:
    i.sort()
  return nums1
x = my_func(nums)
print(nums)
print(x)
"""
"""
def perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n
print(perfect_number(6))
"""
"""
from datetime import datetime
date3 = input('Type a date\n')

date3_dt = datetime.strptime(date3,'%y/%m/%d %H:%M:%S')

#date3s = date3.strptime()
date1 = datetime(2014, 7, 2)
date2 = datetime(2014, 6, 11)
sub = date1 - date2
print(abs(sub))
"""



"""
students = ['Jon','Jack','Bill','Bob']
nums = [3,4,1,5]
"""
"""
human_str = input('Type some words\n')
words = []
for i in human_str:
  if i == '':
    words.append(i)

print(words) 
"""
