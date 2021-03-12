"""
Created on Fri Mar 12 08:16:40 2021

@author: robin
"""

#find files

import glob
py_files = []
py_files = glob.glob('C:/Users/robin/Documents/01_Robin/python/Aufgaben Woche_1-20210309/*.py')
py_files = [w.replace('\\', '/')for w in py_files]

#define separators

separator = '\n#%%\n\n'

#read files

def map_text(file_list):
    for file in file_list:
        with open(file, 'r') as fd:
            yield separator + fd.read()

# merge files

def merge_text(file_list, filename = 'C:/Users/robin/Documents/01_Robin/python/Aufgaben Woche_1_komplett.py')            :
    with open(filename, 'w') as f:
        for line in map_text(file_list):
            f.write("%s\n" % line)

merge_text(py_files)


            