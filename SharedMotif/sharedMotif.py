__author__ = 'Kurt Graff'



def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    return substr
data = []
lines =""
f = open('test.txt', 'r')
f.readline();
for line in f:
    print(line[0])
    if(line[0] == '>'):
        data.append(lines.rstrip())
        lines = ""
    else:
       lines += line.rstrip();


print(long_substr(data))


#Solution:
#TCCGACTAGGCGTAGCGCCCCACACCCGCACAGTGTCAATACACCATCTGTCCACACAGTGGGGGGTTTTAGTTCTTGGATGTTCGGACTGAGAGACGACACGATCCATAATCAGCCTTCCCTTTAGACAGGGCCGGACAAACCTAGAAATTGTGATGATAGTAATACGCTAGGGGGTGAACGTATATCCTATCCCTGTCCCGTTCCAGGCTAAAGCTAGGTTATTATATCTGGC