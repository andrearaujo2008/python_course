# Autenticacao de usuario
usuario = input("Digite o seu nome: ").strip()
senha = input("Digite a sua senha: ")
if usuario == 'admin' and senha == '123':
    print("Voce tem permissao de acesso;")
else:
    print("Voce nao tem permissao de acesso.")
