"""Problem of the week Lent 4"""

#Step 1 Find out all 4 digit square numbers
four_digit_square_number_list = []
for number in range(1,101): #from 1 to 100
    square_number = number**2
    #Check the number of digits of the square number
    if len(str(square_number)) == 4 :
        four_digit_square_number_list.append(square_number)
        
print(f"{four_digit_square_number_list = }\n")

#Step 2 Find out all square numbers that do not always have a remainder of 1
invalid_square_numbers = []
for square_number in four_digit_square_number_list:
    for divisor in [2,3,4,5,6,7,8,9]:
        # "%" means "modulo", it is an operator which returns the remainder
        # "!=" means "not equal"
        if square_number % divisor != 1:
            if square_number not in invalid_square_numbers:
                invalid_square_numbers.append(square_number)
    
print(f"{invalid_square_numbers = }\n")

#Step 3 Compare both list to get Miko's PIN
for square_number in four_digit_square_number_list:
    if square_number not in invalid_square_numbers:
        print(f"Miko's PIN is {square_number}")
        break #Halt the program once the PIN is found
        
