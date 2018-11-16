print("Ex 3.25")

user_lst=[]
for x in range(5):
    a= input("Please enter student" + str(x+1)+ " Name:")
    user_lst.append(a)
for x in range(5):
    if user_lst[x][:1] in ('a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'):
        print(user_lst[x])

