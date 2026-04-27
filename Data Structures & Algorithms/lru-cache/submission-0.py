
class Node:
     def __init__(self,key,val):
        self.key = key
        self.val  = val
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.dict = {}

        self.left = Node(-1,-1)
        self.right = Node(-1,-1)

        self.left.next = self.right
        self.right.prev = self.left 
    

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            self.remove(self.dict[key])
            self.insert(self.dict[key])
            item = self.dict[key].val
            return item
        return -1
        

    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            self.remove(self.dict[key])
                   
        self.dict[key] = Node(key,value)
        self.insert(self.dict[key])   

        if len(self.dict) > self.cap:
            lru  = self.left.next
            self.remove(lru)
            del self.dict[lru.key]
        

    
    def insert(self,node):
        nxt = self.right
        prev = self.right.prev

        prev.next = node
        nxt.prev = node

        node.next = nxt
        node.prev = prev
    
    def remove(self,node):

        nxt = node.next
        prev = node.prev

        prev.next = nxt
        nxt.prev = prev

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)