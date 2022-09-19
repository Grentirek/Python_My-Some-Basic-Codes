import time

Logs = {}
print("Starting program...")
time.sleep(1.7)

print("You're must register first.")
time.sleep(0.45)
name = input("Please enter your name: ")
password = input("Please enter your new password: ")
newlog = {name : password}
Logs[name] = password
time.sleep(1.45)
print("You're succesfully registered. Please now login with your account.")
time.sleep(0.2)

name = input("Please enter your name: ")
password = input("Please enter your password: ")
inputing = {name: password}
if inputing == Logs:
    print("Logging...")
    Log = True
else:
    print("Invalid password or name.")




        