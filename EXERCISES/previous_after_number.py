# This app will sum the previous and after number has typed

# Read the number
n1 = int(input("Type the number: "))

# Sum the number minus 1
previous = n1 - 1
# sum the number plus 1
after = n1 + 1

# This is result
rs = previous + n1 + after

print(f"The result of numbers are: {rs}")
