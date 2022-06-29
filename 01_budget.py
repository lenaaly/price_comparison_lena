"""

budget function v1 - starting with a simple def of budget and making the program
work for asking the user their budget.

v1.1 - making sure the budget entered is an integer between 0-100
"""

def budget(question, error_msg):

    valid = False
    while not valid:
        response = int(input(question))
        print("Your budget is ${:.2f}".format(response))

        if response 'valid':
            return response
        else:
            print("The input was not a valid integer.")



budget("What is your budget? ", "Please enter a valid integer: ")




