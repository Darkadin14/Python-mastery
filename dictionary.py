# dictionary = collection which is UNORDERED, CHANGEABLE of unique key : value pairs
#Fast because they use hashing, allow us to access a value quickly

capital = {"USA":"Washington DC",
           "India":"New Delhi",
           "China":"Beijing",
           "Russia":"Moscow"}

#print(capital["USA"])

#print(capital.get("Nazi"))

#print(capital.keys())

#print(capital.values())

#print(capital.items())

capital.update({"Bangladesh":"Dhaka"})

capital.update({"USA":"Sylhet"})

capital.pop("USA")

#capital.clear()

for key, values in capital.items():
  print(key,"-", values)