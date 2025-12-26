# Este metodo verifica a string inteira para ver se a especifica palavra corresponde

import re
texto = "Python"
if re.fullmatch("Python", texto):
    print("A string e exatamente Python.")
else:
    print("String e diferente de Python.")
