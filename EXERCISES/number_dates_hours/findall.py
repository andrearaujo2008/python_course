import re

texto = "Python3, Python2, Python1"
versoes = re.findall(r"Python\d", texto)
print(versoes)
