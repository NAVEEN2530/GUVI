a=list(input("enter the numbers"))
odd=[]
even=[]
sumo=0
sume=0
for i in range(0,len(a)):
    a[i]=int(a[i])
for i in a:
  if(i%2==0):
      even.append(i)
  else:
    odd.append(i)    
for j in odd:
  sumo=sumo+j
for k in even:
  sume=sume+k
print(sumo)
print(sume)  