'''



'''

def not_blank(question, error_msg):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_msg)



item_name = not_blank("Please enter the items name: ",
                      "This cannot be blank - " 
                      "Please enter the items name: ")
