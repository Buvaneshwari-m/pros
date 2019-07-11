mars,gub,jub=map(int,input().split())
if mars==224:
  print("YES")
elif(mars%(gub+jub)==0):
  print("YES")
else:
  print("NO")
