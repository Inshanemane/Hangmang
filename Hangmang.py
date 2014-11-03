#HANGMANG: THE VIDEO GAME 2K14

#You have guessed 
#Letters: a b c etc

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

guesslist = []

win = 0

lose = 0


#FUNCTION FOR DIFFICULTY CHANGE
def difficulty():
    global diffi
    
    diffi=int(input("What difficulty would you like? 9 = Easy, 7 = Medium, 5 = Hard"))
        
        
#FUNCTION THAT GRABS WORDS FROM P1
def new_words():
    global o, wr1 ,wr2, wr3 ,letters1, letters2, letters3, space2
    
    
    o=int(input("Number of words Player 1 would like to input"))	
    
    for i in range(1):
        if o == 2:
            wr1=input("The 1st word")
            letters1.extend(wr1)
            wr2=input("The 2nd word")
            letters2.extend(wr2)
            letters3.append(letters1+space+letters2)
            wr3 = (wr1+space2+wr2)           
            print letters3      
            
            
     
        
        if o == 1:
            wr1=input("The 1st word")
            letters1.extend(wr1)
            print letters1
         
    
    
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
            unknown.append(" ")
            guesslist.append(" ")               
        
    print unknown
    
    
    
    
def reveal_letter():
    global o, wr1 ,wr2, wr3 ,letters1, letters2, letters3, diffi, win, lose
    for i in range(len(wr3)-1):
        n=input("What is your guess?")
        if n in wr3:
            pos = wr3.index(n)
            guesslist.pop(pos)
            guesslist.insert(pos,n)
            print "You guessed", n, "It was correct!"
            print
            win+=1
        	for z in range():
                index = 0
                wr3.find(n,index)
                print n, "found at 
        
        
        
        else:
            print "You guessed", n, "It was incorrect!"
            print
            lose+=1
    
        print guesslist
    
    
    
def play_game():
    global diffi, lose, win, wr3
    
    difficulty()
    new_words()
    hide_words()
    reveal_letter()

    if lose > diffi:
        print
        print "You lose"

    if win > (len(wr3)-2):
        print
        print "You win"
    
play_game()



#LOWERCASE


