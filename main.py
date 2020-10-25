import week4hw
#num = int(input('Type a num\n'))

"""
n, result = week4hw.div_by_seven()

if result:
  print(f'number is divsible by 7 but not divisible by 3 or 5')
else:
  print(f'number is not satisfying the requirement ')

"""
"""
heads = 0
tails = 0
result2 = week4hw.flip_coin(1000)
for i in result2:
  if i:
    heads += 1
  else:
    tails += 1

print(f'Heads:{heads}')
print(f'Tails:{tails}')


human_str = input('Type a string\n')
result3 = week4hw.pangram(human_str)
if result3:
  print('Yes this is a pangram')
else:
  print('No this is not a pangram')




num = int(input('Enter a number\n'))
result4 = week4hw.factorial(num)

print(next(result4))


n = int(input('Enter a number\n'))
result5 = week4hw.factorial2(n)

print(result5)

"""
"""
result6 = week4hw.float_range(3.4,7.8,.2)
print(next(result6))

n = input('Type a string\n')
result7 = week4hw.xX(n)

if result7:
  print('Yes')
else:
  print('No')


n = int(input('Enter a number\n'))
result8 = week4hw.prime_number(n)
"""
"""
n = int(input('Enter a number\n'))

result9 = week4hw.decimal_octal(n)

print(result9)
"""

# human_input = int(input('Type how many lines of the alphabet diamond you want\n'))
human_input = 4
"""
line_level = 0
diamond_character = [chr(i) for i in range(97,97 + human_input)]
num = -1
length = len(diamond_character)
for i in reversed(diamond_character):
  print(diamond_character[length + num])
  print(diamond_character[length - 1])
  num -= 1
"""
"""
list1 = [chr(i) for i in range(97,97 + human_input)]
list1.reverse()
length = len(list1)
num = 0

for i in range(1,length+1):
  for j in range(i):
    print(' '*(human_input-i-1),list1[j],end = '')

  for k in range(i-1,0,-1):
    print(''*(human_input-i-1),list1[k-1],end = '')

  print()

for i in range(length-1,0,-1):
  for j in range(i):
    print(' '*(human_input-i-1),list1[j],end = '')

  for k in range(i-1,0,-1):
    print(''*(human_input-i),list1[k-1],end = '')
  print()
"""







"""
for i in range(human_input):
  print(' '*(human_input-i-1) + '* '*(i+1))
for i in range(human_input-1):
  print(' '*(i+1)+ '* '*(human_input-i-1))
"""

