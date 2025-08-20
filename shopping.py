# This program it will calculate of two products and show you the result

print("Welcome the Shopping fast, where the lowers prices")

price1 = float(input("Type the first product, please: "))
price2 = float(input("Type the second product, please: "))
discount = float(input("Could you please, insert your discount: "))

total = (price1 + price2) - (price1 + price2) * (discount / 100)

print(f"The total price of two products was: {total}")
