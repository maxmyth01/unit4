#Max Low
#10-16-17
#functionDemo.py -- learning functions

def hw():
    print('Hello, World!')

hw() # actually runs the function
hw()

def bigger(num1, num2): # prints which number is bigger
    if num1 > num2:
        print(num1)
    else:
        print(num2)
        
bigger(13, 27)
bigger(-10, -15)
bigger('Smeds', 'Low')

def slope(x1, y1, x2, y2): # Calculate slope
    print((y2-y1)/(x2-x1))

slope(1,2,2,4)
