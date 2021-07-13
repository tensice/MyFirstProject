'''
Iterable - something you can loop over
__ -> dundar
To check if something is an iterable, do the dir() and if it has __iter__, then it is an iterable
To check if something is an iterator, do the dir() and if it  has __iter__ and __next__, then is is an iterator

Generator - A regular function with a yield keyword instead of return
The function stays in the same state and can be called again and it will start from where it left off.
'''

l1 = [1,2,3,'hello',True]

#print(dir(l1))

# x = l1.__iter__()
# print(dir(x))
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

#x = iter(l1)

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# while True:
#     try:
#         print(next(x))
#     except StopIteration:
#         print("End of list")
#         break

# for i in x:
#     print(i)

def my_func():
    n = 1
    yield n
    n = n + 1
    yield n
    n = n + 1
    yield n

#x = my_func()
#print(dir(x))

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# for i in x:
#     print(i)

def even_generator(max_num):
    n = 0
    for i in range(0,max_num + 1,2):
        yield i

x = even_generator(20)

for i in x:
    print(i)








