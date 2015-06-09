# -*- coding: utf-8 -*-
"""
Created on Mon Jun 08 11:04:30 2015

@author: Matt
"""

def flip_a_string(my_string):
    """
        take a string and invert it, ie:
        >>> flip_a_string("Jeb")
        "beJ"
    """
    my_list = list(my_string)
    my_list.reverse()
    return "".join(my_list)
        
def am_i_greater_than_40(num):
    return num > 40    
    
def is_i_greater_than_40(num):
    if am_i_greater_than_40(num):
        return "Yes"
    else:
        return "No"
        
#def the_third_element(my_string):
#    return my_list[2]        
        
def which_numbers_are_greater_than_forty(num_list):
    my_bool_list = []
    for i in num_list:
        my_bool_list.append(am_i_greater_than_40(i))
    return my_bool_list
    