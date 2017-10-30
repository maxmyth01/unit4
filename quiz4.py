#Max Low
#10-30-17
#quiz4.py -- csia funtion, average function, string last letter function, true/false arguments same function

def csia():
    for x in range(0,5):
        print("Computer Science is Awesome")

def average(num1,num2,num3):
    return (num1+num2+num3)/3

def lastLetter(word):
    x=0
    y=0
    for ch in word:
        x += 1
    for ch in word:
        y +=1
        if y==x:
            print(ch)
            
def same(x,y):
    if x == y:
        return True
    else:
        return False

csia()
print(average(1,2,3))
lastLetter('Maxwell')
print(same(2*3,7-1))
