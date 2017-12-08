def apply_discount(amount):
    discount = 10
    final_amount = amount - (amount*discount)/100
    return final_amount

#To take input from users
no_of_prods = int(input("Enter the number of products: "))

bill_amount = (no_of_prods)*30
print("Your bill before discount - ",bill_amount)

final_bill_amount = apply_discount(bill_amount)
print("Your Final bill after discount - ",final_bill_amount)
print("you saved - ",bill_amount - final_bill_amount)
