# need functions to change the names of the files
# need functions to change the extensions of the files
# need functions to change the names and extensions of the files
# need functions to change the names and extensions of the files in a directory
# functions to add prefixes or suffixes to the files
# call functions conditionally based on user input

import os

def rename(directory_path, prefix='',suffix='', new_extension=''):
    # check if path exists
    if not os.path.exists(directory_path):
        print('Path does not exist')
        return
    # get all files in the directory
    files = os.listdir(directory_path)

    # loop through all files
    for file_name in files: 
        # get full file path
        old_path = os.path.join
