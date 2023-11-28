# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 13:56:45 2021

@author: nikhi
"""


def primenumber(x):
    if x>1:
        for i in range(2,x):
            if(x % i) == 0:
                print(x,"is not a prime Number")
                break
            else:
                print(x,"is a prime number")
    else:
        print(x,"is not a prime number")
                