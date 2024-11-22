Ask = input("Do you want to code or decode?")
if (Ask == "Code"):
  Msg = input("Enter your message: ")
  if (len(Msg) < 3):
    print(Msg[::-1])

  else:
  
    Ex_Msg = (Msg[:1]+Msg[-1:])
    Msg = (Msg[::-1])
    print("Your Encrypted  Msg is : ",Ex_Msg + Msg + Ex_Msg)

else:
  De_Msg = input("Enter Msg to be Decrypted")
  if (len(De_Msg) < 3):
    print(De_Msg[::-1])
  else:
    Ex_Msg = (De_Msg[:1]+De_Msg[-1:])
    De_Msg = (De_Msg[::-1]) 
    print("Your Decrypted Msg is : ",Ex_Msg + De_Msg + Ex_Msg)
    