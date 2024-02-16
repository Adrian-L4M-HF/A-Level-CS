"""Word Score"""
word = input("Type a word: ").upper()
wordScore = 0
addition = ""
 
for letter in word:
  letterValue = ord(letter) - 64
  if (addition == ""):
    addition = str(letterValue)
  else:
    addition = addition + " + " + str(letterValue)
  wordScore += letterValue
  
print(f"{addition} = {str(wordScore)}%")