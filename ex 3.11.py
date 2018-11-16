print('Problem 3.11')
#returns true if all integers even, else false
def allEven(x):
    for yyy in x:
        if yyy % 2==0:
            return 'true'
        else:
            return 'false'
x=[]
integers= int(input('Enter int 1: '))
x.append(integers)
integers1= int(input('Enter int 2: '))
x.append(integers1)
integers2= int(input('Enter int 3: '))
x.append(integers2)
print(str(x) + ' ' + str(allEven(x)))
