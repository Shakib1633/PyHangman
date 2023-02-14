import random
import time

def display(n):
    time.sleep(1)
    if n==6:
        print('   _____ \n'
              '  |      \n'
              '  |      \n'
              '  |      \n'
              '  |      \n'
              '  |      \n'
              '  |      \n'
              '__|__\n')
    elif n==5:
        print('   _____  \n'
              '  |     | \n'
              '  |     | \n'
              '  |       \n'
              '  |       \n'
              '  |       \n'
              '  |       \n'
              '__|__\n')
    elif n==4:
        print('   _____  \n'
              '  |     | \n'
              '  |     | \n'
              '  |     | \n'
              '  |     O \n'
              '  |       \n'
              '  |       \n'
              '__|__\n')
    elif n==3:
        print('   _____  \n'
              '  |     | \n'
              '  |     | \n'
              '  |     | \n'
              '  |     O \n'
              '  |     | \n'
              '  |       \n'
              '__|__\n')
    elif n==2:
        print('   _____  \n'
              '  |     | \n'
              '  |     | \n'
              '  |     | \n'
              '  |     O \n'
              '  |    /|\ \n'
              '  |       \n'
              '__|__\n')
    elif n==1:
        print('   _____  \n'
              '  |     | \n'
              '  |     | \n'
              '  |     | \n'
              '  |     O \n'
              '  |    /|\ \n'
              '  |     |  \n'
              '__|__\n')
    else:
        print('   _____ \n'
              '  |     | \n'
              '  |     | \n'
              '  |     | \n'
              '  |     O \n'
              '  |    /|\ \n'
              '  |     |  \n'
              '  |    / \ \n'
              '__|__\n')
##################################################################################################################################

def gameplay():
    difficulty={"easy":0, "hard":1}
    word_list=[ ["spider","brain","kite","mango","python","color","random"],
                ["acknowledgement","flamingoes","hippopotamus","pythagoras","programming","meticuluos","artillery"] ]


    while True:
        print('\tIn easy mode, all occurences of a guessed letter are shown and the words are shorter in length.')
        print('\tIn hard mode, each guess only shows a single occurence of the letter and the words are longer in length\n')
        s = input("enter difficulty (easy/hard): ")
        if s != "easy" and s!= "hard":
            print("\nEnter again")
        else:
            break

    num=random.randint(0,6)
    word=word_list[ difficulty[s] ][ num ]
    length=len(word)

    flags=[]
    prompt=[]
    for i in range(0,length):
        flags.append(0)
        prompt.append("_")

    numOfGuesses=6
    print(f"Your word is {length} characters long\n")

    count=0
    while True:
        print(f"You have {numOfGuesses} guesses remaining\n")
        display(numOfGuesses)

        letter=input("Enter your guess letter: ")
        guessed=0
        for j in range(0, length):
            if s=="hard":
                if letter == word[j] and flags[j]==0 and guessed==0:
                    prompt[j]=letter
                    flags[j]=1
                    guessed=1
                    count+=1
            elif s=="easy":
                if letter == word[j] and flags[j]==0:
                    prompt[j]=letter
                    flags[j]=1
                    guessed=1
                    count+=1

        string=""
        for i in range(0, length):
            string=string+prompt[i]
        print('Word: ' + string + '\n')

        if guessed == 0:
            numOfGuesses -= 1
        if numOfGuesses == 0:
            display(0)
            print(f"You have failed to guess the word.\n The word was {word}.\n")
            print("Another round perhaps?!\n\n")
            break
        if count == length:
            print("Congrats!! You won.\n")
            print("Another round perhaps?!\n\n")
            break
##########################################################################################################################


print('\n\t\t\tWelcome to Hangman!!!\n\n')

while True:
    q = input('\t\t\tPress the number keys given below. \n'
              '\t\t\t1. Play Game \n'
              '\t\t\t2. Exit \n\n')
    match q:
        case "1":
            print("\n\n")
            gameplay()
        case "2":
            break
        case default:
            print("\t\t\tWrong key pressed. Press again!!!")




