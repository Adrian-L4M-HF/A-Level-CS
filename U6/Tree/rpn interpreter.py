#Iterate through the list
#if operator, then pop top 2 items
#push back in
#return final value

rpn = input("Please enter a reverse polish notation: ").split()

operators = ["+", "-", "*", "/", "%"]
for index, item in enumerate(rpn):
    result = 0
    if item in operators:
        if item == "+":
            result = rpn[index-2]  + rpn[index-1]
        if item == "-":
            result = rpn[index-2]  - rpn[index-1]
        if item == "*":
            result = rpn[index-2]  * rpn[index-1]
        if item == "/":
            result = rpn[index-2]  / rpn[index-1]
        if item == "%":
            result = rpn[index-2]  % rpn[index-1]
        item.pop(index-1)
        item.pop(index-2)

#########################################################
expression = input(">> ")
stack = []

for token in expression.split():
    if token.isnumeric():
        stack.append(int(token))
    else:
        match token:
            case "+":
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            case "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            case "*":
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            case "/":
                b, a = stack.pop(), stack.pop()
                stack.append(a // b)
            case "%":
                b, a = stack.pop(), stack.pop()
                stack.append(a % b)
            case default:
                raise SyntaxError(f"Token: {token}")
            
print(stack)

