# This application it will Decrpyt letter in game murder
# developed by Andre de Araujo
# Date 25/08/2025

from string import ascii_lowercase, ascii_uppercase

# Build the mapping dictionary
# (a<-->Z, b<-> Y, ..., z<-> A and A<-z>, ..., Z<->a)
pairs = list(zip(ascii_lowercase, ascii_uppercase[::-1]))
letters = {lc: uc for lc, uc in pairs}
letters.update({uc: lc for lc, uc in pairs})


def transform(text: str) -> str:
    return ''.join(letters.get(ch, ch)for ch in text)


# Example usage
user_input = input("Type your sequence: ")

resulted = transform(user_input)

print(f"The answer will be: {resulted}")


# Reverse text
test = resulted[::-1]

# show the result
print(f"Reversed: {test}")
