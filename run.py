"""
There are four collection data types in the Python programming language:

    - LIST          is a collection which is ordered and changeable. Allows duplicate members.
    - TUPLE         is a collection which is ordered and unchangeable. Allows duplicate members.
    - SET           is a collection which is unordered and unindexed. No duplicate members.
    - DICTIONARY    is a collection which is unordered, changeable and indexed. No duplicate members.

"""

import my_list
import my_tuple
import my_set
import my_dict

def main(_choose):
    
    if _choose == 'list':
        my_list.study()
    elif _choose == 'tuple':
        my_tuple.study()
    elif _choose == 'set':
        my_set.study()
    elif _choose == 'dict':
        my_dict.study()
    else:
        print("But what did you choose ?? :{}".format(_choose))
    
if __name__ == "__main__":
    
    _choose = input("Choose the structure to study (list, tuple, set, dict): ") 
    
    main(_choose)
