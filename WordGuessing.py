#Steal this code for your own projects to learn if you would like!
#I would recommend using this if you are a beginner like me,
#I am currently writing this program on my first day so hopefully you get
#Some use out of this! -GitHubRootADMIN

import random

word = random.choice(('github', 'microsoft', 'netgear', 'linksys', 'samsung', 'nvidia', 'gigabyte', 'corsair', 'zotac'))
clue = word[0] + word[::-1][0]
word_guess = ''
store_letter = ''

count = 0

limit = 4

print('Welcome to the Word Guessing Game!')
print('Visit my GitHub page at: GitHubRootADMIN')

while count < limit:
    letter_guess = input('Guess a letter: ')
    count += 1

    print("Correct") if letter_guess in word else print("Incorrect")
    store_letter += letter_guess

    if count == 2:
        clue_request = input('Would you like a clue? [y / n] \n')
        if clue_request in ["y", "yes", "left"]: 
            print('\nCLUE: The first and last letter of the word is: ', clue)
        if clue_request in ["n", "no", "right"]:
            print("Making it hard for yourself, huh")

print('Now its time to guess. You have guessed',len(store_letter),'letters correctly.\n')
print('These letters are: ', store_letter)

word_guess = input('Guess the whole word: ')

if word_guess.lower() == word:
    print('Congrats!')
else:
    print('Unlucky! The answer was,', word)

input('Press Enter to leave the program\n')
