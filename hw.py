"""
x = 'Hello, my name is Bob. What is 1.7 * 98.1?'
def rev(string):
    reverse_list = []
    for letter in string:
        if letter == '.' or letter == ' ':
            reverse_list.append(letter)
        else:
            reverse_list.append('#')
    reverse_string = string[::-1]
    index = 0
    for i in reverse_string:
        if i == '.' or i == ' ':
            continue
        if string[index] == '.' or string[index] == ' ':
            index += 1
        if string[index].isupper():
            reverse_list[index] = i.upper()
        else:
            reverse_list[index] = i.lower()
        index += 1
    return ''.join(reverse_list)
print(x)
print(rev(x))
"""
"""
s1 = 'Hello World 123'

upper = 0
lower = 0
digits = 0

for i in s1:
    if i.isupper():
        upper += 1
    if i.islower():
        lower += 1
    if i.isdigit():
        digits += 1

print(f'Uppercase:{upper}')
print(f'Lowercase:{lower}')
print(f'Digits:{digits}')
"""
"""
s1 = 'hello'
s2 = 'truck'

l_s1 = list(s1)
l_s2 = list(s2)
counter = 0
counter_2 = 0
for i in l_s1:
    print(l_s1[counter])
    counter += 1
    for j in l_s2:
        print(l_s1[counter_2])
        counter_2 += 1
"""
"""
l1 = ['Hello','Good','Sweet']
l2 = ['World','Morning','Memories']
l3 = []
for index, element in enumerate(l1):
    x = element + ' ' + l2[index]
    l3.append(x)
print(l3)
"""
"""
l1 = [4,17,21,18]
l2 = [6,3,5,4]
l3 = []
for index, element in enumerate(l1):
    x = element + l2[index]
    l3.append(x)
print(l3)
"""
"""
l1 = ['',5,'hello',0,67,'', '  ']
for i in l1:
    if i == '':
        l1.remove(i)
print(l1)
"""


