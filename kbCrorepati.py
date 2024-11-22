name = input("Enter your name: ")
print("Welcome", name)
list = ["Who is the Prime Minister of India"]
options = ["Arvind kejerewal", "Rahul Gandhi", "Modi", "Eknath Shinde"]
list2 = ["what is squaer of 100"]
options2 = ["1", "10", "100000", "10000"]
list3 = ["Who invented 0"]
options3 = ["Arya bhatta", "Newton", "Shakesphere", "Trump"]
list4 = ["Who started swaraj "]
options4 = ["Shivaji maharaj", "Aurangzeb", "Adilshah", "Mahatma Gandhi"]
i = 0
while (i >= 4):
  continue
print(list)
print(options)
ans = (input("Select Answer"))
if (ans == options[2]):
  print("Congrats you won 5000")
  i = i + 1
else:
  print("Sorry you lost")
  exit()

print(list2)
print(options2)
ans = (input("Select Answer"))
if (ans == options2[3]):
  print("Congrats you won 10000")
  i = i + 1
else:
  print("Sorry you lost")
  exit()

print(list3)
print(options3)
ans = (input("Select Answer"))
if (ans == options3[0]):
  print("Congrats you won 1 Lakh")
  i = i + 1
else:
  print("Sorry you lost")
  exit()

print(list4)
print(options4)
ans = (input("Select Answer"))
if (ans == options4[0]):
  print("Congrats you won 1 CR")
  i = i + 1
else:
  print("Sorry you lost")
  exit()
