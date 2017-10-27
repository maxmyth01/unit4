#Max Low
#10-27-17
#warmup12.py -- take two numbers and find the GCF

def GCF(num1,num2):
    x = min(num1,num2)
    for i in range(x):
        if min(num1,num2) % x == 0:
            return x
        else:
            x -= 1
            
print(GCF(10,15))
        
    
