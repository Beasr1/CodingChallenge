import sys

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
            elif (args.d):
                print("decompress")
            else:
                print("default")
    else:# If no files or stdin, print help
        print("Weird Command : use ccwc -h or ccwc --help to access help")
        parser.print_help()
    return