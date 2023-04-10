from typing import List
from src.strategy.base import *
from src.strategy.sieve_eratosthenes import *

class PrimeUI:
    primeClass: PrimeStrategy
    
    #For dynamic eval of class, register this dict as dict(<class Name> : <Output Name>)
    registered_algorithms = {
        "SieveOfEratosthenes": "Sieve of Eratosthenes",
    }

    @classmethod
    def run(self):
        def get_strategy():
            while True:
                print("Select a strategy for finding prime numbers:")
                for i, alg_name in enumerate(self.registered_algorithms.values()):
                    print(f"{i + 1}. {alg_name}")
                choice = input(f"Enter the strategy number: ")

                try:
                    alg_num = int(choice)
                    alg_key = list(self.registered_algorithms.keys())[alg_num - 1]
                    break
                except ValueError:
                    print("Invalid choice. Please try again.")
                 
            return alg_key
        
        def get_upper_lower():
            while True:
                try:
                    lower = int(input("Enter the lower bound for generating primes: ")) 
                    upper = int(input("Enter the upper bound for generating primes: "))
                    
                    lower = 2 if lower < 2 else lower
                    if upper < lower:
                        raise ValueError("Try again wrong")
                    break
                except ValueError as verror:
                    print(verror)
            return lower, upper
        
        def get_class_strategy(alg_key: str, lower_bound: int,upper_bound: int):
            self.primeClass = self.primeClass = eval(f"{alg_key}({lower_bound}, {upper_bound})")
            
        def get_result():
            print("Computing........")
            print(f"Primes from {self.primeClass.start} to {self.primeClass.end}: {self.primeClass.get_primes()}")
        
        get_class_strategy(get_strategy(), *get_upper_lower())
        get_result()

            
