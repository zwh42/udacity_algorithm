# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path, handler):
        # Insert the node as before
        self.children[path] = RouteTrieNode(handler)

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler = "root handler", not_found_handler = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        self.insert("/", handler, not_found_handler)
      
    def insert(self, path_list, handler, not_found_hander):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        if len(path_list) == 0:
            return
        
        root = self.root
        for path in path_list:
            #print("insert: ", path, handler)
            if path not in root.children:
                root.children[path] = RouteTrieNode(not_found_hander)
            root = root.children[path]
        
        root.handler = handler
        




    def find(self, path_list, not_found_handler):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        root = self.root

        for path in path_list:
            if path not in root.children:
                return not_found_handler
            
            root = root.children[path]
        
        return root.handler
    

        



# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self,  handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root_handler = "root handler"
        self.not_found_handler = handler
        self.route_trie = RouteTrie(self.root_handler)
        


    def add_handler(self, path , handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if path is None or not path.startswith("/"):
            return
        
        path_list = self.split_path(path)
        self.route_trie.insert(path_list, handler, self.not_found_handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        return self.route_trie.find(path_list, self.not_found_handler)


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if not path.startswith("/"):
            raise Exception('path must starts with "/"')
        
        path_list = ["/"]
        return path_list + list(filter(lambda x: x != "", path.split("/")))


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one