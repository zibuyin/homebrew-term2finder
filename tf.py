#!/usr/bin/env python3 

import sys
import os
import subprocess as sp
import argparse
from pathlib import Path

# Constants
RED = "\033[31m"
RESET = "\033[0m"

# Setup arguments
parser = argparse.ArgumentParser(description="Refined CLI to open Finder from Terminal", prog="tf")
parser.add_argument("file_path", nargs="*", default="", help="Path of the directory to open, or path of file to highlight in Finder")
parser.add_argument("-i", action="store_true", help="Sets view mode to icons mode")
parser.add_argument("-l", action="store_true", help="Sets view mode to list mode")
parser.add_argument("-c", action="store_true", help="Sets view mode to columns mode")
parser.add_argument("-s",nargs="?", default="") # Sort mode
parser.add_argument("-p", action="store_true", help="Previews file or folder using qlmanage")
# Gallery view is not supported by AppleScript, blame Apple.
# parser.add_argument("-g", action="store_true", help="Sets view mode to gallary mode")
args = parser.parse_args()
# print(args)

# Get working dir, backup if path not provided
cwd = sp.run("pwd", capture_output=True, text=True).stdout.strip()



# Helper functions
def error(msg):
    print(f"{RED}{msg}{RESET}", file=sys.stderr)
    
# Opens dir based on view args
def open_dir(file_path, args):
    # View options
    if args.i:
        display_option = "icon"
    elif args.l:
        display_option = "list"
    elif args.c:
        display_option = "column"
    # If no display arguments are passed through, just open it dir
    else:
        sp.run(["open", file_path])
        return
    # Sort options

    sort_option = "arranged by name"
    if len(args.s) != 0:
        s = args.s[0]
        if  s == 'n':
            sort_option = "arranged by name"
        elif s == "dm":
            sort_option = "arranged by modification date"
        elif s == "dc":
            sort_option = "arranged by creation date"
        elif s == 's':
            sort_option = "arranged by size"
        elif s == 'k':
            sort_option = "arranged by kind"
        elif s == 'l':
            sort_option = "arranged by label"

    
            

    # Gallery view is not supported by AppleScript, blame Apple
    # elif args.g:
    #     display_option = "gallery"

    
    # If arguments are passed, this runs
    # print(display_option)
    script = f'''
    tell application "Finder"
        set theFolder to POSIX file "{file_path}" as alias
        open theFolder
        set current view of window 1 to {display_option} view
        # set sort column of list view options of window 1 to {sort_option}
        activate
    end tell
    '''
    sp.run(["osascript", "-e", script])

def choose_file_or_dir(file_path):
    if os.path.isdir(file_path):
        open_dir(file_path, args)
    # Highlight it if it's a file
    elif os.path.isfile(file_path):
        sp.run(["open", "-R", file_path])
    # Raise error if nonexist
    elif not os.path.exists(file_path):
            error(f"File '{file_path}' does not exist")
    else:
        error("Unknow error occurred... Consider reporting this to https://github.com/zibuyin/term2finder/issues")

def preview_dir(file_path):
    sp.run(["qlmanage", "-p", file_path], stdout=sp.DEVNULL)

# Handles arguments and directs it to functions
def base_handler(args, cwd):

    # If file path is provided, else give cwd

    if len(args.file_path) != 0:
        file_paths = args.file_path
    else:
        file_path = cwd
    # Use qlmanage to preview it if -p tag is set   
    if args.p:
        for file_path in file_paths:
            preview_dir(file_path)
    else:
        # Runs only if not in preview mode
        # Open dir if it's a dir
        try:
            for file_path in file_paths:
                choose_file_or_dir(file_path)
        except UnboundLocalError:
            choose_file_or_dir(cwd)

base_handler(args, cwd)

# else:
#     for i in range(len(sys.argv) - 1):
#         print(sys.argv[i])
