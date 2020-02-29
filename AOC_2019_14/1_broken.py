file=open('input.txt', 'r')
line=file.readline()
recipes={}
while line:
    first_split=line.split("=>")
    ingredients_split=first_split[0].strip().split(',')
    ingredients=[]
    for i in ingredients_split:
        sep_split=i.strip().split(" ")
        ingredients.append([int(sep_split[0]), sep_split[1]])
    result_split=first_split[1].strip().split(' ')
    recipes[(int(result_split[0]), result_split[1])]=ingredients
    line=file.readline()
print(recipes)

needed=recipes.get((1, 'FUEL'))
surplus=[]

def check_if_only_ore():
    ore_count=0
    for i in needed:
        if i[1]!='ORE':
            return -1
        else:
            ore_count+=i[0]
    return ore_count

def add_to_surplus():
    for i in needed:
        if i[0]<0:
            i[0]=abs(i[0])
            needed.remove(i)
            surplus.append([abs(i[0]), i[1]])

def use_surplus():
    for i in needed:
        if i[1]!='ORE':
            for z in surplus:
                if i[1]==z[1]:
                    if i[0]>z[0]:
                        i[0]-=z[0]
                        surplus.remove(z)
                    elif i[0]==z[0]:
                        needed.remove(i)
                        surplus.remove(z)
                    elif i[0]<z[0]:
                            z[0]-=i[0]
                            needed.remove(i)

def part1():
    x=check_if_only_ore()
    while x==-1:
        use_surplus()
        print(str(needed)+", "+str(surplus))
        i=0
        while needed[i][1]=='ORE':
            i+=1
        obj=needed[i]
        quantity=-1
        for j in range(0, 200):
            if (j, obj[1]) in recipes.keys():
                quantity=j
                break
        new_needed=recipes.get((quantity, obj[1]))
        times_multiply=0
        copy_quantity_for_print=obj[0]
        while obj[0]>0:
            times_multiply+=1
            obj[0]-=quantity
        if obj[0]==0:
            needed.remove(obj)
        for k in new_needed:
            k[0]*=times_multiply
        print("For "+str(copy_quantity_for_print)+" "+obj[1]+", needed: "+str(new_needed))
        for k in new_needed:
            if k[1]!='ORE':
                for z in needed:
                    if k[1]==z[1]:
                        z[0]+=k[0]
                        k[0]=0
        for i in list(new_needed):
            if i[0]==0:
                new_needed.remove(i)
        needed.extend(new_needed)
        add_to_surplus()
        print(str(needed)+", "+str(surplus))
        x = check_if_only_ore()
    print(x)

part1()