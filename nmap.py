#!/usr/bin/python3

import os, sys
from os import system

ip = sys.argv[1]

system(f"nmap -p- -sV -sC --open --reason {ip}")
