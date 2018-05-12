# To create a Hangman Game without GUI
import random
import re
import tkinter
from tkinter import messagebox
root =tkinter.Tk()
root.withdraw()

def replaceCorrectChar(chosen_movie,guess):
    # indexOfChar provides all instances where that letter is present in the word
    indexOfChar = [i for i, charac in enumerate(chosen_movie) if charac == guess]
    for i in indexOfChar:
        temp[i] = guess
    temp2 = ''.join(temp)
    print(temp2)
    checkMatch = temp2.replace(' ', '*')
    return checkMatch

movie_list = {1: 'The*Dark*Knight', 2: 'The*Prestige', 3: 'The*Avengers', 4: 'Avatar', 5: 'Star*Wars', 6: 'Inside*Out'}
print('Welcome')
checkMatch = ""
while (1):
    choice = messagebox.askyesno("Hello","Shall We Play?")
    if choice == True:
        chosen_movie = movie_list[random.randint(1,6)]

        # -----------encrypt the randomed movie into dashes------------------
        while (1):
            temp = chosen_movie
            for i in temp:
                if i == '*':
                    temp=temp.replace(i,' ')
                else:
                    temp = temp.replace(i,'-')
            print(temp)
            break
        # -------------------------------------------------------------------

        countMistake = 5 #counter to keep track of mistakes - 7 mistakes are allowed
        temp = list(temp) # to access letters by index and replace, string is converted to list
        chosen_movie=chosen_movie.upper() # easy to compare

        # ------------------Accept One Letter at a time ---------------------
        while(1):
            guess = input("Guess a Letter\n")
            guess=guess.upper()
            if chosen_movie.find(guess)== -1:    #-1 when not found
                countMistake -= 1
                print('This letter is not present-Lost 1 life\n{0} lives remaining'.format(countMistake))
            else:
                checkMatch = replaceCorrectChar(chosen_movie,guess)

            # when string is same as randomed movie- exit else reduce life and try again
            if (checkMatch == chosen_movie):
                print("Congrats")
                break
            elif countMistake==0:
                print("You Lost")
                break
            else:
                continue
        break
        # ---------------------------------------------------------------------
    else:
        print("Some other Time maybe")
        break