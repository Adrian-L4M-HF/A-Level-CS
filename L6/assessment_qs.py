"""Summer programming assessment questions."""

# Q1
# Write a function that takes a list of digits and returns the number of times
# that the most frequent digit appears. If there are two most numbers that share
# the same frequency then instead return the string "Data was multimodal".
# (Digits can be assumed to be 1, 2, 3, 4, 5, 6, 7, 8, 9 and 0 only.)

def mode(number_list):
    """takes a list of digits and returns the number of times
       that the most frequent digit appears. If there are two most numbers that share
       the same frequency then instead return the string "Data was multimodal"."""
    freq_dict = {}
    for number in number_list:
        if number not in freq_dict:
            freq_dict[number] = 1
        else:
            freq_dict[number] += 1
    max_nums = []
    for number in freq_dict:
        if len(max_nums) == 0:
            max_nums.append(number)
        elif freq_dict[number] == freq_dict[max_nums[0]]:
            max_nums.append(number)
        elif freq_dict[number] > freq_dict[max_nums[0]]:
            max_nums.clear()
            max_nums.append(number)
    if len(max_nums) > 1:
        return "Data was multimodal"
    else:
        return str(freq_dict[max_nums[0]])

# Q2
# One method that can be used to compress text data is run length encoding
# (RLE). When RLE is used the compressed data can be represented as a set of
# character/frequency pairs. When the same character appears in consecutive
# locations in the original text it is replaced in the compressed text by a single
# instance of the character followed by a number indicating the number of
# consecutive instances of that character. Single instances of a character are
# represented by the character followed by the number 1.

# Examples of how text would be compressed using:

# Original text: AAARRRRGGGHH
# Compressed text: A3R4G3H2

# Original text: CUTLASSES
# Compressed text: C1U1T1L1A1S2E1S1

# Write a function that will perform the compression process described above,
# returning the compressed data as a string.

def rle(original_text):
    """transform a text string into RLE compressed text"""
    list_of_original_text = list(original_text)
    list_of_compressed_text = []
    freq_dict = {}
    freq_dict[list_of_original_text[0]] = 1
    for letter1 in list_of_original_text[1:]:
        for letter2 in list_of_original_text: 
            if letter1 != letter2: 
                freq_dict[letter1] = 1 
            else:
                freq_dict[letter1] += 1
    for index in freq_dict:
        list_of_compressed_text.append(freq_dict[index])
    return str(list_of_compressed_text)   
            
            
