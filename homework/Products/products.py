from products_list import products


def display(products):
    in_stock_list=[]
    for product in products:
        if product["in_stock"]==True:
           placeholder=[product["name"],product["price"]]
           in_stock_list.append(placeholder)
    return in_stock_list

in_stock_list = display(products)
total=0
for product in in_stock_list:
    print(product[0],":",product[1])
    total=total+product[1]
print()
print(total)


