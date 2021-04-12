class LinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:
    

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.size = 0
        self.head, self.tail = LinkedNode(), LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        node = self.dict.get(key,None)
        if not node:
            return -1
        self.movetofront(node)
        return node.value
        
    def movetofront(self,node):
        
        self.removenode(node)
        self.addnode(node)
    
    def removenode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addnode(self,node):
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
        
    def put(self, key: int, value: int) -> None:
        node = self.dict.get(key)
        if not node:
            newnode = LinkedNode()
            newnode.key = key
            newnode.value = value
            
            self.dict[key] = newnode
            self.addnode(newnode)
            self.size +=1
            
            if self.size > self.capacity:
                tail = self.poptail()
                del self.dict[tail.key]
                self.size-=1
        else:
            node.value = value
            self.movetofront(node)
    def poptail(self):
        curr = self.tail.prev
        self.removenode(curr)
        return curr

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)