from itertools import groupby
import re
# 1. Given a list, create sublists that groups the numbers in ascending order
# Eg: Input : [5,8,2,5,9,1,3,4,5,2,8,2,9,3,2,5,2]
# Output:[[1],[2,2,2,2,2],[3,3],[4],[5,5,5,5],[8,8],[9,9]]


list1 = [5,8,2,5,9,1,3,4,5,2,8,2,9,3,2,5,2]

def sort_sublist(l1):
    new_list = []
    l1.sort()
    for i,j in groupby(l1):
        new_list.append(list(j))
    return new_list

#print(sort_sublist(list1))

# 3. Check equation: Take an equation as an input string. Evaluate and tell if the equation is True or False
# Eg: Input: "14 / 7 = 2" -> True
# Input: "15 + 8 = 25" -> False
# Input: "64 * 2 = 128" -> True

def check_equation(equation):
    if eval(equation):
        return True
    else:
        return False

#print(check_equation("14 / 7 == 2"))


# 4. Write a function that selects all words that have all the same vowels (in any order and/or number)
# as the first word, including the first word.
# Eg: same_vowel_group(["toe", "ocelot", "maniac"]) ➞ ["toe", "ocelot"]
# same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]) ➞ ["many"]
# same_vowel_group(["hoops", "chuff", "bot", "bottom"]) ➞ ["hoops", "bot", "bottom"]

word_list = ["hoops", "chuff", "bot", "bottom"]

def same_vowel_group(l1):
    vowels = ["a", "e", "i", "o", "u"]
    word_vowels = []
    new_list = set()
    for i in l1[0]:
        if i in vowels:
            word_vowels.append(i)

    for j in l1:
        for k in word_vowels:
                for l in j:
                    if l == k:
                        new_list.add(j)
    print(list(new_list))
#same_vowel_group(word_list)














