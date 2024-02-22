#!/usr/bin/python3
"""script to export data in the JSON format"""


import json
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: ', sys.argv[0], '<employee id>')
        sys.exit(1)