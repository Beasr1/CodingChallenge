import sys
from compress_file import compress_file
from decompress_file import decompress_file

def cccompress(parser,arguments):
    if(arguments[0]=='-h') :
        parser.print_help()
        return
    
    args=parser.parse_args(arguments)
    if not sys.stdin.isatty() or not args.files:
        a=1 #nothing file provided
    elif args.files:
        for file_path in args.files:
            print(file_path)
            if(args.c):
                print("compress")
                compress_file(file_path)
            elif (args.d):
                print("decompress")
                decompress_file(file_path)
            else:
                print("default")
    else:# If no files or stdin, print help
        print("Weird Command : use ccwc -h or ccwc --help to access help")
        parser.print_help()
    return