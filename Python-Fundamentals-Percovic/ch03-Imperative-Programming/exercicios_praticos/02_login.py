usuarios = ['joe', 'sue', 'hani', 'sophie']

usuario = input("Digite seu nome: ")

if usuario in usuarios:
    print(f"Login: {usuario}")
    print("Você entrou!")
    
else:
    print(f"Login: {usuario}")
    print("Usuário desconhecido")

print("Fim.")