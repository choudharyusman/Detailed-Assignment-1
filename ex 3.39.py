print("Ex 3.39")

def collision(x1,y1,r1,x2,y2,r2):
    import math
    radius_sum = r1+r2
    radius_diff= r1-r2
    distance_centre = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    if distance_centre >= radius_diff and distance_centre <= radius_sum:
        print("They collide!")
    else:
        print("They dont collide!")




x1 = eval(input("Please enter the x coordinate of Circle 1:"))
y1 = eval(input("Please enter the y coordinate of Circle 1:"))
r1 = eval(input("Please enter the radius of Circle 1      :"))
x2 = eval(input("Please enter the x coordinate of Circle 2:"))
y2 = eval(input("Please enter the y coordinate of Circle 2:"))
r2 = eval(input("Please enter the radius of Circle 2      :"))

collision(x1,y1,r1,x2,y2,r2)
