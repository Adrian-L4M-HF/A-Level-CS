#Task 1
string = input("Please input a string: ")
char_list = []
number_list = []

def RLE(string):
    char_list.append(string[0])
    number_list.append(1)
    for index, char in enumerate(string[1: len(string)-1]):
        if char == char_list[index-1]:
            number_list[index] += 1
        else:
            number_list.append(1)
    return 



for i in char_list:
    for j in number_list:
        print(f"{i} {j}")
        
