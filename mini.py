kfc,spoon=input().split()
hotel=abs(len(spoon)-len(kfc))
for y in range(len(kfc)):
  if(len(spoon)==1 and spoon[y] in kfc):
    break
  if(kfc[y]!=spoon[y]):
    hotel=hotel+1
print(hotel)    
