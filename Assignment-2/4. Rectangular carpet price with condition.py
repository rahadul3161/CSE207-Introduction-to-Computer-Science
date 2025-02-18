#Problem-4. Write an algorithm that inputs the length and width, in feet, of a rectangular carpet and the price of the carpet in dollars per square yard. It then determines if you can afford to purchase this carpet, given that your total budget for carpeting is $500.

length = float(input("The value of length: "))
width = float(input("The value of width: "))
price_per_square_yard= float(input("The cost per yard: "))

area = (length*width)/9
cost = area*price_per_square_yard

if cost<=500:
    print("You can afford to purchase this carpet. The total cost is: ",cost)
else:
    print("You can't afford to purchase this carpet. The total cost is: ",cost)

