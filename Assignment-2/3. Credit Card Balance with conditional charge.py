#Problem-3. Write an algorithm that gets as input your current credit card balance, the total dollar amount of new purchases, and the total dollar amount of all payments. The algorithm computes the new balance, which this time includes an 8% interest charge on any unpaid balance below $100, 12% interest on any unpaid balance between $100 and $500, inclusive, and 16% on any unpaid balance above $500.
       
current_balance = float(input("Current credit card balance: "))
new_purchases = float(input("Total amount of new purchases: "))
total_payments = float(input("Total amount of all payments: "))

unpaid_balance = (current_balance+total_payments)-new_purchases
if unpaid_balance<100:
    interest_charge = unpaid_balance*.08
elif unpaid_balance<=500:
    interest_charge = unpaid_balance*.12
else:
    interest_charge = (unpaid_balance*.16)
    
new_balance = unpaid_balance+interest_charge
print("The new balance is: ",new_balance)