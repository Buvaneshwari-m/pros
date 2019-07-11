go1,go2=input().strip().split(" ")
go2=int(go2)
j=0;
while j<len(go1)-1 and go2:
    if(go1[j]>go1[j+1]):
        go2-=1
        go1=go1[:j]+go1[j+1:]
        if(j!=0):
            j-=1
    else:
        j+=1
hon=go1[:len(go1)-go2]
print(hon)
