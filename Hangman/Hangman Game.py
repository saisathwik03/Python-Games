
import string
import random
lg=[]
def isWordGuessed(sw, lg):
    count=0
    for char in sw:
        if char in lg:
            count+=1
    return count==len(sw)
# sw="apple"
# lg=['e', 'i', 'k', 'p', 'r', 's']
# print(isWordGuessed(sw,lg))

def getGuessedWord(sw,lg):
    s=''
    for char in sw:
        if char in lg:  #if i in lg:              
            s= s+char      #print(i)
        else:            #else:
            s=s+ '_'         #
            
            
            print("_")
    return s                       

# sw="apple"
# lg=['e', 'i', 'k', 'p', 'r', 's']
# getGuessedWord(sw,lg)

def getAvailableLetters(lg):
    letters=string.ascii_lowercase             
    s = ''                                     
    for char in letters:
        if char not in lg:
            s= s + char
    return s

    

# lg=['e', 'i', 'k', 'p', 'r', 's']
# print(getAvailableLetters(lg))


def loadwords():
    f = open("E:/CSPP/Practice/sgb-words.txt", "r")
    txt=f.read()
    word=chooseword(txt)
    f.close()
    return word
    

def chooseword(txt):
    word_file=txt.split()
    index=random.randint(0, len(word_file)-1)
    word=word_file[index]
    return word


def hangman(sw):
        print(sw)
        print("welcome player!! to the game Hangman")
        print("I am thinking of a word that is", len(sw),"letter")
        print("")
        count=8
        while count>0:
            print("no of guesses remaining:", count)
            print("available letters: ", getAvailableLetters(lg))

            letter=str(input("enter letter to be guessed: "))
            
            if letter in lg:
                print("already exist", getGuessedWord(sw,lg))
                print("")
            else:
                lg.append(letter)
                if letter in sw:
                    print("good guess", getGuessedWord(sw,lg))
                    print("")
                    
                elif letter not in sw:
                    print("try againg for good guess!! ", getGuessedWord(sw,lg))
                    print("")
                    count-=1


            if isWordGuessed(sw,lg):
                print("congartulations", sw , "is your word")
                break
        if count==0:
            print("You ran out of guesses", sw)

sw = loadwords()
sw=sw.lower()
hangman(sw)



