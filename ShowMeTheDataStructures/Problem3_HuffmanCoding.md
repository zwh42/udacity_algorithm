# Huffman Coding

## Implementation

+ encoding  
     1. read in the string data, calculate each character's frequency
     2. build a sorted list of tuple (character, frequency), sorted from lowest to hightest
     3. in function build_huffman_tree() inside function huffman_encoding(), the huffman encoding algorithm is applied to create the huffman tree.
     4. in function create_char_dict(), the mapping between character and its correspoinding encoded representation is set up, which is used to create the encoded data.

+ decoding  
   utilize the built huffman tree to traverse the encoded data

## Time Complexity Analysis
In the encoding function, to create the sorted char tuple list is O(nlogn).To build the huffman tree is O(n)

In the decoding function, it's O(n) 

