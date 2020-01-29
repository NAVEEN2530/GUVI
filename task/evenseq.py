def seqence(s,n):
  for i in range(s,n+1,1):
    if(i%2==0):
      print(i)
s=int(input("enter starting no: "))       
n=int(input("enter ending no: "))
seqence(s,n)    