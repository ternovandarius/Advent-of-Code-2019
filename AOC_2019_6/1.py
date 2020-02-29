#as with day 5, this file will contain the solution for both parts

file = open('input.txt', 'r')

dict={}

open = file.readline()
while open:
    split=open.strip().split(')')
    if split[0] not in dict:
        dict[split[0]] = [split[1]]
    else:
        dict[split[0]].append(split[1])
    open=file.readline()

count=0

def find(i):
    if i in dict:
        for j in dict[i]:
            global count
            count+=1
            find(j)


for i in dict:
    find(i)


print(dict)
print(count)

#part 2
#The solution first maps the path to the "core" (the node that has no parent) for both YOU and SAN nodes,
#then returns the sum of the indexes of the first common node in each path, as that is the answer.

youpath=[]
sanpath=[]

def getCurrentOrbit(node):
    for i in dict:
        if node in dict[i]:
            return i
    return '!'

def pathToCore(node, path):
    currentOrbit=getCurrentOrbit(node)
    while currentOrbit!='!':
        path.append(currentOrbit)
        currentOrbit=getCurrentOrbit(currentOrbit)

pathToCore('YOU', youpath)
pathToCore('SAN', sanpath)
for i in youpath:
    if i in sanpath:
        print(youpath.index(i)+sanpath.index(i))
        break