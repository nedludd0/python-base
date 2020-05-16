# https://www.w3schools.com/python/python_dictionaries.asp

"""
DICT

built-in methods:
 
clear()         :   Removes all the elements from the dictionary
copy()          :   Returns a copy of the dictionary
fromkeys()      :   Returns a dictionary with the specified keys and value
get()           :   Returns the value of the specified key
items()         :   Returns a list containing a tuple for each key value pair
keys()          :   Returns a list containing the dictionary's keys
pop()           :   Removes the element with the specified key
popitem()       :   Removes the last inserted key-value pair
setdefault()    :   Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()        :   Updates the dictionary with the specified key-value pairs
values()        :   Returns a list of all the values in the dictionary

"""

from pprint import pprint

def study():

    _dict = {   "brand": "Ford",
                "model": "Mustang",
                "year": 1964
            }

    print('\n')
    
    print('Complete starting DICT: {}'.format(_dict))
    
    print('\n')
    print('##################')
    print('## ACCESS items ##')
    print('##################')
    print('- Model element, direct access --> {}'.format(_dict["model"]) )
    print('- Model element, access with get --> {}'.format(_dict.get("model")) )
    print('\n')

    print('##############################')
    print('## CHANGE, LOOP, FIND items ##')
    print('##############################')
    
    # CHANGE ITEM VALUE
    _dict["brand"] = "Fiat"
    print('- Dictionary after CHANGE brand --> {}'.format(_dict))
    
    print('\n')
    
    # LOOP THROUGH A DICT
    print('- Simple FOR loop on dict and print only key names')
    for x in _dict:
        print('     {}'.format(x))
        
    print('- Simple FOR loop on dict and print only key values')
    for x in _dict:
        print('     {}'.format(_dict[x]))

    print('- Simple FOR loop on dict and print only key values')
    for x in _dict.values():
        print('     {}'.format(x))

    print('- Complete FOR loop on dict and print all')
    for x, y in _dict.items():
        print('     {} = {}'.format(x,y))

    # CHECK IF ITEM EXISTS
    if "model" in _dict:
        print("- Yes, key name 'model' is in the car dict")
    print('\n')
    
    print('##############################')
    print('## ADD, REMOVE, EMPTY items ##')
    print('##############################') 
    
    # ADD Items
    print('# ADD #')
    print('- Before ADD color = Red: {}'.format(_dict))
    _dict["color"]="Red"
    print('- Post   ADD color = Red: {}'.format(_dict))
    
    print('-------------------------------------------------------')
    
    # REMOVE Items
    print('# REMOVE #')
    print('- Before POP color = Red : {}'.format(_dict))
    _dict.pop("color")
    print('- Post   POP color = Red : {}'.format(_dict))

    print('- Before POPITEM         : {}'.format(_dict))
    _dict.popitem()
    print('- Post   POPITEM         : {}'.format(_dict))

    print('- Before DEL brand = Fiat: {}'.format(_dict))
    del _dict["brand"]
    print('- Post   DEL brand = Fiat: {}'.format(_dict))
    
    print('-------------------------------------------------------')

    # EMPTY a dict
    print('# EMPTY #')
    print('- Before CLEAR dict: {}'.format(_dict))
    _dict.clear()
    print('- Post   CLEAR dict: {}'.format(_dict))
    
    _dict = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    
    print('- Before DEL dict: {}'.format(_dict))
    del _dict
    try:
        print(_dict)
    except Exception as e:
        print('- Post DEL dict: the print (_dict) fails because the dict no longer exists')
    
    print('\n')

    print('########################')
    print('## COPY, BUILD a dict ##')
    print('########################') 
    
    # COPY a dict
    print('# COPY #')
    _dict1 = {"brand": "kia", "model":"XX", "year":1976}
    _dict2 = _dict1.copy()
    print('- Print dict1:                 {}'.format(_dict1))
    print('- Print dict2 COPY from dict1: {}'.format(_dict2))
    _dict1 = {"brand": "kia", "model":"XX", "year":1976}
    _dict2 = dict(_dict1)
    print('- Print dict1:                 {}'.format(_dict1))
    print('- Print dict2 DICT from dict1: {}'.format(_dict2))
    print('-------------------------------------------------------')
    # BUILD a dict
    print('# BUILD #')
    _dict1.clear()
    print('- Before DICT constructor: {}'.format(_dict1))
    _dict1 = dict(brand="Ford", model="Mustang", year=1964)
    print('- Post   DICT constructor: {}'.format(_dict1))
    
    print('\n')

    print('############')
    print('## NESTED ##')
    print('############') 
    
    ## Method 1
    myfamily1 = {
        "child1" : {
            "name" : "Emil",
            "year" : 2004
        },
        "child2" : {
            "name" : "Tobias",
            "year" : 2007
        },
        "child3" : {
            "name" : "Linus",
            "year" : 2011
        }
    }
    
    print('Method 1')
    pprint(myfamily1)
    print('\n')
    
    ## Method 2
    child1 = {
        "name" : "Emil",
        "year" : 2004
    }
    child2 = {
        "name" : "Tobias",
        "year" : 2007
    }
    child3 = {
        "name" : "Linus",
        "year" : 2011
    }
    
    myfamily2 = {
        "child1" : child1,
        "child2" : child2,
        "child3" : child3
    }
    
    print('Method 2')
    pprint(myfamily2)
    print('\n')

    ## Method 3
    child1 = {
        "name" : "Emil",
        "year" : 2004
    }
    child2 = {
        "name" : "Tobias",
        "year" : 2007
    }
    child3 = {
        "name" : "Linus",
        "year" : 2011
    }
    
    myfamily3 = dict(child1=child1, child2=child2, child3=child3)

    print('Method 3')
    pprint(myfamily3)
    print('\n')

    ## Method 4
    myfamily4 = dict(   child1={ "name" : "Emil"  , "year" : 2004 }, 
                        child2={ "name" : "Tobias", "year" : 2007 }, 
                        child3={ "name" : "Linus" , "year" : 2011 })

    print('Method 4')
    pprint(myfamily4)
    print('\n')
