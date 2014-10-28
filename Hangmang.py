#HANGMANG: THE VIDEO GAME 2K14

import math
import random
import simplegui

global WORDBANK

global wrs

wrs=()


def printwords(wrs):
    WORDBANK = []
    n=int(input("Number of words"))	
    for i in range(n):
        wrs=input("The words")
        WORDBANK.append(wrs)
    return 

print WORDBANK
