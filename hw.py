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