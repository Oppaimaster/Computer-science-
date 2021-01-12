username="admin"
password="1234abc"

while True:
  user=input("Enter your username:")
  x=input("Enter your password:")


  if user == username and x == password:
    break
  else:
    print("Incorrect username and/or password")
print("Welcome",username,"you have successfully logger in")
