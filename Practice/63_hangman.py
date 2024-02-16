"""101 Python Problems - no 63 Hangman"""
#import module
import random 
MAX_GUESSES = 6

#main game function
def main():
    #Hangman picture
    hangman_drawing = {
        0: " _______     \n"
           " | /   |     \n"
           " |/   (~)    \n"
           " |     |     \n"
           " |  ---+---  \n"
           " |     |     \n"
           " |    / \\   \n"
           " |   /   \\  \n"
           " |           \n"
           " |__________ ",
        1: " _______\n | /   |\n |/   (~)\n |     |\n |  ---+---\n"
           " |     |\n |\n |\n |\n |__________",
        2: " _______\n | /   |\n |/   (~)\n |     |\n |     +   \n"
           " |     |\n |\n |\n |\n |__________",
        3: " _______\n | /   |\n |/   (~)\n |\n |\n"
           " |\n |\n |\n |\n |__________",
        4: " _______\n | /\n |/\n |\n |\n"
           " |\n |\n |\n |\n |__________",
        5: " \n |\n |\n |\n |\n |\n |\n |\n |\n |__________",
        6: "\n"
    }

    #Extract words from text file
    try:
        with open("beowolf.txt") as file:
            word_list = file.read().split()
            for word in word_list:
                word.strip(".,?!();:")
    #print error message if file not found
    except OSError as error:
        print(error)
        print("'beowolf.txt' not found")
        return


    while True:
        no_of_lives = 6
        secret = random.choice(word_list).upper() #Choose a word
        guesses = set()
        succeeded = False

        while no_of_lives > 0 and not succeeded:
            #Display current result
            print("".join(x if x in guesses else "-" for x in secret))
            #Ask for a guess
            guess = input(str(no_of_lives)
                          + ' lives remaining, '
                          + '"' + ''.join(guesses) + '"'
                          + ' chosen so far. Enter letter: '
                          ).upper()
            #check if guessed letter is in the chosen word
            if guess not in secret:
                print('Nope')
                if guess not in guesses:
                    no_of_lives -= 1
            #print the hangman drawing if wrong guess
            print(hangman_drawing[no_of_lives])
            #Check if current result is equal to the chosen word
            guesses.add(guess)
            if set(secret).issubset(guesses):
                succeeded = True

        #Display Answer
        if not succeeded:
            print('---\nYou failed! The word was', secret)
        else:
            print('---\nWell done! The word was', secret)
        #Exit point / New Game?
        if input('Another game? ').upper()[0] != 'Y':
            print('Exiting game.')
            break
        print('\n\n\nNew game.')


main()
