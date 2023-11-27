import sys
import json
import os
from .ccjsonparser import JSONParser
from .ccjsonCustomException import JSONDecodeErrorCustom

def customJsonParser(file_path):
    print("\n")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_file_path=script_dir+file_path
    try:
        with open(absolute_file_path,'r') as file: #read the file : file currently contains metadata
            stringData=file.read()
            print("STRING DATA : ",stringData)
            parser= JSONParser(stringData) #JSONParser
            jsonData=parser.loadData()
            print(jsonData)
        return 0
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 2
    except JSONDecodeErrorCustom as err:
        print(f"Error: Invalid JSON format in file '{file_path}'.")
        print(err)
        return 1
    except Exception as err:
        print(f"Some other unexpected exception in :  '{file_path}'.")
        print(err)
        return 1

        

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
            #print (file.read())
            #print(type(file.read()))
            #print(file)
            json_data=json.load(file)
            #print(json_data)
        print("JSON file loaded successfully:")
        print(json.dumps(json_data, indent=2))  # Display JSON content with indentation and style
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
            #valid=jsonParse(file_path) inbuilt json module
            valid=customJsonParser(file_path)
            print(valid)
    else:# If no files or stdin, print help
        print("Weird Command : use ccwc -h or ccwc --help to access help")
        parser.print_help()
    return

#automating test
def automateCalling():
    files=['\\tests\\step1\\invalid.json','\\tests\\step1\\valid.json','\\tests\\step2\\invalid.json','\\tests\\step2\\invalid2.json','\\tests\\step2\\valid.json','\\tests\\step2\\valid2.json','\\tests\\step3\\invalid.json','\\tests\\step3\\valid.json','\\tests\\step4\\invalid.json','\\tests\\step4\\valid.json','\\tests\\step4\\valid2.json']
    for file in files:
        #print(file)
        val=customJsonParser(file)
        #print(val)

# automateCalling()