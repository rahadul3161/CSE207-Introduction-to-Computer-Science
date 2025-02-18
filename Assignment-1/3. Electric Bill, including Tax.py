#Problem-3. An algorithm that gets the amount of electricity used in kilowatt-hours and the cost of electricity per kilowatt-hour. Its output is the total amount of the electric bill, including an 8% sales tax.

electricity_used = float(input("The amount of electricity used : "))
cost_of_electricity = float(input("the cost of electricity kWh : "))

total_cost = electricity_used*cost_of_electricity
total_electric_bill = total_cost+(total_cost*0.08)
print("The total amount of the electric bill",total_electric_bill)