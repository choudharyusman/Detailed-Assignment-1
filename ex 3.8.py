print("Problem 3.8")
#perimeter of circle= 2*pi*r
import math
def perimeter(x):
    res= 2* math.pi* x
    return res
x= int(input('Enter Radius of circle: '))
if x <=0:
    print('Good bye!')
else:
    print('The perimeter of cirlce with radius: ' + str(x)+ ' ' + 'is' + str(perimeter(x)))

