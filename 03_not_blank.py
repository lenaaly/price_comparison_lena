'''



'''

name_list = []

def item_name(question, error_msg):

    response = input(question)

    while response != "xxx" or "":
        name_list.append(response)

        if response == "xxx":
            break

        elif response == "":
            print(error_msg)
        else:
            response = input(question)



item_name("Enter the items name: ",
          "Please enter an item - this cannot be blank")
print(name_list)
print()
