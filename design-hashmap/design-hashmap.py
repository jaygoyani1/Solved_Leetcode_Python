class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 1000
        self.table = [None]*self.capacity
        
    def hash(self,key):
        return key%self.capacity
    
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = self.hash(key)
        
        if self.table[index] == None:
            self.table[index] = Node(key,value)
        else:
            curr_node = self.table[index]
            while curr_node:
                if curr_node.key == key:
                    curr_node.value = value
                    return
                if curr_node.next == None:
                    break
                curr_node = curr_node.next
            curr_node.next = Node(key,value)
                
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = self.hash(key)
        curr_node = self.table[index]
        while curr_node:
            if curr_node.key == key:
                return curr_node.value
            else:
                curr_node = curr_node.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = self.hash(key)
        
        if self.table[index] == None:
            return
        curr_node = prev_node = self.table[index]
        
        if curr_node.key == key:
            self.table[index] = curr_node.next
            
        else:
            curr_node = curr_node.next
            while curr_node:
                if curr_node.key == key:
                    prev_node.next = curr_node.next
                    break
                else:
                    prev_node = prev_node.next
                    curr_node = curr_node.next
                    
                
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)