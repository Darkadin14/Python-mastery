length = int(input("Length = "))
breadth = int(input("Breadth = "))
symbol = input("What symbol do you want?: ")

for i in range(length):
  for j in range(breadth):
    print(symbol, end ="")
  print()