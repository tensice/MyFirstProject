import random
import re
class Zombie:
    name = ''
    legs = 0
    eyes = 0
    weapon = ''
    size = 0
    def __init__(self,legs,eyes,size,weapon,name=None):
        if name == None:
            num = random.randint(1,100)
            name = f'z{num}'
        if eyes < 5:
            print('Eyes cannot be less than 5')
            exit()
        self.name = name
        self.legs = legs
        self.eyes = eyes
        self.size = size
        self.weapon = weapon
        #print(f'zombie {name} created')
    def get_attributes(self):
        return f'name:{self.name}, legs:{self.legs}, eyes:{self.eyes},weapon:{self.weapon}, size:{self.size}'

d1 = Zombie(name='Bob',eyes=6,legs=5,size=3,weapon='gun')
# d1.eyes = 7
# d1.name = 'Bob'
# d1.legs = 5
# d1.size = 3
# d1.weapon = 'gun'

d2 = Zombie(eyes=100,legs=2,size=2,weapon='knife')
# d2.name = 'Jeff'
# d2.legs = 2
# d2.size = 2
# d2.weapon = 'knife'
#print(d1.get_attributes())
#print(d2.get_attributes())
"""
"""
class Student:
    name = ''
    marks = 0
    major = ''
    def __init__(self,name,marks,major):
        my_string = r'[A-Z][A-z]{4,},[A-Z][A-z]{4,}'
        pattern = re.compile(my_string)
        match = pattern.match(name)
        majors = ['Math','English','Physics','Chemistry','History','Accountancy']
        if marks < 30 or marks > 100:
            print('Marks cannot be less than 30 or greater than 100')
            exit()
        if major not in majors:
            print('Your major has to be Math, English, Physics, Chemistry, History, or Accountancy')
            exit()
        if not match:
            print('Name doesnt follow the conditions')
            exit()
        self.name = name
        self.marks = marks
        self.major = major
        #print(f'Student {name} created')
    def get_attributes(self):
        return f'name:{self.name}, marks:{self.marks}, major:{self.major}'


s1 = Student(name='Raghuraman, Visvesh',marks=80,major='English')

s2 = Student(name='Kalyanaraman,Rahguraman',marks=92,major='Chemistry')

print(s1.get_attributes())
print(s2.get_attributes())


class Employee:
    name = ''
    salary = 0
    city = ''
    bonus = 0
    type1 = ''
    def __init__(self,salary,city,bonus,type1,name=None):
        if name == None:
            num = random.randint(1, 100)
            name = f'e{num}'
        if type1 == 'Engineer':
            bonus = salary * 5/100
        if type1 == 'Manager':
            bonus = salary * 3/100
        self.name = name
        self.salary = salary
        self.city = city
        self.bonus = bonus
        self.type1 = type1
        #print(f'Employee {name} has been created')
    def get_attributes(self):
        return f'name:{self.name}, salary:{self.salary}, city:{self.city}, bonus:{self.bonus}, type:{self.type1}'

emp1 = Employee(name='Bob',salary=5000,city='Austin',bonus=0,type1='Manager')

emp2 = Employee(salary=3000,city='New York City',bonus=0,type1='Engineer')

#print(emp1.get_attributes())
#print(emp2.get_attributes())