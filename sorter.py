'''
sorter.py

A simple program that looks through the contents of this directory for files with names of the form:

    [species name]_[table||function]_[temperature range]_[comp_range]_[paper key].pdf
    
Then [optionally] if can perform a search on the contents to find specific papers.

Search with args when running the script:

    python sorter.py [parameter]:[criteria]
    
As many parameters as you like can be added:
    
    python sorter.py species:glycerol infotype:table temprange:0c-100c

Author: Chris Boyle (kfb12157@strath.ac.uk)
'''



from glob import glob
from sys import argv
from copy import copy

## for each file in folder
## ## read title
## ## parse information about file from title
## ## offer ability to search through files for specific

files = glob('*.pdf')  # find any pdf file

indexes    = list()

name       = dict()
paper_type = dict()
temp_range = dict()
comp_range = dict()
bibkey     = dict()

for i in range(len(files)):
    
    f_s = files[i][:-4].split('_')
    
    # fname is of the form:
    #       [species name]_[table||function]_[temperature range]_[comp_range]_[paper key].pdf
    # e.g.
    #       glycerol+water_table_0c-100c_0wt-100wt_SEGUR1951.pdf
    
    indexes.append(i)  # add index to list
    name[i] = f_s[0]
    paper_type[i] = f_s[1]
    
    if len(f_s) > 2:
        temp_range[i] = f_s[2]
        if len(f_s) > 3:
            comp_range[i] = f_s[3]
            if len(f_s) > 4:
                bibkey[i] = f_s[4]
            else:
                comp_range[i] = "na"
                bibkey[i] = f_s[3]
        else:
            comp_range = "na"
            bibkey[i] = "na"
    else:
        temp_range[i] = "na"
        comp_range[i] = "na"
        bibkey[i] = "na"
    
def display(id_list=indexes):
    
    print "o{}-{}-{}-{}-{}-{}o".format("-" * 8, "-" * 15, "-" * 15, "-" * 15, "-" * 15, "-" * 26)
    print "|{}|{}|{}|{}|{}|{}|".format("index".center(8), "species".center(15), "info type".center(15), "temp range".center(15), "comp range".center(15), "bibkey".center(26))
    print "|{}|{}|{}|{}|{}|{}|".format("-" * 8, "-" * 15, "-" * 15, "-" * 15, "-" * 15, "-" * 26)
    for i in id_list:
        print "|{}|{}|{}|{}|{}|{}|".format(str(i).center(8), name[i].center(15), paper_type[i].center(15), temp_range[i].center(15), comp_range[i].center(15), bibkey[i].center(26))
    print "o{}-{}-{}-{}-{}-{}o".format("-" * 8, "-" * 15, "-" * 15, "-" * 15, "-" * 15, "-" * 26)
    

# args of the form:
#       [param]:[value]
#
# e.g.
#       species:glycerol
print "\n"
res = copy(indexes)
for i in range(1, len(argv)):
    p = argv[i].split(":")
    
    if p[0] == "species":
        print "* matching species name \"{}\"".format(p[1])
        for id in range(0, len(res)):
            idx = len(res) - id - 1
            if name[res[idx]] != p[1]: res.pop(idx)
    elif p[0] == "infotype":
        print "* matching paper type \"{}\"".format(p[1])
        for id in range(0, len(res)):
            idx = len(res) - id - 1
            if paper_type[res[idx]] != p[1]: res.pop(idx)
    elif p[0] == "temprange":
        print "* matching temperature range \"{}\"".format(p[1])
        for id in range(0, len(res)):
            idx = len(res) - id - 1
            if temp_range[res[idx]] != p[1]: res.pop(idx)
    elif p[0] == "comprange":
        print "* matching composition range \"{}\"".format(p[1])
        for id in range(0, len(res)):
            idx = len(res) - id - 1
            if comp_range[res[idx]] != p[1]: res.pop(idx)
print "\n"

display(res)
