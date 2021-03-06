import re
import os
import sys

def to_file(filename, msg):
    try:
        with open(filename, "w") as f:
            f.write(msg)
        print(f"Successfully writing message to {os.path.abspath(filename)}")
    except:
        print("Failed to writing to the file.")
        print("Here is the plaintext")
        print(msg)

def check_input(text):
    """Check if text only contain alphabet and space character (  , \t,\n, \r, \f, \v)"""
    return re.match(r"^[a-zA-Z\s]+$", text)

def check_dir(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            return True
        else:
            sys.exit("Directory isn't file")
    else:
        sys.exit("Directory doesn't exist")

def read_file(path):
    if check_dir(path):
        try:
            with open(path, "r") as file:
                lines = file.readlines()
            return "".join(lines)
        except:
            sys.exit("Failed to read file")
