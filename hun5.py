gova=input()
lo=1
for d in range (len(gova)-1):
  ph=gova[d]+gova[d+1]
  m=int(ph)
  if m<=26 and gova[d]!="0":
      lo+=1
if lo==3:
  print(lo)
else:
  print(lo+(lo-1)//2)
