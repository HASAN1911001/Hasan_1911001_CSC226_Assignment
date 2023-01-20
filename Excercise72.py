"""------------------------------------------------------------------------------
Exercise 7.2.
The built-in function eval takes a string and evaluates it using the Python
interpreter. For example:

>>> eval('1 + 2 * 3')
7
>>> import math
>>> eval('math.sqrt(5)')
2.2360679774997898
>>> eval('type(math.pi)')
<class 'float'>

Write a function called eval_loop that iteratively prompts the user, takes the
resulting input and evaluates it using eval, and prints the result.
It should continue until the user enters 'done', and then return the value of
the last expression it evaluated.
---------------------------------------------------------------------------------"""
import math
def eval_loop():
    while True:
        user_input = input(">>> ")
        
        if user_input == 'done':  
            break
        print(eval(user_input))
        last_input = user_input

    return eval(last_input)

eval_loop()