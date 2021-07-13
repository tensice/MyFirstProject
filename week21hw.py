
# 3. Write the max and min numbers that can be formed from a number. Numbers cannot start with zeros.
# Eg: maxmin(74290) -> 97420, 20479
# maxmin(4000) -> 4000, 4000

def maxmin(num):
    str_num = str(num)
    sort_num_max = sorted(str_num)
    max_num = reversed(sort_num_max)
    list_max = [str(i) for i in max_num]
    max_join = "".join(list_max)
    max_num_int = int(max_join)

    print(f'Max: {max_num_int}')
    sort_num_min = sorted(str_num)
    if sort_num_min[0] == "0":
        sort_num_min[0],sort_num_min[1] = sort_num_min[1],sort_num_min[0]

        min_join = "".join(sort_num_min)
        min_num_int = int(min_join)
        print(f'Min: {min_num_int}')
    else:
        min_str = "".join(sort_num_min)
        min_num = int(min_str)
        print(f"Min: {min_num}")


#maxmin(74290)


# 4. Write a function in python to count the number of lines from a text file "my_file.txt" that does not contain
# the word "the" (case insensitive)

def not_the_count():
    with open("my_file.txt") as file:
        count = 0
        word = "the"
        for i in file:
            if word not in i.lower().split():
                print(i)
                count += 1
        print(count)

#not_the_count()


# 5. Write a function display_words() in python to read lines from a text file "my_file.txt", and display those words,
# which are less than 4 characters.

def four_chars():
    with open("my_file.txt") as file:
        for i in file:
            for j in i.split():
                if len(j) < 4:
                    print(j)
#four_chars()

# 1. The Polybius Square cipher is a simple substitution cipher that makes use of a 5x5 square grid.
# The letters A-Z are written into the grid, with "I" and "J" typically sharing a slot
# (as there are 26 letters and only 25 slots).
# Note: Alphabets are case-insensitive
#
# 1 2 3 4 5
# 1 A B C D E
# 2 F G H I/J K
# 3 L M N O P
# 4 Q R S T U
# 5 V W X Y Z
#
# To encipher a message, each letter is merely replaced by its row and column numbers in the grid.
# Deciphering...always replace 24 with I instead of J
# Write a function to encipher any text as numbers.
# Eg: polybius('Hi') = 23 24




def polybius_square_cipher(string):
    polybius = {1:('A','B','C','D','E'),2:('F','G','H','I','K'),3:('L','M','N','O','P'),4:('Q','R','S','T','U'),5:('V','W','X','Y','Z')}

    for i in string.upper():
        for k,j in polybius.items():
            if i in j:
                if " " in string:
                    print(f'{k}{j.index(i) + 1} ',end="")
                else:
                    print(f'{k}{j.index(i) + 1}',end="")


#polybius_square_cipher("hi")


def polybius_square_decipher(cipher):
    polybius = {1:('A','B','C','D','E'),2:('F','G','H','I','K'),3:('L','M','N','O','P'),4:('Q','R','S','T','U'),5:('V','W','X','Y','Z')}

    cipher_no_space = cipher.replace(" ","")

    split = [(cipher_no_space[i:i+2]) for i in range(0, len(cipher_no_space),2)]
    final = ""

    for i in split:
        int_i = int(i)
        first_char = int_i // 10
        second_char = int_i % 10
        for j,k in polybius.items():
            if first_char == j:
                value = k[second_char - 1]
                final += value
    if " " in cipher:
        space_index = cipher.index(" ") - 2
        print(f'{final.lower()[:space_index]} {final.lower()[space_index:]}')
    else:
        print(final.lower())

#polybius_square_decipher("2324 4423154215")


def polybius(cipher):
    if cipher.replace(" ","").isdigit():
        polybius_square_decipher(cipher)
    else:
        polybius_square_cipher(cipher)

#polybius("2324 4423154215")








