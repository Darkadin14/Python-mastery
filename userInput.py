name = str(input("What is your name? :"))
age = int(input("What is your age? :"))
u = (input("How tall are you in cm? :"))
print("Your name is " + name)
if u == float or int:
  print("Your age is " + str(age) + "years old")
  print("Your height is " + str(u) + "cm")
else:
  print("TYPE INT OR DECIMALS!")