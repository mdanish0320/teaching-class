# why function is needed
# code organation and remove code repetition

order_1_item_1 = "laptop"
order_1_destination = "China"

if order_1_destination == "New York":
    shipment_price = 10
elif order_1_destination == "California":
    shipment_price = 20
elif order_1_destination == "China":
    shipment_price = 30
print(shipment_price)


order_1_destination = "New York"

if order_1_destination == "New York":
    shipment_price = 10
elif order_1_destination == "California":
    shipment_price = 20
elif order_1_destination == "China":
    shipment_price = 30
print(shipment_price)


order_1_destination = "China"

if order_1_destination == "New York":
    shipment_price = 10
elif order_1_destination == "California":
    shipment_price = 20
elif order_1_destination == "China":
    shipment_price = 30
print(shipment_price)


# solution: use function
def get_shipping_price(order_destination):
    if order_destination == "New York":
        shipment_price = 10
    elif order_destination == "California":
        shipment_price = 20
    elif order_destination == "China":
        shipment_price = 30
    print(shipment_price)

get_shipping_price("New York")
get_shipping_price("California")
get_shipping_price("China")
   

# why do we need to return the value out of the function
# because we have other functions i.e 
# get_total_amount(orders)
# calculate_shipment_rate(location)
# calculate_discount(total_amount)
# final_amount = discounted_amount + shipment_rate
# calculate_tax_based_on_currency(final_amount, "dollar")



# class task
# here x_1 and y_1 are called parameters
def multiply(x_1, y_1):
    print(x_1 * y_1)
   
x = 2
y = 5

# here x and y are called arugments
multiply(x, y)


# multiple arguments of the function
x = 5
y = 5

def do_sum(*abc):
   print(abc)
    

do_sum(1, 2, 3, 4, 5,6 ,7 ,8)