# tuple = collection which is ordered and unchangeable
#used to group related data

student = ("Fardin", 15, "Male")

print(student.count("Fardin"))
print(student.index("Male"))

for i in student:
  print(i)
if "Bro" in student:
  print("Bro is here!")