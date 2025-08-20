# This program it will calculate how many kilometers your car make.

kilometers = 100
liters = float(input("Type the liters you spend por 100 km: "))
destination = float(input("Type the kilometers your destination: "))

consumption = kilometers / liters
consume = destination / consumption
print(f"Your car do {consumption:.2f} km per liter")
print(f"You will spend your destination {destination}")
print(f"Km total {consume:.2f} liters")
