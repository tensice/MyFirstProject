import math

def div_by_seven(num = 14): 
  if num % 3 != 0 and num % 5 != 0 and num % 7 == 0:
    return num, True
  else:
    return num, False




def flip_coin(n = 1):
  import random
  for i in range(n):
    rand = random.randint(1,2)
    if rand == 1:
      yield True
    else:
      yield False




def pangram(human_str):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  for i in alphabet:
    if i not in human_str.lower():
      return False
  return True


def factorial(num):
  fact = math.factorial(num)
  yield fact



def factorial2(n): 
  fac = 1
  for i in range(1,n + 1):
    fac = fac * i
  return fac



def float_range(start = 0,stop = 10,step = 1):
  while start < stop:
    start += step

    


def xX(n):


  for i in n:
    if 'x' in n:
      if 'X' in n:
        return True
      else:
        return False


def prime_number(n):
  for i in range(2,n + 1):
    if i > 1:
      for j in range(2, i // + 2):
        if i % j == 0:
          break
        else:
          if j == i // 2 + 1:
            return i


def decimal_octal(n):
  binary = bin(n)
  octal = oct(n)
  hexadecimal = hex(n)

  return binary,octal,hexadecimal