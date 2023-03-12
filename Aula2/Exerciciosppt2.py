import re

texto = "O tio da Maria e do Tiago comprou, na terça feira, dia 2 do 07 de 2019 tapete." \
        "Pagou 0,60€ por um café."

# Exercicio 1
print(re.findall(r'\b\w*t\w*\b', texto))

print('\n')

# Exercicio 2
print(re.findall(r'\b\w*[tT]\w*\b', texto))

print('\n')

# Exercicio 3
print(re.findall(r'[A-Za-z][^\s]*', texto))
print(len(re.findall(r'[A-Za-z][^\s]*', texto)))

print('\n')

# Exercicio 4
print(re.findall(r'\d{1,}', texto))

print('\n')

# Exercicio 5
print(re.findall(r'\d{1,},\d{1,}', texto))

print('\n')

# Exercicio 6
print(re.findall(r'\w{4,}', texto))

print('\n')

# Exercicio 7
if re.findall(r'^[^m]*M[^m]*$', texto):
    print("A string tem M e não tem M", texto)
else:
    print("A string não se enquadra no padrão")

print('\n')

# Exercicio 8
palavra = "texto"
p = "azul"
if re.findall(r'(\w).*\1',palavra):
    print("A palavra tem um caracter repetido duas vezes", "-", palavra)
else:
    print("A palavra não tem um caracter repetido duas vezes", "-", palavra)

print('\n')

# Exercicio 9
palavra = "ttttttt"
p = "azulosjc"
if re.findall(r'^(\w)\1+$',palavra):
    print("A palavra tem apenas um caracter repetido", "-", palavra)
else:
    print("A palavra tem mais do que um ou nenhum caracter repetido", "-", palavra)

print('\n')

# Exercicio 10
t = "O {rapaz} foi comprar {comida} ontem {e amanhã}"
print(re.findall(r'\{(?:\w+\s*)+\}',t))