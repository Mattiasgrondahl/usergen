#!/usr/bin/env python

'''
Author: Mattias Grondahl
Date: June 2018
Filename: usergen.py
Description: Generate a list of possible usernames
Copyright (c) 2018, Mattias Grondahl All rights reserved.
'''

import argparse
import sys
from colorama import Fore, Back, Style, init
import progressbar
import string
__author__ = 'Mattias Grondahl'

class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.BLUE = ''
        self.GREEN = ''
        self.ORANGE = ''
        self.RED = ''
        self.ENDC = ''

def banner():
        print (bcolors.GREEN +'''
                       ___
 /\ /\  ___  ___ _ __ / _ \___ _ __
/ / \ \/ __|/ _ \ '__/ /_\/ _ \ '_ \
\ \_/ /\__ \  __/ | / /_\\  __/ | | |
 \___/ |___/\___|_| \____/\___|_| |_|

'''
+ bcolors.ENDC)

def help():
        print('''
Username Generation Tool

optional arguments:
  -h,           --help                                   show this help message and exit
  -f FIRST,     --first         FIRST                    number of characters of the firstname
  -l LAST,      --last          LAST                     number of characters of the lastnames
  -o OUTPUT,    --output        OUTPUT                   filename to output the results
  -v,           --version                                show program's version number and exit
''')

def examples():
        print (bcolors.BLUE +'''

Examples:
python usergen.py -f 3 -l 3 -o first3_plus_+last3.list

python usergen.py -f 2 -l 2 -o first2_plus_+last2.list

python usergen.py -f 2 -l 3 -o first2_plus_+last3.list

'''
+ bcolors.ENDC)

def input(firstname_char, lastname_char, output_file):
        firstname_file = open('firstname.txt', 'r')
        lastname_file = open('lastname.txt', 'r')

        firstnameArray = firstname_file.read()
        lastnameArray = lastname_file.read()

        firstnames = [name.lower() for name in firstnameArray.split()]
        lastnames = [name.lower() for name in lastnameArray.split()]

        names = []
        names = generate(firstnames, lastnames, firstname_char, lastname_char)

        names = list(set(names))
        names = sorted(names)
        with open(output_file, 'w') as output:
             for acronym in names:
                output.write(acronym + "\n")
        count = len(names)
        banner()
        print(bcolors.RED + str(count) + bcolors.ENDC + " entries created.")
        print("The first " + bcolors.RED + str(firstname_char) + bcolors.ENDC + " characters of the firstname and.")
        print("The first " + bcolors.RED + str(lastname_char) + bcolors.ENDC + " characters of the lastname was used.")
        print("The result was written to " + bcolors.RED + str(output_file) + bcolors.ENDC)


def generate(firstnames, lastnames, firstname_char, lastname_char):
        firstname_char = int(firstname_char)
        lastname_char = int(lastname_char)
        namelist = []
        for x in firstnames:
                for y in lastnames:
                        name = x[:firstname_char] + y[:lastname_char]
                        namelist.append(name)
        return namelist

def main():

        parser = argparse.ArgumentParser(description="Username Generation Tool")
        parser.add_argument("-f", "--first", help="number of characters of the firstname")
        parser.add_argument("-l", "--last", help="number of characters of the lastnames")
        parser.add_argument("-o", "--output", help="filename to output the results")
        parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

        args = parser.parse_args()
        firstname_char = args.first
        lastname_char = args.last
        output_file = args.output

        if (args.first == None):
                banner()
                help()
                examples()
                sys.exit(1)

        input(firstname_char, lastname_char, output_file)

if __name__ == '__main__':
    main()
