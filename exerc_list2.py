# Ask the user to input 5 names
names = []
for i in range(5):
    name = input("Enter a name: ")
    names.append(name)

# print the list in revest order
print("The name is:", names[::-1])

# Check if "Alice" is in the list
if "Alice" in names:
    print("Alice is in the list")
else:
    print("Alice is not in the list")
