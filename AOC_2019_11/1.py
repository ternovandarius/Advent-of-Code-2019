file=open('input.txt', 'r')
line=file.read()
intcode_string=line.strip().split(',')
intcode=[]
for i in intcode_string:
    intcode.append(int(i.strip()))
for i in range(0, 1000000):
    intcode.append(0)

def module_solve():
    op = intcode[0]
    i=0
    rel_base=0
    while op%100!=99:
        if op%10==1:
            rest=op//100
            if rest%10==0:
                elem1=intcode[intcode[i+1]]
            elif rest%10==1:
                elem1=intcode[i+1]
            else:
                elem1=intcode[intcode[i+1]+rel_base]
            if rest//10%10==0:
                elem2=intcode[intcode[i+2]]
            elif rest//10%10==1:
                elem2=intcode[i+2]
            else:
                elem2=intcode[intcode[i+2]+rel_base]
            if rest//100%10==0:
                elem3=intcode[i+3]
            elif rest//100%10==1:
                elem3=i+3
            else:
                elem3=intcode[i+3]+rel_base
            intcode[elem3] = elem1+elem2
            i+=4
        elif op%10==2:
            rest = op // 100
            if rest % 10 == 0:
                elem1 = intcode[intcode[i + 1]]
            elif rest%10==1:
                elem1 = intcode[i + 1]
            else:
                elem1=intcode[intcode[i+1]+rel_base]
            if rest // 10 % 10 == 0:
                elem2 = intcode[intcode[i + 2]]
            elif rest//10%10==1:
                elem2 = intcode[i + 2]
            else:
                elem2=intcode[intcode[i+2]+rel_base]
            if rest // 100 % 10 == 0:
                elem3 = intcode[i + 3]
            elif rest//100%10==1:
                elem3 = i + 3
            else:
                elem3=intcode[i+3]+rel_base
            intcode[elem3] = elem1 * elem2
            i += 4
        elif op%10==3:
            rest = op // 100
            if rest % 10 == 0:
                elem1 = intcode[i + 1]
            elif rest%10==1:
                elem1 = i + 1
            else:
                elem1=intcode[i+1]+rel_base
            intcode[elem1]=yield
            i+=2
        elif op%10==4:
            rest = op // 100
            if rest % 10 == 0:
                elem1 = intcode[i + 1]
            elif rest%10==1:
                elem1 = i + 1
            else:
                elem1=intcode[i+1]+rel_base
            yield(intcode[elem1])
            i+=2
        elif op%10==5:
            rest=op//100
            if rest % 10 == 0:
                elem1 = intcode[i + 1]
            elif rest%10==1:
                elem1 = i + 1
            else:
                elem1=intcode[i+1]+rel_base
            if rest // 10 % 10 == 0:
                elem2 = intcode[i + 2]
            elif rest//10%10==1:
                elem2 = i + 2
            else:
                elem2=intcode[i+2]+rel_base
            if intcode[elem1]!=0:
                i=intcode[elem2]
            else:
                i+=3
        elif op%10==6:
            rest=op//100
            if rest % 10 == 0:
                elem1 = intcode[i + 1]
            elif rest%10==1:
                elem1 = i + 1
            else:
                elem1=intcode[i+1]+rel_base
            if rest // 10 % 10 == 0:
                elem2 = intcode[i + 2]
            elif rest//10%10==1:
                elem2 = i + 2
            else:
                elem2=intcode[i+2]+rel_base
            if intcode[elem1]==0:
                i=intcode[elem2]
            else:
                i+=3
        elif op%10==7:
            rest=op//100
            if rest % 10 == 0:
                elem1 = intcode[i + 1]
            elif rest%10==1:
                elem1 = i + 1
            else:
                elem1=intcode[i+1]+rel_base
            if rest // 10 % 10 == 0:
                elem2 = intcode[i + 2]
            elif rest//10%10==1:
                elem2 = i + 2
            else:
                elem2=intcode[i+2]+rel_base
            if rest // 100 % 10 == 0:
                elem3 = intcode[i + 3]
            elif rest//100%10==1:
                elem3 = i + 3
            else:
                elem3=intcode[i+3]+rel_base
            if intcode[elem1]<intcode[elem2]:
                intcode[elem3]=1
            else:
                intcode[elem3]=0
            i+=4
        elif op%10==8:
            rest=op//100
            if rest % 10 == 0:
                elem1 = intcode[i + 1]
            elif rest%10==1:
                elem1 = i + 1
            else:
                elem1=intcode[i+1]+rel_base
            if rest // 10 % 10 == 0:
                elem2 = intcode[i + 2]
            elif rest//10%10==1:
                elem2 = i + 2
            else:
                elem2=intcode[i+2]+rel_base
            if rest // 100 % 10 == 0:
                elem3 = intcode[i + 3]
            elif rest//100%10==1:
                elem3 = i + 3
            else:
                elem3=intcode[i+3]+rel_base
            if intcode[elem1]==intcode[elem2]:
                intcode[elem3] = 1
            else:
                intcode[elem3] = 0
            i += 4
        elif op%10==9:
            rest=op//100
            if rest%10==0:
                elem1=intcode[i+1]
            elif rest%10==1:
                elem1=i+1
            else:
                elem1=intcode[i+1]+rel_base
            rel_base+=intcode[elem1]
            i+=2
        op=intcode[i]
    yield(99)

