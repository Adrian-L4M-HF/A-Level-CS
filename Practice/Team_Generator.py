import random
with open("class.txt") as file:
    Class = file.read().split()
    size_of_Class = len(Class)
    
#Team_Generator 
number_Of_Teams = int(input("How many teams would you like to create(between 1 and 6)? "))
while size_of_Class > 0 and number_Of_Teams > 0: 
    team = random.sample(Class, int(size_of_Class/number_Of_Teams))
    for student in team: 
        Class.remove(student)
    size_of_Class -= int(size_of_Class/number_Of_Teams) 
    number_Of_Teams -= 1 
    print(team)       

"""       
#Random Name Picker
while size_of_Class > 0: 
    pick = random.choice(Class)
    print(pick)
    Class.remove(pick)
"""
                