# A simple program to find out an age
Age=float(input("Enter age: "))
if Age<0 or Age>120:
    print("Invalid input")
else:
    Agein2100=str(Age+79)
    print("You will be " +  Agein2100 + " years old in 2100.")
