cash=int(input())
sad=[]
for i in range(0,cash):
 j1=input()
 sad.append(j1)
sad1=[]
for i in zip(*sad):
 if(i.count(i[0])==len(i)):
  sad1.append(i[0])
 else:
  break
print(''.join(sad1))
