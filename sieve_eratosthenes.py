import math

def sieve_of_eratosthones(n):
    prime_map = [False, False] + [True] * (n - 1)
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if prime_map[i]:
            j = i * i
            k = 1
            while j <= n:
                prime_map[j] = False
                j = i * i + k*i
                k += 1
                
    prime = []
    for i in range(len(prime_map)):
        if prime_map[i] == True:
            prime.append(i)
    
    print(*prime)

sieve_of_eratosthones(20)