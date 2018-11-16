print('a')
age= int(input('Enter your age:'))
if age > 62:
    print('You can get your pension benefits')

print('b')
name= input('Enter your name')
lst= ['Musial' , 'Aaraon' , 'Williams' , 'Gehrig' , 'Ruth' ]
if name in lst:
    print('One of the top 5 baseball players ever!')

print('c')
hits= int(input('Enter no of hits'))
if hits >10:
    print('hold on a second')
shield= int(input('Enter no of shields'))
if shield == 0:
    print('You are dead')
print('d')
direction= input('Enter your direction')
lst_1= ['north', 'south', 'esst', 'west']
if direction in lst_1:
    print('I can escape')
print('3.3, B')
ticket_no= (input('Enter your ticket number'))
lottery_lst= ['007', '008', '009', '010']
if ticket_no in lottery_lst:
    print('You won')
else:
    print('Better luck next time')
print('3.4')
login_username= input('Enter your username id')
login_lst= ['joe', 'sue', 'hani', 'sophie']
if login_username in login_lst:
    print('login:' + str(login_username))
    print('You are in!')
else:
    print('login:' + str(login_username))
    print('User unknown')
print('done')

print('3.5')
lst_words=[]
word=input('please enter a word:')
lst_words.append(word)
word=input('please enter a word:')
lst_words.append(word)
word=input('please enter a word:')
lst_words.append(word)

print('the four letter words are')
for x in lst_words:
    if len(x)==4:
        print(x)
 
print('3.6')
print('This program will run integers 0-9')
for c in range(10):
    print(c)
    
print('3.6, B')
print('This program will run integers 0 and 1')
for v in range(2):
    print(v)
    
print('3.7')
for d in range(3,13):
    print(d)
    
print('3.7,b')
for u in range(0,9,2):
    print(u)
    
print('3.7,c')
for e in range(0,24,3):
    print(e)
    
print('3.7,d')
for o in range(3,12,5):
    print(o)
