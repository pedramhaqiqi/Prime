import math
from src.strategy.base import PrimeStrategy

class SieveOfEratosthenes(PrimeStrategy):   
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_primes(self):
        n = self.end
        for i in range(self.start, math.floor(math.sqrt(n)) + 1):
            if self.prime_map[i]:
                j = i * i
                k = 1
                while j <= n:
                    self.prime_map[j] = False
                    j = i * i + k*i
                    k += 1
                    
        prime = []
        for i in range(len(self.prime_map)):
            if self.prime_map[i] == True:
                prime.append(i)
        
        return prime
    
    def get_biggest_prime() -> list:
        #!Todo: Implement get biggest primes
        return super().get_biggest_prime()

