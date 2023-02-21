from .linkedlist import LinkedList
from .dynamic_array import DynamicArray
from typing import Any

INIT_CAPACITY = 11
LOAD_FACTOR_BOUNDARY = 0.75
KEY = 0
VALUE = 1

def hash_function(key: str) -> int:
    hash = 0
    for symbol, index in zip(key, range(len(key))):
        hash += (index + 1) * ord(symbol)
    return hash

class HashMap:
    def __init__(self, capacity=INIT_CAPACITY, hf=hash_function) -> None:
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

    def get_item(self, key) -> Any:
        index = (self._hash_function(key)) % self._capacity

        if self._buckets[index].contains(key) is not None:
            return self._buckets[index].contains(key)

    def insert(self, key: Any, value: Any) -> None:
        index = (self._hash_function(key)) % self._capacity
        bucket = self._buckets[index]

        if (self.load_factor >= LOAD_FACTOR_BOUNDARY):
            new_capacity = self._capacity * 2
            self._resize_table(new_capacity)

        if len(bucket) == 0:
            bucket.append([key, value])
        else:
            for pair in bucket:
                if pair[KEY] == key:
                    pair[VALUE] = value
                    return
            
            bucket.append([key, value])

        self._size += 1
    
    def contains_key(self, key: Any) -> bool:
        index = (self._hash_function(key)) % self._capacity
        node = self._buckets[index].contains(key)

        return bool(node)
    
    def remove(self, key: Any) -> None:
        index = (self._hash_function(key)) % self._capacity
        
        if self.contains_key(key):
            position = 0

            for value in self._buckets[index]:
                if value[KEY] == key:
                    self._buckets[index].erase(position)
                position += 1
            
            self._size -= 1
    
    def _resize_table(self, new_capacity: int) -> None:
        if not self._is_prime(new_capacity):
            new_capacity = self._next_prime(new_capacity)

        new_storage = DynamicArray()
        for i in range(new_capacity):
            new_storage.append(LinkedList())
        keys = LinkedList()
        
        for i in range(self._capacity):
            bucket = self._buckets[i]
            for chain in bucket:
                keys.append([chain[KEY], chain[VALUE]])

        self._buckets = new_storage
        self._capacity = new_capacity
        self._size = 0

        for item in keys:
            self.insert(item[KEY], item[VALUE])

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        if not isinstance(capacity, int):
            raise TypeError("It's impossible to check primary of non-integer arguments")

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

    @classmethod
    def _next_prime(cls, capacity: int) -> int:
        if capacity % 2 == 0:
            capacity += 1
        
        while not cls._is_prime(capacity):
            capacity += 2

        return capacity

    def clear(self) -> None:
        bucket = self._buckets

        for i in range(self._capacity):
            bucket[i].clear()
        
        self._size = 0

    @property
    def get_size(self) -> int:
        return self._size

    @property
    def get_capacity(self) -> int:
        return self._capacity
    
    @property
    def load_factor(self) -> float:
        return self._size / self._capacity

    @property
    def empty_buckets_counts(self) -> int:
        result, bucket = 0, self._buckets

        for i in range(self._capacity):
            if len(bucket[i]) == 0:
                result += 1
            
        return result