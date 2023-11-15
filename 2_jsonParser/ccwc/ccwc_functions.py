import sys
import os

def count_bytes(file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_file_path = os.path.join(script_dir, file_path)

    with open(absolute_file_path, 'rb') as file:
        byte_count = len(file.read())
    return byte_count

def count_lines(file_path):
    #print(file_path)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the full path to the file
    # I want relative to my script file : not relative to my terminall directory
    absolute_file_path = os.path.join(script_dir, file_path)
    #absolute_file_path=os.path.abspath(file_path)
    #print(absolute_file_path)
    with open(absolute_file_path, 'r',encoding='utf-8') as file:
        line_count = sum(1 for line in file)
    return line_count

#https://www.geeksforgeeks.org/python-program-to-count-words-in-text-file/
def count_words(file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_file_path = os.path.join(script_dir, file_path)

    with open(absolute_file_path, 'rb') as file:
        byte_count = len(file.read().split())#split file into words
    return byte_count

def count_chars(file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_file_path = os.path.join(script_dir, file_path)

    with open(absolute_file_path, 'r',encoding='utf-8') as file:
        byte_count = len(file.read())
    return byte_count

def process_files(file_paths):
    for file_path in file_paths:
        byte_count = count_bytes(file_path)
        print(f"{byte_count}\t{file_path}")

def process_stdin():
    # data = sys.stdin.buffer.read()
    # byte_count = len(data)
    byte_count = 0
    # try:
    #     while True:
    #         data = sys.stdin.buffer.read(4096)  # Adjust the chunk size as needed
    #         if not data:
    #             break
    #         byte_count += len(data)
    # except KeyboardInterrupt:
    #     pass
    try:
        while True:
            line = input()
            byte_count += len(line.encode('utf-8'))  # Assuming UTF-8 encoding
    except KeyboardInterrupt:
        pass
    print(f"{byte_count}\tBytes-")  # Use '-' to represent standard input


