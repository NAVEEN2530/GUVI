str='y'
while(str=='y'or str=='Y'):
  a=int(input("enter source"))
  b=int(input("enter destination"))
  c=b-a
  print("1.micro(10 rs/km)")
  print("2.prime(20rs/km)")
  print("3.mini(50rs/km)")
  print("4.suv(80rs/km)")
  t=int(input("enter the type of cab"))
  if(t==1):
    print("the total fare is",10*c)
  elif(t==2):
    print("the total fare is ",20*c)
  elif(t==3):
    print("the total fare is ",50*c)
  elif(t==4):
    print("the total fare is ",80*c)
  else:
    print("enter proper value")
  str=input("do you want to continue(y/n)?") 