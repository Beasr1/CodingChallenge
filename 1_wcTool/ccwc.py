import argparse
import sys
from ccwc_functions import count_bytes, process_files, process_stdin, count_lines, count_words, count_chars
import locale
# START of main() function --------------------------------------------------------------------------------------------------------
def main():
    print(locale.getdefaultlocale())
    while True:
        # read command from user of terminal
        user_input=input('> ')

        #split into command and arguments
        parts=user_input.split()
        command=parts[0]
        arguments=parts[1:]

        print("Command is : ",parts)
        if (command=='ccwc'):
            parser = argparse.ArgumentParser(description='Custom Word Count (ccwc) command implementation in Python.')
            parser.add_argument('-c', action='store_true', help='Count bytes')
            parser.add_argument('-l', action='store_true', help='Count lines')
            parser.add_argument('-w', action='store_true', help='Count Words')
            parser.add_argument('-m', action='store_true', help='Count Chars')
            parser.add_argument('files', nargs='*', help='Input file(s) to count (default: test.txt)')
            args = parser.parse_args(arguments)
            # print(parser)
            # print(args)
            # print(parser.print_help())

            if not sys.stdin.isatty() or not args.files:
                # If data is being piped in, use it
                print("piping")
                process_stdin()

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
                    else:
                        print("No valid option provided. Use -c or -l.")
                        #no option provide
                        line_count = count_lines(file_path)
                        word_count= count_words(file_path)
                        byte_count= count_bytes(file_path)
                        print(f"{byte_count}\t{line_count}\t{word_count}\t{file_path}")

            else:
                # If no files or stdin, print help
                parser.print_help()
        elif (command=='exit'):
            break;
        else :
            print("Unknown Command.")
            print("Type command 'exit' to end simulation or 'help' to display information about shell builtin commands")
# END of main() function --------------------------------------------------------------------------------------------------------


if (__name__ == "__main__"):
    main()