name = ""

while len(name) == 0:
  name = input("What is your name?: ")
  if len(name) > 0:
    break
print("Hello "+ name)

# OR

name = None

while name == None:
  name = input("What is your name?: ")
print("Hello "+ name)