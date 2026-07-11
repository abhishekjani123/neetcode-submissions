class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.map = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        # A <-> node <-> B
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_front(self, node):
        # Head <-> node <-> X
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove(node)
        self.add_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        node = Node(key, value)
        self.map[key] = node
        self.add_front(node)
        if len(self.map) > self.c:
            lru = self.tail.prev
            self.remove(lru)
            del self.map[lru.key]
        
