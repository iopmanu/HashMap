from linkedlist import LinkedList
from dynamic_array import DynamicArray

def hash_function(key: str) -> int:
    hash = 0
    for symbol, index in zip(key, range(len(key))):
        hash += (index + 1) * ord(symbol)
    return hash

class HashMap:
    def __init__(self, capacity=11, hf=hash_function) -> None:
        if not isinstance(capacity, int) or capacity <= 0:
            raise TypeError("Size must be a positive number")
                
        self._buckets = DynamicArray()
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())
        
        self._hash_function = hf
        self._size = 0
    
    def __str__(self) -> str:
        out = ''
        for i in range(len(self._buckets)):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def __len__(self) -> int:
        return self._size

    def __get_item__(self, key):
        pass

    @staticmethod
    def _is_prime(capacity) -> bool:
        if capacity == 2 or capacity == 3:
            return True
        elif capacity == 1 or capacity % 2 == 0:
            return False
        
        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2
        
        return True

    def _next_prime(self, capacity) -> int:
        if capacity % 2 == 0:
            capacity += 1
        
        while not self._is_prime(capacity):
            capacity += 2
            print(self._is_prime(capacity))

        return capacity

    @property
    def get_size(self):
        return self._size

    @property
    def get_capacity(self):
        return self._capacity
    
    @property
    def load_factor(self):
        return self._size / self._capacity