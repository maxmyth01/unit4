#Max Low
#10-23-17
#multiply.py -- rand in 1-12 encourgaing message at 5 right

from random import randint

def encouraging():
    from random import randint
    x = randint(1,4)
    if x== 1:
        print('Great Job!')
    elif x==2:
        print('Keep it up!')
    elif x==3:
        print('Nice multiplying!')
    elif x==4:
        print('Nice work!')
    

x=0
while x<5:
    
    rand1 = randint(1,12)
    rand2 = randint(1,12)
    
    answer = intput('What is',rand1,'*',rand2,'?')
    if answer == rand1*rand2:
        x += 5
    else:
        print('Incorrect, Try Again.')
