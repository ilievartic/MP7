# MP7
#Our MP7 project

def game():
    print("Type the corresponding number for the game you wish to play:")
    print("1. Battleship")
    print("2. Hangman")
    chosen = input("")
    if chosen == "2":
        hangman()
def guess(guess, word, lim):
    
    return word.find(guess,lim,len(word))
        
def setWord():
    word = input("What word should your opponent guess?")
    word = " " + word 
    return word.capitalize()
def pos1():
    print("     ________             ")
    print("    |        |         ")
    print("    |                    ")
    print("    |                     ")
    print("    |                     ")
    print("    | ")
    print("---------------------      ")
def pos2():
    print("     ________             ")
    print("    |        |         ")
    print("    |        O            ")
    print("    |                    ")
    print("    |                     ")
    print("    | ")
    print("---------------------      ")
def pos3():
    print("     ________             ")
    print("    |        |         ")
    print("    |        O            ")
    print("    |        |              ")
    print("    |                     ")
    print("    | ")
    print("---------------------      ")
def pos4():
    print("     ________             ")
    print("    |        |         ")
    print("    |        O            ")
    print("    |       /|              ")
    print("    |                    ")
    print("    | ")
    print("---------------------      ")
def pos5():
    print("     ________             ")
    print("    |        |         ")
    print("    |        O            ")
    print("    |       /|\              ")
    print("    |                    ")
    print("    | ")
    print("---------------------      ")
def pos6():
    print("     ________             ")
    print("    |        |         ")
    print("    |        O            ")
    print("    |       /|\              ")
    print("    |         \             ")
    print("    | ")
    print("---------------------      ")
def pos7():
    print("     ________             ")
    print("    |        |         ")
    print("    |        O            ")
    print("    |       /|\              ")
    print("    |        /\             ")
    print("    | ")
    print("---------------------      ")
def show(tries):
    if tries==6:
        pos1()
    if tries==5:
        pos2()
    if tries==4:
        pos3()
    if tries==3:
        pos4()
    if tries==2:
        pos5()
    if tries==1:
        pos6()
    if tries==0:
        pos7()
def hangman():
    word = setWord().capitalize()
    hint = input("Give the opponent a hint (book,person,place):")
    print("                      "*400)
    tries = 6
    sofar = []
    used = ""
    pos = 1
    new = ""
   
    for c in range(0,len(word)-1):
        sofar.append( " _")
    print(" ")
    print("                                         HANGMAN")
    print("*Hint: " + hint)
    while pos < len(word):
        if guess(" ",word,pos) > 0:
            sofar[guess(" ",word,pos)-1]="  "
        pos = pos + 1
    pos = 1
        
    while tries>0:
        
        guessed = input("Letter? ")
        
        while pos < len(word):
            if guess(guessed,word,pos) > 0:
                sofar[guess(guessed,word,pos)-1]=" " + guessed
            pos = pos + 1
        pos = 1
        for x in range(0, len(word)-1):
            new = new + sofar[x]
        if not guess(guessed,word,pos) > 0:
           tries = tries - 1
        show(tries)    
        print(new)
        if new.find("_",0,len(word)*2)==-1:
            print(" ")
            print("                                       YOU WON !!!")
            break
        new = ""
                
        if not guess(guessed,word,pos) > 0:
           
           
           used = used + " " + guessed
           print("You've got " + str(tries) + " tries left")
           print("Used letters:" + used)

    print("         ")
    print("                                      GAME OVER !!!")     
    
 
