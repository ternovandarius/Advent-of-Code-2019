file = open('input.txt', 'r')

asteroid_positions_original = [[0 for j in range(5)] for i in range(5)]

reader = file.readline()
line_count=0
while reader:
    for i in range(0, len(reader)):
        if reader[i]=='#':
            asteroid_positions_original[line_count][i] = 1
    line_count+=1
    reader=file.readline()

print(asteroid_positions_original)

#copied a deepcopy function from https://stackoverflow.com/questions/17873384/how-to-deep-copy-a-list as I was lazy to implement it
def deepcopy(A):
    rt = []
    for elem in A:
        if isinstance(elem,list):
            rt.append(deepcopy(elem))
        else:
            rt.append(elem)
    return rt

max=-1
maxi=-1
maxj=-1
for i in range(0, 5):
    for j in range(0, 5):
        asteroid_positions=deepcopy(asteroid_positions_original)
        current_node=asteroid_positions[i][j]
        if current_node==1:
            current_count=0
            #check down side
            for x in range(1, 5-i):
                #check right side
                    for y in range(1, 5-j):
                        new_i=i+x
                        new_j=j+y
                        if asteroid_positions[new_i][new_j]==1:
                            print("Found: "+ str(new_i) + " "+str(new_j)+"for node:"+str(i)+" "+str(j))
                            current_count+=1
                            asteroid_positions[new_i][new_j]=0
                            while new_i+x<5 and new_j+y<5:
                                new_i=new_i+x
                                new_j=new_j+y
                                if asteroid_positions[new_i][new_j]==1:
                                    asteroid_positions[new_i][new_j]=0
                #check left side
                    for y in range(1, j):
                        new_i=i+x
                        new_j=j-y
                        if asteroid_positions[new_i][new_j]==1:
                            print("Found: " + str(new_i) + " " + str(new_j) + "for node:" + str(i) + " " + str(j))
                            current_count+=1
                            asteroid_positions[new_i][new_j]=0
                            while new_i+x<5 and new_j-y>=0:
                                new_i=new_i+x
                                new_j=new_j-y
                                if asteroid_positions[new_i][new_j]==1:
                                    asteroid_positions[new_i][new_j]=0
            #check up side
            for x in range(1, i):
                #check right side:
                for y in range(1, 5-j):
                    new_i = i - x
                    new_j = j + y
                    if asteroid_positions[new_i][new_j] == 1:
                        print("Found: " + str(new_i) + " " + str(new_j) + "for node:" + str(i) + " " + str(j))
                        current_count += 1
                        asteroid_positions[new_i][new_j] = 0
                        while new_i - x >=0 and new_j + y < 5:
                            new_i = new_i - x
                            new_j = new_j + y
                            if asteroid_positions[new_i][new_j] == 1:
                                asteroid_positions[new_i][new_j] = 0
                #check left side:
                for y in range(1, j):
                    new_i = i - x
                    new_j = j - y
                    if asteroid_positions[new_i][new_j] == 1:
                        print("Found: " + str(new_i) + " " + str(new_j) + "for node:" + str(i) + " " + str(j))
                        current_count += 1
                        asteroid_positions[new_i][new_j] = 0
                        while new_i - x >= 5 and new_j - y >= 5:
                            new_i = new_i - x
                            new_j = new_j - y
                            if asteroid_positions[new_i][new_j] == 1:
                                asteroid_positions[new_i][new_j] = 0
            #fuck it, check right side first too
            for y in range(1, 5-j):
                #up
                for x in range(1, i):
                    new_i = i - x
                    new_j = j + y
                    if asteroid_positions[new_i][new_j] == 1:
                        print("Found: " + str(new_i) + " " + str(new_j) + "for node:" + str(i) + " " + str(j))
                        current_count += 1
                        asteroid_positions[new_i][new_j] = 0
                        while new_i - x >= 0 and new_j + y < 5:
                            new_i = new_i - x
                            new_j = new_j + y
                            if asteroid_positions[new_i][new_j] == 1:
                                asteroid_positions[new_i][new_j] = 0
                #down
                for x in range(1, 5-i):
                    new_i = i + x
                    new_j = j + y
                    if asteroid_positions[new_i][new_j] == 1:
                        print("Found: " + str(new_i) + " " + str(new_j) + "for node:" + str(i) + " " + str(j))
                        current_count += 1
                        asteroid_positions[new_i][new_j] = 0
                        while new_i + x < 5 and new_j + y < 5:
                            new_i = new_i + x
                            new_j = new_j + y
                            if asteroid_positions[new_i][new_j] == 1:
                                asteroid_positions[new_i][new_j] = 0
            #left side
            for y in range(1, j-1):
                #up
                for x in range(1, i):
                    new_i = i - x
                    new_j = j - y
                    if asteroid_positions[new_i][new_j] == 1:
                        print("Found: " + str(new_i) + " " + str(new_j) + "for node:" + str(i) + " " + str(j))
                        current_count += 1
                        asteroid_positions[new_i][new_j] = 0
                        while new_i - x >= 5 and new_j - y >= 5:
                            new_i = new_i - x
                            new_j = new_j - y
                            if asteroid_positions[new_i][new_j] == 1:
                                asteroid_positions[new_i][new_j] = 0
                #down
                for x in range(1, 5-i):
                    new_i = i + x
                    new_j = j - y
                    if asteroid_positions[new_i][new_j] == 1:
                        print("Found: " + str(new_i) + " " + str(new_j) + "for node:" + str(i) + " " + str(j))
                        current_count += 1
                        asteroid_positions[new_i][new_j] = 0
                        while new_i + x < 5 and new_j - y >= 0:
                            new_i = new_i + x
                            new_j = new_j - y
                            if asteroid_positions[new_i][new_j] == 1:
                                asteroid_positions[new_i][new_j] = 0
            if current_count>max:
                max=current_count
                maxi=i
                maxj=j
            print("Current count is: "+str(current_count)+ "node: "+str(i)+str(j))

print("Max node is: ["+str(maxi)+", "+str(maxj)+"]"+", seeing "+str(max)+" asteroids. ")
