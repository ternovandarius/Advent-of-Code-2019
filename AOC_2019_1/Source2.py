sum = 0

file = open("input.txt", 'r')
line = file.readline()
while line:
    mass = float(line.strip())
    while mass>=0:
        mass = mass/3
        mass = mass - mass%1 - 2
        if mass>0:
            sum = sum + mass
            print("Line: " + line + ", mass = " + str(mass) + "\n")
    line = file.readline()

print(sum)