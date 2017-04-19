# Name:  Debbie Yung
# Student Number:  10417380

# This file is provided to you as a starting point for the "word_game.py" program of Assignment 1
# of CSP1150/CSP5110 in Semester 1, 2016.  It mainly provides you with a suitable list of words.
# Please use this file as the basis for your assignment work.  You are not required to reference it.

#FUNCTIONS

#FUNCTION TO COMPARE TWO WORDS
def compareWords(word1, word2):
    count = 0
    i = 0
    length = len(word1)
    for i in range(length):
        if word1[i] == word2[i]:
            count = count + 1
    return count #RETURNS NUMBER OF LETTERS CORRECT

#FUNCTION TO CHECK INVALID INPUT (REFERENCES CLASS MATERIAL)
def inputInt(prompt):
    while True:
        response = input(prompt)

        try:
            numResponse = int(response)

        except ValueError:
            print('Invalid Input')
            continue

        return numResponse



#RANDOM MODULE
import random

#GAME RESTART LOOP
while True:
    #VARIABLES
    candidateWords = ['AETHER', 'BADGED', 'BALDER', 'BANDED', 'BANTER', 'BARBER', 'BASHER', 'BATHED', 'BATHER', 'BEAMED', 'BEANED', 'BEAVER', 'BECKET', 'BEDDER', 'BEDELL', 'BEDRID', 'BEEPER', 'BEGGAR', 'BEGGED', 'BELIES', 'BELLES', 'BENDED', 'BENDEE', 'BETTER', 'BLAMER', 'BLOWER', 'BOBBER', 'BOLDER', 'BOLTER', 'BOMBER', 'BOOKER', 'BOPPER', 'BORDER', 'BOSKER', 'BOTHER', 'BOWYER', 'BRACER', 'BUDGER', 'BUMPER', 'BUSHER', 'BUSIER', 'CEILER', 'DEADEN', 'DEAFER', 'DEARER', 'DELVER', 'DENSER', 'DEXTER', 'EVADER', 'GELDED', 'GELDER', 'HEARER', 'HEIFER', 'HERDER', 'HIDDEN', 'JESTER', 'JUDDER', 'KIDDED', 'KIDDER', 'LEANER', 'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'LIDDED', 'MADDER', 'MEANER', 'MENDER', 'MINDER', 'NEATER', 'NEEDED', 'NESTER', 'PENNER', 'PERTER', 'PEWTER', 'PODDED', 'PONDER', 'RADDED', 'REALER', 'REAVER', 'REEDED', 'REIVER', 'RELIER', 'RENDER', 'SEARER', 'SEDGES', 'SEEDED', 'SEISER', 'SETTER', 'SIDDUR', 'TEENER', 'TEMPER', 'TENDER', 'TERMER', 'VENDER', 'WEDDER', 'WEEDED', 'WELDED', 'YONDER']
    guessHistory = ['', '', '', '', '', '', '', '']
    won = False
     
    #WELCOME
    print('Welcome to the Guess-The-Word Game')
    
    #SELECT DIFFICULTY
    difficulty = input('Select Difficulty: (Easy [e], Medium [m], hard, [h]) ')
    if difficulty == 'e':
        guessesRemaining = 5
    elif difficulty == 'm':
        guessesRemaining = 4
    elif difficulty == 'h':
        guessesRemaining = 3

        
    print('Password is one of these words:')
      
    #RANDOM WORDS GENERATED
    wordList = random.sample(candidateWords, 8)

    #SET PASSWORD
    password = random.choice(wordList)

    #LOOP USER GUESSES AND OUTCOMES
    while guessesRemaining > 0 and won == False:

        #PRINT WORDLIST, INDICES AND GUESS HISTORY
        for index, words in enumerate(wordList):
            print("{})".format(index+1),words,guessHistory[index])
                #reference http://stackoverflow.com/questions/21542694/difference-between-using-commas-concatenation-and-string-formatters-in-python
        print('\n')
        print('Guesses remaining:', guessesRemaining)

        #USER PROMPT GUESS
        guessNum = inputInt('Guess (enter 1-8):') - 1
        
        guessesRemaining -= 1
        
        wordGuess = wordList[guessNum]
        print('\nYour guess:' '\n'+ wordGuess)

        if wordGuess == password:
            print('Password Correct.')
            won = True
        else:
            lettersCorrect = compareWords(wordGuess, password)
            print('Incorrect. \n')
            guessHistory[guessNum] = "{}/6 correct.".format(lettersCorrect)

    #WIN OR LOSE MESSAGE
    if won == True:
        print('Congratulations, you win!')
    else:
        print('No more guesses. You lost.')

    #RESTART
    restart = input('\nWould you like to play again? y/n ')
    if restart == 'n':
        break
   


