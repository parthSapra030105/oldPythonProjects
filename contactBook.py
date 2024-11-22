Contact = {"Parth": 9004317180, "Tejal": 9082869484}
print(Contact)


def add_info():
  Insert_contact = input("Enter Contact Name: ")
  Insert_contact_No = int(input("Enter Contact No: "))
  Contact[Insert_contact] = Insert_contact_No


def search_info():
  searched_contact = input("Enter a Contact you want to search : ")
  if (searched_contact in Contact):
    print("Your Contact is present : ", Contact[searched_contact])
  else:
    print("Given Contact is not present")


def delete_info():
  contact_to_delete = input("Enter a Contact you want to search : ")
  if (contact_to_delete in Contact):
    print("Your Contact ", Contact[contact_to_delete], "is deleted")
    Contact.pop(contact_to_delete)
  else:
    print("Given Contact is not present")


print("Add Contact Info")
print("Search for Contact Info")
print("Display Contacts")
print("Delete Contact")
print("Exit")

while (True):
  try:
    Operation = int(
        input("Enter which Operation would you like to   perform :"))
    if (Operation == 1):
      add_info()
    elif (Operation == 2):
      search_info()
    elif (Operation == 3):
      print(Contact)
    elif (Operation == 4):
      delete_info()
    else:
      break

  except:
    print("Enter an Integer")
