#!/usr/bin/python3

import sys
from os import system

url = sys.argv[1]

if len(sys.argv) ==  3:
    system(f"gobuster dir -u {url} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t "+ sys.argv[2])
else:
    system(f"gobuster dir -u {url} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt")
    
