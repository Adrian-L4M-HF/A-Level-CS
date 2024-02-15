#<<<Iteration>>>

"""Program A"""
Num=int(input("Enter a number: "))
for i in range(1,Num+1):
    print(i)  
 
"""Program A (While loop)"""
NumWhile=int(input("Enter a number: "))
j=1
while j <= NumWhile:
    print(j)
    j += 1

"""Program B"""
Password="none"
while Password != "turning":
    Password=input("Enter a password: ")
print("Password Correct")

#<<<Subroutines>>>

"""Program A"""
def areaCalc(W,H):
    Area= W * H
    return Area
print(areaCalc(10, 8))

"""Program B"""
def average(A,B,C):
    Total = A + B + C
    Average = Total / 3
    return Average
print(average(4,3,4))

"""Program C"""
def compare(A,B):
    if A > B:
        return A
    else:
        return B
print(compare(6, 4))





