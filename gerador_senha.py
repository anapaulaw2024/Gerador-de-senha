import random

cripto = [1,2,6,5,"d","A",3.14,56,32,64]

def gerar_senha(comprimento_senha):
    caracteres = cripto
    senha = ""
    for i in range(comprimento):
        senha += random.choice(caracteres)
    return senha

comprimento_senha = int(input("Digite o comprimento da senha desejada: "))
nova_senha = gerar_senha(comprimento_senha)
print("Nova senha gerada:", nova_senha)
