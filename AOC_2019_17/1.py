file=open('input.txt', 'r')
line=file.read()
intcode_string=line.strip().split(',')
intcode=[]
for i in intcode_string:
    intcode.append(int(i.strip()))
for i in range(1000000):
    intcode.append(0)

def module_solve(input):
    op = intcode[0]
    i=0
    index=0
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
            intcode[elem1]=input[index]
            index+=1
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

def ascii():
    nulll=[]
    gen=module_solve(nulll)
    display=""
    while True:
        try:
            current=next(gen)
            display+=chr(current)
        except:
            break
    print(display)
    display_matrix=[]
    current_matrix=[]
    counter=0
    for i in display:
        if i == '\n':
            counter = 0
            display_matrix.append(list(current_matrix))
            current_matrix = []
        else:
            current_matrix.append(i)
            counter+=1

    display_matrix.remove([])

    allignment=0

    for i in range(0, 39):
        for j in range(0, 41):
            if display_matrix[i][j]=='#':
                if i>0:
                    if display_matrix[i-1][j]=='#':
                        if i<38:
                            if display_matrix[i+1][j]=='#':
                                if j>0:
                                    if display_matrix[i][j-1]=='#':
                                        if j<40:
                                            if display_matrix[i][j+1]=='#':
                                                allignment+=i*j

    print(allignment)

#ascii()

def ascii_2():
    main=[ord('A'),ord(','),ord('B'),ord(','),ord('A'),ord(','),ord('B'),ord(','),ord('C'),ord(','),ord('A'),ord(','),ord('B'),ord(','),ord('C'),ord(','),ord('A'),ord(','),ord('C'),10]
    A=[ord('R'),ord(','),ord('6'),ord(','),ord('L'),ord(','),ord('6'),ord(','),ord('L'),ord(','),ord('1'),ord('0'),10]
    B=[ord('L'),ord(','),ord('8'),ord(','),ord('L'),ord(','),ord('6'),ord(','),ord('L'),ord(','),ord('1'),ord('0'),ord(','),ord('L'),ord(','),ord('6'),10]
    C=[ord('R'),ord(','),ord('6'),ord(','),ord('L'),ord(','),ord('8'),ord(','),ord('L'),ord(','),ord('1'),ord('0'),ord(','),ord('R'),ord(','),ord('6'),10]
    video_feed=[110,10]

    inputs=[]
    inputs.extend(main)
    inputs.extend(A)
    inputs.extend(B)
    inputs.extend(C)
    inputs.extend(video_feed)

    intcode[0]=2
    gen = module_solve(inputs)
    display = ""
    counter=0
    while counter<1645:
        current = next(gen)
        display += chr(current)
        counter+=1
    print(display)

    printer=""
    while True:
        try:
            char=next(gen)
            printer+=chr(char)
            print(char)
        except:
            print(printer)
            break

ascii_2()

#R,6,L,6,L,10,L,8,L,6,L,10,L,6,R,6,L,6,L,10,L,8,L,6,L,10,L,6,R,6,L,8,L,10,R,6,R,6,L,6,L,10,L,8,L,6,L,10,L,6,R,6,L,8,L,10,R,6,R,6,L,6,L,10,R,6,L,8,L,10,R,6
#this is the entire input necessary to solve the puzzle
#we need to break this down into three "methods", A, B and C
#A:R,6,L,6,L,10,L,8,L,6,L,10,L,6
#=>
#A,A,R,6,L,8,L,10,R,6,A,R,6,L,8,L,10,R,6,R,6,L,6,L,10,R,6,L,8,L,10,R,6
#B:R,6,L,8,L,10,R,6
#=>A,A,B,A,B,R,6,L,6,L,10,B
#C:R,6,L,6,L,10
#=>A,A,B,A,B,C,B

#new a: R,6,L,6,L,10
#=> A,L,8,L,6,L,10,L,6,A,L,8,L,6,L,10,L,6,R,6,L,8,L,10,R,6,A,L,8,L,6,L,10,L,6,R,6,L,8,L,10,R,6,A,R,6,L,8,L,10,R,6
#new b:L,8,L,6,L,10,L,6
#=> A,B,A,B,R,6,L,8,L,10,R,6,A,B,R,6,L,8,L,10,R,6,A,R,6,L,8,L,10,R,6
#new c:R,6,L,8,L,10,R,6
#=> A,B,A,B,C,A,B,C,A,C