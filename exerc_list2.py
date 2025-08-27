# Put the names

a = input("Type the first name:")
b = input("Type the second name:")
c = input("Type the third name:")
d = input("Type the fourth name:")
e = input("Type the fifth name:")
names = a, b, c, d, e
sorted_name = sorted(names)

print("The name is:", sorted_name[::-1])

if "Alice" in sorted_name:
    print("Alice is in the list")
else:
    print("Alice is not in the list")
