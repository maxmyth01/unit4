#Max Low
#10-18-17
#printSquares -- row then colums 

def square(row,column):
    for i in range(0,column):    
        print('+--'*row,'+')
        print('|  '*row,'|')
    print('+--'*row,'+')
        
        
        
square(4,3)

square(5,7)

square(10,2)
    