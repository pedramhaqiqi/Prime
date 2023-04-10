from abc import ABC, abstractmethod

class PrimeStrategy(ABC):
    
    strategy_name: str
    start: int
    end: int
    prime_map: list
    
    @abstractmethod
    def get_primes() -> list:
        """Base method to implement for subclasses strategy

        Returns:
            list: list of primes numbers up until n
        """
        pass

    
    @abstractmethod
    def get_biggest_prime() -> list:
        """Base method to implement for subclasses strategy

        Returns:
            list: list of primes numbers up until n
        """
        pass
    
    def __init__(self, start: int, end: int):
        self.prime_map = [False, False] + [True] * (end - 1)
        if start < 2:
            raise ValueError("`start` must be more than 1")
        self.start = start
        self.end = end