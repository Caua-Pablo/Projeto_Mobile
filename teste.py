import secrets
import string
import hashlib

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

def gerar_novamente():
    resposta = input("Deseja Gerar Outra Senha (sim/não)? ")
    if resposta.lower() == "sim":
        return True
    return False

def criptografar_senha():
    while True:
        criptograf = int(input("Deseja Criptografar sua senha?: "))
        if criptograf == "sim":
            print("Sua Senha Será Gerada Abaixo!")
        if not gerar_novamente():
            continue

    senha = criptograf(criptograf)
    criptograf = hashlib.sha256()
    criptograf.update(senha)
    print(criptograf)

while True:
    tamanho = int(input("Digite a Quantidades de Caracteres a ser Inseridos na Senha: "))
    senha = gerar_senha(tamanho)
    print("Senha gerada:", senha)
    criptografar_senha()
    if not gerar_novamente():
        break