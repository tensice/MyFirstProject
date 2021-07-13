from fuzzywuzzy import fuzz
from fuzzywuzzy import process
str1 = "visvesh"
str2 = "visvesh"

# ratio = fuzz.ratio(str1,str2)
# print(ratio)
#
# partial_ratio = fuzz.partial_ratio(str1,str2)
# print(partial_ratio)
#
# w_ratio = fuzz.WRatio(str1,str2)
#
# print(w_ratio)
#
# token_sort_ratio = fuzz.token_sort_ratio(str1,str2)
# print(token_sort_ratio)
#
# token_set_ratio = fuzz.token_set_ratio(str1,str2)
# print(token_set_ratio)

my_query = "Visvesh Raghuraman"

choices = ["Vis Raghuraman", "Visvesh Raghuram", "Vis Raghuram vesh", "Veshvis amanRaghur", "VR", "Raghur Vis", "Bisbesh Raghur", "Vishvesh Raghuraman"]
choices2 = [1,2,3,4,5]
#print(process.extract(my_query,choices2))
#print(process.extractOne(my_query,choices))

"""
fruits = ["apple", "orange", "mango", "durian"]

user_fruit = input("What fruit would you like\n")

x = process.extractOne(user_fruit,fruits)

if x[1] >= 80:
    print(x)
    print(f' {x[0]} is your fruit')
elif x[1] >= 50 and x[1] <= 80:
    print(x)
    print(f'I think {x[0]} is your fruit')
else:
    print(f'Sorry, we dont carry {user_fruit} in our store')
"""





