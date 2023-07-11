color = {}
n = int (input("Enter the number of elements:"))
for i in range(n):
 key = input("Enter the key: ")
 value = input("Enter the value: ")
 color[key]=value
print("Dictionary elements are:\n")
for key,value in color.items():
 print(key,value)