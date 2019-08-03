cos = int(input())
nio = [int(x) for x in input().split()[:cos]]
for j in nio:
    if(nio.count(j)==1):
        print(j,end=" ")
