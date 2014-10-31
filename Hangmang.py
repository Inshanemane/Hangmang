#HANGMANG: THE VIDEO GAME 2K14


letters1 = []
letters2 = []
letters3 = []

unknown = []

def new_words():
    global n
    global wr1
    global wr2
    global letters1
    global letters2
    global letters3
    
    
    n=int(input("Number of words Player 1 would like to input"))	
    
    for i in range(1):
        if n == 2:
            wr1=input("The word1")
            letters1.extend(wr1)
            letters1.append(" ") 
            wr2=input("The word2")
            letters2.extend(wr2)
            letters2.append(" ") 
            
            letters3.append(letters1+letters2)
    
    
    print letters1
    print letters2
    print letters3
def hide_words():
    global n
    global letters1
    global letters2
    
    
    for i in range(len(letters1)):
        unknown.append("_")
    
    for z in range(len(letters2)):
        unknown.append("_")

        

        
    
    print unknown
    
    
def play_game():
    
    new_words()
    hide_words()
    
play_game()
