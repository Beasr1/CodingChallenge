import heapq
import os
from collections import defaultdict, Counter
from huffman import HuffmanNode

def build_huffman_tree(data):
    frequency = Counter(data)
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq)
        merged.left, merged.right = left, right
        heapq.heappush(heap, merged)
    return heap[0]
def build_huffman_codes(node, code="", mapping=None):
    if mapping is None:
        mapping = {}
    if node:
        if not node.left and not node.right:  # Leaf node
            mapping[node.char] = code
        build_huffman_codes(node.left, code + "0", mapping)
        build_huffman_codes(node.right, code + "1", mapping)
    return mapping


def compress_data(data):
    root = build_huffman_tree(data)
    codes = build_huffman_codes(root)
    compressed_data = "".join(codes[char] for char in data)
    print(compressed_data,codes,root)
    return compressed_data, root

def write_compressed_file(file_path, compressed_data, original_size, huffman_tree):
    output_path = file_path + ".huffman"
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
        print(0)
        file.write(b"0")
        return
    #print(1)
    file.write(b"1")
    if(not (node.left or node.right)):
        print(node.char)
        leafnode.append(node.char)

    write_tree(file, node.left,leafnode)
    write_tree(file, node.right,leafnode)


def write_compressed_data(file, compressed_data):
    # Convert the binary string to bytes
    byte_array = bytearray(int(compressed_data[i:i+8], 2) for i in range(0, len(compressed_data), 8))
    file.write(bytes(byte_array))

def compress_file(file_path,output_file="output"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_file_path=script_dir+file_path
    print(absolute_file_path)


    data="ascbeei"
    comp_data, huffman_tree=compress_data(data)
    output_path= write_compressed_file(absolute_file_path, comp_data, len(data), huffman_tree)

    return 1 

compress_file('\\file.txt')