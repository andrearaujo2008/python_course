def obter_url_base():
    return "https://google.com"


ub = obter_url_base  # Funcao chamada () no final
print(ub)  # Saida <function obter_url_base at 0x000002DD70151440>

# Correto
print(ub())
