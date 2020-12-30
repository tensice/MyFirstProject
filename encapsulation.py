import random
class Zombie:
    name = ''
    legs = 0
    __eyes = 0
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
        self.__eyes = eyes
        self.size = size
        self.weapon = weapon
        print(f'zombie {name} created')
    def test(self):
        print('hello')


    def get_attributes(self):
        return f'name:{self.name}, legs:{self.legs}, eyes:{self.__eyes},weapon:{self.weapon}, size:{self.size}'
z1 = Zombie(legs=10,eyes=7,weapon='grenade',size=3,name='jeff')
z1.__eyes = 3
print(z1.get_attributes())
print(z1.__eyes)
z1.__test()