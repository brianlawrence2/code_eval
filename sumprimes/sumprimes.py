from math import sqrt, floor

def isprime(n):
    
    if n == 2 or n == 3:
        return True
    elif n == 0 or n ==1:
        return False
        
    for i in range(floor(sqrt(n)) + 1):
        if i == 0 or i == 1:
            pass
        elif n % i == 0:
            return False
            
    return True
    
def sumprimes(n):
    prime_sum = 0
    num_primes = 0
    count = 0
    more_primes = True
    while more_primes:
        if num_primes >= n:
            more_primes = False
            
        if isprime(count):
            prime_sum += count
            num_primes += 1
        
        count += 1

    return prime_sum
    
if __name__ == '__main__':
    print(sumprimes(1000))