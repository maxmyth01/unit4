#Max Low
#10-23-17
#warmup11.py -- primes numbers

def isPrime(num):
    x=num - 1
    while x > 1:
        if num % x == 0:
            return(False)
        else:
            x -= 1
    return(True)
    
    
print(isPrime(6))
