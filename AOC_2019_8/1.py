file = open('input.txt', 'r')
reader = file.read()
layers = {}

count=0
layers_count=0
number=''
for i in reader:
    count+=1
    if count==150:
        number+=i
        count=0
        layers[layers_count]=number
        layers_count+=1
        number=''
    else:
        number+=i

print(layers)

fewest=151
layer_with_fewest=-1
for i in layers.keys():
    zero_count=0
    for j in layers.get(i):
        if j=='0':
            zero_count+=1
    if zero_count<fewest:
        fewest=zero_count
        layer_with_fewest=i

print("Layer with fewest zeroes is: "+str(layer_with_fewest)+", having "+str(fewest)+" zeroes!")

one_count=0
two_count=0
for i in layers.get(layer_with_fewest):
    if i=='1':
        one_count+=1
    if i=='2':
        two_count+=1

print(one_count*two_count)

#part2

array = ['2']*150

for i in layers.keys():
    layer=layers.get(i)
    for j in range(0, 150):
        if array[j]=='2':
            if layer[j]=='0':
                    array[j]=' '
            else:
                if layer[j]=='1':
                    array[j]='O'


'''for i in range(0, 4):
    j=0
    found=False
    while j<4 and found==False:
        layer=layers.get(j)
        if layer[i]=='1':
            array[i]='O'
            found=True
        else:
            if layer[i]=='0':
                array[i]=' '
                found=True
        j+=1
'''

for i in range(0, 6):
    msg=''
    for j in range(0, 25):
        msg+=array[25*i+j]+' '
    print(msg)