import random
from wordsforhangman import word_list
#randomใช้สำหรับสุ่มคำออกมาจาก wordsforhangman


def get_word():
    word = random.choice(word_list)
    return word.upper()
#รับคำจาก word_list(ตัวแปรในwordsforhangman)


def play(word):
    word_completion = "_" * len(word)#_ _ _ ช่องว่างสำหรับใส่ตัวอักษร
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")#Introduction
    print(display_hangman(tries))#เสา
    print(word_completion)#_ _ _ ช่องว่างสำหรับใส่ตัวอักษร
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter")
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("YAYYY", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word")
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("T_T Out of tries. The word was " + word + ". Maybe next time!")



def display_hangman(tries):
    stages = [  # หัว + ลำตัว + แขนซ้าย + แขนขวา + ขาซ้าย + ขาขวา ตายแน่ๆ
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # หัว + ลำตัว + แขนซ้าย + แขนขวา + ขาซ้าย
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # หัว + ลำตัว + แขนซ้าย + แขนขวา
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # หัว + ลำตัว + แขนซ้าย
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # หัว + ลำตัว
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # หัว
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # เริ่มต้น
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    if input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)
    else:
        print("Okay, Maybe let's play later")

main()
