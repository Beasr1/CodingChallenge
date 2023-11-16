import sys
import json
import os

#I am learning about classes with python

class JSONTokenizer:
    def __init__(self, input_str):
        self.input_str = input_str
        self.position = 0

    def get_next_token(self):
        #ignore space
        while self.position < len(self.input_str) and self.input_str[self.position].isspace():
            self.position += 1
        # End of input
        if self.position == len(self.input_str):
            return None  
        
        current_char=self.input_str[self.position]
        if current_char == '{': #OPEN OBJECT
            self.position += 1
            return ('LBRACE', '{')
        elif current_char == '}': #CLOSE OBJECT
            self.position += 1
            return ('RBRACE', '}')
        elif current_char == ':': #SEPERATES KEY : VALUE
            self.position += 1
            return ('COLON', ':')
        elif current_char == ',': #SEPARATES (key,value)
            self.position += 1
            return ('COMMA', ',')
        elif current_char == '"': #READ STRING
            return self.read_string()
        elif current_char.isdigit() or current_char == '-': #NUMBER
            return self.read_number()
        elif current_char.isalpha(): #KEYBOARD
            return self.read_keyword()
        else:
            raise ValueError(f"Unexpected character: {current_char}")

    def read_string(self): # Implement string reading logic
        pass

    def read_number(self): # Implement number reading logic
        pass

    def read_keyword(self): # Implement true, false, null reading logic
        pass

class JSONParser:
    def __init(self,input_str):
        self.lexer=JSONTokenizer(input_str)
        self.current_token=self.lexer.get_next_token()

    def parse(self):
        return self.parse_value()
    
    def parse_value(self):
        token_type, token_value = self.current_token
        if token_type == 'LBRACE':
            return self.parse_object()
        elif token_type == 'RBRACE':
            return None  # End of input
        elif token_type == 'STRING':
            return token_value
        elif token_type == 'NUMBER':
            return float(token_value) if '.' in token_value else int(token_value)
        elif token_type == 'TRUE':
            return True
        elif token_type == 'FALSE':
            return False
        elif token_type == 'NULL':
            return None
        else:
            raise ValueError(f"Unexpected token: {token_type}")


def customJsonParser(file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_file_path=script_dir+file_path
    try:
        with open(absolute_file_path,'r') as file:#read the file : file currently contains metadata
            print (file.read())
            print(type(file.read()))
            parser= JSONTokenizer(file.read())#JSONParser
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 2
        

#I'll implement it myself later
# I beilive the challenge did not want me to use builtin function
# but creating this flexible cli was challenge enough for today
def jsonParse(file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_file_path=script_dir+file_path
    print(absolute_file_path)
    try:
        with open(absolute_file_path,'r') as file:
            #read the file : file currently contains metadata
            print (file.read())
            print(type(file.read()))
            print(file)
            json_data=json.load(file)
            print(json_data)
        print("JSON file loaded successfully:")
        print(json.dumps(json_data, indent=2))  # Display JSON content
        return 0
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 2
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{file_path}'.")
        return 1


def ccjson(parser,arguments):
    if(arguments[0]=='-h') :
        parser.print_help()
        return
    

    args=parser.parse_args(arguments)

    if not sys.stdin.isatty() or not args.files:
        #nothing file provided
        a=1
    elif args.files:
        for file_path in args.files:
            valid=jsonParse(file_path)
            print(valid)
    else:# If no files or stdin, print help
        print("Weird Command : use ccwc -h or ccwc --help to access help")
        parser.print_help()
    return

#automating test
files=['\\tests\\step1\\invalid.json','\\tests\\step1\\valid.json','\\tests\\step2\\invalid.json','\\tests\\step2\\invalid2.json','\\tests\\step2\\valid.json','\\tests\\step2\\valid2.json','\\tests\\step3\\invalid.json','\\tests\\step3\\valid.json','\\tests\\step4\\invalid.json','\\tests\\step4\\valid.json','\\tests\\step4\\valid2.json']
for file in files:
    #print(file)
    val=jsonParse(file)
    #print(val)