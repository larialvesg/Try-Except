class Usuario:
    def __init__(self, numero):
        self.numero = numero

    def Conta(self, numero):
        try:
            resultado = 100 / numero
            return resultado
        except ZeroDivisionError:
            print("Você não pode digitar 0")


try:
    resposta = int(input("Digite um número: "))
    usuario1 = Usuario(resposta)
    print(usuario1.Conta(resposta))
except ValueError:
    print("Você não pode digitar um valor que não é numérico!")
