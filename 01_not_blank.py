'''

v1 -

'''

name_list = []

def not_blank(question, error_msg):
    response = input(question)

    while response != "xxx":
        name_list.append(response)

        if response == "xxx":
            return response
        else:
            response = input(question)



not_blank( "Enter the items name: ", "This cannot be blank")
