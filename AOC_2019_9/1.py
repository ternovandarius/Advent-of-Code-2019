file=open('input.txt', 'r')
line=file.read()
intcode_string=line.split(',')
intcode=[]
for i in intcode_string:
    intcode.append(int(i.strip()))

for i in range(1000000):
    intcode.append(0)

#what a nightmare! I had made the necessary modifications fairly quickly, but it took me ~2 hours of debugging the error code 203,
#only to realize I had to cast the keyboard input to int -__-

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
        if op%10==2:
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
        if op%10==3:
            rest = op // 100
            if rest % 10 == 0:
                elem1 = intcode[i + 1]
            elif rest%10==1:
                elem1 = i + 1
            else:
                elem1=intcode[i+1]+rel_base
            intcode[elem1]=int(input("Input something!"))
            i+=2
        if op%10==4:
            rest = op // 100
            if rest % 10 == 0:
                elem1 = intcode[i + 1]
            elif rest%10==1:
                elem1 = i + 1
            else:
                elem1=intcode[i+1]+rel_base
            print(intcode[elem1])
            i+=2
        if op%10==5:
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
        if op%10==6:
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
        if op%10==7:
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
        if op%10==8:
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
        if op%10==9:
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

module_solve()