print("""
----------------------------------------------

FUNCTION
    
    block of code to complete a task 

- maximize code reuse and minimize redundancy
- increase readability in large program 

Note:
    In python, function does not exist until execution. 
----------------------------------------------
\n\n\n""")



print("""
----------------------------------------------

DEFINE FUNCTION 

Syntax:

    def function_name (parameter):
        code 
        return code 

Note: 
    keyword def creates a function object and assign it an identifier (e.g. function_name) 
    code block begins with : and and is indented 
    code block use parameter(s) to complete task 
    use keyword return to provide output to user 

Example:
""")


# 1 parameter
def add_1(x):
    return x + 1


# 2 parameter
def sum(x, y):
    return x + y


# variable length
def total(*x):
    sum_result = 0
    for value in x:
        sum_result += value
    return sum_result


# function with argument and default argument
def quotient(dividend, divisor=1):
    return dividend / divisor


# parameter is pass by reference only
# the called function can modify the value of the parameter
def update(x):
    x = 9
    print("x is " + str(x))



print("""
----------------------------------------------

CALL/INVOKE FUNCTION 
    
    call function with 1 parameter 
    
Example:
""")
number = 4
print("Number:", number)
print('Call function: add_1(number)')
print('Result:', add_1(number), end="\n\n")


print("""
----------------------------------------------

CALL/INVOKE FUNCTION 

    call function with 2 parameter 

Example:
""")
numbers = [1, 2]
print("Numbers:", numbers)
print('Call function: sum(numbers[0], numbers[1])')
print('Result:', sum(numbers[0], numbers[1]), end="\n\n")

print("""
----------------------------------------------

CALL/INVOKE FUNCTION 

    call function with variable parameter 

Example:
""")
print("Numbers:", 1, 2, 3)
print('Call function: total(1, 2, 3)')
print('Result:', total(1, 2, 3), end="\n\n")


print("""
----------------------------------------------

CALL/INVOKE FUNCTION 

    call function with default parameter 

Example:
""")
print("Number:", number)
print('Call function: quotient(number)')
print('Result:', quotient(number), end="\n\n")


print("Number:", number)
print('Call function: quotient(number, 2)')
print('Result:', quotient(number, 2), end="\n\n")


print("""
----------------------------------------------

CALL/INVOKE FUNCTION 

    call function by keyword argument 

Note:

This allows you to skip arguments or place them
out of order because the Python interpreter is able to use the
keywords provided to match the values with parameters.

Example:
""")
print('Call function: quotient(divisor=4, dividend=8)')
print('Result:', quotient(divisor=4, dividend=8), end="\n\n")

print("""
----------------------------------------------

LAMBDA

    lambda is an anonymous function.
    
    purpose:
    
    Lambda functions are mainly used in combination with the functions 
    filter(), map() and reduce()
    
syntax:
    
    function_object = lambda parameter_1, parameter_2: expression 

Note:
    operator lambda can have any number of arguments
    
Example:
""")
add = lambda x, y: x + y
print("lambda:", 'add = lambda x, y: x + y')
print('Result:', add(3, 4))

print("""
----------------------------------------------

LAMBDA AND MAP

    using lambda with python built-in map function 
    
MAP:
    
    Applies the given function to each item of a given iterable
    (list, tuple, ...) 

Example 1:
""")

print("Given numbers:", numbers)
map_object = map(add_1, numbers)
print("Mapped with function add_1:", list(map_object))

print("""
----------------------------------------------

LAMBDA AND MAP

Example 2:
""")
print("Given set 1:", numbers)
print("Given set 2:", numbers)
map_object = map(sum, numbers, numbers)
print("Mapped with function sum:", list(map_object))


