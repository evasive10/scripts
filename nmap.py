#!/usr/bin/python3

import os, argparse
from os import system

parser = argparse.ArgumentParser(description="Conduct nmap scan on all ports with version detection enabled, using the default set of nmap scripts. Configured to show only open or possibly open ports and the reason each port is set to specific state and reason each host is up or down.")

parser.add_argument('IP', help="Desired IP address to perform scan on")

args=parser.parse_args()
ip = args.IP

system(f"nmap -p- -sV -sC --open --reason {ip}")
