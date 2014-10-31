#HANGMANG: THE VIDEO GAME 2K14


#You have guessed 
#Letters: a b c etc

#LETTERS
letters1 = []
letters2 = []
letters3 = []
#SPACE FOR 2 WORDS
space=[" "]
#UNDERSCORE
unknown = []
#NUMBER CHANGES CHANCES
difficulty = []

guessnum = []



#FUNCTION FOR DIFFICULTY CHANGE
def difficulty():
    global diff
    for i in range(1):
        diff=int(input("What difficulty would you like? 6 = Easy, 5 = Medium, 4 = Hard"))

        
#FUNCTION THAT GRABS WORDS FROM P1
def new_words():
    global o, wr1 ,wr2 ,letters1, letters2,letters3
    
    
    o=int(input("Number of words Player 1 would like to input"))	
    
    for i in range(1):
        if o == 2:
            wr1=input("The word1")
            letters1.extend(wr1)
            wr2=input("The word2")
            letters2.extend(wr2)
            letters3.append(letters1+space+letters2)
                        
            print letters3      
            
            
     
        
        if o == 1:
            wr1=input("The word1")
            letters1.extend(wr1)
            print letters1
         
    
    
def hide_words():
    global unknown, o, letters1, letters2
    
    if o == 2:
        for i in range(len(letters1)):
            unknown.append("_")
        for p in range(len(space)):
            unknown.append(" ")
        for z in range(len(letters2)):
            unknown.append("_")
        
    if  o == 1:
        for i in range(len(letters1)):
            unknown.append(" ")
                           
        
    print unknown
    
def reveal_letter():
    n=input("What is your guess?")
    if n in wr1:
        print "gj"
#Have it index form letters and then remove and replace unknown            
    
    
    
def play_game():
    
    difficulty()
    new_words()
    hide_words()
    reveal_letter()

play_game()
