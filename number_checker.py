'''

v1 - checks that the number is a whole number

'''

def int_checker(question):
     error = "Please enter a number between 0 and 10"
     response = input(question)
     print("Your budget is $", response)

     valid = False

     while response == False:
         return error

amount = int_checker("What is your budget? ")
