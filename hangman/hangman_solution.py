'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):

        self.word = word_list[random.randint(0, len(word_list)-1)]
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.list_letters = []
        print("The mystery word has {} characters".format(self.num_letters))
        print("{}".format(self.word_guessed))

        pass

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''

        self.list_letters.append(letter)
        if letter in self.word:
            idx = [i for i, char in enumerate(self.word) if char == letter]
            for index in idx:
                self.word_guessed[index] = letter
            print('Nice! {} is in the word!'.format(letter))
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print('Sorry, {} is not in the word.'.format(letter))
            print('You have {} lives left.'.format(self.num_lives))
        pass

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''

        while True:
            letter = input("Enter a letter to guess: ").lower()
            lengthOfGuess = len(letter)
            if lengthOfGuess > 1:
                print("Please, enter just one character")
                continue
            asciiChar = ord(letter)
            if not(asciiChar >= 97 and asciiChar <= 122):
                continue
            if not letter in self.list_letters:
                break
            else:
                print("{} was already tried".format(letter))
                continue
        self.check_letter(letter)

        pass

def play_game(word_list):

    game = Hangman(word_list, num_lives=5)
    visuals = ['   ____ \n' +
               '      | \n' +
               '      | \n' +
               '      | \n' +
               '      | \n' +
               '     _|_\n', 
               '   ____ \n' +
               '  |   | \n' +
               '      | \n' +
               '      | \n' +
               '      | \n' +
               '     _|_\n',
               '   ____ \n' +
               '  |   | \n' +
               '  O   | \n' +
               '      | \n' +
               '      | \n' +
               '     _|_\n',
               '   ____ \n' +
               '  |   | \n' +
               '  O   | \n' +
               ' \|/  | \n' +
               '      | \n' +
               '     _|_\n',
               '   ____ \n' +
               '  |   | \n' +
               '  O   | \n' +
               ' \|/  | \n' +
               '  |   | \n' +
               '     _|_\n',
               '   ____ \n' +
               '  |   | \n' +
               '  O   | \n' +
               ' \|/  | \n' +
               '  |   | \n' +
               ' / \ _|_\n',]
    
    while True:
        print(visuals[5 - game.num_lives])
        game.ask_letter()
        if game.num_lives == 0:
            print(visuals[5 - game.num_lives])
            print('You lost! The word was {}'.format(game.word))
            break
        if not '_' in game.word_guessed:
            print('Congratulations! You won!')
            break
    
    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
