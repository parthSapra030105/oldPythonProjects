print("This is a Calculator")
a = int(input("Enter the value if a: "))
b = int(input("Enter the value of b :"))
c = int(input("Enter what operation : "))
if (c == 1):
  print("Sum is: ", a + b)
elif (c == 2):
  print("Diff is : ", a - b)
elif (c == 3):
  print("Product is : ", a * b)
elif (c == 4):
  print("quotient is : ", a / b)
else:
  print("Remainder is : ", a % b)
