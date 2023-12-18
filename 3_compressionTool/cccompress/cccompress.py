import sys
from cccompress.compress_file import compress_file
from cccompress.decompress_file import decompress_file

def cccompress(parser,arguments):
    if(arguments[0]=='-h') :
        parser.print_help()
        return
    
    args=parser.parse_args(arguments)
    if not sys.stdin.isatty() or not args.files:
        a=1 #nothing file provided
    elif args.files:
        print(args.files)
        arr=args.files
        #for file_path in args.files:
            #print(file_path)
        if(args.c):
            print("compress")
            if(len(arr)==1): compress_file(arr[0])
            elif(len(arr)==2): compress_file(arr[0],arr[1])
            else: print("format is wrong : more than 2 files paths are stated")

        elif (args.d):
            print("decompress")
            #decompress_file(file_path)
            if(len(arr)==1): decompress_file(arr[0])
            elif(len(arr)==2): decompress_file(arr[0],arr[1])
            else: print("format is wrong : more than 2 files paths are stated")
        else:
            print("default")
    else:# If no files or stdin, print help
        print("Weird Command : use ccwc -h or ccwc --help to access help")
        parser.print_help()
    return