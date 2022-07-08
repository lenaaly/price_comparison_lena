"""
Lena Aly 2022

This is the base component - the program takes the users budget and
recommends which items are at the best value for money, based on the weight and
price of the item. Then the program returns the best recommended item within the users budget

base v1 - skeleton of program, setting up functions

base v2 - setting up of item name function and its main routine
        - setting up of num checker function and also its main routine

"""

# setup functions****

#item_info = [[name_list], [price_list], [weight_list]]

# item name function, will take the item name and append it to a list
def item_name(question):

    response = input(question)

    while response != "xxx":
        name_list.append(response)

        if response == "xxx":
            break
        else:
            response = input(question)

# item price function, will take the item price and append it to a list

# item weight function, will take the item weight and append it to a list

# weight g to kg converting function, changes the appended weights from g to kg

# budget function, will ask the user for the budget and store it in a variable
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
    print()


#  **** MAIN ROUTINE ****

# asking the user what their budget is
num_checker("What is your budget? ")

# asking the user the names of their items
name_list = []
item_name("Enter the items name: ")
print(name_list)

