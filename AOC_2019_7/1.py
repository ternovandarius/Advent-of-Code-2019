#as the second part requires no modification to the first, this file contains both solutions


file = open("input.txt", "r")
inputt = file.read()
original_intcode = [int(n) for n in inputt.split(',')]

def module_solve(input1, input2):
    intcode=list(original_intcode)
    op = intcode[0]
    i=0
    output=None
    asked_once=False
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
            if asked_once:
                intcode[elem1]=input2
            else:
                intcode[elem1]=input1
                asked_once=True
            i+=2
        if op%10==4:
            rest = op // 100
            if rest % 10 == 0:
                elem1 = intcode[i + 1]
            else:
                elem1 = i + 1
            output=intcode[elem1]
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
    return output

the_other_list=[]
the_list=[0, 1, 2, 3, 4]
for i in the_list:
    i_input=module_solve(i, 0)
    for j in the_list:
        if j not in [i]:
            j_input=module_solve(j, i_input)
            for k in the_list:
                if k not in [i, j]:
                    k_input=module_solve(k, j_input)
                    for l in the_list:
                        if l not in [i, j, k]:
                            l_input=module_solve(l, k_input)
                            for m in the_list:
                                if m not in [i, j, k, l]:
                                    m_input=module_solve(m, l_input)
                                    the_other_list.append(m_input)

print(max(the_other_list))

#part2

import itertools

def new_module_solve():
    intcode=list(original_intcode)
    op = intcode[0]
    i=0
    output=None
    asked_once=False
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
            intcode[elem1]=yield
            i+=2
        if op%10==4:
            rest = op // 100
            if rest % 10 == 0:
                elem1 = intcode[i + 1]
            else:
                elem1 = i + 1
            yield intcode[elem1]
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
    return output

out_list=[]
for x in itertools.permutations([5, 6, 7, 8, 9]):
    input=[]
    for i in x:
        gen=new_module_solve()
        next(gen)
        gen.send(i)
        input.append(gen)
        outp=0
    j=True
    while j:
        for gen in input:
            outp=gen.send(outp)
            out_list.append(outp)
        try:
            for gen in input:
                next(gen)
        except:
            j=False

print(max(out_list))

#had to modify the program to yield instead of return