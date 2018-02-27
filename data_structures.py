# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:06:49 2018

@author: shravan
"""

""" ********** Dictionaries in python *********** """"


""" converting 2 lists into a dictionary in python """
a = ['a','c','b','f','d']
b = [1,3,2,6,4]

dictVal = dict(zip(a,b))
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 6}    


""" sorting the dictionaries  """

sorted(dictVal.values())

sorted(dictVal) # sorts the keys of dictionaries

# sorting the keys using dict values

sorted(dictVal, key=dictVal.__getitem__)

#sort the dict values using dict keys

[v for k,v in sorted(dictVal.items())]
