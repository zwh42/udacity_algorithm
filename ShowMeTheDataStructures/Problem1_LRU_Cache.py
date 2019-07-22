class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

    def __repr__(self):
        return "Node(key = {}, value = {})\n".format(self.key, self.value) 

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.hash_map = dict()
        
        self.head = None
        self.tail = None


        self.capacity = capacity
        self.size = 0



    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.hash_map:
            return -1
        
        node = self.hash_map[key]
        self.remove_node(node)
        self.add_to_head(node)
        return node.value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.capacity <= 0:
            raise Exception("cache's capacity mush > 0 !")
        
        if self.get(key) == -1:
            node = Node(key, value)
            
            if self.size == self.capacity:
                del self.hash_map[self.tail.key]
                self.remove_node(self.tail)
            
            self.add_to_head(node)
            self.hash_map[key] = node

           
        else:
            node = self.hash_map[key]
            node.value = value
            self.remove_node(node)
            self.add_to_head(node)

    def add_to_head(self, node):
        node.next = self.head
        node.pre = None
        if self.head is not None:
            self.head.pre = node

        self.head = node
        if self.tail is None:
            self.tail = node

        self.size += 1 
  
    def remove_node(self, node):

        if self.head is None:
            return
        
        if node.pre is not None:
            node.pre.next = node.next
        else:
            self.head = node.next
        
        if node.next is not None:
            node.next.pre = node.pre
        else:
            self.tail = node.pre
        
        if self.tail == node:
            self.tail.pre.next = None
        
        self.size -= 1


    def __repr__(self):
        
        result = "cache:\ncapacitcy = {}, size = {}\n".format(self.capacity, self.size)
        result += "hash: " + str(self.hash_map) + "\n"
        result += "linked list (from top to bottom):\n"
        t = self.head
        
        while(t):
            result += str(t)
            t = t.next
       
        return result        




if __name__ == "__main__":
    
    # test case 1
    print("test case 1:\n")
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)    
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    print(our_cache)
    print("1, 2, 3, 4 inserted")    
    #print("get(1)")
    assert our_cache.get(1) == 1       # returns 1
    #print("get(2)")
    print(our_cache)
    assert our_cache.get(2) == 2      # returns 2
    #print("get(9)")
    print(our_cache)
    assert our_cache.get(9) == -1      # returns -1 because 9 is not present in the cache
    #print("set(5)")
    our_cache.set(5, 5) 
    print(our_cache)
    #print("set(6)")
    our_cache.set(6, 6)
    print(our_cache)
    assert our_cache.get(3) == -1      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    # test case 2
    print("\ntest case 2:\n")
    our_cache = LRU_Cache(2)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(1, 10)
    print(our_cache)
    assert our_cache.get(1) == 10
    assert our_cache.get(2) == 2

    # test case 3
    our_cache = LRU_Cache(0)
    our_cache.set(1, 1)
    print(our_cache.get(1))
    
