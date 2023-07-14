import time
name = input("Name: ")
value = input("How much you want: ")
currenttime = time.ctime()
print(f"Hello {name}. You've just withdraw {value}$ at {currenttime}. Have a nice day!")