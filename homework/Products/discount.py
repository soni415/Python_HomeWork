from products_list import products

def discount(products):
    length=len(products)
    print("Enter a number from 0 to ",length-1," to apply the product")
    count=0
    for product in products:
        print(product["name"]," : ",count)
        count=count+1
    index=int(input("enter product: "))

    discount=input("Enter discount from 0 to 1: ")

    final_price=products[index]["price"]*float(discount)
    print(final_price)

discount(products)