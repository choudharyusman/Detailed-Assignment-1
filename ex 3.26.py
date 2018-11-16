print("ex 3.26")

lst=[]
for x in range(5):
    y=input("Enter int" +str(x+1)+ ": ")
    lst.append(x)
for x in range(5):
    print("The first element is: " + str(lst[0]))
    print("The last element is: " + str(lst[4]))
