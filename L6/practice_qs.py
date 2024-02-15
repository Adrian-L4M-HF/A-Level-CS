"""Practice programming task questions"""

# Q1
# Write a function which checks to see if numbers are primes.
# The function should accept a list of numbers to be checked, and return
# a list of the same length, consisting only of True and False values.
#
# eg. if [1,4,6,7,9] is passed to the function,
# it will return [True, False, False, True, False]
# (remove the 'raise NotImplementedError' lines)


def isPrime(number):
    """Check if a number is prime"""
    if number < 2 or type(number) == float: 
        return False
    for divisor in range(2, number): 
        if number % divisor == 0:
            return False
            break
    return True

def prime_checker(integer_list):
    """Return a list of booleans showing 
    True if number is prime and False if not prime"""
    bool_list = []
    for number in integer_list:
        if isPrime(number) == False:
            bool_list.append(False)
        elif isPrime(number) == True:
            bool_list.append(True)
    return bool_list


# Q2
# Write a function that takes two words as arguments and returns a boolean
# to say if the first word can be created from letters of the second word.
# Each letter can only be used once.
#
# eg. EAT can be formed from ATE
#     EAT can be formed from HEART
#     TO can be formed from POSITION
# but MEET cannot be formed from the word MEAT, as the second word has
# one E while the first word needs two Es.
#
# assume all words are lower-case.

def letter_in_word(word):
    """Take a word and return a letter frequency dictionary"""
    dict_word = {}
    for letter in word:
        if letter not in dict_word:
            dict_word[letter] = 1
        else:
            dict_word[letter] += 1
    return dict_word

            
def word_in_word(word1, word2):
    """takes two words as arguments and returns a boolean 
    to say if the first word can be created from letters of the second word."""
    word1, word2 = word1.upper(), word2.upper()
    dict_word1 = letter_in_word(word1)
    dict_word2 = letter_in_word(word2)
    for letter in dict_word1:
        if (letter not in dict_word2) or (dict_word2[letter] < dict_word1[letter]):
            return False
    return True
