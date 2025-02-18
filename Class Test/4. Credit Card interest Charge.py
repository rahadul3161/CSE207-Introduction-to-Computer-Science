#Q4 An algorithm that inputs your current credit card balance, the total dollar amount of new purchases, and the total dollar amount of all payments. The algorithm computes the new balance, which includes a 12% interest charge on any unpaid balance.

current_credit_card_balance = float(input("Enter the current credit card balance: "))
total_amount_of_new_purchases = float(input("Enter the total dollar amount of new purchases: "))
total_amount_of_all_payments = float(input("Enter the total dollar amount of all payments: "))

unpaid_balance=current_credit_card_balance+total_amount_of_new_purchases-total_amount_of_all_payments
interest_charge=unpaid_balance*0.12
new_balance= unpaid_balance+interest_charge

print("New balance with charge: ",new_balance)