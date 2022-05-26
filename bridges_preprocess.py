# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 00:16:43 2022

@author: User
"""

def solution(A):
    # write your code in Python 3.6
    prev = 0
    smallest = 0
    A = sorted(set(A))
    prev = 0
    for i in range(0, len(A) - 1):
        # if A[i] < 0:
        #     continue
        
        if A[i] > 0: 
            if A[i+1] - A[i] >  1:
                return (A[i]+ 1)
            else:
                prev = i
    return 0



solution([1, 3, 6, 4, 1, 2])