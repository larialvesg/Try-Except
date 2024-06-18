import csv


def criar_arquivo(nome_arquivo, numeros):
    with open(nome_arquivo, 'w', newline='') as arquivo:
        escrever = csv.writer(arquivo)
        escrever.writerow(numeros)
    print(f"Arquivo {nome_arquivo} criado com sucesso.")

def soma_numeros(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            leitor_csv = csv.reader(arquivo)
            soma = 0
            for linha in leitor_csv:
                for valor in linha:
                    try:
                        numero = float(valor)
                        soma += numero
                    except ValueError:
                        print(f"Valor não identificado como número: {valor}")
            return soma
    except FileNotFoundError:
        print(f"Não foi possível encontrar esse arquivo: {nome_arquivo}")
        return None


if __name__ == "__main__":
    nome_arquivo = 'numeros.csv'
    numeros = [10, 20, 30, 40, 50.5]

    criar_arquivo(nome_arquivo, numeros)

    soma = soma_numeros(nome_arquivo)
    if soma is not None:
        print(f"A soma dos números é: {soma}")