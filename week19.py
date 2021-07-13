import math
from datetime import datetime

def is_prime(n):
    is_p = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_p = False
            break
    return is_p

def next_prime(x):
    while True:
        if is_prime(x):
            return x
        else:
            x += 1

#print(next_prime(32))

def prev_prime(x):
    while True:
        if x == 1:
            return None
        if is_prime(x):
            return x
        else:
            x -= 1

#print(prev_prime(18))

def closest_prime(n):
    if n <= 1:
        print(f'Closest prime of {n} is 2')
        return
    if is_prime(n):
        print(f'Closest prime of {n} is {n}')
    else:
        np = next_prime(n)
        pp = prev_prime(n)
        if pp is None:
            print(f'Closest prime of {n} is {np}')
        else:
            if np - n > n - pp:
                print(f'Closest prime of {n} is {pp}')
            else:
                print(f'Closest prime of {n} is {np}')


#closest_prime(8)

dates = ['03-04-1982_12:11', '09-08-2010_09:11', '14-12-2004_10:32','08-12-2004_08:00', '08-12-2004_08:45',
'12-02-1985_00:58']


def sorting_date(d,order):
    my_dates = list(map(lambda x: datetime.strptime(x,'%d-%m-%Y_%H:%M'),d))
    if order == 'asc':
        my_dates.sort()
    else:
        my_dates.sort(reverse = True)

    my_dates = list(map(lambda x: datetime.strftime(x, '%d-%m-%Y_%H:%M'), my_dates))
    return my_dates

#print(sorting_date(dates,'dsc'))



