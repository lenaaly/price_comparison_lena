'''

v1 - calculating unit price (unit price = total price / # of units)


'''



def unit_price(total_price, num_units):
    response1 = int(input(total_price))
    response2 = int(input(num_units))

    calculate = response1/response2
    print("Unit price is ${:.2f}".format(calculate))


unit_price("Please enter the total price: ", "Please enter the number of units: ")
