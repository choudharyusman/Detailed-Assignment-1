print("Ex 3.24")

x=[]
a=input("Enter word 1: ")
x.append(a)
b=input("Enter word 2: ")
x.append(b)
c=input("Enter word 3: ")
x.append(c)
d=input("Enter word 4: ")
x.append(d)
e=input("Enter word 5: ")
x.append(e)

for char in x:
    if char=='secret':
        break
    else:
        print(char)
