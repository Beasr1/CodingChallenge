import heapq
import os
from collections import defaultdict, Counter
from huffman import HuffmanNode

def build_huffman_tree(data):
    frequency = Counter(data)
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    #print(frequency)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        #print(left.freq,right.freq,left.char,right.char)
        merged = HuffmanNode(freq=(left.freq + right.freq))
        merged.left, merged.right = left, right

        heapq.heappush(heap, merged)
    return heap[0]
def build_huffman_codes(node, code="", mapping=None):
    if mapping is None:
        mapping = {}

    if node:
        if node.left==None and node.right==None:  # Leaf node
            mapping[node.char] = code
            #print(node.char, code)
            return 
        build_huffman_codes(node.left, code + "0", mapping)
        build_huffman_codes(node.right, code + "1", mapping)
    return mapping


def compress_data(data):
    root = build_huffman_tree(data)
    codes = build_huffman_codes(root)
    compressed_data = "".join(codes[char] for char in data)
    #print(compressed_data,codes,root)
    return compressed_data, root

def write_compressed_file(file_path, compressed_data, original_size, huffman_tree,output_file):
    output_path = output_file + ".huffman"
    with open(output_path, "wb") as output_file:
        # Write the original size to the compressed file
        print("size : ",original_size.to_bytes(4, byteorder="big"))
        output_file.write(original_size.to_bytes(4, byteorder="big"))
        output_file.write(b"\n")  # Separate sections with newline

        # Write the Huffman tree to the compressed file
        leaf_nodes= []
        write_tree(output_file, huffman_tree,leaf_nodes)
        output_file.write(b"\n")  # Separate sections with newline
        print("leafnodes : ",leaf_nodes)

        leaf_nodes_str = ",".join(leaf_nodes)
        output_file.write(leaf_nodes_str.encode())
        output_file.write(b"\n")  # Separate sections with newline


        # Write the compressed data to the compressed file
        write_compressed_data(output_file, compressed_data)

    return output_path


def write_tree(file, node,leafnode):
    if not node:
        file.write(b"0")
        return
    #print(1)
    file.write(b"1")
    if(not (node.left or node.right)):
        leafnode.append(node.char) #order

    write_tree(file, node.left,leafnode)
    write_tree(file, node.right,leafnode)


def write_compressed_data(file, compressed_data):
    # Convert the binary string to bytes
    #print(compressed_data)
    # for i in range(0, len(compressed_data), 8):
    #     print(i,compressed_data[i:i+8],int(compressed_data[i:i+8], 2))
    #     # 8 111101 61
    #     # 61 becomes like : 00111101
    #     # I have taken padding into account but in reverse direction
    #     # so lets padd it like this : 11110100
    #     print(len(compressed_data[i:i+8]))

    last_len=len(compressed_data) % 8
    #print(last_len)
    while(last_len<8):
        compressed_data+='0'
        last_len+=1

    byte_array = bytearray(int(compressed_data[i:i+8], 2) for i in range(0, len(compressed_data), 8))
    #byte_array=bytearray(compressed_data)
    #print(byte_array)
    file.write(bytes(byte_array))

def compress_file(file_path,output_file="output"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_file_path=script_dir+file_path
    absolute_output_path=script_dir+"\\"+output_file
    print(absolute_file_path)


    data="I want to be a better person. I hope I can do it."
    comp_data, huffman_tree=compress_data(data)
    output_path= write_compressed_file(absolute_file_path, comp_data, len(data), huffman_tree,absolute_output_path)

    return 1 

compress_file('\\file.txt')