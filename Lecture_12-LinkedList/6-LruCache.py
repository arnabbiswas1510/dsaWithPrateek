"""
https://leetcode.com/problems/lru-cache/

Other popular Cache implementations are:
1. LFU (least Frequently Used)
2.
"""

from collections import defaultdict
class Item:
    def __init__(self,key, data):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None

class LRUCache2:
    def __init__(self,size):
        self.maxsize=size
        self.cache=defaultdict(Item)
        self.head=Item(0,0)
        self.tail=Item(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def addItemAtFirst(self, item):
        item.next=self.head.next
        item.prev=self.head
        self.head.next.prev=item
        self.head.next=item

    def removeItem(self, item):
        item.prev.next=item.next
        item.next.prev=item.prev

    def get(self, key):
        item=self.cache.get(key)
        if item:
            if len(self.cache) == 1:
                return item
            self.removeItem(item)
            self.addItemAtFirst(item)
            return item.data
        else:
            return None

    def put(self, key, data):
        item=self.cache.get(key) #Use get to avoid KeyError in Python
        if not item:
            item=Item(key, data)
            self.cache[key]=item
            self.addItemAtFirst(item)
            if len(self.cache) == self.maxsize+1:
                self.cache.pop(self.tail.prev.key)
                self.removeItem(self.tail.prev)
        else:
            item.data=data
            self.removeItem(item)
            self.addItemAtFirst(item)

    def displayLRUCache(self):
        temp = self.head.next
        while temp.next:
            print(temp.data,end=", ")
            temp=temp.next

"""
From python 3.7, dict preserves the order. Therefore, there is no need to use double linked list
"""
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = defaultdict(int)

    def get(self, key: int) -> int:
        if self.cache.get(key) != None:
            val = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key) != None:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.cap:
                self.cache.pop(next(iter(self.cache)))
            self.cache[key] = value

lc=LRUCache(2)
lc.put(1,1)
lc.put(2,2)
print(lc.get(1))
lc.put(3,3)
print(lc.get(2))
lc.put(4,4)
print(lc.get(1))
print(lc.get(3))
print(lc.get(4))


