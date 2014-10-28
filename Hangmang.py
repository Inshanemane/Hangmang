#HANGMANG: THE VIDEO GAME 2K14

import math
import simplegui



wordbank = []

def new_words():
    global wordbank
    
    n=int(input("Number of words Player 1 would like to input"))	
    
    for i in range(n):
        wrs=input("The words")
        wordbank.append(wrs)
   
    return wordbank

print new_words()

def hide_words():
    global wordbank
    
