'''

v1 - checks that the number is a whole number

'''

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


