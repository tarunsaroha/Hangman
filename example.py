import string
from words import choose_word
from images import IMAGES

def is_word_guessesd(secret_word,letters_guessed):
    return False
index=0
guessed_word=""
while(index<len(secret_word)
    if(secret_word[index] in (letters_word + (secret_word[index])
    else:
        (guessed_word+="_")
    index+=1
    (return(guessed_word)
def get_available_letters(letters_guessed)
    import string
    letters_left=string.ascii_lowercase
    return letters_left

def hangman(secret_word):
    print("welcome to the game,hangman")
    print("I am thinking of a word that is" + str(len(secret_word))+"letters long.")
    print("")

letters_guessed=[]
available_letters=get_available_letters(letters_guessed)
print("available_letters: + available_letters")

guess=input("please guess letter")