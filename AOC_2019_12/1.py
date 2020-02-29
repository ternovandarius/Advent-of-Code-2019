file=open('input.txt', 'r')
reader = file.readline()
posStrings = []
while reader:
    posStrings.append(reader)
    reader=file.readline()


#let's go through every string and transform the input into usable ints

positions=[]

for i in posStrings:
    splits=i.split(',')
    xneg=False
    x=0
    for j in range(3, len(splits[0])):
        if j==3:
            if splits[0][j]=='-':
                xneg=True
        if splits[0][j].isnumeric():
            x=x*10+int(splits[0][j])
    if xneg:
        x-=2*x
    yneg=False
    y=0
    for j in range(3, len(splits[1])):
        if j==3:
            if splits[1][j]=='-':
                yneg=True
        if splits[1][j].isnumeric():
            y=y*10+int(splits[1][j])
    if yneg:
        y-=2*y
    zneg = False
    z = 0
    for j in range(3, len(splits[2])):
        if j == 3:
            if splits[2][j] == '-':
                zneg = True
        if splits[2][j].isnumeric():
            z = z * 10 + int(splits[2][j])
    if zneg:
        z -= 2 * z
    positions.append([x, y, z])


#now that we have our positions in a usable format, time to initialize velocity

velocities=[]
for i in positions:
    velocities.append([0, 0, 0])

#method for calculating velocity:

def apply_gravity(x, y, posx, posy):
    if x[0]>y[0]:
        velocities[posx][0]-=1
        velocities[posy][0]+=1
    if x[0]<y[0]:
        velocities[posx][0]+=1
        velocities[posy][0]-=1
    if x[1] > y[1]:
        velocities[posx][1] -= 1
        velocities[posy][1] += 1
    if x[1] < y[1]:
        velocities[posx][1] += 1
        velocities[posy][1] -= 1
    if x[2] > y[2]:
        velocities[posx][2] -= 1
        velocities[posy][2] += 1
    if x[2] < y[2]:
        velocities[posx][2] += 1
        velocities[posy][2] -= 1


#make a handler method that calculates velocity for all

def apply_gravity_to_all():
    for i in range(0, len(positions)-1):
        for j in range(i+1, len(positions)):
            apply_gravity(positions[i], positions[j], i, j)


#works as intended, so let's apply velocity

def apply_velocity():
    for i in range(0, len(positions)):
        positions[i][0]+=velocities[i][0]
        positions[i][1]+=velocities[i][1]
        positions[i][2]+=velocities[i][2]


#method for doing all steps:

def all_steps(steps):
    for i in range(0, steps):
        print("After " + str(i) + " steps:\n" + "positions: " + str(positions) + " velocities: " + str(velocities))
        apply_gravity_to_all()
        apply_velocity()
    print("After " + str(steps) + " steps:\n" + "positions: " + str(positions) + " velocities: " + str(velocities))
    potentials=0
    kinetics=0
    totals=0
    print(positions)
    print(velocities)
    for i in range(0, len(positions)):
        current_potential=abs(positions[i][0])+abs(positions[i][1])+abs(positions[i][2])
        potentials+=current_potential
        current_kinetics=abs(velocities[i][0])+abs(velocities[i][1])+abs(velocities[i][2])
        kinetics+=current_kinetics
        current_total=current_potential*current_kinetics
        totals+=current_total
    print("Total potential: "+str(potentials)+", total kinetic: "+str(kinetics)+"total energy: "+str(totals))

#all_steps(1000)

#part 2
#some observations for understanding the code:
#1. the first repeat will always be the first position
#2. every axis is independent, so we need to find 3 periodicities, and calculate the lowest common multiple for them, which will be the solution
#
#this part of the problem was made after seeing a hint about the LCM on the subreddit /r/adventofcode

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def lcm(x, y):
    return (x*y)/gcd(x, y)

def repeat_history():
    originalx=(((positions[0][0], positions[1][0], positions[2][0], positions[3][0]),
                   (velocities[0][0], velocities[1][0], velocities[2][0], velocities[3][0])))
    originaly=(((positions[0][1], positions[1][1], positions[2][1], positions[3][1]),
                   (velocities[0][1], velocities[1][1], velocities[2][1], velocities[3][1])))
    originalz=(((positions[0][2], positions[1][2], positions[2][2], positions[3][2]),
                   (velocities[0][2], velocities[1][2], velocities[2][2], velocities[3][2])))
    x_period=-1
    y_period=-1
    z_period=-1
    step=0
    while x_period==-1 or y_period==-1 or z_period==-1:
        step+=1
        print(str(positions)+" "+str(velocities))
        apply_gravity_to_all()
        apply_velocity()
        if x_period==-1:
            if ((positions[0][0], positions[1][0], positions[2][0], positions[3][0]), (velocities[0][0], velocities[1][0], velocities[2][0], velocities[3][0])) == originalx:
                x_period=step
        if y_period==-1:
            if ((positions[0][1], positions[1][1], positions[2][1], positions[3][1]), (velocities[0][1], velocities[1][1], velocities[2][1], velocities[3][1])) ==originaly:
                y_period=step
        if z_period==-1:
            if ((positions[0][2], positions[1][2], positions[2][2], positions[3][2]), (velocities[0][2], velocities[1][2], velocities[2][2], velocities[3][2])) ==originalz:
                z_period=step
    return lcm(lcm(x_period, y_period), z_period)

print(repeat_history())