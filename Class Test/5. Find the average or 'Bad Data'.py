#Q5 Write an algorithm that gets as input three data values x, y, and z and outputs the average of these values if the value of x is positive. If the value of x is either 0 or negative, your algorithm should not compute the average but should print the error message ‘Bad Data’ instead.

x=float(input("Enter 1st value: "))
y=float(input("Enter 2nd value: "))
z=float(input("Enter 2rd value: "))

if x>0:
    average=(x+y+z)/3
    print("Average is: ",average)
else:
    print("Bad Data")

