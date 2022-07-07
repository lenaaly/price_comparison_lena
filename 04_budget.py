"""

budget function v1 - starting with a simple def of budget and making the program
work for asking the user their budget.

v1.1 - making sure the budget entered is an integer between 0-100
"""

def budget(question, error_msg):
    response = int(input(question))

    valid = False
    while not valid:
        return(response)
        print("Your budget is ${:.2f}".format(response))



budget("What is your budget? ", "Please enter a valid integer: ")




