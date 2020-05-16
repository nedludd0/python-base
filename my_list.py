# https://www.w3schools.com/python/python_lists.asp

"""
LIST

built-in methods:
 
append()    :   Adds an element at the end of the list
clear()     :   Removes all the elements from the list
copy()      :   Returns a copy of the list
count()     :   Returns the number of elements with the specified value
extend()    :   Add the elements of a list (or any iterable), to the end of the current list
index()     :   Returns the index of the first element with the specified value
insert()    :   Adds an element at the specified position
pop()       :   Removes the element at the specified position
remove()    :   Removes the item with the specified value
reverse()   :   Reverses the order of the list
sort()      :   Sorts the list

"""

def study():

    _list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    
    print('\n')
    
    print('Complete starting LIST: {}'.format(_list))
    
    print('\n')
    print('##################')
    print('## ACCESS items ##')
    print('##################')
    print('- Item index 1  --> {}'.format(_list[1]) )
    print('- Item index -1 --> {}'.format(_list[-1]) )
    print('- Items range index 2:5   --> {}'.format(_list[2:5]) )
    print('- Items range index :4    --> {}'.format(_list[:4]) )
    print('- Items range index 2:    --> {}'.format(_list[2:]) )
    print('- Items range index -4:-1 --> {}'.format(_list[-4:-1]) )
    print('\n')


    print('##############################')
    print('## CHANGE, LOOP, FIND items ##')
    print('##############################')
    
    # CHANGE ITEM VALUE
    _list[0] = "lemon"
    print('- Complete list after CHANGE item index 0 --> {}'.format(_list))
    
    # LOOP THROUGH A LIST
    print('- FOR loop on list and print individual items')
    for x in _list:
        print('     {}'.format(x))
        
    # CHECK IF ITEM EXISTS
    if "banana" in _list:
        print("- Yes, 'banana' is in the fruits list")
    print('\n')


    print('##############################')
    print('## ADD, REMOVE, EMPTY items ##')
    print('##############################') 
    
    # ADD Items
    print('# ADD #')
    print('- Before APPEND papaya: {}'.format(_list))
    _list.append("papaya")
    print('- Post   APPEND papaya: {}'.format(_list))

    print('- Before INSERT fragole at 1: {}'.format(_list))
    _list.insert(1, "fragole")
    print('- Post   INSERT fragole at 1: {}'.format(_list))
    
    print('-------------------------------------------------------')
    
    # REMOVE Items
    print('# REMOVE #')
    print('- Before REMOVE fragole: {}'.format(_list))
    _list.remove("fragole")
    print('- Post   REMOVE fragole: {}'.format(_list))

    print('- Before POP: {}'.format(_list))
    _list.pop()
    print('- Post   POP: {}'.format(_list))
    
    print('- Before DEL from 1: {}'.format(_list))
    del _list[1]
    print('- Post   DEL from 1: {}'.format(_list))
    
    print('-------------------------------------------------------')
    
    # EMPTY a list
    print('# EMPTY #')
    print('- Before CLEAR list: {}'.format(_list))
    _list.clear()
    print('- Post   CLEAR list: {}'.format(_list))
    
    _list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    
    print('- Before DEL list: {}'.format(_list))
    del _list
    try:
        print(_list)
    except Exception as e:
        print('- Post DEL list: the print (_list) fails because the list no longer exists')
    
    print('\n')
    
    print('##############################')
    print('## COPY, JOIN, BUILD a list ##')
    print('##############################') 
    
    # COPY a list
    print('# COPY #')
    _list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    _list2 = _list1.copy()
    print('- Print list1:                 {}'.format(_list1))
    print('- Print list2 COPY from list1: {}'.format(_list2))
    print('-------------------------------------------------------')
    # JOIN two list
    print('# JOIN #')
    _list1 = ["a", "b" , "c"]
    _list2 = [1, 2, 3]
    _list3 = _list1 + _list2
    print('- Print list1:                      {}'.format(_list1))
    print('- Print list2:                      {}'.format(_list2))    
    print('- Print list3 JOIN list1 and list2: {}'.format(_list3))
    print('-------------------------------------------------------')
    # BUILD a list
    print('# BUILD #')
    _list1.clear()
    print('- Before LIST constructor: {}'.format(_list1))
    _list1 = list(("apple", "banana", "cherry"))
    print('- Post   LIST constructor: {}'.format(_list1))
    
    print('\n')