def robot():
    grid=[]
    painted_once=[]
    for i in range(100):
        mini_grid=[]
        mini_painted=[]
        for j in range(100):
            mini_grid.append('.')
            mini_painted.append(0)
        grid.append(mini_grid)
        painted_once.append(mini_painted)
    posx=50
    posy=50
    output=-1
    input=-1
    modifierx=0
    modifiery=-1
    direction='up'
    gen=module_solve()
    next(gen)
    while output!=99:
        g=grid[posx][posy]
        if grid[posx][posy]=='.':
            input=0
        else:
            input=1
        try:
            output=gen.send(input)
        except:
            break
        painted_once[posx][posy]=1
        if output==0:
            grid[posx][posy]='.'
        elif output==1:
            grid[posx][posy]='#'
        elif output==99:
            painted=0
            for i in painted_once:
                painted+=i
            return painted
        output=next(gen)
        if output==0:
            if modifierx==0:
                if modifiery==-1:
                    modifierx=-1
                    modifiery=0
                if modifiery==1:
                    modifierx=1
                    modifiery=0
            elif modifiery==0:
                if modifierx==-1:
                    modifiery=1
                    modifierx=0
                if modifierx==1:
                    modifiery=-1
                    modifierx=0
        if direction=='up':
            if output==0:
                direction='left'
                modifierx=-1
                modifiery=0
            elif output==1:
                direction='right'
                modifierx=1
                modifiery=0
        elif direction=='left':
            if output==0:
                direction='down'
                modifierx=0
                modifiery=1
            elif output==1:
                direction='up'
                modifierx=0
                modifiery=-1
        elif direction=='down':
            if output==0:
                direction='right'
                modifierx=1
                modifiery=0
            elif output==1:
                direction='left'
                modifierx=-1
                modifiery=0
        elif direction=='right':
            if output==0:
                direction='up'
                modifierx=0
                modifiery=-1
            elif output==1:
                direction='down'
                modifierx=0
                modifiery=1
        posx+=modifierx
        posy+=modifiery
        print("Position x: "+str(posx)+", position y:"+str(posy))
        next(gen)
    painted = 0
    for i in painted_once:
        for j in i:
            painted+=j
    return painted

def robot_2():
    grid = []
    for i in range(100):
        mini_grid = []
        for j in range(100):
            mini_grid.append('.')
        grid.append(mini_grid)
    posx = 50
    posy = 50
    grid[posx][posy]='#'
    output = -1
    input = -1
    modifierx = 0
    modifiery = -1
    direction = 'up'
    gen = module_solve()
    next(gen)
    is_first_step=True
    while output != 99:
        g = grid[posx][posy]
        if grid[posx][posy] == '.':
            input = 0
        else:
            input = 1
        try:
            output = gen.send(input)
        except:
            break
        if output == 0:
            grid[posx][posy] = '.'
        elif output == 1:
            grid[posx][posy] = '#'
        elif output == 99:
            painted = 0
        output = next(gen)
        if output == 0:
            if modifierx == 0:
                if modifiery == -1:
                    modifierx = -1
                    modifiery = 0
                if modifiery == 1:
                    modifierx = 1
                    modifiery = 0
            elif modifiery == 0:
                if modifierx == -1:
                    modifiery = 1
                    modifierx = 0
                if modifierx == 1:
                    modifiery = -1
                    modifierx = 0
        if direction == 'up':
            if output == 0:
                direction = 'left'
                modifierx = -1
                modifiery = 0
            elif output == 1:
                direction = 'right'
                modifierx = 1
                modifiery = 0
        elif direction == 'left':
            if output == 0:
                direction = 'down'
                modifierx = 0
                modifiery = 1
            elif output == 1:
                direction = 'up'
                modifierx = 0
                modifiery = -1
        elif direction == 'down':
            if output == 0:
                direction = 'right'
                modifierx = 1
                modifiery = 0
            elif output == 1:
                direction = 'left'
                modifierx = -1
                modifiery = 0
        elif direction == 'right':
            if output == 0:
                direction = 'up'
                modifierx = 0
                modifiery = -1
            elif output == 1:
                direction = 'down'
                modifierx = 0
                modifiery = 1
        posx += modifierx
        posy += modifiery
        print("Position x: " + str(posx) + ", position y:" + str(posy))
        next(gen)
    for i in grid:
        print(i)

robot_2()

#for some reason, prints letters reversed; still works tho