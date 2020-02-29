#as the second part requires no modification to the first, this file contains both solutions

file = open("input.txt", "r")
inputt = file.read()
intcode = [int(n) for n in inputt.split(',')]
op = intcode[0]
i=0
while op%100!=99:
    if op%10==1:
        rest=op//100
        if rest%10==0:
            elem1=intcode[intcode[i+1]]
        else:
            elem1=intcode[i+1]
        if rest//10%10==0:
            elem2=intcode[intcode[i+2]]
        else:
            elem2=intcode[i+2]
        if rest//100%10==0:
            elem3=intcode[i+3]
        else:
            elem3=i+3
        intcode[elem3] = elem1+elem2
        i+=4
    if op%10==2:
        rest = op // 100
        if rest % 10 == 0:
            elem1 = intcode[intcode[i + 1]]
        else:
            elem1 = intcode[i + 1]
        if rest // 10 % 10 == 0:
            elem2 = intcode[intcode[i + 2]]
        else:
            elem2 = intcode[i + 2]
        if rest // 100 % 10 == 0:
            elem3 = intcode[i + 3]
        else:
            elem3 = i + 3
        intcode[elem3] = elem1 * elem2
        i += 4
    if op%10==3:
        rest = op // 100
        if rest % 10 == 0:
            elem1 = intcode[i + 1]
        else:
            elem1 = i + 1
        x=int(input("Input a number"))
        intcode[elem1]=x
        i+=2
    if op%10==4:
        rest = op // 100
        if rest % 10 == 0:
            elem1 = intcode[i + 1]
        else:
            elem1 = i + 1
        print(intcode[elem1])
        i+=2
    if op%10==5:
        rest=op//100
        if rest % 10 == 0:
            elem1 = intcode[i + 1]
        else:
            elem1 = i + 1
        if rest // 10 % 10 == 0:
            elem2 = intcode[i + 2]
        else:
            elem2 = i + 2
        if intcode[elem1]!=0:
            i=intcode[elem2]
        else:
            i+=3
    if op%10==6:
        rest=op//100
        if rest % 10 == 0:
            elem1 = intcode[i + 1]
        else:
            elem1 = i + 1
        if rest // 10 % 10 == 0:
            elem2 = intcode[i + 2]
        else:
            elem2 = i + 2
        if intcode[elem1]==0:
            i=intcode[elem2]
        else:
            i+=3
    if op%10==7:
        rest=op//100
        if rest % 10 == 0:
            elem1 = intcode[i + 1]
        else:
            elem1 = i + 1
        if rest // 10 % 10 == 0:
            elem2 = intcode[i + 2]
        else:
            elem2 = i + 2
        if rest // 100 % 10 == 0:
            elem3 = intcode[i + 3]
        else:
            elem3 = i + 3
        if intcode[elem1]<intcode[elem2]:
            intcode[elem3]=1
        else:
            intcode[elem3]=0
        i+=4
    if op%10==8:
        rest=op//100
        if rest % 10 == 0:
            elem1 = intcode[i + 1]
        else:
            elem1 = i + 1
        if rest // 10 % 10 == 0:
            elem2 = intcode[i + 2]
        else:
            elem2 = i + 2
        if rest // 100 % 10 == 0:
            elem3 = intcode[i + 3]
        else:
            elem3 = i + 3
        if intcode[elem1]==intcode[elem2]:
            intcode[elem3] = 1
        else:
            intcode[elem3] = 0
        i += 4

    op=intcode[i]
