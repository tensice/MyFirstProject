import csv
from datetime import datetime
from collections import defaultdict
import math

# 5. Sort the list of dates given in a list either ascending or descending. The date in the list is of the
# format DD-MM-YYYY_HH:MM. The priority you need to sort with is Year, Month, Day, Hours, and Minutes
# Input: sort_dates(["09-02-2000_10:03", "10-02-2000_18:29", "01-01-1999_00:55"], "asc")
# Output: ["01-01-1999_00:55", "09-02-2000_10:03", "10-02-2000_18:29"]
#
# dates = ['03-04-1982_12:11', '09-08-2010_09:11', '14-12-2004_10:32','08-12-2004_08:00', '08-12-2004_08:45',
# '12-02-1985_00:58']
# Input: sort_dates(dates, "dsc")
# Output: ['09-08-2010_09:11','14-12-2004_10:32', '08-12-2004_08:45','08-12-2004_08:00','12-02-1985_00:58', '03-04-1982_12:11']


"""
dates = ['03-04-1982_12:11', '09-08-2010_09:11', '14-12-2004_10:32','08-12-2004_08:00', '08-12-2004_08:45',
'12-02-1985_00:58']


def sort_dates(dates, dsc_asc):
    if dsc_asc == "asc":
        dates.sort(key=lambda date: datetime.strptime(date, '%d-%m-%Y_%H:%M'))
    elif dsc_asc == "dsc":
        dates.sort(reverse = True,key=lambda date: datetime.strptime(date, '%d-%m-%Y_%H:%M'))


    return dates
print(sort_dates(dates,"asc"))
"""


# 4. Create a function that takes a list and a string. For each letter in the string, remove that letter once from the
# list. At the end print the list. If all the data in list is gone, print an empty list
# Eg: ['b', 'r', 't', 'q', 'b', 'l', 'l']
# bulb
# Output: ['r', 't', 'q', 'l']
"""
l1 = ['b', 'r', 't', 'q', 'b', 'l', 'l']

def remove_letter(l1,str1):
    for i in str1:
        if i in l1:
            l1.remove(i)
    return l1

#print(remove_letter(l1,"bulb"))
"""

# 2. Given a positive integer you can find a new number by squaring all the digits and adding it. You can repeat
# this process and you will end up with a sequence of numbers. If the given number is a uni-number then at
# some point the number in the sequence will reach 1. In that case return True. If the number is a non uni-number,
# at some point in the sequence you will get 4. At that point stop the process and return False
# Eg: 7 The sequence will be 49, 97, 130, 10, 1 (True) Uni-number
# 23 The sequence will be 13, 10, 1 (True) Uni-number
# 12 The sequence will be 5, 25, 29, 85, 89, 145, 42, 20, 4 (False) Non uni-number
# 108 The sequence will be 65, 61, 37, 58, 89, 145, 42, 20, 4 (False) Non uni-number


# def uni_number(num):
#     new_num = int
#
#     for i in str(num):
#         new_num = int(i) ** 2
#         print(new_num)
#         for j in str(new_num):
#             new_num = int(j) ** 2
#             print(new_num)
# uni_number(7)


# 1. Download Disney movies data from the URL https://www.dropbox.com/s/xh8n1lk3oc5nvla/disney_movies.csv?dl=0
# Write a program to read the CSV file and convert into a list of dictionary with the headers as key for the
# dictionary. Provide a choice for the users with the following questions:
# a) Disney movies released before 1st Jan 2000
# b) Disney movies sorted and listed by Genre (alphabetical)
# c) Disney movies sorted by year (reverse chronological order) [It means starting with the latest movie first]
# d) Disney movies that has 4 or more words
# e) Disney movies that has numbers in it
# Note: I have just given you 5 things, you are welcome to add more



path = 'data/disney_movies.csv'
with open(path) as file:
    reader = csv.reader(file)
    header = next(reader)
    data = [i for i in reader]

disney_list = []
for d in data:
    disney_dict = {}

    movie_title = d[0]
    release_date = d[1]
    genre = d[2]
    mpaa_rating = d[3]
    total_gross = d[4]
    inflation_adjusted_gross = d[5]
    disney_dict['movie_title'] = movie_title
    disney_dict['release_date'] = release_date
    disney_dict['genre'] = genre
    disney_dict['mpaa_rating'] = mpaa_rating
    disney_dict['total_gross'] = total_gross
    disney_dict['inflation_adjusted_gross'] = inflation_adjusted_gross

    disney_list.append(disney_dict)

#print(disney_list)

def question1():
    for i in data:
        value = i[1]
        year = value[:-6]
        int_year = int(year)
        if int_year < 2000:
            print(i[0], i[1])

#question1()


def question2():
    d_genre = defaultdict(list)
    for i in data:
        value = i[0]
        d_genre[i[2]].append(value)

    for j in sorted(d_genre.keys()):
        print(j, d_genre[j])
        print()


#question2()


def question3():
    d_year = {}
    for i in data:
        value = i[0]
        d_year[i[1]] = value

    for j in reversed(sorted(d_year)):
        print(d_year[j], j)



#question3()

def question4():
    for i in data:
        value = i[0]
        if value.count(' ') >= 3:
            print(value)


#question4()

def question5():
    for i in data:
        value = i[0]
        if '0' in value or '1' in value or '2' in value or '3' in value or '4' in value\
                or '5' in value or '6' in value or '7' in value or '8' in value or '9' in value:
           print(value)


#question5()


def choose_question():
    question = int(input("1.Disney movies released before 1st Jan 2000\n"
                         "2.Disney movies sorted and listed by Genre (alphabetical)\n"
                         "3.Disney movies sorted by year (reverse chronological order)\n"
                         "4.Disney movies that has 4 or more words\n"
                         "5.Disney movies that has numbers in it\n\nChoose a question number 1 through 5\n"))

    if question == 1:
        question1()
    elif question == 2:
        question2()
    elif question == 3:
        question3()
    elif question == 4:
        question4()
    elif question == 5:
        question5()
    else:
        print("Invalid question number")


choose_question()




# 3. Get a number as input and return the closet prime number to that number. The prime number can be greater or smaller
# to the given number, but it should be closest
#
# Eg: 3 -> should return 3 since 3 itself is a prime number and it is closest to 3
# 8 -> should return 7
# 15 -> can return either 13 or 17 (either one is correct)



def closest_prime_number(num):
    is_prime = bool
    is_prime2 = bool
    is_prime3 = bool
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    else:
        is_prime = True
    if is_prime:
        print(num)
        quit()


    for j in range(num + 1, num + 10):
        for k in range(2, int(math.sqrt(j)) + 1):
            if j % k == 0:
                is_prime2 = False
                break
        else:
            is_prime2 = True

        if is_prime2:
            big = j
            break
    for a in range(num - 1,0,-1):
        for b in range(2, int(math.sqrt(a)) + 1):
            if a % b == 0:
                is_prime3 = False
                break
        else:
            is_prime3 = True


        if is_prime3:
            small = a
            break

    diff1 = abs(big - num)
    diff2 = abs(small - num)

    if diff1 > diff2:
        print(small)
    elif diff2 > diff1:
        print(big)
    else:
        print(big, small)



#closest_prime_number(80)








