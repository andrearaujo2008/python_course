# This application will select just numbers from 10 so on

numbers = [5, 12, 18, 7, 20, 3]
# Select the number just greather than 10
resultado = list(filter(lambda x: x > 10, numbers))
# Result
print(resultado)  # Output [12, 18, 20]
