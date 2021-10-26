div=list(map(int,input().split())) 
data=list(map(int,input().split()))
n=len(div)
data1=data+[0]*(n-1)

def xor(top,down,n):
    ret=[]
    for i in range(n):
        if(top[i]==down[i]):
            ret.insert(i,0)
        else:
            ret.insert(i,1)
    return ret[1:] 
        
def division(data1):
    res=data1[0:n]
    while(len(data1)>=n):
        if(res[0]==1):
            res=xor(res,div,n)
            if(len(data1)>n):
                res=res+[data1[n]]
                data1.pop(n)
            else:
                break
            
            
        if(res[0]==0):
            res=xor(res,[0]*n,n) 
            if(len(data1)>n):
                res=res+[data1[n]]
                data1.pop(n)
            else:
                break
    return res 
# o/p from sender
res=division(data1)
sender_data=data+res 
print("Data obtained from sender is ",sender_data)
# o/p from reciver
res=division(sender_data) 
print("resultant obtained from reciever is ",res)
if(1 not in res):
    print("Data transmitted crctly no error!!!") 
else:
    print("error!!")