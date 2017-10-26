#Max Low
#10-26-17
#recursionDemo.py -- a recurssive version of countdown function

def countdown(n):
    if n ==0:
        print('Boom!')
    else:
        print(n)
        countdown(n-1)
countdown(5)
