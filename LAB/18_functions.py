#  Write a Python program to create a function that takes a string as input and prints it.
def print_string(input_string):
    print(input_string)
print_string('Hello world')

#  Write a Python program to create a calculator using functions.

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error! Divide by zero is not allowed."
    else:
        return x/y

fun=input('Select \n1.add\n2.subtract\n3.multiply\n4.divide\n ')
if fun=='1':
    n=int(input('Enter your 1st number: '))
    n1=int(input('Enter your 2nd number: '))
    print(add(n,n1))
elif fun=='2':
    n=int(input('Enter your 1st number: '))
    n1=int(input('Enter your 2nd number: '))
    print(subtract(n,n1))
elif fun=='3':
    n=int(input('Enter your 1st number: '))
    n1=int(input('Enter your 2nd number: '))
    print(multiply(n,n1))
elif fun=='4':
    n=int(input('Enter your 1st number: '))
    n1=int(input('Enter your 2nd number: '))
    print(divide(n,n1))
else:
    print('Invalid input')

# Practical Examples: 
# 19) Write a Python program to print a string using a function. 
# 20) Writea Python program to create a parameterized function that takes two arguments and prints their sum. 
# 21) Write a Python program to create a lambda function with one expression. 
square = lambda x: x * x
print(square(5))
# 22) Writea Python program to create a lambda function with two expressions.
# Create a lambda function with two expressions
math_operations = lambda x, y: (x + y, x * y)
sum_result, product_result = math_operations(5, 3)
print(f"Sum: {sum_result}, Product: {product_result}")