from math import sqrt, floor

def isprime(n):
    for i in range(floor(sqrt(n))):
        if i == 0 or i == 1:
            pass
        elif n % i == 0:
            return False
            
    return True