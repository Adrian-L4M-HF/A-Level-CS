with open("word_count_sample.txt",'r') as document:
    doc = document.read()
    text = doc.split()
        
    cleaned_words = []
    for word in text:
        cleaned_words.append(word.strip(".,!?()"))
    
def wordcount(doc):    
    print(f"Characters: {len(doc)}")
    print(f"Words     : {len(cleaned_words)}")
    char = '\n'
    print(f"Lines     : {doc.count(char)+1}")

def n_characters(n):
    n_char_words = []
    for word in cleaned_words:
        if len (word) == n:
           n_char_words.append(word)      
    print(f"{n}_char_words = {n_char_words}")
    print(f"number of {n}_char_words = {len(n_char_words)}")

def word_appeared():
    tally={}
    for word in cleaned_words:
        if word in tally:
           tally[word] += 1
        else:
           tally[word] = 1
    return tally

def most_frequent_word():
    sorted_tally = sorted(word_appeared().items(), key=lambda x:x[1], reverse=True)
    print(f"Most Frequent Word(s) = {sorted_tally[0]}")
    
def main():
    wordcount(doc)
    n_characters(12)
    most_frequent_word()
   
main()