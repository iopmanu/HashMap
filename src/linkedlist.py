from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    value: Any
    next:  object = None
    prev:  object = None

    def __add__(self, value : Any):
        self.next = Node(value)

    def __str__(self) -> str:
        return 'node(' + str(self.value) + ')'

    def __iter__(self):
        return LinkedListIter(self)

class LinkedListIter():
    def __init__(self, item) -> None:
        self._item = item
    
    __iter__ = lambda self:self

    def __next__(self):
        if self._item is None:
            raise StopIteration
        
        item, self._item = self._item, self._item.next
        return item

@dataclass
class LinkedList:
    head:    Node = None
    tail:    Node = None
    size:    int  = 0

    def append(self, src):
        src_node = Node(src, None, self.tail)
        if self.size != 0:
            self.tail.next = src_node
            self.tail = src_node
        else:
            self.head = src_node
            self.tail = src_node
        
        self.size += 1

    def insert(self, value : Any, before=None, after=None) -> None:
        if after is not None:
            if before is not None:
                raise ValueError('Impossible to insert between 2 nodes')
            before = after.next
        
        if before is None:
            return self.append(value)
        
        if not isinstance(before, Node):
            raise TypeError('Type of var before&after must be Node')

        node = Node(value, before, before.prev)
        before.prev.next = node
        before.prev = node
        self.size += 1
        

    def prepend(self, src : Any) -> None:
        src_node = Node(src, self.head, None)
        if (self.size != 0):
            self.head.prev = src_node
            self.head = src_node
        else:
            self.head = src_node
            self.tail = src_node
        
        self.size += 1

    def erase(self, index : int) -> None:
        if index >= self.size or index < 0:
            raise IndexError("Index is out of range in erase operation with index: {}".format(index))

        if index == 0:
            if self.size == 0:
                self.head = None
                self.tail = None
            else:
                return self.pop_first()

        elif index == self.size - 1:
            return self.pop_last()
        
        else:
            slow = self.head
            fast = self.head.next
            counter = 0

            while counter < index - 1:
                slow = fast
                fast = fast.next
                counter += 1
            
            if fast != self.tail:
                slow.next = fast.next
                fast.next.prev = slow

        self.size -= 1

    def pop_last(self) -> None:
        if self.size == 0:
            raise IndexError("Empty list")
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:    
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
    
    def pop_first(self) -> None:
        if self.size == 0:
            raise IndexError("Empty list")
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1

    def contains(self, key : Any) -> None:
        for value in self:
            if value[0] == key:
                return value[1]
        
        return None

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self) -> Any:
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __reversed__(self) -> Any:
        current = self.tail
        while current is not None:
            yield current.value
            current = current.prev

    def __len__(self) -> int:
        return self.size