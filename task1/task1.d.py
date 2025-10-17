import math
def calculate_dis(x1,y1,x2,y2):
    distance=math.sqrt((x2-x1)**2+(y2-y2)**2)
    return distance
x_ram=float(input("Enter the x-coordinate of Ram : "))
y_ram=float(input("Enter the y-coordinate of Ram : "))
x_sita=float(input("Enter the x-coordinate of sita : "))
y_sita=float(input("Enter the y-coordinate of sita : "))
distance=calculate_dis(x_ram,y_ram,x_sita,y_sita)
print(f"The distanc between them is : {distance:.2f}")
