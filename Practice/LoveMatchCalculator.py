#Love Match Calculator - www.101computing.net/love-match-calculator/  
print("*****************************")  
print("*   Love Match Calculator   *")  
print("*****************************")  
  
#Retrieve User Inputs  
name1=input("Type a firstname: ").lower()  
name2=input("Type another firstname: ").lower() 
  
#Initialise key variables  
score=0  
vowels=["a","e","i","o","u","y"]  
consonants=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]  
vowelsInName1=0  
vowelsInName2=0  

#Check if both names have the same number of characters  
if len(name1)==len(name2):  
  score += 20  
 
#Check if both names start with a vowel  
if (name1[0] in vowels) and (name2[0] in vowels):  
    score += 10  
  
#Check if both first names start with a consonant
if (name1[0] in consonants) and (name2[0] in consonants):  
    score += 5 
     
#Check if both first names have the same number of vowels
def vowelInNameCounter(name, vowel_In_Name):
    for letter in name:
        if letter in vowels:
            vowel_In_Name += 1
    return vowel_In_Name
No_of_vowels_in_1 = vowelInNameCounter(name1, vowelsInName1)
No_of_vowels_in_2 = vowelInNameCounter(name2, vowelsInName2)
if  No_of_vowels_in_1 == No_of_vowels_in_2:
    score += 12

#Check if both first names have the same number of consonants
consonant_in_name1 = len(name1) - No_of_vowels_in_1
consonant_in_name2 = len(name2) - No_of_vowels_in_2
if consonant_in_name1 == consonant_in_name2:
    score += 12

#Check if both first names contain at least a “l”, “o”, “v” or “e”
def loveCheck(name):
    Love = "love".split()
    for letter in name:
        if letter in Love:
            return True
    return False
if loveCheck(name1) == True and loveCheck(name2) == True:
    score += 7

#Display final love match score  
print("Your love match score is: " + str(score))