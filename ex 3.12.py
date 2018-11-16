print('problem 3.12')
#take list of negatives and print one per line

def negatives():
    for char in x:
        if char <0:
            print(char)
x=[]
neg1= int(input('Enter int 1: '))
x.append(neg1)
neg2= int(input('Enter int 2: '))
x.append(neg2)
neg3= int(input('Enter int 3: '))
x.append(neg3)
neg4= int(input('Enter int 4: '))
x.append(neg4)
neg5= int(input('Enter int 5: '))
x.append(neg5)
print(negatives())

