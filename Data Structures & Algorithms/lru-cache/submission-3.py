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

        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head 
        
    
    def insert(self, node): 
        prevNode = self.head 
        nextNode = self.head.next 

        self.head.next = node
        node.prev = self.head 
        nextNode.prev = node
        node.next = nextNode

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode 


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
        self.cache[key] = newNode
        self.insert(newNode)

        if self.capacity < len(self.cache): 
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]

        
