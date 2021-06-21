usuario = input("Digite se usuário: ")
caracteres = len(usuario)

print(usuario, caracteres, type(caracteres))

if caracteres < 6:
    print("Você precisa digitar pelo menos 6 caracteres")
else:
    print("Você foi cadastrado no sistema")
