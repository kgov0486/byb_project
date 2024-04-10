#Prime numbers portfolio task
#A simple application to identify prime numbers within a specified user input range. 

#MAIN PROGRAM
num2 = int(input("end range "))
print()
print ("The prime numbers are")
print()
for i in range(1, num2+1):
  for j in range(2, i):
    if i % j == 0:
      break 
  else:
     #removing 1 from output 1 not being prime
     if(i!=1):
      print(i)
  

       

