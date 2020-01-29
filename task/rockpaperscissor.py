import random
def randomno():
  no=random.randint(1,3)
  return no

ch='y'
while(ch=='y' or ch=='Y'):
  no=randomno()
  print("1.ROCK")
  print("2.PAPER")
  print("3.SCISSOR")
  guess =int(input("enter your choice"))
  print("computer choice was",no)
  if(guess==no):
    print("its a draw !")
     
  elif(guess==2 and no==1):
    print("you won !! congrats")
  elif(guess==1 and no==2):
    print("sorry ! you lost")
  elif(guess==3 and no==1):
      print("sorry ! you lost")
  elif(guess==1 and no==3):
     print("you won !! congrats") 
  elif(guess==2 and no==3):
    print("sorry ! you lost")
  elif(guess==3 and no==2): 
    print("you won !! congrats") 
  else:
    print("enter valid choice") 
  ch=input("do yo want to continue(y/n)? ")  