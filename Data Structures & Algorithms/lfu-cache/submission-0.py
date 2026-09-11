class Node: 
    def __init__(self, key, value): 
        self.key = key 
        self.value = value
        self.freq = 1 
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    Holds node of the same frequency
    Head side = most recently used withing this frequency
    Tail side = least recently used within this frequency
    """ 

    def __init__(self): 
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def remove(self, node: Node): 
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        node.prev = node.next = None
        self.size -= 1 
    def insert_mru(self, node: Node): 
        nextNode = self.head.next
        nextNode.prev = node
        node.next = nextNode
        node.prev = self.head
        self.head.next = node
        self.size += 1 
    def pop_lru(self):
        """
        Remove and return the least-recently used node in the list. 
        """
        if self.size == 0: 
            return None
        node = self.tail.prev
        self.remove(node)
        return node
    
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.size = 0
        self.cache = {} # key -> Node
        self.freqMap = {} # freq -> DoulbyLinkedList 
        self.minFreq = 0
    
    def _touch(self, node: Node): 
        oldFreq = node.freq
        oldList = self.freqMap[oldFreq]
        oldList.remove(node)

        # if we remove the last node frome minFreq list, minFreq increase
        if oldFreq == self.minFreq and oldList.size == 0:
            self.minFreq += 1 
        
        node.freq += 1
        newFreq = node.freq
        if newFreq not in self.freqMap: 
            self.freqMap[newFreq] = DoublyLinkedList()
        self.freqMap[newFreq].insert_mru(node)

    def get(self, key: int) -> int:
        if key not in self.cache: 
            return -1 
        node = self.cache[key]
        self._touch(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 
        
        # Update existing
        if key in self.cache: 
            node = self.cache[key]
            node.value = value
            self._touch(node)
            return 
        
        # Evict if full 
        if self.size == self.capacity: 
            lfuList = self.freqMap[self.minFreq]
            lfu = lfuList.pop_lru()
            del self.cache[lfu.key]
            self.size -= 1 
        
        # Insert new node with freq=1
        node = Node(key, value)
        self.cache[key] = node
        if 1 not in self.freqMap: 
            self.freqMap[1] = DoublyLinkedList()
        self.freqMap[1].insert_mru(node)
        self.minFreq = 1
        self.size += 1  

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)