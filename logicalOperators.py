#logical statements (and/or/not): Those that help to check if two or more conditions are true

temp = int(input("What's the temperature outside?: "))

if temp >= 0 and temp <= 30:
  print("The temperature is good today!")
elif temp < 0 or temp > 30:
  print("The temperature is bad today!")

# OR

if temp >= 0 and temp <= 30:
  print("The temperature is good today!")
elif not(temp >= 0 or temp <= 30):
  print("The temperature is bad today!")