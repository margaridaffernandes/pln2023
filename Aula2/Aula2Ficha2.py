import re


# Exercicio 1
def iso_8601(texto):
    datas = re.findall(r'(\d{2})/(\d{2})/(\d{4})', texto)
    for date in datas:
        x = '/'.join(date)
        dia = re.match('(\d{2})/(\d{2})/(\d{4})', x).group(1)
        mes = re.match('(\d{2})/(\d{2})/(\d{4})', x).group(2)
        ano = re.match('(\d{2})/(\d{2})/(\d{4})', x).group(3)
        nova_data = f'{ano}-{mes}-{dia}'
        texto = re.sub(x, nova_data, texto)
    return (texto)


print(iso_8601("""A 03/01/2022, Pedro viajou para a praia com a sua família.
Eles ficaram hospedados num hotel e aproveitaram o sol e o mar durante toda a semana.
Mais tarde, no dia 12/01/2022, Pedro voltou para casa e começou a trabalhar num novo projeto.
Ele passou muitas horas no escritório, mas finalmente terminou o projeto a 15/01/2022."""))

print('\n')

# Exercício 2
file_names = [
    "document.txt",  # válido
    "file name.docx",  # inválido
    "image_001.jpg",  # válido
    "script.sh.txt",  # válido
    "test_file.txt",  # válido
    "file_name.",  # inválido
    "my_resume.docx",  # válido
    ".hidden-file.txt",  # válido
    "important-file.text file",  # inválido
    "file%name.jpg"  # inválido
]


def validacao(linhas):
    for ficheiro in linhas:
        if re.search(r'^[\w\-.]+(\.[\w]+)$', ficheiro):
            print(ficheiro, "-", "Válido")
        else:
            print(ficheiro, "-", "Inválido")


validacao(file_names)

print('\n')


# Exercício 2.1
def validacao_modificada(linhas):
    validos = {}
    for ficheiro in linhas:
        if re.search(r'^[\w\-.]+(\.[\w]+$)', ficheiro):
            nome = re.search(r'(^[\w\-.]+)(\.[\w]+)$', ficheiro).group(1)
            extensao = re.search(r'(^[\w\-.]+)(\.[\w]+)$', ficheiro).group(2)
            validos[nome] = extensao
    return (validos)


print(validacao_modificada(file_names))

print('\n')


# Exercício 3
def conversor_nomes(texto):
    return (re.sub(r'([A-Z]\w+)\s?((?:[A-Z]\w+\s?|[dD][oea]s?\s?)*)\s([A-Z]\w+)', r'\3, \1', texto))


print(conversor_nomes("""Este texto foi feito por Sofia Guilherme Rodrigues dos Santos, com 
base no texto original de Pedro Rafael Paiva Moura, com a ajuda
dos professores Pedro Rangel Henriques e José João Antunes Guimarães Dias De Almeida.
Apesar de partilharem o mesmo apelido, a Sofia não é da mesma família do famoso
autor José Rodrigues dos Santos."""))

print('\n')

# Exercício 4
lista = [
    "4700-000",  # válido
    "9876543",  # inválido
    "1234-567",  # válido
    "8x41-5a3",  # inválido
    "84234-12",  # inválido
    "4583--321",  # inválido
    "9481-025"  # válido
]


def divide_cdpostal(lista):
    codigos = []
    for elemento in lista:
        if re.search(r'-', elemento) and re.search(r'\d{4}-\d{3}', elemento):
            x = re.split(r'[-]', elemento)[0]
            y = re.split(r'[-]', elemento)[1]
            codigos.append((x, y))
    return (codigos)


print(divide_cdpostal(lista))

print('\n')

# Exercício 5
abreviaturas = {
    "UM": "Universidade do Minho",
    "LEI": "Licenciatura em Engenharia Informática",
    "UC": "Unidade Curricular",
    "PL": "Processamento de Linguagens"
}


def expande_abreviaturas(texto):
    novo_texto = re.sub(r'abrev{([A-Z]*)}', lambda match: abreviaturas.get(match.group(1)), texto)
    return (re.sub(r'/', '', novo_texto))


print(expande_abreviaturas("A /abrev{UC} de /abrev{PL} é muito fixe! "
                           "É uma /abrev{UC} que acrescenta muito ao curso de /abrev{LEI} da /abrev{UM}."))

print('\n')

# Exercício 6
matriculas = [
    "AA-AA-AA",  # inválida
    "LR-RB-32",  # válida
    "1234LX",  # inválida
    "PL 22 23",  # válida
    "ZZ-99-ZZ",  # válida
    "54-tb-34",  # inválida
    "12 34 56",  # inválida
    "42-HA BQ"  # válida, mas inválida com o requisito extra
]

def validade_matriculas(lista):
    for matricula in lista:
        if re.search(r'[A-Z]{2}([-\s])[A-Z]{2}(\1)\d{2}', matricula) or \
                re.search(r'[A-Z]{2}([-\s])\d{2}(\1)[A-Z]{2}', matricula) or \
                re.search(r'\d{2}([-\s])[A-Z]{2}(\1)[A-Z]{2}', matricula) or \
                re.search(r'[A-Z]{2}([-\s])\d{2}(\1)\d{2}', matricula) or \
                re.search(r'\d{2}([-\s])[A-Z]{2}(\1)\d{2}', matricula) or \
                re.search(r'\d{2}([-\s])\d{2}(\1)[A-Z]{2}', matricula):
            print(matricula, '-', 'Válida')
        else:
            print(matricula, '-', "Inválida")

validade_matriculas(matriculas)

print('\n')

# Exercício 7
def madlibs(texto):
    extra = re.findall(r'\[([\w\s]+)\]', texto)
    for e in extra:
        escrever = str(input(f"Introduza {e} "))
        texto = re.sub(e, escrever, texto)
        texto = re.sub('\[|\]','', texto)
    return(texto)

print(madlibs("""Num lindo dia de [ESTAÇÃO DO ANO], [NOME DE PESSOA] foi passear com o seu [EXPRESSÃO DE PARENTESCO MASCULINA]. 
Quando chegaram à [NOME DE LOCAL FEMININO], encontraram um [OBJETO MASCULINO] muito [ADJETIVO MASCULINO].
Ficaram muito confusos, pois não conseguiam identificar a função daquilo.
Seria para [VERBO INFINITIVO]? Tentaram perguntar a [NOME DE PESSOA FAMOSA], que também não sabia.
Desanimados, pegaram no objeto e deixaram-no no [NOME DE LOCAL MASCULINO] mais próximo. 
Talvez os [NOME PLURAL MASCULINO] de lá conseguissem encontrar alguma utilidade para aquilo."""))

print('\n')

# Exercício 8
def elimina_repetidos(texto):
    palavras = texto.split()
    distintas = []
    for p in palavras:
        if p not in distintas:
            distintas.append(p)
    return ' '.join(distintas)

print(elimina_repetidos("O sol hoje está hoje bastante brilhante mas ontem não estava nada brilhante o sol estava escuro."))