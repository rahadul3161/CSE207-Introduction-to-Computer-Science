#Problem-4. An algorithm that inputs your current credit card balance, the total dollar amount of new purchases, and the total dollar amount of all payments. The algorithm computes the new balance, which includes a 12% interest charge on any unpaid balance.

current_balance = float(input("Enter current credit card balance: "))
new_purchases = float(input("Enter total dollar amount of new purchases: "))
total_payments = float(input("Enter total dollar amount of all payments: "))

unpaid_balance = current_balance + new_purchases - total_payments
interest_charge = unpaid_balance*0.12
new_balance = unpaid_balance + interest_charge
print("New Balance:", new_balance)