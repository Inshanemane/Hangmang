#HANGMANG: THE VIDEO GAME 2K14

letters1 = []
letters2 = []
letters3 = []
space=[" "]
unknown = []
difficulty = []
guessnumber = []




def difficulty():
    global diff
    for i in range(1):
    	diff=int(input("What difficulty would you like? 1 = Easy, 2 = Medium, 3 = Hard"))

        

def new_words():
    global n, wr1 ,wr2 ,letters1, letters2,letters3
    
    
    n=int(input("Number of words Player 1 would like to input"))	
    
    for i in range(1):
        if n == 2:
            wr1=input("The word1")
            letters1.extend(wr1)
            wr2=input("The word2")
            letters2.extend(wr2)
            letters3.append(letters1+space+letters2)
                        
            print letters3      
            
            
     
        
        if n == 1:
            wr1=input("The word1")
            letters1.extend(wr1)
            print letters1
         
    
    
def hide_words():
    global n, letters1, letters2
    
    
    for i in range(len(letters1)):
        unknown.append("_")
    
    for p in range(len(space)):
        unknown.append(" ")
    
    
    for z in range(len(letters2)):
        unknown.append("_")

        
        
    
    print unknown


    
def reveal_letter():
    for i in range():
        input("What is your guess?")
    
            
    
    
    
def play_game():
    
    difficulty()
    new_words()
    hide_words()
    reveal_letter()

play_game()        
        
        
        
        
