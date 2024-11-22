import random

Random_number = random.randint(0, 10)
#print(Random_number)

while (True):
  try:
    Number = int(input("Enter a Random Number: "))
    if (Number == Random_number):
      print("You guessed it right")
      break
    elif (Number > Random_number):
      print("The number is Smaller")
    elif (Number < Random_number):
      print("The number is Greater")
    else:
      print("Invalid")
  except:
    print("Provide an Integer")

print("Game Over!!!")
