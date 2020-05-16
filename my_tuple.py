# https://www.w3schools.com/python/python_tuples.asp

"""
TUPLE

built-in methods:
 
count() -   Returns the number of times a specified value occurs in a tuple
index() -   Searches the tuple for a specified value and returns the position of where it was found

"""

def study():

    _tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    
    print('\n')
    
    print('Complete starting TUPLE: {}'.format(_tuple))
    
    print('\n')
    print('##################')
    print('## ACCESS items ##')
    print('##################')
    print('- Item index 1  --> {}'.format(_tuple[1]) )
    print('- Item index -1 --> {}'.format(_tuple[-1]) )
    print('- Items range index 2:5   --> {}'.format(_tuple[2:5]) )
    print('- Items range index :4    --> {}'.format(_tuple[:4]) )
    print('- Items range index 2:    --> {}'.format(_tuple[2:]) )
    print('- Items range index -4:-1 --> {}'.format(_tuple[-4:-1]) )
    print('\n')

    print('######################')
    print('## LOOP, FIND items ##')
    print('######################')
    
    # LOOP THROUGH A LIST
    print('- FOR loop on tuple and print individual elements')
    for x in _tuple:
        print('     {}'.format(x))
        
    # CHECK IF ITEM EXISTS
    if "banana" in _tuple:
        print("- Yes, 'banana' is in the fruits tuple")
    print('\n')

    
    print('################################')
    print('## EMPTY, JOIN, BUILD a tuple ##')
    print('################################') 
    
    # EMPTY a list
    print('# EMPTY #')
    print('- Before DEL tuple: {}'.format(_tuple))
    del _tuple
    try:
        print(_tuple)
    except Exception as e:
        print('- Post DEL tuple: the print (_tuple) fails because the tuple no longer exists')
    print('-------------------------------------------------------')
    # JOIN two tuple
    print('# JOIN #')
    _tuple1 = ("a", "b" , "c")
    _tuple2 = (1, 2, 3)
    _tuple3 = _tuple1 + _tuple2
    print('- Print tuple1:                        {}'.format(_tuple1))
    print('- Print tuple2:                        {}'.format(_tuple2))    
    print('- Print tuple3 JOIN tuple1 and tuple2: {}'.format(_tuple3))
    print('-------------------------------------------------------')
    # BUILD a tuple
    print('# BUILD #')
    _tuple = tuple(("apple", "banana", "cherry"))
    print('- Post   TUPLE constructor: {}'.format(_tuple))
    
    print('\n')
