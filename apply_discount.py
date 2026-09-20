def apply_discount(price , discount):
    if not isinstance(price, (int , float)):
        print("The price should be a number")
        return
    if not isinstance(discount, (int , float)):
        print("The discount should be a number")
        return
    if price <= 0:
        print("The price should be greater than 0")
        return
    if 0 > discount < 100 :
        print("The discount should be between 0 and 100")
        return
    print(price - ((price*discount)/100))

apply_discount(50,-5)
