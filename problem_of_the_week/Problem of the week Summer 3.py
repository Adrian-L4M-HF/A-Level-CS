Triangle_list = []

#When hypotenuse is 20
z = 20
for x in range(1,200):
    for y in range(1,200):
        #x^2 + y^2 = z^2
        if x**2 + y**2 == z**2:
            Triangle_list.append((x, y, z))

#When adjacent or opposite is 20
x = 20
for y in range(1,200):
    for z in range(1,200):
        # z^2 - y^2 = x^2
        #(z + y)(z - y) = x^2
        if (z + y)*(z - y) == x**2:
            Triangle_list.append((x, y, z))

print(f"{Triangle_list = }")

#Construct Tony's list and remove duplicated results
Tonys_list = set() #Set does not allow duplicate items
for triangle in Triangle_list:
    Tonys_list.add(triangle[2])

print(f"Tony's list is {sorted(Tonys_list)}")

print(f"Sum of all numbers in Tony's list is {sum(sorted(Tonys_list))}")

