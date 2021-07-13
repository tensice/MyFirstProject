import csv
from collections import defaultdict
import random

# 1. Perfect seating arrangement
# Create a function that will tell whether the seating arrangement is perfect. The seating arrangement is perfect
# if the number in front is equal or smaller. The input will be a list of lists.
# seats1 = [[1, 2, 3, 2, 1, 1],
# [3, 5, 4, 3, 2, 2],
# [5, 5, 5, 5, 4, 4],
# [6, 6, 7, 6, 5, 5]]
# Eg: perfect_seats(seats1) -> True as you can see in the first element of each list 6>5>3>1, in the 2nd element
# 6>5>=5>2 and so on
# seats2 = [[1, 2, 3, 2],
# [2, 4, 4, 3],
# [5, 5, 5, 10],
# [6, 6, 7, 6]]
# Eg: perfect_seats(seats1) -> False as you can see in the last element of each list 6 not >10>3>2




seats1 = [[1, 2, 3, 2, 1, 1], [3, 5, 4, 3, 2, 2], [5, 5, 5, 5, 4, 4], [6, 6, 7, 6, 5, 5]]
seats2 = [[1, 2, 3, 2], [2, 4, 4, 3], [5, 5, 5, 10], [6, 6, 7, 6]]

def order_seats(seat_list):
    for i in range(len(seat_list)):
        if i + 1 == len(seat_list):
            break
        l1 = seat_list[i]
        l2 = seat_list[i + 1]
        for j,k in zip(l1,l2):
            if j > k:
                return False
                #print(f'Row:{i + 1}, {i + 2}: Seat number {j}, {k}')
    return True


#print(order_seats(seats1))


#2. Write a program to create 26 files. The names should be A.txt, B.txt, C.txt .... up to Z.txt




#alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


"""
for i in alphabet1:
     with open(f'{i}.txt','w') as f:
        pass
"""


# 3. Download the file Motivational_Quotes.csv from the dropbox folder
# https://www.dropbox.com/sh/yts98am3nsly5sm/AAC2rA-XQ8jG9u29vCd8wOBOa?dl=0
# Write three functions (user should pick from the choice)
# a) displays the author name and the total number of quotes they have made
# The list should be in alphabetical order (ascending)
# Eg: Author 1 --> 20 quotes
# Author 2 --> 7 quotes
# ...
# Author 100 --> 34 quotes
#
# b) displays the summary, author name and the total number of quotes they have made
# The list should be in descending order of total number of quotes
# Eg: Author 17 --> 76 quotes
# Author 14 --> 53 quotes
# ...
# Author 12 --> 3 quotes
#
# c) Display a random quote each time the user picks this choice, along with its author


path = 'data/motivational_quotes.csv'
with open(path) as file:
    reader = csv.reader(file)
    header = next(reader)
    data = [i for i in reader]

for d in data:
    quote_dict = {}
    quote = d[0]
    author = d[1]

    quote_dict['Quote'] = quote
    quote_dict['Author'] = author



def question1():
    l_quote = []
    d_quote = {}
    for i in data:
        value = i[1]
        l_quote.append(value)
    for j in sorted(l_quote):
        d_quote[j] = l_quote.count(j)
    print(d_quote)

#question1()

def question2():
    new_dict = {}
    l_quote2 = []
    d_quote2 = {}
    for i in data:
        value = i[1]
        l_quote2.append(value)
    for j in l_quote2:
        d_quote2[j] = l_quote2.count(j)

    for l in d_quote2:
        new_dict[d_quote2.get(l)] = l

    for k in reversed(sorted(new_dict)):
        print(new_dict[k],k)



#question2()


def question3():
    dict1 = {}
    for i in data:
        value = i[0]
        dict1[i[1]] = value
    l1 = list(dict1.items())
    random_quote = random.choice(l1)
    print(random_quote)


#question3()


def choose_question():
    question = int(input("1.Displays the author name and the total number of quotes they have made. "
                         "The list should be in alphabetical order (ascending)\n"
                         "2.Displays the summary, author name and the total number of quotes they have made. "
                         "The list should be in descending order of total number of quotes\n"
                         "3.Display a random quote each time the user picks this choice, along with its author\n\n"
                         "Choose a question number 1 through 3\n"))
    if question == 1:
        question1()
    elif question == 2:
        question2()
    elif question == 3:
        question3()
    else:
        print("Invalid question number")

#choose_question()





