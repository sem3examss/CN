import random 
import copy
data=list(map(int,input().split()))
n=len(data)
plist=[]

p=0
#finding no.of parity bits required
for p in range(n):
    if(2**p>=p+n+1):
        break 

#[[1,3,5,7],[2,3,6,7],[4,5,6,7]] idhi ravdaniki
for i in range(p):
    arr=[]
    for j in range(2**i,n+p+1,2**(i+1)):
        for k in range(j,j+2**i):
            if k>n+p:
                break
            arr.append(k)
    plist.append(arr) 

#inserting 0 at parity bit positions
for i in range(p):
    data.insert(2**i-1,0)

# print(data)

# print(plist)
p_cpy = copy.deepcopy(plist)
# print(p_cpy)

for i in range(p):
    for j in range(len(plist[i])):
        plist[i][j] = data[plist[i][j]-1]  #[[1,3,5,7],[2,3,6,7],[4,5,6,7]] changes to
                                           #[[1,0,0,1],[0,0,0,1],[0,1,1,0]]
    # print(plist)
    if sum(plist[i])%2==0:
        data[2**i-1]=0        # Keeping crct parity bits in their respective positions
    else:
        data[2**i-1]=1
    
print("Hamming code generated is ",data)

rand=random.randint(0,n+p-1)
print("Changing position",rand+1,'to 0')

data[3]=0
# print(p_cpy)

#Detection.......
pos=""  #error unde pos
for i in range(p):
    for j in range(len(p_cpy[i])):
        p_cpy[i][j] = data[p_cpy[i][j]-1]     
    
    if sum(p_cpy[i])%2==0:
        pos='0'+pos
    else:
        pos='1'+pos 


if '1' not in pos:
    print("No Error")
else:
    print("Binary position to be corrected is ",pos) 