class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {} # key : Node
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            prev = self.cache[key].prev
            nxt = self.cache[key].next

            prev.next = nxt
            nxt.prev = prev

            prev = self.tail.prev
            
            self.cache[key].next = self.tail
            self.tail.prev = self.cache[key]

            self.cache[key].prev = prev
            prev.next = self.cache[key]
            return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = Node(key, value)
            if len(self.cache) > self.capacity:
                deleted = self.head.next
                nxt = self.head.next.next
                self.head.next = nxt
                nxt.prev = self.head
                del self.cache[deleted.key]
        else:
            prev = self.cache[key].prev
            nxt = self.cache[key].next

            prev.next = nxt
            nxt.prev = prev

            self.cache[key].val = value
        prev = self.tail.prev
            
        self.cache[key].next = self.tail
        self.tail.prev = self.cache[key]

        self.cache[key].prev = prev
        prev.next = self.cache[key]
