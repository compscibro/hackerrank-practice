'''
Problem 8: Exclusive Elements
Given two lists lst1 and lst2, write a function exclusive_elemts() that returns a new list
that contains the elements which are in lst1 but not in lst2 and the elements that are in
lst2 but not in lst1.
'''

def exclusive_elemts(lst1, lst2):
	pass

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
exclusive_elemts(lst1, lst2) # ["pooh", "roo", "eeyore", "owl"]

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
exclusive_elemts(lst1, lst2) # ["pooh", "roo", "piglet", "eeyore", "owl", "kanga"]

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
exclusive_elemts(lst1, lst2) # []