import datetime
import random
import os
"""
info = open("Personal_Information.txt","a")
while True:
    name = input("Please enter your name\n")
    if name == "-1":
        info.close()
        break

    zip_code = input("Please enter your zipcode\n")
    city = input("Please enter your city\n")
    info.write(f'{name}, {zip_code}, {city}\n')
"""

"""
with open("Personal_Information.txt","a") as info:
    while True:
        name = input("Please enter your name\n")
        if name == "-1":
            info.close()
            break

        zip_code = input("Please enter your zipcode\n")
        city = input("Please enter your city\n")
        info.write(f'{name}, {zip_code}, {city}\n')
"""

"""
with open("Personal_Information.txt") as info:
    for line in info:
        line = line[:-1]
        data = line.split(",")
        if data == [""]:
            continue
        print(data[1])
"""

"""
def convert(n):
    z = (n * 9/5) + 32
    return z
output_file = open("c_to_f.txt","w")
def write_data(c, f):
    output_file.write(f'{c}, {f} \n')
with open("temp.txt","r") as f:
    for cel_india in f:
        cel_india_float = float(cel_india[:-1])
        write_data(cel_india_float, convert(cel_india_float))
"""


# 1. Write a program that will take input for collecting student info and store in file. Leave a blank line
# after each student. One detail in each line (Name, Gender, DOB, City). End the program when Name is "-1"
# Note: Each time I run the program the previous data should still exist.
# Eg: John Paul
# Male
# 10/11/2005
# Chicago

"""
with open("Student_Info.txt","a") as info:
    while True:
        name = input("Please enter your name\n")
        if name == "-1":
            info.close()
            break

        gender = input("Please enter your gender\n")
        date_of_birth = input("Please enter your date of birth\n")
        city = input("Please enter your city\n")

        info.write(f'{name}\n{gender}\n{date_of_birth}\n{city}\n')

"""
# 2. Write a program to collect Student names and their marks in 5 subjects (English, Maths, Physics, Chemistry, Biology)
# Marks will be entered in comma separated format. Leave blank line after each student
# Eg: Ravi Teja
# 85,98,91,74,38

"""
with open("Student_Marks.txt","a") as info:
    while True:
        name = input("Please enter your name\n")
        if name == "-1":
            info.close()
            break
        english = input("Enter your marks in from english\n")
        math = input("Enter your marks in from math\n")
        physics = input("Enter your marks in from physics\n")
        chemistry = input("Enter your marks in from chemistry\n")
        biology = input("Enter your marks in from biology\n")

        info.write(f'{name}\n{english},{math},{physics},{chemistry},{biology}\n')
"""

# 3. Write a program to collect information about the cars/trucks/suv a Honda dealer has. This time the data should
# be in comma separated format with a header 'model', 'vehicle_type', 'seat_type', 'capacity', 'gas', 'mpg'
# as the first line
# Eg: 'model', 'vehicle_type', 'seat_type', 'capacity', 'gas', 'mpg'
# 'Odyssey','Mini-van','Leather',7,True,28
# Note: Look online to find data for Honda models. Do 5-10 models of various categories. Also note that if it is
# text data it needs to be in single quotes. 'gas' is boolean. True if it is gas model, False if it is diesel model


"""
with open("Honda.txt","a") as info:
    if os.stat("Honda.txt").st_size == 0:
        info.write("Model, Vehicle-type, Seat_type, Capacity, Gas, Mpg\n")

    str_gas = ""
    while True:
        model = input("Enter the car model\n")
        if model == "-1":
            break

        vehicle_type = input("Enter the car vehicle type\n")
        seat_type = input("Enter the seat type\n")
        capacity = input("Enter the car's capacity\n")
        gas = input("Enter gas type.(True = gas, False = diesel)\n")
        if gas == "True":
            str_gas = "Gas"
        else:
            str_gas = "Diesel"

        mpg = input("Enter the car's miles per gallon\n")

        info.write(f'{model}, {vehicle_type}, {seat_type}, {capacity}, {str_gas}, {mpg}\n')

"""
# 4. Write a program to create a file with a specific filename based on timestamp.
# Eg: If i run the program at 4:08 pm on Oct 5th 2020, the file name should be 10202020_1608.txt



"""
today = datetime.datetime.now()
month = today.strftime("%m")

day = today.strftime("%d")

year = today.strftime("%Y")

hour = today.strftime("%H")

minute = today.strftime("%M")

with open(f'{month}{day}{year}_{hour}{minute}.txt',"a") as date1:
    pass
"""


# 5. Write a program that contains 4 functions (add, sub, mul, div) which takes 2 parameters. Each time I run the
# program, randomly call any one of the four functions and in a log file keep appending the function name that
# was called with the parameters that were passed and the result. (Parameters should also be random).
# Note: Watch out that for the div function you cannot have the divisor as 0


"""
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y


with open("Operation.txt","a") as operation:
    random1 = 0
    random2 = 0
    set_op = {"+", "-", "*", "/"}
    random_op = set_op.pop()
    if random_op == "+":
        random1 = random.randint(1,100)
        random2 = random.randint(1,100)
        operation.write(f'{random1} + {random2} = {add(random1,random2)}\n')
    elif random_op == "-":
        random1 = random.randint(1, 100)
        random2 = random.randint(1, 100)
        operation.write(f'{random1} - {random2} = {sub(random1,random2)}\n')
    elif random_op == "*":
        random1 = random.randint(1, 100)
        random2 = random.randint(1, 100)
        operation.write(f'{random1} * {random2} = {mul(random1,random2)}\n')
    elif random_op == "/":
        random1 = random.randint(1, 100)
        random2 = random.randint(1, 100)
        operation.write(f'{random1} / {random2} = {div(random1,random2)}\n')

"""




with open("Mini_mart.txt","a") as stock:
    while True:
        item_number = int(input("Enter the item number\n"))
        if item_number == -1:
            break
        item_name = input("Enter the item name\n")
        price_per_lb = input("Enter the price per pound\n")
        quantity_available = int(input("Enter the quantity available for the item\n"))

        stock.write(f'{item_number}, {item_name}, {price_per_lb}, {quantity_available}\n')

with open("Mini_mart.txt") as read:
    while True:
        item_search = input("Enter the item number or name\n")
        if item_search == "-1":
            break
        for line in read:
            if item_search in line:
                print(line)
                break
















