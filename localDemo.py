#Max Low
#10-23-17
#localDemo.py -- understanding local varibles

def f():
    x=77 # x is a local varible
    y=10 # y is also a local varible


x=5
f() # x doesn't change
print(x)
print(y) # this will cause an error

