
print("""
----------------------------------------------
Operator

    a character which represents an action

""")


print("""
----------------------------------------------

Arithmetic Operators

     Name                   operator
    _____________________________________

    Addition                    +
    Subtraction                 -
    Multiplication              *
    Division                    /
    Floor                       //
    Exponent                    **
    Modulus                     %

Example:
""")


number_1 = 8
number_2 = 2

result = number_1 + number_2
print("Addition: {number1} + {number2} = {result}".format(number1=number_1, number2=number_2, result=result))

result = number_1 - number_2
print("Subtraction: {number1} - {number2} = {result}".format(number1=number_1, number2=number_2, result=result))

result = number_1 * number_2
print("Multiplication: {number1} * {number2} = {result}".format(number1=number_1, number2=number_2, result=result))

result = number_1 / number_2
print("Division: {number1} / {number2} = {result}".format(number1=number_1, number2=number_2, result=result))

result = number_1 // number_2
print("Division: {number1} // {number2} = {result}".format(number1=number_1, number2=number_2, result=result))

result = number_1 ** number_2
print("Exponent: {number1} ** {number2} = {result}".format(number1=number_1, number2=number_2, result=result))

result = number_1 % number_2
print("Modulus: {number1} % {number2} = {result}".format(number1=number_1, number2=number_2, result=result))


print("""
----------------------------------------------

Comparison (Relational) Operators

     Name                   operator
    _____________________________________

    Equal                   ==
    Not equal               !=
    greater than            >
    less than               <
    greater than or equal   >=
    less than or equal      <=

Compare two numbers with result given as true/false

Example:
""")


result = number_1 == number_2
print("Result of {one} == {two}: {result}".format(one=number_1, two=number_2, result=result))

result = number_1 != number_2
print("Result of {one} != {two}: {result}".format(one=number_1, two=number_2, result=result))

result = number_1 > number_2
print("Result of {one} > {two}: {result}".format(one=number_1, two=number_2, result=result))

result = number_1 < number_2
print("Result of {one} < {two}: {result}".format(one=number_1, two=number_2, result=result))

result = number_1 >= number_2
print("Result of {one} >= {two}: {result}".format(one=number_1, two=number_2, result=result))

number_2 = number_1
result = number_1 <= number_2
print("Result of {one} <= {two}: {result}".format(one=number_1, two=number_2, result=result))


print("""
----------------------------------------------

Assignment Operators
      operator      Syntax         equivalent
       = 
       +=          a += b         a = a + b  
       -=          a -= b         a = a - b 
       *=          a *= b         a = a * b
       /=          a /= b         a = a / b
       //=         a //= b        a = a // b
       **=         a **= b        a = a ** b
       %=          a %= b         a = a % b
       
Example:
""")

number_1 = 4
print("number_1: {number_1}\tnumber_2: {number_2}".format(number_1=number_1, number_2=number_2))
print("Execute: number1 += number2")
number_1 += number_2
print("number_1: {number_1}\tnumber_2: {number_2}\n".format(number_1=number_1, number_2=number_2))


number_1 = 4
print("number_1: {number_1}\tnumber_2: {number_2}".format(number_1=number_1, number_2=number_2))
print("Execute: number1 -= number2")
number_1 -= number_2
print("number_1: {number_1}\tnumber_2: {number_2}\n".format(number_1=number_1, number_2=number_2))

number_1 = 4
print("number_1: {number_1}\tnumber_2: {number_2}".format(number_1=number_1, number_2=number_2))
print("Execute: number1 *= number2")
number_1 *= number_2
print("number_1: {number_1}\tnumber_2: {number_2}\n".format(number_1=number_1, number_2=number_2))

number_1 = 4
print("number_1: {number_1}\tnumber_2: {number_2}".format(number_1=number_1, number_2=number_2))
print("Execute: number1 /= number2")
number_1 /= number_2
print("number_1: {number_1}\tnumber_2: {number_2}\n".format(number_1=number_1, number_2=number_2))

number_1 = 4
print("number_1: {number_1}\tnumber_2: {number_2}".format(number_1=number_1, number_2=number_2))
print("Execute: number1 //= number2")
number_1 //= number_2
print("number_1: {number_1}\tnumber_2: {number_2}\n".format(number_1=number_1, number_2=number_2))

