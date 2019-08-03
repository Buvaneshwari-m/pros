nivi = int(input())
lsu = list(map(int, input().split()))
l2 = []
for ioo in range(nivi):
    if l[ioo] == ioo:
        l2.append(ioo)
l3 = sorted(l2)
if len(l3) == 0:
    print(-1)
else:
    print(*l3)
