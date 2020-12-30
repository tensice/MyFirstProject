# #a function that calls itself
import  math
# def x ():
#     print('start of x')
#     x()
#     print('end of x')
# # def y ():
# #     print('start of y')
# #     z()
# #     print('end of y')
# # def z ():
# #     print('start of z')
# #     #x()
# #     print('end of z')
# x()

# def factorial(n):
#     return math.factorial(n)
#
# #print(factorial(5))
#
# #factorial of 5 = 5*4*3*2*1
# #factorial of 4 = 4*3*2*1
#
# def r_factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * r_factorial(n-1)
# print(r_factorial(998))
fibo_cache = {}
def r_fibonacci(n):
    if n in fibo_cache:
        return fibo_cache.get(n)
    else:

        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            value =  r_fibonacci(n-1) + r_fibonacci(n-2)
            fibo_cache[n] = value
            return value
#print(r_fibonacci(30))
#1,1,2,3,5,8,13,21
# for i in range(1,100):
#     print(f'fibonacci of {i} is {r_fibonacci(i)}')
#memoization
import functools

@functools.lru_cache()
def r_fibonacci_internal_cache(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return r_fibonacci_internal_cache(n - 1) + r_fibonacci_internal_cache(n - 2)
for i in range(1,10000):
    print(f'fibonacci of {i} is {r_fibonacci_internal_cache(i)}')
