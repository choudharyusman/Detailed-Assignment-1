print("ex 3.37")

lst=[]
import math
def points(x1,x2,y1,y2):
    slope_line= (y2-y1)/(x2-x1)
    dist_co= math.sqrt(((x2-x1)**2)+(y2-y1)**2)
    if x2-x1!=0:
        print("The slope of the line is: " + str(slope_line) +" and the distance between the two points is: " +str(dist_co))
    if x2-x1==0:
        print("The slope is infinite and the distance is: " + str(dist_co))


x1=int(input("Enter co-ordinate x1: "))
x2=int(input("Enter co-ordinate x2: "))
y1=int(input("Enter co-ordinate y1: "))
y2=int(input("Enter co-ordinate y2: "))
print(points(x1,x2,y1,y2))

        
