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
        while True:
            print("Select a strategy for finding prime numbers:")
            for i, alg_name in enumerate(self.registered_algorithms.values()):
                print(f"{i + 1}. {alg_name}")
            choice = input(f"Enter the strategy number: ")

            try:
                alg_num = int(choice)
                alg_key = list(self.registered_algorithms.keys())[alg_num - 1]
                break
            except (ValueError, IndexError):
                print("Invalid choice. Please try again.")

        while True:
            try:
                n = int(input("Enter the upper bound for generating primes: "))
                self.primeClass = self.primeClass = eval(f"{alg_key}({2}, {n})")
                print("Computing...") 
                prime = self.primeClass.get_primes()
                print("Prime numbers:", prime)
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
