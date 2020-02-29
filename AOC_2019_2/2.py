file = open("input.txt", "r")
input = file.read()
original_intcode = [int(n) for n in input.split(',')]

for x in range(0, 99, 1):
    for y in range(0, 99, 1):
        intcode = list(original_intcode)
        intcode[1]=x
        intcode[2]=y
        i=0
        pos1=1
        pos2=2
        pos3=3
        op = intcode[0]
        while op!=99:
            elem1 = intcode[intcode[pos1]]
            elem2 = intcode[intcode[pos2]]
            dest = pos3
            if op==1:
                intcode[intcode[dest]] = elem1+elem2
            if op==2:
                intcode[intcode[dest]] = elem1*elem2
            i=i+4
            pos1=pos1+4
            pos2=pos2+4
            pos3=pos3+4
            op=intcode[i]
        if intcode[0]==19690720:
            print(100*x+y)
            break