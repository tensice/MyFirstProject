import random
import re
#EAFP - it is Easy to Ask for Forgiveness than Permission
#operator overloading
class Gun:
    def fight(self):
        print('Bang Bang Bang')

class Sword:
    def fight1(self):
        print('swish swish swish')

class Zombie:
    name = ''
    legs = 0
    eyes = 0
    weapon = ''
    size = 0
    #Funtion overloading is not supported in python
    """
    def add(self,a,b):
        return a + b
    def add(self,a,b,c):

        return a+b+c
        """

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
    def use_weapons(self):
        try:
            self.weapon.fight()
        except AttributeError as e:
            print(e)
        """if hasattr(self.weapon, 'fight'):
            if callable(self.weapon.fight):
                self.weapon.fight()
            else:
                print('cannot execute fight attribute')"""
    def __add__(self, other):
        legs = self.legs + other.legs
        eyes = self.eyes + other.eyes
        size = self.size + other.size
        z = Zombie(legs=legs,eyes=eyes,size=size,weapon=self.weapon)
        return z
    def get_attributes(self):
        return f'name:{self.name}, legs:{self.legs}, eyes:{self.eyes},weapon:{self.weapon}, size:{self.size}'
g1 = Gun()
d1 = Zombie(name='Bob',eyes=6,legs=5,size=3,weapon=g1)
# d1.eyes = 7
# d1.name = 'Bob'
# d1.legs = 5
# d1.size = 3
# d1.weapon = 'gun'

s1 = Sword()
d2 = Zombie(eyes=100,legs=2,size=2,weapon=s1)
# d2.name = 'Jeff'
# d2.legs = 2
# d2.size = 2
# d2.weapon = 'knife'
print(d1.get_attributes())
d1.use_weapons()
d2.use_weapons()

#print(d2.get_attributes())

x = 10
y = 20
a = '123'
b = '456'
print(x+y)
print(a+b)
print(a.__add__(b))
d3 = d1+d2
print(d3.get_attributes())