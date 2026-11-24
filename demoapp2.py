# importing the math module  
import math
import random

'''	  
# using the variables and functions from the imported module  
print("Pi =", math.pi)  # returns value of Pi  
print("Square root of 16 =", math.sqrt(16))  # returns square root of 16  
print("Floor value of 19.5 =", math.floor(19.5)) # returns floor value of 19.5  
print("Ceiling value of 24.7 =", math.ceil(24.7))  # returns ceiling value of 24.7  
print("Factorial of 6 =", math.factorial(6)) # returns factorial of 6  
'''
list_1 = [1, 4, True, 800, "python", 27, "hello"]

print("Random Integer between 10 and 50 =", random.randint(1, 30)) # returns a random integer between 10 and 50  

print("Random Floating Point between 0 and 1 =", random.random())  # returns a floating point between 0 and 1  

print("Random Item from the List =", random.choice(list_1)) # returns a random item from the list  
