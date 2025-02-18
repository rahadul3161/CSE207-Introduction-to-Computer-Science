#Problem-6. An algorithm that is given three numbers corresponding to the number of times a race car driver has finished first, second, and third. The algorithm computes and displays how many points that driver has earned given 5 points for a first, 3 points for a second, and 1 point for a third place finish.

frist = float(input("Enter how many times has the person won first place: "))
second = float(input("Enter how many times has the person won second place: "))
third = float(input("Enter how many times has the person won third place: "))

total_point = frist*5+second*3+third*1
print("Total point the driver has earned: ",total_point)
