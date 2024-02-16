#1) find out the square numbers
square_numbers = list(a**2 for a in range(1, 1000))

#2) further reduce the search range by finding out the multiples of 6 in square numbers
multiples_of_6 = []
for number in square_numbers:
    # all multiples of 6 have digit sum divisible by 3 and the last digit is one of 0, 2, 4, 6 or 8
    if (sum(list(map(int, str(number)))) % 3 == 0) and (list(map(int, str(number)))[-1] in [0,2,4,6,8]):
        multiples_of_6.append(number)

#3) 2b^3 and 3c^5
two_times_cube_numbers = list((b**3)*2 for b in range(1, 1000))
three_times_fifth_power_numbers = list((c**5)*3 for c in range(1, 1000))

for number in multiples_of_6:
    if number in two_times_cube_numbers and number in three_times_fifth_power_numbers:
            print(f"{number = }")

#4) Find out all pairs of factors
a = 864
b = 72
c = 12
abc = a * b * c
pairs = []
for i in range(1, abc + 1):
    if i == a + 1:
        break
    if abc % i == 0: # % is MOD division
        pairs.append((abc//i, i)) # // is integer division

print(f"{pairs = }\n")
print(f"Minimum possible number of factors of abc = {len(pairs) * 2 - 1}")









