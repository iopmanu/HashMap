import pytest
from src.linkedlist import *

TEST_SIZE = 1000

@pytest.mark.init
def test_empty_list():
    l = LinkedList()
    assert(l.head is None)
    assert(l.tail is None)
    assert(l.size == 0)

@pytest.mark.init
def test_append_iter():
    l = LinkedList()
    for i in range(1000):
        l.append(i)
    
    for lvalue, correct in zip(l, range(TEST_SIZE)):
        assert(lvalue == correct)

@pytest.mark.init
def test_append_iter():
    l = LinkedList()
    for i in range(TEST_SIZE):
        l.append(i)
    
    for lvalue, correct in zip(l, range(TEST_SIZE)):
        assert(lvalue == correct)

@pytest.mark.init
def test_prepend_iter():
    l = LinkedList()
    for i in range(TEST_SIZE):
        l.prepend(i)
    
    for lvalue, correct in zip(l, reversed(range(TEST_SIZE))):
        assert(lvalue == correct)

@pytest.mark.init
def test_append_reverse():
    l = LinkedList()
    for i in range(1000):
        l.append(i)
    
    for lvalue, correct in zip(reversed(l), reversed(range(TEST_SIZE))):
        assert(lvalue == correct)

@pytest.mark.init
def test_prepend_reverse():
    l = LinkedList()
    for i in range(1000):
        l.prepend(i)
    
    for lvalue, correct in zip(reversed(l), range(TEST_SIZE)):
        assert(lvalue == correct)

@pytest.mark.init
def test_len():
    l = LinkedList()
    for i in range(TEST_SIZE):
        l.prepend(i)
    
    assert(len(l) == TEST_SIZE)

@pytest.mark.init
def test_pop_front_back():
    l = LinkedList()
    for i in range(TEST_SIZE):
        l.append(i)
    
    for _ in range(TEST_SIZE // 5):
        l.pop_first()

    for _ in range(TEST_SIZE // 4):
        l.pop_last()

    for value, correct in zip(l, range(200, 799)):
        assert(value == correct)

    assert(len(l) == 550)

@pytest.mark.init
def test_erase():
    l = LinkedList()
    for i in range(TEST_SIZE // 100):
        l.append(i)
    
    l.erase(4)
    l.erase(0)
    l.erase(l.size - 1)
    correct_list = [1, 2, 3, 5, 6, 7, 8]

    for value, correct in zip(l, correct_list):
        assert(value == correct)

    assert(len(l) == 7)