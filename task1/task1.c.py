import math
def calculate_area_in_acres(radius_in_feet):
    area_in_acres=math.pi*(radius_in_feet**2)/435600
    return area_in_acres
radius_in_feet=float(input("Enter the radius of the field in feet: "))
area_in_acres=calculate_area_in_acres(radius_in_feet)
print(f"The area of the field is : {area_in_acres:.2f} acres")               
