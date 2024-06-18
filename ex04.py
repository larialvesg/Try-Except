class Usuario:
    def __init__(self, numero):
        self.numero = numero

    def Conta(self, numero):
        antecessor = numero - 1
        while antecessor > 0:
            numero = numero * antecessor
            antecessor = antecessor - 1
            if antecessor == 0:
                return numero


try:
    resposta = int(input("Digite um número: "))
    while resposta < 0:
        resposta = int(input("Digite um número positivo: "))
        if resposta > 0:
            break
except ValueError:
    print("Você precisa digitar um número inteiro")
else:

    usuario1 = Usuario(resposta)
    print("O fatorial desse número é", usuario1.Conta(resposta))


