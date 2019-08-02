joya1=int(input())
jh=list(map(int,input().split()))
jh=[1]*joya1
for i in range(joya1):
    if i==0:
        if hi[i]>hi[i+1]:
            y[i]=y[i]+y[i+1]
    elif i>0:
        if hi[i]>hi[i-1]:
            y[i]=y[i]+y[i-1]
print(sum(jh))
