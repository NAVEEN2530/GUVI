n= int(input(" Enter any Number: "))  
f = 1
if (num < 0):
   print("factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,n+ 1):
       f = f*i
   print(f)
