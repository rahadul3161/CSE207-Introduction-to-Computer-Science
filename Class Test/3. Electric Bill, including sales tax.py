#Q3. An algorithm that gets the amount of electricity used in kilowatthours and the cost of electricity per kilowatt-hour. Its output is the total amount of the electric bill, including an 8% sales tax.

electricity_used = float(input("Electricity used in kilowatt-hour: "))
cost_per_kwh = float(input("Cost of electricity per kilowatt-hour: "))

electricity_cost = electricity_used * cost_per_kwh
sales_tax = 0.08 * electricity_cost

total_bill = electricity_cost + sales_tax
print("Total electric bill: ", total_bill) 