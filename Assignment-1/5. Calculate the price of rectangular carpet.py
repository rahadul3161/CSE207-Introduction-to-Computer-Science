#Problem-5. An algorithm that is given the length and width, in feet, of a rectangular carpet and determines its total cost given that the material cost is $23 per square yard.

length=float(input("Enter the length in feet: "))
width=float(input("Enter the width in feet: "))

area_of_carpet_in_yard=(length*width)/3
total_cost=area_of_carpet_in_yard*23
print("The total cost of the rectangular carpet is: ",total_cost)




