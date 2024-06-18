class Usuario:
    def __init__(self, frase):
        self.frase = frase

    def receber_frase(self, frase):
        frase = len(resposta.split())
        return frase

try:
    resposta = str(input("Digite uma frase e irei retornar o número de palavras nela: "))
    usuario1 = Usuario(resposta)
    print(f"Sua frase possui {usuario1.receber_frase(resposta)} palavras")
except "":
    print("Você não escreveu nada")
