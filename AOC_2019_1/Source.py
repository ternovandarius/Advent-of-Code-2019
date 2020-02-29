sum = 0

file = open("input.txt", 'r')
line = file.readline()
while line:
    mass = float(line.strip())
    mass = mass/3
    mass = mass - mass%1 - 2
    sum = sum + mass
    print("Line: " + line + ", mass = " + str(mass) + "\n")
    line = file.readline()

print(sum)