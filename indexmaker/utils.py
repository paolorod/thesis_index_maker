from __future__ import print_function
import functools
import logging as log
import csv



def flatten(l):
    flat_list = [item for sublist in l for item in sublist]
    return flat_list

def to_unicode_string(list_objects):
    ret_list = list()
    for o in list_objects:
        if isinstance(o, basestring):
            ret_list.append(o.encode("utf-8"))
        else:
            ret_list.append(str(o).encode("utf-8"))
    return ret_list

# write a csv file from a reverse index
def write_csv(filename,reverse_index):

    def element_to_interable(index_element):
        return index_element.to_array()
    
    index_as_iterables = map(element_to_interable,reverse_index)
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for el in index_as_iterables:
            writer.writerow(to_unicode_string(el))

def nested_dict(n, type):
    from collections import defaultdict
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n-1, type))

def write_string(filename,s):
    with open(filename, 'wb') as f:
        f.write(s.encode("UTF-8"))

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '#'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total: 
        print()