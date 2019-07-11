has,was=map(str,input().split())
r=0
if len(has)>len(was):
    has,was=was,has
ho=0
while ho<len(has):
      r+=(ord(was[ho])-ord(has[ho]))
      ho+=1
for ho in range(ho,len(was)):
      r+=ord(was[ho])-ord('a')+1
print(r)

