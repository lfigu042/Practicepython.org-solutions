# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input("Enter num to check: "))
check = int(input("Enter num to divide by : "))

if(num%4 == 0):
  print(" number is divisible by 4!")
elif(num%check == 0):
  print("The number divided evenly")
else:
  print("The division left a remainder")
