print("Welcome to your to do list")
tasks = []


def addtask():
  tasks.append(input("Enter the Tasks: "))


def listtask():
  print(tasks[::])


def deletetask():
  try:
    listtask()
    task = int(input("Task no :"))
    tasks.pop(task)
    listtask()

  except:
    print("Statement Invalid")


def cleartasks():
  tasks.clear()
  print(tasks[:])


while (True):
  print("1. Add a task")
  print("2. Delete a task")
  print("3. List a task")
  print("4. End")

  Choice = input("Select an option: ")

  if (Choice == "1"):
    addtask()
  elif (Choice == "2"):
    deletetask()
  elif (Choice == "3"):
    listtask()
  else:
    cleartasks()
    break
