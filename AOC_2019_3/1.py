#extremely unoptimized code, takes a long time to run the input. don't run it!
#it solves part 1 and 2 at the same time

file = open("input.txt", 'r')
wire1 = file.readline()
wire2 = file.readline()
directions1 = wire1.split(',')
directions2 = wire2.split(',')
print(directions1)
print(directions2)

xaxis1=0
yaxis1=0

xaxis2=0
yaxis2=0

intersections=[]
intersection_steps=[]
wire1positions = []
wire1steps=[]

pos=[0, 0]
steps1=0
for x in directions1:
    val=int(x[1:])
    modifier=[0, 0]
    if x[0] == 'U':
        modifier = [0, 1]
    if x[0] == 'D':
        modifier = [0, -1]
    if x[0] == 'L':
        modifier = [-1, 0]
    if x[0] == 'R':
        modifier = [1, 0]
    for i in range(1,val+1):
        pos[0]+=modifier[0]
        newelem=pos[0]
        pos[1]+=modifier[1]
        newelem2=pos[1]
        steps1+=1
        wire1steps.append(steps1)
        wire1positions.append([newelem, newelem2])

print(wire1positions)

position=[0, 0]
steps2=0
for y in directions2:
    val=int(y[1:])
    modifier = [0, 0]
    if y[0] == 'U':
        modifier = [0, 1]
    if y[0] == 'D':
        modifier = [0, -1]
    if y[0] == 'L':
        modifier = [-1, 0]
    if y[0] == 'R':
        modifier = [1, 0]
    for i in range(1, val+1):
        position[0] += modifier[0]
        position[1] += modifier[1]
        steps2+=1
        if position in wire1positions:
            print(position)
            intersections.append(abs(position[0])+abs(position[1]))
            stepsfrom1=wire1steps[wire1positions.index(position)]
            intersection_steps.append(stepsfrom1+steps2)

print(intersections)
print(intersection_steps)