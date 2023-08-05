def divide(x, y):
    try:

        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:

        print("Sorry ! you are dividing by zero")


"""Else Clause
The code enters the else block only if the try clause does not raise an exception.

Example: Else block will execute only when no exception occurs."""


def divide_else(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)


"""Finally Keyword
Python provides a keyword finally, which is always executed after try and except blocks. 
The finally block always executes after normal termination of try block or after try block terminates due to some exception. 
Even if you return in the except block still the finally block will execute"""


def divide_final(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)

    finally:
        print('This is always executed')


# Look at parameters and note the working of Program

# divide(3, 2)
# divide(3, 0)

# divide_else(3, 2)
# divide_else(3, 0)

divide_final(3, 2)
divide_final(3, 0)
