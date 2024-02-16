#Scrabble Challenge - 101computing.net/scrabble-challenge

from random import randint

#Using a dictionary we store the Scrabble value of each letter of the alphabet
letterValues= {"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":4,"I":1,"J":8,"K":5,"L":1,"M":3,"N":1,"O":1,"P":3,"Q":10,"R":1,"S":1,"T":1,"U":1,"V":4,"W":4,"X":8,"Y":4,"Z":10}

while True:
    #Let's generate 7 random letters and store them in a list called letters
    randomLetters=[]
    for i in range(0,7):
    	#Use ASCII code to generate  random letter between A (ascii code: 65) to Z (ascii code 90)
    	randomLetter=chr(randint(65,90))
    	randomLetters.append(randomLetter)
    
    print("##################################################")
    print("#                                                #")
    print("#              SCRABBLE CHALLENGE                #")
    print("#                                                #")
    print("##################################################")
    print("\n")
    
    line1 = "" #will be used to display the 7 random letters
    line2 = "" #will be used to display the value of each letter underneath
    
    
    for letter in randomLetters:
      line1 = line1 + "     " + letter
      line2 = line2 + "     " + str(letterValues[letter])
    
    print(line1)
    print(line2)
    
    word=input("\n\nUse the given letters to create a word? ").upper()
    print("\nYour word: " + word)	
    #complete this code to find out if the word given is valid (can only use letters from the 7 letters that have been given)
    #If the word is valid, calculate and display the value of the given word using the value of each letter.
    
    def validation(word):
        for letter in word:
            if letter not in randomLetters:
                return False
        return True
    
    score = 0
    if validation(word) == True:
        for letter in word:
            score += letterValues[letter]    
    else:
        print("Invalid Word")
    print(f"score: {score}")
