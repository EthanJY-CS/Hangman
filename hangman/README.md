# Hangman - A python Introduction Project

> Classic game of hangman, where a few select fruits are given as the words to guess for the user. The user has 5 lives before the man is hanged, don't let him die!

> UML Diagram of Hangman Design
> ![image](https://user-images.githubusercontent.com/78024243/161451078-24a943ea-1035-459e-9697-ffe96a7fc810.png)

## Milestone 1: Ask the user for input - ask_letter() func

So what's the first thing we need, a letter from the user. Sounds pretty simple but even then, we need to assume the user is a dystopian monkey and can break a simple hangman game, and this is where we use error handling. Okay so there's no real error handling code used but what we do is handle their input and check/validate the data making it so our game can still continue.

First we need a loop to continue asking the user for a letter until we know that the user input a valid input. I use lower() straight away on their input as I thought ahead making it easier to compare in our following conditional statements, which are;

- A letter to guess is only 1 character long, any input longer should be dismissed.
- A letter to guess must lie within the alphabet, any other characters should be dismissed.
    - I used ascii to validate the character within the defined range of lowercase alphabet as lower() was used on input.
- A letter to guess must not have already been tried.


```python
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
```

> ![image](https://user-images.githubusercontent.com/78024243/161450589-c8ecc1bc-bd9c-4902-a879-45cccda78fc1.png)

## Milestone 2: Define all the attributes - __Init__() func

To define the class Hangman with attributes, we need to define and assign it's class variables with some values. Using the docstring of the python file, the variables needed are explained with discription, so you then need to translate that into code. All variables have self. as it's a class of Hangman and so to access variables elsewhere, it needs to know it's variables are owned to the instance of itself. The variables are;

- word: (Type str) The word to be guessed picked randomly from the word_list
- word_guessed: (Type list) A list of the letters of the word, with '_' for each letter not yet guessed
- num_letters: (Type int) The number of UNIQUE letters in the word that have not been guessed yet
- num_lives: (Type int) The number of lives the player has
- list_letters: (Type list) A list of the letters that have already been tried

```python
        self.word = word_list[random.randint(0, len(word_list)-1)]
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.list_letters = []
        print("The mystery word has {} characters".format(self.num_letters))
        print("{}".format(self.word_guessed))
```

## Milestone 3: Code logic for checking letter - check_letter() func

After asking the user for a letter and it's validated, we then need to check the letter for if it exists in the word they're trying to guess. First we add the letter to the list of letters guessed. Then the only condition is if the letter exists in the word;

- If it is a correct guess and is in the word, find every time the letter is in the word.
    - this is done using enumerate() and list comprehension to create a list of indeces of where that letter is found in the word, then replaces all empty       spaces with the letter in the word_guessed list. Then print they got a correct guess.
- If not then decrement a life, and print they got an incorrect guess.

```python
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
```

> ![image](https://user-images.githubusercontent.com/78024243/161450622-b0a9e856-18a5-4f46-ad8f-31ddddb2025b.png)


## Milestone 4: Code logic for the game - play_game() func

The game logic now puts all functions together and plays a game of Hangman for which the user is asked for a letter to guess until either they run out of lives or they guess the word correctly. Some fancy (basic) visuals were added for fun, if it wasn't obvious with the added 40 lines of code.

```python
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
```

> ![image](https://user-images.githubusercontent.com/78024243/161450689-1298f461-a88a-4403-a8ff-a83f1096a375.png)
> ![image](https://user-images.githubusercontent.com/78024243/161450743-d8ef906d-871f-42a7-bcb2-12e04b96806e.png)

## Conclusions

Hangman is a classic, very simple, but it's always a good project to refresh my memory as I've had plenty of experience in the past with Computer Science at university, A-levels and GCSE.


