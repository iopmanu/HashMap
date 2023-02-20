from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    value: Any
    next:  object = None
    prev:  object = None

@dataclass
class LinkedList:
    head:    Node = None
    tail:    Node = None
    size:    int  = 0

    def get_size(self):
        return self.size

    def append(self, src):
        src_node = Node(src, None, self.tail)
        if self.size != 0:
            self.tail.next = src_node
            self.tail = src_node
        else:
            self.head = src_node
            self.tail = src_node
        
        self.size += 1

    def prepend(self, src):
        src_node = Node(src, self.head, None)
        if (self.size != 0):
            self.head.prev = src_node
            self.head = src_node
        else:
            self.head = src_node
            self.tail = src_node
        
        self.size += 1

    def erase(self, index):
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

    def pop_last(self):
        if self.size == 0:
            raise IndexError("Empty list")

        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
    
    def pop_first(self):
        if self.size == 0:
            raise IndexError("Empty list")

        self.head = self.head.next
        self.head.prev = None
        self.size -= 1