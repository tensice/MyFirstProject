

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
#num = int(input('Type a number\n'))
#n = num - 1
#factorial = num
"""
if num == 0:
  factorial = 1
while n > 1:
  factorial = factorial * n
  n = n - 1
print(f'The factorial of {num} is {factorial}')

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

fan_on = False
while True:
  command = input('Type a command. On, Off, or Quit\n')
  command = command.casefold()
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



