#Max Low
#10-23-17
#trangle.py -- uses 3 pt to determine area

def distance(x1,y1,x2,y2):
    print(((x2-x1)**2+(y2-y1)**2)**0.5)
    

def area(x1,y1,x2,y2,x3,y3):
    a = distance(x1,y1,x2,y2)
    b = distance(x2,y2,x3,y3)
    c = distance(x3,y3,x1,y1)
    s = 0.5*(a+b+c)
    return((s*(s-a)*(s-b)*(s-c))**0.5)


print(area(3,4,-5,2,-7,1))
