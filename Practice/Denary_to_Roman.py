#Roman Numerals Conversion - www.101computing.net/roman-numerals-conversion/  

print(" ---------- Roman Numberals Conversion ----------")  

def Roman_to_Denary(Roman_number):
    denary = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    Denary_number = 0
    for index in range(len(Roman_number)-1):
        s1 = denary[Roman_number[index]]
        s2 = denary[Roman_number[index+1]]
        if s1 >= s2:
            Denary_number += s1
        else:
            Denary_number -= s1
    Denary_number += denary[Roman_number[-1]]
    return Denary_number

def Denary_to_Roman(Denary_number):
    Roman_Number = ""
    while Denary_number > 0:
        if (Denary_number - 1000) >= 0:
            Roman_Number += "M"
            Denary_number -= 1000
        elif (Denary_number - 500) >= 0:
            Roman_Number += "D"
            Denary_number -= 500
        elif (Denary_number - 100) >= 0:
            Roman_Number += "C"
            Denary_number -= 100
        elif (Denary_number - 50) >= 0:
            Roman_Number += "L"
            Denary_number -= 50
        elif (Denary_number - 10) >= 0:
            Roman_Number += "X"
            Denary_number -= 10
        elif (Denary_number - 5) >= 0:
            Roman_Number += "V"
            Denary_number -= 5
        elif (Denary_number - 1) >= 0:
            Roman_Number += "I"
            Denary_number -= 1
    return Roman_Number
#is there a better way?          
            


print(Denary_to_Roman(2017))


def test_single():
    assert Roman_to_Denary(("I")) == 1
    assert Roman_to_Denary(("X")) == 10

    

     
        