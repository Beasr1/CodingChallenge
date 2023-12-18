import os
from huffman import HuffmanNode

def write_decompressed_file(file_path, decompressed_data):
    output_path = file_path[:-8]  # Remove the ".huffman" extension
    with open(output_path, "w") as output_file:
        output_file.write(decompressed_data)

def decompress_data(comp,huffman_tree,size): # padding may be there so also saved the size of riginal string
    #print(size)
    decoded_data = []
    current_node = huffman_tree  # Start at the root of the Huffman tree

    
    for byte_index, byte in enumerate(comp):
        print(byte)
        for i in range(8):
            bit = (byte >> (7 - i)) & 1  # Extract each bit from the byte (MSB to LSB)
            #print(bit)
            if bit == 0:
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node.left is None and current_node.right is None:  # Leaf node
                decoded_data.append(current_node.char)
                size-=1
                #print(size)
                if(size==0): break #I finally got the use of saving orignal size of string : so code works
                current_node = huffman_tree  # Reset to the root for the next sequence of bits

    decompressed_data = ''.join(decoded_data)
    return decompressed_data

def extract_data(file_path):
    with open(file_path, "rb") as input_file:
        content = input_file.read()

    sections = content.split(b"\n")

    original_size_bytes = sections[0]
    original_size = int.from_bytes(original_size_bytes, byteorder="big")
    #print(original_size)

    leaf_nodes_line = sections[2].decode()
    leaf_nodes = leaf_nodes_line.split(",")
    #print(leaf_nodes)

    huffman_tree = read_tree(sections[1],leaf_nodes)
    compressed_data = sections[3]

    #print(sections)
    return compressed_data,huffman_tree,original_size

def read_tree(data,arr):
    #print(data)
    index=0 #refrence it once
    max_index=len(data)

    def build_tree():
        nonlocal index
        if index >= max_index:
            return None
        
        bit = data[index:index+1] #from index to index+1
        #print(bit,index)
        index += 1

        if bit == b"0":
            #print("NULL")
            return None
        node = HuffmanNode()
        node.char = None #will enter it later
        node.left = build_tree()
        node.right = build_tree()
        return node
    
    def traverse_tree(node):
        nonlocal index
        if not node:
            return
        if(not (node.left or node.right)):
            node.char=arr[index]
            index+=1
            #print(node.char)
        traverse_tree(node.left)
        traverse_tree(node.right)

    index = 0
    max_index = len(data)
    root= build_tree()

    index=0
    traverse_tree(root)
    return root #enter huffma tree

def is_compressed_file(file_path):
    return file_path.lower().endswith('.huffman')

def decompress_file(file_path,output_file="output"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_file_path=script_dir+file_path
    print(absolute_file_path)

    if not is_compressed_file(absolute_file_path):
        print("Not a valid compressed file.")
        return None


    decomp_data, huffman_tree, size=extract_data(absolute_file_path)
    print(decomp_data,huffman_tree,size)
    
    print(decomp_data)
    data=decompress_data(decomp_data,huffman_tree,size)
    print(data)

    write_decompressed_file(absolute_file_path, data)
    return data 

decompress_file("//output.huffman")