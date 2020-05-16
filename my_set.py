# https://www.w3schools.com/python/python_sets.asp

"""
SET

built-in methods:
 
add()                           :   Adds an element to the set
clear()                         :   Removes all the elements from the set
copy()                          :   Returns a copy of the set
difference()                    :   Returns a set containing the difference between two or more sets
difference_update()             :   Removes the items in this set that are also included in another, specified set
discard()                       :   Remove the specified item
intersection()                  :   Returns a set, that is the intersection of two other sets
intersection_update()           :   Removes the items in this set that are not present in other, specified set(s)
isdisjoint()                    :   Returns whether two sets have a intersection or not
issubset()                      :   Returns whether another set contains this set or not
issuperset()                    :   Returns whether this set contains another set or not
pop()                           :   Removes an element from the set
remove()                        :   Removes the specified element
symmetric_difference()          :   Returns a set with the symmetric differences of two sets
symmetric_difference_update()   :   inserts the symmetric differences from this set and another
union()                         :   Return a set containing the union of sets
update()                        :   Update the set with the union of this set and others

"""

def study():

    _set = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
    
    print('\n')
    
    print('Set completo di partenza: {}'.format(_set))
    
    print('\n')
    print('#######################')
    print('## LOOP e FIND items ##')
    print('#######################')
    
    # LOOP THROUGH A SET
    print('- Ciclo FOR su set e print singoli elementi')
    for x in _set:
        print('     {}'.format(x))
        
    # CHECK IF ITEM EXISTS
    if "banana" in _set:
        print("- Yes, 'banana' is in the fruits set")
    print('\n')

    print('##############################')
    print('## ADD, REMOVE, EMPTY items ##')
    print('##############################') 
    
    # ADD Items
    print('# ADD #')
    print('- Before ADD papaya: {}'.format(_set))
    _set.add("papaya")
    print('- Post   ADD papaya: {}'.format(_set))

    print('- Before UPDATE fragole e cocco: {}'.format(_set))
    _set.update(["fragole","cocco"])
    print('- Post   UPDATE fragole e cocco: {}'.format(_set))

    print('-------------------------------------------------------')
    
    # REMOVE Items
    print('# REMOVE #')
    print('- Before REMOVE fragole: {}'.format(_set))
    _set.remove("fragole")
    print('- Post   REMOVE fragole: {}'.format(_set))

    print('- Before DISCARD fragole again will NOT raise an error: {}'.format(_set))
    _set.discard("fragole")
    print('- Post   DISCARD fragole again will NOT raise an error: {}'.format(_set))

    print('-------------------------------------------------------')
    
    # EMPTY a set
    print('# EMPTY #')
    print('- Before CLEAR set: {}'.format(_set))
    _set.clear()
    print('- Post   CLEAR set: {}'.format(_set))

    _set = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    
    print('- Before DEL set: {}'.format(_set))
    del _set
    try:
        print(_set)
    except Exception as e:
        print('- Post   DEL set: il print(_set) va in errore poichè il set non esiste più')
    
    print('\n')

    print('#######################')
    print('## JOIN, BUILD a set ##')
    print('#######################') 
    
    # JOIN two set
    print('# JOIN #')
    _set1 = {"a", "b" , "c"}
    _set2 = {1, 2, 3}
    _set3 = _set1.union(_set2)
    print('- Print set1:                     {}'.format(_set1))
    print('- Print set2:                     {}'.format(_set2))    
    print('- Print set3 UNION set1 and set2: {}'.format(_set3))
    print('-------------------------------------------------------')
    _set1 = {"a", "b" , "c"}
    _set2 = {1, 2, 3}
    _set1.update(_set2)
    print('- Print set1:                  {}'.format(_set1))
    print('- Print set2:                  {}'.format(_set2))    
    print('- Print set1 UPDATE with set2: {}'.format(_set1))
    print('-------------------------------------------------------')    
    # BUILD a set
    print('# BUILD #')
    _set1.clear()
    print('- Before SET constructor: {}'.format(_set1))
    _set1 = set(("apple", "banana", "cherry"))
    print('- Post   SET constructor: {}'.format(_set1))
    
    print('\n')