number_1 = 4
print("number_1: {number_1}\tnumber_2: {number_2}".format(number_1=number_1, number_2=number_2))
print("Execute: number1 **= number2")
number_1 **= number_2
print("number_1: {number_1}\tnumber_2: {number_2}\n".format(number_1=number_1, number_2=number_2))


number_1 = 4
print("number_1: {number_1}\tnumber_2: {number_2}".format(number_1=number_1, number_2=number_2))
print("Execute: number1 %= number2")
number_1 %= number_2
print("number_1: {number_1}\tnumber_2: {number_2}\n".format(number_1=number_1, number_2=number_2))


print("""
----------------------------------------------


Logical Operators

    
    operator    description
      and       if both of the operands are True then logic state is True
      or        if any of the two operands are True then logic state is True
      not       reverse the logic state 

Note:

    logic state can be either True or False 
    
Example:
""")

a = True
b = False

print("a={a}\tb={b}".format(a=a, b=b), end="\n\n")

print('c = a and b ')
c = a and b
print('c=', c, end="\n\n")

print('c = a or b ')
c = a or b
print('c=', c, end="\n\n")

print('c = not a ')
c = not a
print('c=', c, end="\n\n")




print("""
----------------------------------------------

Bitwise Operators

    operator        Definition 
    
      &             bitwise AND 
      |             bitwise OR 
      ^             bitwise exlusive or 
      ~             bitwise NOT 
      <<            bitwise left shift 
      >>            bitwise right shift 

Example:
""")


def print_binary_operation(operator, bin_1, bin_2, res):
    print("binary_1:  \t{binary_1:#06b}".format(binary_1=bin_1))
    print("operation: {operator}".format(operator=operator))
    print("binary_2:  \t{binary_2:#06b}".format(binary_2=bin_2))
    print("---------------------------")
    print("result:    \t{result:#06b}".format(result=res), end="\n\n")


def print_unary_operation(operator, bin_1, res):
    print("binary_1:  \t{binary_1:#06b}".format(binary_1=bin_1))
    print("operation: {operator}".format(operator=operator))
    print("---------------------------")
    print("result:    \t{result:#06b}".format(result=res), end="\n\n")


binary_1 = 0b1100
binary_2 = 0b1010

result = binary_1 & binary_2
print_binary_operation("&", binary_1, binary_2, result)

result = binary_1 | binary_2
print_binary_operation("|", binary_1, binary_2, result)

result = binary_1 ^ binary_2
print_binary_operation("^", binary_1, binary_2, result)


operator = "~"
result = ~binary_2
print(result)
print_unary_operation(operator, binary_1, result)


operator = "<< 2"
result = binary_1 << 2
print_unary_operation(operator, binary_1, result)

operator = ">> 1"
result = binary_1 >> 1
print_unary_operation(operator, binary_1, result)


print("""
----------------------------------------------

Membership Operators
    
    not in 
    in 
    
Example:
""")

numbers = [1, 2, 3]
number = 1

result = number in numbers
print("Number '{number}' is in {list}. Answer: {result}".format(number=number, list=numbers, result=result))

result = number not in numbers
print("Number '{number}' is NOT in {list}. Answer: {result}".format(number=number, list=numbers, result=result))



print("""
----------------------------------------------

Identity Operators

Example:
""")

result = number is numbers
print("Number '{number}' equals to numbers '{list}'. Answer: {result}".format(number=number, list=numbers, result=result))

result = number is not numbers
print("Number '{number}' not equals to numbers '{list}'. Answer: {result}".format(number=number, list=numbers, result=result))


print("""
----------------------------------------------
Operator precedence 

    operator is executed by priority level. 
    List of operator from highest to lowest priority 
    
    
    High
            operator                definition 
            **                      Exponent operator
            ~ + -                   Unary operator e.g. ~logic_state, +positive_number, -negative_number
            * / % //                arithmetic operator 
            + -                     arithmetic operator
            >> <<                   bit shifting operator 
            &                       bit operator
            ^ |                     bit operator 
            <= < > >=               comparison operator
            == !=                   equality operator 
            = %= /= *= **= += -=    assignment operator 
            is is not               identity operator 
            in not in               membership operator
            not or and              logical operator
    Low
    
    
""")