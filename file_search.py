#!/usr/bin/env python3
# ^ For Dot-Slash Command Line Running

import os
import sys
from os.path import join

#THIS LOCKS THE SCRIPT INTO THE DIRECTORY IT IS FOUND IN
#~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
def dir_lock(filename:str):
    filepath = os.path.dirname(os.path.abspath(filename))
    if filepath != os.getcwd():
        return os.chdir(filepath)

ARGUMENTS = sys.argv.copy()
FILE = ARGUMENTS.pop(0)

dir_lock(FILE)                                           
#^ you can comment this line out to disable directory lock
#~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

#Creating the list of all file paths in the directory and subdirectories for both types seperately (files and directories)
FILE_PATH_LIST, DIR_PATH_LIST = [],[]
for root, dirs, files in os.walk("."):
    FILE_PATH_LIST += [join(root, name) for name in files]
    DIR_PATH_LIST += [join(root, name) for name in dirs]

#Creating the matching directories that associates a filename(key) with its path(value)
#note: if two files or two directories share a name, they are placed in the same "bucket" within their specified dict
FILE_PATH_DICT, DIR_PATH_DICT = {},{}
for i in FILE_PATH_LIST:
    key = i[i.rfind("/") + 1:]
    if FILE_PATH_DICT.get(key) is None:
        FILE_PATH_DICT[key] = [i]
    else:
        FILE_PATH_DICT[key] = FILE_PATH_DICT[key] + [i]
for i in DIR_PATH_LIST:
    key = i[i.rfind("/") + 1:]
    if DIR_PATH_DICT.get(key) is None:
        DIR_PATH_DICT[key] = [i]
    else:
        DIR_PATH_DICT[key] = DIR_PATH_DICT[key] + [i]

#This is to be used in conjuction with the dicts to find the file path(s) associated with a name
def find_path(name:str,is_dir = False) -> list:
    """Function to search the file path dicts or the directory path dicts for a given name

    Args:
        name (str): Name to search for
        is_dir (bool, optional): Whether or not the expected result is a directory. Defaults to False.

    Returns:
        list: the list of all paths found for the given name
    """    
    return DIR_PATH_DICT.get(name) if is_dir else FILE_PATH_DICT.get(name)
    


#For Command Line Running
if __name__ == "__main__":
    result = None
    valid_switches = ['-d','-f']

    counter = 0
    while counter < len(ARGUMENTS):
        arg = ARGUMENTS[counter]
        if arg in valid_switches:
            try:
                counter+=1
                val = ARGUMENTS[counter]
            except Exception as e:
                raise TypeError(f"{FILE} missing filename after switch '{arg}'")
            
            if arg == '-d':
                result = find_path(val,is_dir=True)
            elif arg == "-f":
                result = find_path(val)
            break
        elif arg.startswith("-"):
            raise TypeError(f"{FILE} unknown switch '{arg}'")
        else:
            result = find_path(arg)
            break
    
    if result is not None:  
        #normal case
        print(f"Paths associated with name: {ARGUMENTS[counter]}")
        for i in range(len(result)):
            print(f"[{str(i+1)}] {result[i]}") 
    else:
        #no result case
        print(f"No paths found for name: {ARGUMENTS[counter]}")