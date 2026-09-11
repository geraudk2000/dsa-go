
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



    def insert(self, node): 
        prev_node = self.head
        next_node = self.head.next 

        node.next = next_node
        next_node.prev = node
        node.prev = self.head 
        self.head.next = node
    


    def remove(self, node): 
        node_prev = node.prev
        node_next = node.next 

        node_prev.next = node_next 
        node_next.prev = node_prev


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
        
