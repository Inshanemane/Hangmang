#HANGMANG: THE VIDEO GAME 2K14


letters1 = []
unknown = []

def new_words():
    global n
    global wrs
    global letters
    n=int(input("Number of words Player 1 would like to input"))	
    
    for i in range(n):
        wrs=input("The words")
        letters.extend(wrs)
        letters.append(" ")   
    letters.pop(len(letters)-1)
    
    print letters


def hide_words():
    global n
    global letters
    
    
    for i in range(len(letters)):
        unknown.append("_")
    

        

        
    
    print unknown
    
    
def play_game():
    
    new_words()
    hide_words()
    
play_game()
