# Count Word Terminal Simulation

This challenge is to build your own version of the Unix command line tool wc!

The Unix command line tools are a great metaphor for good software engineering and they follow the Unix Philosophies of:

- Writing simple parts connected by clean interfaces each tool does just one thing and provides a simple CLI that handles text input from either files or file streams.
- Design programs to be connected to other programs - each tool can be easily connected to other tools to create incredibly powerful compositions.

## 🔗 Link to Challenge

[![Challenge 1](https://img.shields.io/badge/Challenge:1-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://codingchallenges.fyi/challenges/challenge-wc/)

## Deployment

To deploy this project run

```bash
  python ccwc.py
```

## Commands :

Terminal Simulation will run :

ccwc :

```bash
> ccwc -c test.txt
> ccwc -l test.txt
> ccwc -w test.txt
> ccwc -m test.txt
```

exit :

```bash
> exit
```

help :

```bash
> help
```

## Flags

- `-l` : Prints the number of lines in the file.
- `-w` : Prints the number of words in the file.
- `-c` : Prints the number of bytes in the file.
- `-m` : Prints the number of characters in a file. If the current locale does not support multibyte characters this will match the -c option

If no flag is provided, number of lines, words, and bytes are printed.
