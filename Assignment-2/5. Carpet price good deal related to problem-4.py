#Problem-5. Add the following feature to the algorithm created in the Practice Problem-5: If the cost of the carpet is less than or equal to $250, output a message that this is a particularly good deal.

length = float(input("The value of length: "))
width = float(input("The value of width: "))
price_per_square_yard= float(input("The cost per yard: "))

area = (length*width)/9
cost = area*price_per_square_yard

if cost<=250:
    print("This is a particularly good deal. The total cost is: ",cost)
else:
    print("This is not particularly a good deal.")
