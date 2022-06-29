"""
item name v1 - starting with a simple def of item_name and making the program
work for asking the user the items name more than once


"""
name_list = []

def item_name(question):

    response = input(question)

    while response != "xxx":
        name_list.append(response)

        if response == "xxx":
            break
        else:
            response = input(question)



item_name("Enter the items name: ")
print(name_list)
print()


