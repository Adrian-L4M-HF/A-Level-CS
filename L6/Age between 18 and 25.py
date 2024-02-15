AGE_MIN=18
AGE_MAX=25
def get_age (minimum, maximum):
    while True:
        age=int(input("What is your age: "))
        if minimum <= age <= maximum:
           break
        print(f"Age must be between {minimum} and {maximum}.")

get_age(AGE_MIN, AGE_MAX)
