# Insert user and password and show only normal caracters.

import re

# Insert user and password
name = input("Insert your name: ").strip().lower()  # strip = remove spaces lower = all caracteres is small
password = input("insert your password: ").strip().lower()

# Remove all alphanumeric that is not permited
new_name = re.sub(r"\W", "", name)  # \W it will remove just alphanumerics
new_passd = re.sub(r"[^A-Za-z0-9]", "", password)  # Remove all that is not letter and numbers

# Show the result
print(f"name is: {new_name}")
print(f"password is: {new_passd}")
