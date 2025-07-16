```
███████╗██╗██████╗  ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
╚══███╔╝██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
  ███╔╝ ██║██████╔╝██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
 ███╔╝  ██║██╔═══╝ ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
███████╗██║██║     ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚══════╝╚═╝╚═╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
████████╗ ██████╗  ██████╗ ██╗     ██╗  ██╗██╗████████╗
╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██║ ██╔╝██║╚══██╔══╝
   ██║   ██║   ██║██║   ██║██║     █████╔╝ ██║   ██║   
   ██║   ██║   ██║██║   ██║██║     ██╔═██╗ ██║   ██║   
   ██║   ╚██████╔╝╚██████╔╝███████╗██║  ██╗██║   ██║   
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   
```


# ZipCracker Toolkit

## Overview

ZipCracker Toolkit is a Python-based utility designed to extract potential passwords from a text file and use them to crack password-protected ZIP archives.
It was developed as part of a programming exercise to demonstrate file handling, regular expressions (or tokenization), error management, and ZIP manipulation using Python's standard librairies.

The tool consists of a single script that:

- extract words longer than 4 characters from a source text file to build a wordlist (modifiable from the original 8-character requirement).

- Attempts to extract a ZIP archive, first without a password, and if protected, brute-forces it using the generated or provided wordlist.

This project emphasizes robust error handling, such as checking for file existence and handling extraction failures, making it suitable for educational purposes or simple security testing scenarios.

Note: This tool is for educational and ethical use only. Cracking passwords without permission may violate laws or terms of service.

## Features

- Wordlist Generation: Scans a text file for isolated words (non-whitespace sequences) longer than 4 characters, stripping punctuation while preserving internal special characters.

- ZIP Cracking: Tries to extract ZIP files without a password first; if needed, iterates through a wordlist to find the correct password.

- Command line interface uses `argparse` for flexible input
 	- Required path to the ZIP file
	- "-l" or "--wordlist" for a custom wordlist path

- Error handling: Checks for files/folder existence, invalid ZIPs, empty wordlists

- UTF-8 support: Handles special characters like @ or £

## Requirements

Python 3.x

No external dependencies : uses `os`, `zipfile`, `string`, `argparse`

## Installation

Clone the repository :

`git clone https://github.com/yourusername/zipcracker-toolkit.git`

`cd zipcracker-toolkit`

## Usage 

Run the script from the command line Arguments

- zip_path : Path to the password-protected ZIP file (required)

- -l, --wordlist : path to the wordlist file (required) 

# Example

python3 zipCracker_toolkit.py path/to/the/zip -l wordlist
