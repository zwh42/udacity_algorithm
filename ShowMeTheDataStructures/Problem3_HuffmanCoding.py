import sys
from queue import PriorityQueue


class Node:

    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self._left_child = None
        self._right_child = None
    
    @property
    def left_child(self):
        return self._left_child
    
    @left_child.setter
    def left_child(self, node):
        self._left_child = node
    
    @property
    def right_child(self):
        return self._right_child
    
    @right_child.setter
    def right_child(self, node):
        self._right_child = node
    
    def __repr__(self):
        return "Node([char = {}, frequency = {}])".format(self.char, self.frequency)

class Tree:
    def __init__(self, root = None):
        self._root = root
    
    @property
    def root(self):
        return self._root
    
    @root.setter
    def root(self, node):
        self._root = node
    
   
        
    

    
    
def huffman_encoding(data):
    if len(data) == 0:
        return "", None
    
    frequency_dict = {}
    for char in data:
        if char not in frequency_dict:
            frequency_dict[char] = 1
        else:
            frequency_dict[char] += 1
    frequency_list = sorted(frequency_dict.items(), key = lambda x: x[1])
    print(frequency_list)
    
    tree_root = build_huffman_tree(frequency_list)
    char_dict = create_char_dict(tree_root)

    encoded_data = "1"
    encoded_data = ""
    for char in data:
        encoded_data += char_dict[char]
        #print("encoded: {}".format(encoded_data))
    
    return encoded_data, tree_root


def create_char_dict(node, code_string = "", char_dict = {}):
    if node.char is not None:
        char_dict[node.char] = code_string
    
    if node.left_child is not None:
        create_char_dict(node.left_child, code_string + "0", char_dict)
    
    if node.right_child is not None:
        create_char_dict(node.right_child, code_string + "1", char_dict)
    
    return char_dict

def build_huffman_tree(frequency_list):
    if len(frequency_list) == 0:
        return None

    root = None
    while len(frequency_list) > 0:
        if len(frequency_list) >= 2:
            temp = frequency_list.pop(0)
            left = Node(temp[0], temp[1])
            #print(left)
            temp = frequency_list.pop(0)
            right = Node(temp[0], temp[1])
            #print(right)
            #print("remaining size:", len(frequency_list))
            parent = Node(None, left.frequency + right.frequency)
            parent.left_child = left
            parent.right_child = right

            if root is None:
                root = parent
            else:
                new_root = Node(None, root.frequency + parent.frequency)
                new_root.left_child = parent
                new_root.right_child = root
                root = new_root
        
        else:
            temp = frequency_list.pop(0)
            left = Node(temp[0], temp[1])
            parent = Node(None, left.frequency)
            parent.left_child = left
            if root is None:
                root = parent
            else:
                new_root = Node(None, root.frequency + parent.frequency)
                new_root.left_child = parent
                new_root.right_child = root
                root = new_root
    
    return root
                  


    




def huffman_decoding(data,tree):
    if tree is None:
        return data
    
    def decode(data, root, index, decoded_string):
        if root.left_child is None and root.right_child is None:
            decoded_string += root.char
            return index, decoded_string
        elif data[index] == "0":
            return decode(data, root.left_child, index + 1, decoded_string)
        else:
            return decode(data, root.right_child, index + 1, decoded_string)
    
    index = 0
    decoded_string = ""
    while(index <= len(data) - 1):
        index, decoded_string = decode(data, tree, index, decoded_string)
    
    return decoded_string


if __name__ == "__main__":
    codes = {}

    print("\ntest case 1:\n")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("\ntest case 2:\n")
    a_great_sentence = "qqqqqqqqqqq"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


    print("\ntest case 3:\n")
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    #print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))