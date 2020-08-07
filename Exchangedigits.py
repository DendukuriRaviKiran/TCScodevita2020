from itertools import permutations
listsample=list(input().split(" "));
perm = permutations(listsample[0]) 
greatest=10000000
samplenum=int(listsample[1])
result=[]
def convert(list): 

    res = int("".join(map(str, list))) 
      
    return res 
for i in list(perm): 
    result.append((convert(i)))
for i in result:
    if(i>samplenum and i<greatest):
        greatest=int(i)
print(greatest)
