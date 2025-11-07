# AtUntil python version 3.10 this method was used with
# function and dictionaries python
# After that now you have case to do

linguagem = input(
    'Qual e a linguagem de programacao que voce tem maior dominio: ')

match linguagem:
    case 'Python':
        print('Muito usada em IoT e Inteligencia Artificial')
    case 'JavaScript':
        print('Muito usada em desenvolvimento web')
    case 'C#':
        print('Muito usada em aplicacoes em geral.')
    case _:
        print("A Linguagem nao importa, o que importa e resolver problemas!")
