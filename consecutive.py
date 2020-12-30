import re
def is_consecutive(my_string,divider=22):
    if divider > len(my_string) // 2:
       return False
    x = re.findall(r'.{1,' + str(divider) + '}', my_string)
    print(x)
    x = list(map(int,x))
    print(x)
    x1 = [a+1==b for a,b in zip(x,x[1:])]
    print(x1)
    x1 = all(x1)
    print(x1)
    if x1:
        return True,divider
    else:
        return is_consecutive(my_string, divider + 1)
print(is_consecutive('2526272829'))


