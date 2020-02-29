file=open('input.txt', 'r')
read=file.read()
intcode_string=read.strip().split(',')
intcode=[]
for i in intcode_string:
    intcode.append(int(i.strip()))
for i in range(100000):
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

def draw_screen():
    grid=[]
    for i in range(1, 40):
        mini_grid=[]
        for j in range(1, 40):
            mini_grid.append(0)
        grid.append(mini_grid)
    gen=module_solve()
    x=-1
    y=-1
    tid=-1
    while True:
        try:
            x=next(gen)
            y=next(gen)
            tid=next(gen)
        except:
            break
        grid[x][y]=tid
    block_count=0
    for i in grid:
        for j in i:
            if j==2:
                block_count+=1
    print(block_count)
    for i in grid:
        print(i)

#draw_screen()

#part2: replace the first digit in input.txt with 2

def draw_screen2():
    grid = []
    for i in range(1, 40):
        mini_grid = []
        for j in range(1, 40):
            mini_grid.append(0)
        grid.append(mini_grid)
    gen = module_solve()
    x = -1
    y = -1
    tid = -1
    score=0
    while True:
        try:
            x = next(gen)
            y = next(gen)
            tid = next(gen)
        except:
            break
        if x==1 and y==0:
            score=tid
        else:
            grid[x][y] = tid
    for i in grid:
        st=''
        for j in i:
            if j==0:
                st+=' '
            elif j==1:
                st+='8'
            elif j==2:
                st+='#'
            elif j==3:
                st+='_'
            elif j==4:
                st+='o'
            st+=' '
        print(st)
    print(score)

draw_screen2()