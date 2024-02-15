string = "The green, green grass grows"

"""
char_dict = {}
current_char = []
for char in string:
    if char != " ":
        if char not in [",", ".","?","!"]:
            current_char.append(char)
    else:
        if current_char.join() in char_dict:
            char_dict[current_char.join()] += 1
        else:
            char_dict[current_char.join()] = 1

print(char_dict)
"""

string = string.replace(",","").lower()
counter = {}
for word in string.split():
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1
#print(counter)

