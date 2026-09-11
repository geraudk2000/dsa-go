class Node: 
    def __init__(self, key, value): 
        self.key = key
        self.value = value 
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head 

    def remove(self, node): 
        prevNode = node.prev
        nextNode = node.next 

        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def insert(self, node): 
        prevNode = self.head 
        nextNode = self.head.next 

        prevNode.next = node
        node.prev = prevNode
        nextNode.prev = node
        node.next = nextNode

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1 
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            node = self.cache[key]
            self.remove(node)
        newNode = Node(key, value)
        self.insert(newNode)
        self.cache[key] = newNode

        if self.capacity < len(self.cache): 
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]

        
