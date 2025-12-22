
n1 = int(input("Type a number you want to start: "))
n2 = int(input("Type a number you want to end: "))

print("The even numbers are:", end=" ")

for i in range(n1, n2 + 1):
    if i % 2 == 0:

        print(i, end=" ")
