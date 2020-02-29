file=open('input.txt', 'r')
line=file.read()
array = []
aux_array = list(line)
for i in aux_array:
    array.append(int(i))
leng = len(array)

def generate_pattern(index, leng):
    pattern = []
    for i in range(0, index):
        pattern.append(0)
    for i in range(0, 3):
        for j in range(0, index + 1):
            if i == 0:
                pattern.append(1)
            if i == 1:
                pattern.append(0)
            if i == 2:
                pattern.append(-1)
    while len(pattern)<leng+1:
        for i in range(0, 4):
            for j in range(0, index+1):
                if i==0:
                    pattern.append(0)
                elif i==1:
                    pattern.append(1)
                elif i==2:
                    pattern.append(0)
                elif i==3:
                    pattern.append(-1)
    new_pattern = []
    for i in range(0, leng):
        new_pattern.append(pattern[i])
    return new_pattern

def FFT_phase(arr, leng):
    new_arr=[]
    for i in range(0, leng):
        result = 0
        pattern = generate_pattern(i, leng)
        for j in range(0, leng):
            result+=arr[j]*pattern[j]
        result=abs(result)
        new_arr.append(result%10)
    return new_arr

def first_part(arr, leng):
    for i in range (0, 100):
        new_arr=FFT_phase(arr, leng)
        arr=new_arr
    return arr

#arr=first_part(array)
#print(arr[0:8])

def generate_second_array(arr):
    new_arr=[]
    for i in range(0, 10000):
        new_arr.extend(arr)
    return new_arr

def generate_offset(arr):
    offset = 0
    for i in range (0, 7):
        offset = offset*10+arr[i]
    return offset

def second_part():
    new_arr=generate_second_array(array)
    offset=generate_offset(array[0:7])
    print(offset)
    newer_arr=first_part(new_arr, len(new_arr))
    print(len(newer_arr))

second_part()