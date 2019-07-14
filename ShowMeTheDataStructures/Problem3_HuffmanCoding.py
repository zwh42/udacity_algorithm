import sys

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None

def huffman_encoding(data):
    char_frequency = []
    frequency_dict = {}
    for char in data:
        if char not in frequency_dict:
            frequency_dict[char] = 1
        else:
            frequency_dict[char] += 1
    char_frequency = sorted(frequency_dict.items(), key = lambda x: x[1])
    print(char_frequency)



def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))