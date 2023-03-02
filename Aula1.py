# Questão 1
import string

a = input("Qual é o teu nome? ")
b = a.upper()
print(b)


# Questão 2
def pares():
    n = int(input("Quantos números quer escrever? "))
    lista = []
    for i in range(n):
        x = int(input("Introduza um número: "))
        lista.append(x)
        i += 1
    y = [c for c in lista if c%2==0]
    print(y)
pares()


# Questão 3
def lerinverso():
    nome = input("Qual é o nome do ficheiro? ")
    ficheiro = open(nome,"r") # Abrir o ficheiro em modo de leitura
    linhas = ficheiro.readlines() # Ler todas as linhas do ficheiro para uma lista
    linhas.reverse() # Inverter a ordem da lista
    for linha in linhas:
        print(linha.strip())
lerinverso()


# Questão 4
def ordena(e):
    return e[1]

def maispalavras():
    nome = input("Qual é o nome do ficheiro? ")
    ficheiro = open(nome,"r") # Abrir o ficheiro em modo de leitura
    linhas = ficheiro.read()  # Ler todas as palavras do ficheiro para uma lista
    sempontuacao = linhas.translate(str.maketrans('','',string.punctuation)) # Retirar pontuação
    semmaiusculas = sempontuacao.lower()  # Retirar maiusculas
    palavras = semmaiusculas.split() # Separar as palavras
    dicionario = {}
    for p in palavras:
        if p in dicionario:
            dicionario[p] += 1
        else:
            dicionario[p] = 1
    ordenado = sorted(dicionario.items(), key=ordena, reverse=True) # Dicionario ordenado decrescente
    for chave, valor in ordenado[:10]:
        print(f"{chave}:{valor}") # Imprimir primeiros 10
maispalavras()


# Questão 5
from unidecode import unidecode
def limpar():
    nome = input("Qual é o nome do ficheiro? ")
    ficheiro = open(nome, "r") # Abrir o ficheiro em modo de leitura
    leitura = ficheiro.read() # Ler o ficheiro
    sempontuacao = leitura.translate(str.maketrans('', '', string.punctuation))  # Retirar pontuação
    semmaiusculas = sempontuacao.lower()  # Retirar maiusculas
    texto = unidecode(semmaiusculas)
    print(texto)
limpar()


def geral():
    questao = int(input("Qual é a operação?"
                    "\n1 - inverter"
                    "\n2 - contar maiúsculas e minúsculas"
                    "\n3 - contar vogais"
                    "\n4 - colocar maiúsculo"
                    "\n5 - colocar minúsculo \n"))
    frase = input("Introduza a frase: ")

    if questao == 1:
        invertida = frase[::-1]
        print(invertida)
    elif questao == 2:
        maiusculas = 0
        for x in frase:
            if x.isupper():
                maiusculas += 1
        minusculas = 0
        for x in frase:
            if x.islower():
                minusculas += 1
        print("Maiusculas: " + str(maiusculas))
        print("Minusculas: " + str(minusculas))
    elif questao == 3:
        contagem = 0
        vogais = ['a','e','i','o','u','A','E','I','O','U']
        for v in frase:
            if v in vogais:
                contagem += 1
        print("Vogais: " + str(contagem))
    elif questao == 4:
        print(frase.upper())
    elif questao == 5:
        print(frase.lower())
geral()
