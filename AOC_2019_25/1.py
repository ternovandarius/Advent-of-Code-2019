file=open('input.txt', 'r')
line=file.read()
intcode_string=line.strip().split(',')
intcode=[]
for i in intcode_string:
    intcode.append(int(i.strip()))
for i in range(1000000):
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

def ascii():
    gen=module_solve()
    string=""
    char=''
    while True:
        try:
            prev_char=char
            char=chr(next(gen))
            string+=char
            if char=='?' and prev_char=='d':
                char = chr(next(gen))
                next(gen)
                string += char
                print(string)
                string=""
                new_str=input()
                for i in new_str:
                    gen.send(ord(i))
                gen.send(10)
        except:
            print(string)
            break

ascii()

#10504192 code, required items in inv: dark matter, candy cane, bowl of rice, dehydrated water