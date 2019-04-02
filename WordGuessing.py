#Steal this code for your own projects to learn if you would like!
#I would recommend using this if you are a beginner like me,
#I am currently writing this program on my first day so hopefully you get
#Some use out of this! -GitHubRootADMIN

import random

#This is the list of words, it picks one and than you have to guess what word it is. You can add more
#By following what I did
word = random.choice(('github', 'microsoft', 'netgear', 'linksys', 'samsung', 'nvidia', 'gigabyte', 'corsair', 'zotac'))
clue = word[0] + word[::-1][0]
word_guess = ''
store_letter = ''

#I would recommend to just not touch count
count = 0

#This is how many letter guesses it will give you
limit = 4

#What prints out at the beginning to welcome and shit
print('Welcome to the Word Guessing Game!')
print('Visit my GitHub page at: GitHubRootADMIN')

#Tells you to guess a letter. Count is 1 because it takes 1 letter
while count < limit:
    letter_guess = input('Guess a letter: ')
    count += 1

#This basically tells it, if its one of the letters to display correct and if it doesnt display incorrect
    print("Correct") if letter_guess in word else print("Incorrect")
    store_letter += letter_guess

#Asks you yes or no if you would like a clue.
    if count == 2:
        clue_request = input('Would you like a clue? [y / n] \n')
        if clue_request in ["y", "yes", "left"]: 
            print('\nCLUE: The first and last letter of the word is: ', clue)
        if clue_request in ["n", "no", "right"]:
            print("Making it hard for yourself, huh")

#Asks at the end for the word and shows you the letters you have guessed
print('Now its time to guess. You have guessed',len(store_letter),'letters correctly.\n')
print('These letters are: ', store_letter)

word_guess = input('Guess the whole word: ')

#Tells you if the word you guessed was correct or not
if word_guess.lower() == word:
    print('Congrats!')
else:
    print('Unlucky! The answer was,', word)

input('Press Enter to leave the program\n')
