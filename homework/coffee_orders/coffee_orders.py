from orders import coffee_list


def display(coffee_list):
    print("Order List :")
    print("------------")
    for order in coffee_list:
        for key, value in order.items():
            print(key, " : ", value)
def display_Large(coffee_list):
    print("Order List Of Large Coffee:")
    for order in coffee_list:
       if order["size"] == "Large":
           print(order["name"])


def format_order(order):
    name = order["name"]
    coffee_type = order["coffee_type"]
    size = order["size"]
    return [name, coffee_type, size]



display(coffee_list)
print()
display_Large(coffee_list)


