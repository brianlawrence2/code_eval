from math import sqrt, floor

def isprime(n):
    for i in range(floor(sqrt(n))):
        if i == 0 or i == 1:
            pass
        elif n % i == 0:
            return False
    
    return True
    
def ispal(n):
    n_str = str(n)
    n_rev = n_str[::-1]
    
    if n_str == n_rev:
        return True
    else:
        return False
        
def largest_prime_pal(n):
    largest_prime = 0
    for i in range(n):
        if isprime(i) and ispal(i):
            largest_prime = i
    
    return largest_prime
    
def time_wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
        
    return wrapped

if __name__ == '__main__':
    import timeit
    
    wrapped = time_wrapper(largest_prime_pal, 1000)
    print(timeit.timeit(wrapped, number=100))