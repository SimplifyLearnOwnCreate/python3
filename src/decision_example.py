"""
    Flow control/ Decision making
"""

print("""
----------------------------------------------

if else

    TAKE ACTION BASED ON CONDITION


Syntax:

    if condition1:
        statement(s)

    elif condition2:
        statement(s)

    else:
        statement(s)

where
         statement(s):   line(s) of code

Example:
""")

answer = 'b'

if answer == 'a':
    print("a")
elif answer == 'b':
    print('b')
elif answer == 'c':
    print('c')
else:
    print("not valid")


print("""
----------------------------------------------

BETWEEN RANGE


Syntax:

    if min <= number <= max:
        statements

where
         min, max:       a number
         statement(s):   line(s) of code


Example:
""")

number = 0

if 1 <= number <= 5:
    print("Number '{number}' is between range 1-5.".format(number=number))
else:
    print("out of range")


print("""
----------------------------------------------

ALL CONDITIONS SATISFY


Syntax:

    if condition1 and condition2:
        statement(s)

where
         statement(s):   line(s) of code

Example:
""")

have_passport = False
have_boarding_pass = True

if have_boarding_pass and have_passport:
    print("You can board.")
else:
    print("Come back later.")



print("""
----------------------------------------------

ANY CONDITION IS TRUE


Syntax:

    if condition1 or condition2:
        statement(s)

where
         statement(s):   line(s) of code

Example:
""")



have_passport = False
have_boarding_pass = False

if have_boarding_pass or have_passport:
    print("You can board.")
else:
    print("Come back later.")


print("""
----------------------------------------------

ITEM IS IN LIST


Syntax:

    if item in list:
        statement(s)

where
         statement(s):   line(s) of code

Example:
""")


menu = ['hot dog', 'fried']

if 'pizza' in menu:
    print('pizza is in the menu')
else:
    print('pizza is not in the menu')



