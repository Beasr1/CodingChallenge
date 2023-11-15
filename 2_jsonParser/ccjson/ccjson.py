import sys
import json
import os


#I'll implement it myself later
# I beilive the challenge did not want me to use builtin function
# but creating this flexible cli was challenge enough for today
def jsonParse(file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_file_path = os.path.join(script_dir, file_path)
    print(absolute_file_path)
    try:
        with open(absolute_file_path,'r') as file:
            json_data=json.load(file)
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