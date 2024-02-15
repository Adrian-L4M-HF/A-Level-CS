"""binary to decimal"""
def bin2dec (binary=None):
# ask user to input a binary number
    if not binary:
        binary=input("Enter a binary number: ")
# check if it is really a binary number 
    for x in binary:
        if x != "1" and x != "0":
           return("invalid binary number")
# binary number to decimal number
    decimal=0
    for index in binary:
        binaryNum=int(index)
        decimal = decimal*2 + binaryNum
    return(f"Equivalent decimal number is: {decimal}")
# call function
print(bin2dec())    


"""decimal to binary"""
def dec2bin (decimal=None):
# ask user to input a decimal number
    if not decimal:
        decimal=input("Enter a decimal number: ")
# decimal number to "reversed" binary number in a list
    BinaryList=[]
    DividedNum=int(decimal)    
    while DividedNum > 0:
         Remainder = str(DividedNum % 2)
         BinaryList.append(Remainder)
         DividedNum = DividedNum // 2
# Turn the list to string
# reverse the "reversed" binary number to binary number
    Binary=""
    for string in BinaryList:
        Binary += string
    Binary=Binary[::-1]         
    return (f"Equivalent binary number is: {Binary}")
# call fuction         
print(dec2bin())        
    
