# LRU Cache

---
## Data Structure
  
   + a Double linked list, used to track the cache access. The head of the list is the most recently accessed key. The tail of the list is least recently accessed key. New node will always be added to the head. When a node is visited, it will be moved to the head of the list. When the list reached it capactiy, node at the tail of the list will be removed.        
 + a Hash map, implementend by a Python dictionary. The hash map is used to store the cache items.The key of each hash item is the key of the cache, and the value of the hash item is a node, which cotains the cache key and the cache value. When add a new cache item, an new key/node pair will be added to the hash map. When a node needs to be removed, it will also be removed from the hash map.

## Runtime Complexity Anaylis
The time complexity of hash table access is O(1). For the double linked list, the add, remove, move operation's time complexity is also O(1).   
