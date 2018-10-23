print("""
----------------------------------------------

EXCEPTION

    definition:

        Exceptions are triggered automatically on errors from your code.
        If exception is not intercepted, python interpreter will crash program and show error.

""")

print("""
----------------------------------------------

HANDLE EXCEPTION

    Capture and resolve an exception to prevent program crash.

Syntax:

    try:
        statements that may raise exception
    except Exception_1:
        handler_1
    except (Exception_2, Exception_3):
        handler_2_and_3
    except Exception_4 as variable:
        handler_4
    except:
        general_handler
    else:
        statements if no exception
    finally:
        statements with or without exception

Example:
""")

numbers = [1, 2, 3]
try:
    index = 0
    print("*FETCH OPERATION*")
    print('list:', numbers)
    print('Fetch number at index {index}:'.format(index=index))
    number = numbers[index]
# except IndexError:
#     print("Encounter index error exception")
# except IndexError as exception:
#     print("Encounter index error exception:", exception)
except Exception as exception:
    print("Encounter generalize exception:", exception)
else:
    print('Result:', number)
finally:
    print('*END OF OPERATION*')

print("""
----------------------------------------------

RAISE AN EXCEPTION


    Inform python interpreter of an error.  Have it go to higher level of your program
    to find an exception handler or crash the program. This is useful because at time lower level
    program can't handle error, but higher level of your program can.





    Signal python interpreter of an existent exception with the following purposes:

    1. Have python interpreter go to higher level of your program
    2. Have python interpreter find an exception handler or crash the program
    3. Benefits of 1 and 2, in certain cases lower level of your program can't handle an error, but higher
       level or your program can.
    4. Similar to 3, but there isn't any error to handle, whereas you want to provide outcome or status to
       other higher level of your program for reference.

    -A way to tell python interpreter that you can't handle a task and assume
        that higher level of your program can.
        -Indicate to python interpreter with your incapability to handle an unusual outcome of a task
        and assume that higher level of your program will handle it.
        A way to provide a status of a task to higher level of your program.
Syntax:

    raise Exception("message")

Example:
""")
print('raise Exception("Testing exception")')
#raise Exception("Testing exception")


print("""
----------------------------------------------

EXCEPTION CAUGHT BY PYTHON INTERPRETER

    After an exception is raised, python interpreter navigates to higher level of
    your program to find an exception handler. If no handler is found, python interpreter
    will crash program.

Example:
""")
print('divide_by_zero = 8 / 0')
# divide_by_zero = 8 / 0






print("""
----------------------------------------------

ASSERT

        Check assumptions made by programmer before executing code that follows.
        Assert raise an exception if assumption made is false.

    purpose:

        A debug method used at the start of a function to validate inputs.
        A debug method used at the start of a large code.

Syntax:

    A) assert test
    B) assert test, data

Note:

A) If test is false, signal an assert exception.
B) Same as A. In addition, print an error message.

Example:
""")
x = 8
assert x != 0, "divide by zero error"
y = 5 / x
print('result:', y)




with open(r'C:\misc\data') as myfile:
    for line in myfile:
        print(line)