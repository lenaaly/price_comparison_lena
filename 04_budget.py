"""

budget function v1 - starting with a simple def of budget and making the program
work for asking the user their budget.

v1.1 - making sure the budget entered is an integer between 0-100
"""

def num_checker(question):
    error = "Please enter a valid number: "

    valid = False
    while not valid:
        try:
            budget = int(input(question))

            if budget <= 0:
                return budget
                print(error)
            else:
                print()
                print("Your budget is ${:.2f}".format(budget))
                break

        except ValueError:
            print(error)




num_checker("What is your budget? ")


