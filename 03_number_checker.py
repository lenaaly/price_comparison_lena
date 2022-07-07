'''

v1 - checks that the number is a whole number

'''
def num_checker(question):
    response = input(question)
    error = "Please enter a valid number: "
    if response != type(int):
        return response
        print("Please enter a valid number")

    else:
        print("Your budget is ${:.2f}".format(response))



num_checker("What is your budget? ")

