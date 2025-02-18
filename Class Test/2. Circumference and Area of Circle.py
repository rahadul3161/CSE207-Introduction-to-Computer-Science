#Q2. An algorithm to get both the circumference and the area of a circle.

import math
radius=float(input("Enter the value of radius: "))
circumference = 2*math.pi*radius
print("The value of Circumference of the circle is: ",circumference)
area=math.pi*radius**2
print("The value of Area of the circle is: ",area)

