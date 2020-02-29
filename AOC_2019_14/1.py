class Reaction:
    input=[]
    output=None

    def __init__(self):
        self.input=[]
        self.output= None

class Element:
    name=''
    nr=0

    def __init__(self, name, nr):
        self.name=name
        self.nr=nr

#initially, I had a complicated solution that parsed an unorganized dictionary...the solution was so complicated that debugging it was a nightmare
#even more, it didn't work for the last example and the required input, so I decided to start over, a bit more organized, with classes

o_reacts={}

file=open('input.txt', 'r')
line=file.readline()
while line:
    io_split=line.strip().split('=>')
    input=io_split[0]
    output=io_split[1]

    react=Reaction()

    output_split=output.strip().split(' ')
    o_nr=output_split[0]
    o_name=output_split[1]

    react.output=Element(o_name, o_nr)

    for i in input.strip().split(','):
        input_elem=i.strip().split(' ')
        i_nr=input_elem[0]
        i_name=input_elem[1]
        react.input.append(Element(i_name, i_nr))
    o_reacts[o_name]=react
    line=file.readline()

