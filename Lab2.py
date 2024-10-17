#Input
var_1 = input("Enter the amount of your first purchase:")
var_2 = input("Enter the amount of your second purchase:")
var_3 = input("Enter the amount of your third purchase:")
total = float(var_1) + float(var_2) + float(var_3)
print("Total Purchased:",total)

#For Discount
if total >= 100:
    discount = total *0.1
    updated_total = total-discount
    print("You are qualified for a discount!")
    print("Updated total:",updated_total)

else:
    updated_total=total
    print("Discount cannot be availed. Total remains",updated_total)
    
#For Loyalty Points
loyalty_points = updated_total *0.1
print("Loyalty Points Earned:",loyalty_points)
payment = float(input("Enter your payment:"))

if payment>=updated_total:
    change=payment-updated_total
    print("change:",change)
    
else:
    print("Payment Failed")
    


