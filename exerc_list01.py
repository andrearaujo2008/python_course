# Create a list of 10 number
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter and print only even numbers
# even numbers = numeros pares (pt)
even_numbers = []
for n in a:
    if n % 2 == 0:
        even_numbers.append(n)


print(f"The number is: {even_numbers}")
print("Total even numbers", len(even_numbers))
