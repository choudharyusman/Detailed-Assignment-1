print('Ex 3.21')

x=[]
a=int(input('No 1: '))
x.append(a)
b=int(input('No 2: '))
x.append(b)
c=int(input('No 3: '))
x.append(c)
d=int(input('No 4: '))
x.append(d)
e=int(input('No 5: '))
x.append(e)
f=int(input('No 6: '))
x.append(f)
g=int(input('No 7: '))
x.append(g)
for char in x:
    if char %2==0:
        print(char)

