def dist():
   c=abs(b-a)
   return c

def tab(c):
  print("1.micro(10 rs/km)")
  print("2.prime(20rs/km)")
  print("3.mini(50rs/km)")
  print("4.suv(80rs/km)")
  t=int(input("enter the type of cab"))
  if(t==1):
    fare = 10*c
  elif(t==2):
    fare=20*c
  elif(t==3):
     fare=50*c
  elif(t==4):
     fare= 80*c
  else:
    print("enter proper value")
    tab(c)
  return fare
  taxi['fare']=fare 
   
taxi = {'distance':0,'fare':0}  
str='y'
while(str=='y'or str=='Y'):
  a=int(input("enter source"))
  b=int(input("enter destination"))
  if(a<b):
    c= dist()
    fare=tab(c)
    taxi['distance']=c
    taxi['fare']=fare
  else:
    print("enter valid destination")   
  str=input("do you want to continue(y/n)?") 