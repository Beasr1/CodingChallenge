import sys
from .ccwc_functions import count_bytes, process_files, process_stdin, count_lines, count_words, count_chars
import locale

#TO DO : if file is not present show in the terminal do not
# exit the terminal

# ccwc -h
def ccwc(parser,arguments) :
    if(arguments[0]=='-h') :
        parser.print_help()
        return
    
    #ccwc -h : will make show_help but makes me exit the terminal
    # I do ot want to exit : so I'll control it before
    args=parser.parse_args(arguments)

    if not sys.stdin.isatty() or not args.files:
        print("piping : enter your own data : ")
        process_stdin() # If data is being piped in, use it
    elif args.files:
        # Process files provided as arguments
        # I can provide multiple multiple files together together
        # so check for all
        for file_path in args.files:
            if args.c:
                byte_count = count_bytes(file_path)
                print(f"{byte_count}\t{file_path}")
            elif args.l:
                line_count = count_lines(file_path)
                print(f"{line_count}\t{file_path}")
            elif args.w:
                word_count= count_words(file_path)
                print(f"{word_count}\t{file_path}")
            elif args.m:
                char_count= count_chars(file_path)
                print(f"{char_count}\t{file_path}")
            else:#no option provide
                print("No valid option provided. Use -c or -l.")
                file_path='test.txt'
                line_count = count_lines(file_path)
                word_count= count_words(file_path)
                byte_count= count_bytes(file_path)
                print(f"{byte_count}\t{line_count}\t{word_count}\t{file_path}")
    else:# If no files or stdin, print help
        print("Weird Command : use ccwc -h or ccwc --help to access help")
        parser.print_help()
    return