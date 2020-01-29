import random
def randomno(n):
  no=random.randint(0,n)
  return no

n=int(input("enter range"))
no=randomno(n)
for i in range(n):
  guess =int(input("enter your guess"))
  if(guess==no):
    print("winner !!")
    break 
  elif(guess!=no) :
       print("try again")
  else:
    print("you lost")     