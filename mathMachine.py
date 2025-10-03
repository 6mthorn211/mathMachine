
global slope

#Getting coords from user
def get_coordinates():
    global x1, x2, y1, y2
    while True:
        user_input1 = float(input("Enter the first set of coordinates in the format (x,y): "))
        user_input2 = float(input("Enter the second set of coordinates in the format (x,y): "))
        try:
            x1, y1 = user_input1.strip('()').split(',')
            x2, y2 = user_input2.strip('()').split(',')
            return x1, y1, x2, y2
        except ValueError:
            print("Invalid format. Please enter coordinates like (x,y). ")

#Defining equations
def calculate_slope(x1, y1, x2, y2):
    return (y2-y1) / (x2-x1)

def point_slope_form(x, x1, y1, slope):
    return (x-x1) + y1

def midpoint (x1, y1, x2, y2):
    return (x1+x2)/2, (y1+y2)/2

#Displaying equations
print ("1 - Slope from 2 points\n2 - Point slope form\n3 - Midpoint formula ")
eq_type = int(input("Which type of equation would you like to solve? "))

#Deciding which formula to use
if eq_type == 1:
    print (f"Slope: {calculate_slope(x1, y1, x2, y2)}")
elif eq_type == 2:
    slope = calculate_slope(x1, y1, x2, y2)
    print(f"y = {point_slope_form(1, x1, y1, slope)}")
elif eq_type == 3:
    print(f"Midpoint: {midpoint(x1, y1, x2, y2)}")
