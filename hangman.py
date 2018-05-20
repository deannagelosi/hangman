import random
import os

def pick_word(words):
    """Selects a word randomly from a predefined list."""
    selection = random.choice(words)
    return selection

def word_to_list(selection):
    """Transforms word to a list with each letter in a seperate index."""
    longer = list(selection)
    return longer

def generate_hangman(lives):
    """Creates a hangman as user guesses incorrect letters"""
    clear_screen()
    print """
         _   _                                         
        | | | |                                        
        | |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
        |  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        \_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |                      
                           |___/                       """
    if len(lives) == 7:
        print """ 
                ____
               |    |       
               |     
               |        
               |     
               |    
              _|_
             |   |______
             |          |
             |__________| """
    if len(lives) == 6:
        print """
                ____
               |    |       
               |    o 
               |        
               |     
               |    
              _|_
             |   |______
             |          |
             |__________| """ 
    if len(lives) == 5:
        print """
                ____
               |    |       
               |    o 
               |    |    
               |     
               |    
              _|_
             |   |______
             |          |
             |__________| """
    if len(lives) == 4:
        print """
                ____
               |    |       
               |    o 
               |   /|    
               |     
               |    
              _|_
             |   |______
             |          |
             |__________| """
    if len(lives) == 3:
        print """
                ____
               |    |       
               |    o 
               |   /|\    
               |     
               |    
              _|_
             |   |______
             |          |
             |__________| """
    if len(lives) == 2:
        print """
                ____
               |    |       
               |    o 
               |   /|\    
               |    | 
               |    
              _|_
             |   |______
             |          |
             |__________| """ 
    if len(lives) == 1:
        print """
                ____
               |    |       
               |    o 
               |   /|\    
               |    | 
               |   /
              _|_
             |   |______
             |          |
             |__________| """
    if len(lives) <= 0:
        print """
                ____
               |    |       
               |    o 
               |   /|\    
               |    | 
               |   / \\
              _|_
             |   |______
             |          |
             |__________| """ 
    # make_space()
    print
  
def check_letter(guess, divided, progress, lives, guessed_letters):
    """Cross checks guessed letter with selected word. If they are equal, fills 
    in the word for the user with the correct letter."""
    
    generate_hangman(lives)
    # first, check if guess is valid
    if guess.isalpha() == False:
        print "Please enter a letter."
        return
    if len(guess) != 1:
        print "Please enter one letter at a time."
        return
    if guess in progress or guess in guessed_letters:
        print "This letter has already been entered. Please try again."
        return

    # then use guess in game
    count = 0
    if guess in divided:
        for letter in divided:
            if letter == guess:
                progress[count] = guess
            count += 1  
    else:
        guessed_letters.append(guess)
        del lives[0]
        generate_hangman(lives)

    
def clear_screen():
    """Clears the previous screen and pushes text to the top"""
    os.system('clear')

def play_game(words):
    """The game runs and checks for progress and ends when the game is won or 
    lost."""
    word = pick_word(words)
    divided = word_to_list(word)
    lives = ['X', 'X', 'X', 'X', 'X', 'X', 'X']
    progress = ['_ ' for x in range(len(divided))]
    guessed_letters = []
    
    generate_hangman(lives)
    while len(lives) > 0:
        if progress == divided:
            print "\n\nYou win! The word is {}.".format(word)
            break
        print "\n\nYour word: " + " ".join(progress)
        print "\n\nGuessed letters: " + ", ".join(guessed_letters)
        guess = raw_input("\n\nGuess a letter: ").lower()
        check_letter(guess, divided, progress, lives, guessed_letters)
    else:
        generate_hangman(lives)
        print "\n\nGuessed letters: " + ", ".join(guessed_letters)
        print "\n\nYou lose. The word is {}.".format(word)

def run_program():
    """The welcome screen and controls when the game is run."""

    words = ['feminist', 'patriarchy', 'misogyny', 'cisgender', 'privledge', 
            'sexism', 'intersectionality', 'racism', 'heteronormative',
            'mansplaining', 'discrimination', 'empowerment', 'marginalize',
            'objectification', 'oppression', 'sexuality', 'stereotyping']

    play = True   
    while play == True:
        play_game(words)
        response = None
        while response is None:
            response = raw_input("\n\nWould you like to play again? (y/n): ").lower()
            if response == "y" or response == "yes":
                play = True
            elif response == "n" or response == "no":
                play = False
                print "See you next time!"
            else:
              response = None
              generate_hangman(['X', 'X', 'X', 'X', 'X', 'X', 'X'])
              print "\n\nI'm sorry, I didn't understand."

run_program()
