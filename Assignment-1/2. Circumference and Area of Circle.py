#Problem-2. An algorithm that gets the radius r of a circle as input. Its output is both the circumference and the area of a circle of radius r.

r = float(input("The radius is : "))
pi = 3.14159

circumference = 2*pi*r
print("The circumference is : ",circumference)

area = pi*(r**2)
print("The area is : ",area)