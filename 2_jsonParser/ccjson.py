import argparse
import sys
from ccwc.ccwc import ccwc

'''
I want a cli with a good and clean workflow
and in my control

terminal exits when I want it to

'''

# START of create parser -------------------------------------------------------------------------------------------------------------
def create_parser():
    parser = argparse.ArgumentParser(prog="", description='Custom Word Count (ccwc) command implementation in Python.')
    subparsers = parser.add_subparsers(title='Available commands', dest='command')

    ccwc_parser = subparsers.add_parser('ccwc', help='Word Count command : ccwc [-h] [-c] [-l] [-w] [-m] [files ...]')
    ccwc_parser.add_argument('-c', action='store_true', help='Count bytes')
    ccwc_parser.add_argument('-l', action='store_true', help='Count lines')
    ccwc_parser.add_argument('-w', action='store_true', help='Count words')
    ccwc_parser.add_argument('-m', action='store_true', help='Count characters')
    ccwc_parser.add_argument('files', nargs='*', help='Input file(s) to count (default: test.txt)')

    help_parser = subparsers.add_parser('help', help='Help command : help')
    exit_parser = subparsers.add_parser('exit', help='Exit Terminal command : exit')

    # Create a dictionary to store parsers with names
    # I want to access subparser
    # argparse does not have inbuilt method to access them efficicently so lets make my own
    parsers_dict = {
        'ccwc': ccwc_parser,
        'help': help_parser,
        'exit': exit_parser,
        # Add more commands as needed
    }

    return parser, parsers_dict
# END of create parser -------------------------------------------------------------------------------------------------------------

# START of main() function --------------------------------------------------------------------------------------------------------
def main():
    parser, parser_dict = create_parser()
    #print(parser_dict)

    while True:
        user_input=input('> ') # read command from user of terminal

        parts=user_input.split() #split into command and arguments
        command=parts[0]
        arguments=parts[1:]

        
        if (command=='ccwc'):
            ccwc_parser=parser_dict['ccwc']
            ccwc(ccwc_parser,arguments)  
        elif (command=='exit'):
            break;
        elif (command=='help'):
            parser.print_help()
        else :
            print("Unknown Command.")
            print("Type command 'exit' to end simulation or 'help' to display information about shell builtin commands")
# END of main() function --------------------------------------------------------------------------------------------------------


if (__name__ == "__main__"):
    main()