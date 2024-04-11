import math
# import os
# import math

# def factorial(n):
#     if n>=1 :
#         return n * factorial(n-1)
 
# n = 5
# w  = factorial(n)

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def apply_operation(func, value):
    result = func(value)
    return result

# Example usage
number = 5

# Pass the 'square' function to 'apply_operation'
result_square = apply_operation(square, number)
print(f"Square of {number}: {result_square}")

# Pass the 'cube' function to 'apply_operation'
result_cube = apply_operation(cube, number)
print(f"Cube of {number}: {result_cube}")

def addition(x):
    
    y = 5
    return x + y

def mult(w, value):
    return 3 + w(value) 

scr = mult(addition, 2)

print(scr)
