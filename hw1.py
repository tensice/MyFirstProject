import random
from num2words import num2words
from math import factorial
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
computer_guess = random.randint(0,100)
points = 0
for i in range(10):
    human_input = int(input("Enter a number less than 100\n"))
    if human_input == computer_guess and i <= 5:
        points += 10
        print(f'Human Input: {human_input}, Computer Guess: {computer_guess}, Points: {points}')
        break
    if human_input == computer_guess and i > 5:
        points += 5
        print(f'Human Input: {human_input}, Computer Guess: {computer_guess}, Points: {points}')
        break

if human_input != computer_guess:
    print("You Lose")
"""


"""
def num_to_words(number):
    return num2words(number)


print(num_to_words(36))
"""

"""
n = int(input("How many lines of Pascal's Triangle do you want?\n"))
for i in range(n):
    for j in range(n - i + 1):
        print(end=" ")

    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")

    print()
"""





