import random
import math
def my_func(times):
    heads = 0
    tails = 0
    for i in range(times):
        random_number = random.randint(1, 2)
        if random_number == 1:
            heads += 1
        elif random_number == 2:
            tails += 1

    return f'heads:{heads}', f'tails:{tails}'

#print(my_func(1000))


def my_gcd(num1, num2):
    g = math.gcd(num1,num2)
    return g
#print(my_gcd(12,16))

def is_prime(num):
    prime = True
    for i in range(2,int(math.sqrt(num) + 1)):
        if num % i == 0:
            prime = False
            break
    return prime

#print(is_prime(169))

def get_primes(count):
    my_prime_list = []
    n = 2
    while True:
        if is_prime(n):
            my_prime_list.append(n)
        if len(my_prime_list) == count:
            break
        n += 1
    return my_prime_list

#print(get_primes(10))


def get_primes_between(start, end):
    my_prime_list = []
    for i in range(start,end + 1):
        if is_prime(i):
            my_prime_list.append(i)
    return my_prime_list
print(get_primes_between(11,19))


