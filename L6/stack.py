string = "abcdefghijklmnopqrstuvwxyz"
stack = []
reverse_stack = ""
#push
for letter in string:
    stack.append(letter)
#pop
while True:
    try:
        reverse_stack += stack.pop()
    except:
        break
print(reverse_stack)