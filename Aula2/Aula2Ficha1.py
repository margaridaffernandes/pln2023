import re

# Exercicio 1
# 1.1
line1 = "hello world"
line2 = "goodbye world"
line3 = "hi, hello there"
lines = [line1,line2,line3]

for l in lines:
    if re.match("hello", l):
        print(l,"-","Aparece no início da frase")
    else:
        print(l,"-", "Não aparece no início")

print("\n")

# 1.2
for l in lines:
    if re.search("hello", l):
        print(l,"-","Aparece na frase")
    else:
        print(l,"-", "Não aparece na frase")

print("\n")

# 1.3
line3 = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
print(re.findall(r'[hH][eE][lL]{2}[oO]',line3))

print("\n")

# 1.4
line4 = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
print(re.sub(r'[hH][eE][lL]{2}[oO]','*YEP*',line4))

print("\n")

# 1.5
line5 = "bananas, laranjas, maçãs, uvas, melancias, cerejas, kiwis, etc."
print(re.split(r',',line5))

print("\n")

# Exercício 2
def palavra_magica(frase):
  if re.search(r'por favor[.!?]$',frase):
      return("Termina com a expressão 'por favor'")
  else:
      return("Não termina com a expressão 'por favor'")

print(palavra_magica("Posso ir à casa de banho, por favor?"))
print(palavra_magica("Preciso de um favor."))

print("\n")

# Exercício 3
def narcissismo(linha):
    x = re.findall(r'[eE][uU]',linha)
    print("Aparece",len(x), "vezes")

narcissismo("Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou.")

print("\n")

# Exercício 4
novo_curso = str(input("Introduza o nome do curso "))
def troca_de_curso(linha, novo_curso):
  return(re.sub(r'LEI',novo_curso,linha))

print(troca_de_curso("LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei.", novo_curso))

print("\n")

# Exercício 5
def soma_string(linha):
    x = re.split(r',',linha)
    soma = 0
    for elemento in x:
        novo = int(elemento)
        soma += novo
    return(soma)

print(soma_string("4,-6,2,3,8,-3,0,2,-5,1"))

print("\n")

# Exercício 6
def pronomes(linha):
    return(re.findall(r'[eEtT][uU]|[eE][lL][eEaA][sS]?|[nNvV][óÓ][sS]', linha))

print(pronomes("eu sou tu e eu e ELAS também são nós e Vós e eleS e ele"))

print("\n")

# Exercício 7
def variavel_valida(linha):
    if re.match(r'[a-zA-Z]', linha) and re.search(r'^\w+$', linha): #^inicio letraspalavrasunderscore 0ou+vezes fim
        return("A variável é válida")
    else:
        return("A variável não é válida")

print(variavel_valida("Eusou1?"))

print("\n")

# Exercício 8
def retorna_inteiro(linha):
    return(re.findall(r'[-]?[0-9]+', linha))

print(retorna_inteiro("A sal11sicha 30 é tr 1 -19 1000 -23"))


print("\n")

# Exercício 9
def underscores(linha):
    return(re.sub(r'[ ]+','_',linha))

print(underscores("Posso              ir à casa de banho, por favor?"))

print("\n")

# Exercício 10
lista = ["4700-000","1234-567","8541-543","4123-974","9481-025"]
def divide_cdpostal(lista):
    codigos = []
    for elemento in lista:
        x = re.split(r'[-]',elemento)[0]
        y = re.split(r'[-]', elemento)[1]
        codigos.append((x,y))
    return(codigos)

print(divide_cdpostal(lista))
