class Usuario:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def Conta(self):
        resultado = numero1 + numero2
        return resultado

try:
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
except ValueError:
    print("Você digitou uma string")
else:
    usuario1 = Usuario(numero1, numero2)
    print("A soma desses números é", usuario1.Conta())
