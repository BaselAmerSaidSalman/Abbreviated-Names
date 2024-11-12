names = input("Enter the first name and the last name of your friends seperated by comma: ").split(", ")
abbreviated_names = []
for i in names:
  name = i.split(" ")
  print(name)
  abbreviated_names.append(name[0][0] + "." + name[1][0] + ".")
print("Abbreviated_names:")
print("\n".join(abbreviated_names))
   
  

  
