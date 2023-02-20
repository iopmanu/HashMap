import pytest
from src.hashmap import *
import math

@pytest.mark.init
def test_empty_hashmap():
    h = HashMap()
    assert(h.get_size == 0)
    assert(h.empty_buckets_counts == INIT_CAPACITY)
    assert(h.load_factor == 0.0)

@pytest.mark.init
def test_insert_hashmap():
    h = HashMap()
    h.insert('Vanya', 1)
    h.insert('MEPhI', 2)
    h.insert('Pizza', 3)
    h.insert('Milk', 4)
    h.insert('News', 5)
    h.insert('Job', 6)
    h.insert('Bob', 7)
    h.insert('Bold Bob', 8)
    h.insert('Data', 9)
    h.insert('Hash', 10)
    h.insert('Maybe', 11)
    h.insert('Auwaw', 12)
    h.insert('Spring', 13)
    h.insert('Analyst', 14)
    h.insert('Key', 15)
    h.insert('Value', 16)
    h.insert('Value', 25)

    assert(math.isclose(h.load_factor, 0.69565217, abs_tol=1e-7))
    assert(h.empty_buckets_counts == 12)
    assert(h.get_size == 16)
    assert(h.get_capacity == 23)

    assert(h.get_item('Vanya') == 1)
    assert(h.get_item('MEPhI') == 2)
    assert(h.get_item('Pizza') == 3)
    assert(h.get_item('Milk') == 4)
    assert(h.get_item('News') == 5)
    assert(h.get_item('Job') == 6)
    assert(h.get_item('Bob') == 7)
    assert(h.get_item('Bold Bob') == 8)
    assert(h.get_item('Data') == 9)
    assert(h.get_item('Maybe') == 11)
    assert(h.get_item('Auwaw') == 12)
    assert(h.get_item('Spring') == 13)
    assert(h.get_item('Analyst') == 14)
    assert(h.get_item('Key') == 15)
    assert(h.get_item('Value') == 25) # 25 Replaced with 16
    assert(h.get_item('Random phrase') is None) # Key ins't in the HashMap

    assert(h.contains_key('Pizza') == True) # chaining with 'Key'
    assert(h.contains_key('Pizza123556') == False) # Key isn't in the HashMap

@pytest.mark.init
def test_remove_hashmap():
    h = HashMap()
    h.insert('Vanya', 1)
    h.insert('MEPhI', 2)
    h.insert('Pizza', 3)
    h.insert('Milk', 4)
    h.insert('News', 5)
    h.insert('Job', 6)
    h.insert('Bob', 7)
    h.insert('Bold Bob', 8)
    h.insert('Data', 9)
    h.insert('Hash', 10)
    h.insert('Maybe', 11)
    h.insert('Auwaw', 12)
    h.insert('Spring', 13)
    h.insert('Analyst', 14)
    h.insert('Key', 15)
    h.insert('Value', 16)
    h.insert('Value', 25)

    h.remove('Value')
    assert(h.get_item('Value') is None)
    assert(h.contains_key('Value') is False)

    h.remove('RandomPhrase')                        # Key ins't in the HashMap
    assert(h.get_item('RandomPhrase') is None)
    assert(h.contains_key('RandomPhrase') == False)

    h.remove('Pizza')                               # Chaining with 'Key'
    assert(h.get_item('Pizza') is None)
    assert(h.contains_key('Pizza') == False)
    assert(h.get_item('Key') == 15)

    assert(h.get_size == 14)
    assert(math.isclose(h.load_factor, 0.60869565, abs_tol=1e-7))
    assert(h.get_capacity == 23)

@pytest.mark.init
def test_clear():
    h = HashMap()
    h.insert('Vanya', 1)
    h.insert('MEPhI', 2)
    h.insert('Pizza', 3)
    h.insert('Milk', 4)
    h.insert('News', 5)
    h.insert('Job', 6)
    h.insert('Bob', 7)
    h.insert('Bold Bob', 8)
    h.insert('Data', 9)
    h.insert('Hash', 10)
    h.insert('Maybe', 11)
    h.insert('Auwaw', 12)
    h.insert('Spring', 13)
    h.insert('Analyst', 14)
    h.insert('Key', 15)
    h.insert('Value', 16)
    h.insert('Value', 25)

    h.clear()
    
    assert(h.contains_key('Milk') == False)
    assert(h.contains_key('Bob') == False)
    assert(h.contains_key('Hash') == False)

    assert(h.get_size == 0)
    assert(math.isclose(h.load_factor, 0.0, abs_tol=1e-7))
    assert(h._capacity == 23)


@pytest.mark.init
def test_is_primary():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    prime_flags = [False, True, True, False, True, False, True, False, False, False]
    
    for number, flag in zip(numbers, prime_flags):
        assert(HashMap._is_prime(number) == flag)

@pytest.mark.init
def test_next_primary():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    next_primary = [3, 3, 3, 5, 5, 7, 7, 11, 11, 11]
    
    for number, correct in zip(numbers, next_primary):
        assert(HashMap._next_prime(number) == correct)