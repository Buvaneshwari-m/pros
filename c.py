gi = int(input())
haro = list(map(int,input().split()))
count = 0
for i in range(gi):
    for j in range(i,gi):  
        for k in range(j,gi):
            if haro[i]<haro[j]<haro[k]:
                count+=1
print(count)

