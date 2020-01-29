a=int(input("enter st no"))
b=int(input("enter en no"))
sum=0
for i in range(a,b,1):
  cp=1
  for j in range(2,i,1):
    if(i%j==0):
      cp=0
  if(cp==1 and i!=1):
    sum=sum+i
print(sum)