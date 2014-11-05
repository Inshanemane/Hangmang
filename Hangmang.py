#HANGMANG: THE VIDEO GAME 2K14

#LETTERS
letters1 = []
letters2 = []
letters3 = []

#SPACE FOR 2 WORDS
space=[" "]
space2=(" ")

#UNDERSCORE
unknown = []

#NUMBER CHANGES CHANCES
difficulty = []

#List that reveals correctly guessed letters
guesslist = []

#WIN, when the win hits the max game beat
win = 0

#LOSE, when the lose hits the max game over
lose = 0

print "                                _____ "
print "|        |     /\     |\     | |        "              
print "|        |    /  \    | \    | |         "         
print "||||||||||   /____\   |  \_  | |   ___    "                
print "|        |  /      \  |    \ | |      |    "              
print "|        | /        \ |     \| |______|     "                    

print

print "                                _____    "
print "|\      /|     /\     |\     | |          "                
print "| |    | |    /  \    | \    | |           "                                                   
print "| |    | |   /____\   |  \_  | |   ___      " 
print "|  \  /  |  /      \  |    \ | |      |      "  
print "|   \/   | /        \ |     \| |______|       "             

print
print "                 2K14"
print

print "WARNING:"
print "______________________________________________________________________"
print
print "This game is terrible and requires you to input a letter a second time"
print "if there are two or more instances of a letter"
print "______________________________________________________________________"
print



#FUNCTION FOR DIFFICULTY CHANGE
def difficulty():
    global diffi
    
    diffi=int(input("What difficulty would you like? 7=Easy 5=Medium 3=Hard"))
        
        
#FUNCTION THAT GRABS WORDS FROM P1
def new_words():
    global o, wr1 ,wr2, wr3 ,letters1, letters2, letters3, space2
    
    #Determines how many words up to 2
    o=int(input("Number of words Player 1 would like to input, up to 2"))	
    
    for i in range(1):
        if o == 2:
            
            wr1=str.lower(input("The 1st word"))
            
            letters1.extend(wr1)
            
            wr2=str.lower(input("The 2nd word"))
            
            letters2.extend(wr2)
            
            letters3.append(letters1+space+letters2)
            
            wr3 = (wr1+space2+wr2)           
                 
            
            
     
        
        if o == 1:
            
            wr1=str.lower(input("The 1st word"))
            
            letters1.extend(wr1)
            
            wr3 = (wr1)
            
            print letters1
            print 
    
    
def hide_words():
    global guesslist, unknown, o, letters1, letters2
    
    if o == 2:
        for i in range(len(letters1)):
            unknown.append("_")
            guesslist.append("_")
        for p in range(len(space)):
            unknown.append(" ")
            guesslist.append(" ")
        for z in range(len(letters2)):
            unknown.append("_")
            guesslist.append("_")
        
    if  o == 1:
        for i in range(len(letters1)):
            unknown.append("_")
            guesslist.append("_")               
        
    print unknown
    print
    
    
    
def reveal_letter():
    global o, wr1 ,wr2, wr3 ,letters1, letters2, letters3, diffi, win, lose
    
    if o == 2:
        for i in range(len(wr3)-1):
            n=str.lower(input("What is your guess?"))
            if n in wr3:
                pos = wr3.index(n)
                guesslist.pop(pos)
                guesslist.insert(pos,n)
                wr3=list(wr3)
                wr3.pop(pos)
                wr3.insert(pos,"+")
                
                print guesslist     
                print "You guessed", n, "It was correct!"
                print
                win+=1
                
        
        
        
            else:
                print guesslist
                print "You guessed", n, "It was incorrect!"
                print
                lose+=1
                
                
        
        
    if o == 1:
        for i in range(len(wr3)):
            n=input("What is your guess?")
            
            if n in wr3:
                
                pos = wr3.index(n)
                
                guesslist.pop(pos)
                
                guesslist.insert(pos,n)
                
                wr3=list(wr3)
                
                wr3.pop(pos)
                
                wr3.insert(pos,"+")
                
                print guesslist
                print "You guessed", n, "It was correct!"
                print
                win+=1
                print win
        
        
        
            else:
                print guesslist
                print "You guessed", n, "It was incorrect!"
                print
                lose+=1
                
            
          
    
    
def play_game():
    global diffi, lose, win, wr3
    
    difficulty()
    new_words()
    hide_words()
    reveal_letter()

    if lose >= diffi:
        print
        print "You lose"

    if o == 1:
        if win >= (len(wr3)):
            print
            print "You win"
    
    else:
        if win >= (len(wr3)-1):
            print
            print "You win"
    
    
    
play_game()
