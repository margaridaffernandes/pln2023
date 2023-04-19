import re
import json

# abrir o arquivo e ler o conteúdo
with open("Ficheiros/dicionario_termos_medicos_pt_es_en.xml", "r") as f:
    text = f.read()

match = re.search(r'<b>Dicionário de termos médicos.*', text) # encontrar a linha Dicionário de termos médicos (tem <b> e as restantes não)
new_text = text[match.start():] # extrair o texto a partir dessa linha


clean_file = re.sub(r'\n</page>\n<.*>', '', new_text) # aqui tirei as páginas, o \n antes e depois é para colar todas as linhas
clean_file = re.sub(r'<.*">', '', clean_file) # aqui tirei as partes iniciais de cada linha, coloquei as aspas porque todos os iniciais têm "" e os restantes não
clean_file = re.sub(r'</text>', '', clean_file) # aqui limpei os </text>
clean_file = re.sub(r'\n<i>.*</i>', '', clean_file) # aqui estou a tirar os m e os f
clean_file = re.sub(r'<b>português</b>\n<b>–</b>\n<b>inglês</b>\n<b>–</b>\n<b>espanhol</b>\n', '',clean_file) # aqui tirei a parte inicial de cada página que dizia as linguas
clean_file = re.sub(r'<b>Dicionário de termos médicos</b>\n<b>português – inglês – espanhol</b>\n', '', clean_file) # aqui tirei a parte inicial do documento
clean_file = re.sub(r'-\n', '', clean_file) # aqui corrigi as palavras que estavam dividas em duas linhas
clean_file = re.sub(r'\s*<fontspec.*/>','', clean_file)
clean_file = re.sub(r'<b>.*</b>\n<b>\d{2}[0|2|4|6|8]</b>\n<b>[A-Z]</b>\n', '', clean_file)
clean_file = re.sub(r'<b>[A-Z]</b>\n', '', clean_file) # aqui tirei as letras sozinhas que estavam no inicio de cada página
clean_file = re.sub(r'<b>\d{2}[1|3|5|7|9]</b>\n<b>.*</b>\n', '', clean_file) # aqui tirei os número de página ímpares
clean_file = re.sub(r'<b>bloqueador-</b>\nβ', r'<b>bloqueador-β</b>', clean_file)
clean_file = re.sub(r'<b>.*</b>\n<b>\d{2}[0|2|4|6|8]</b>\n', '', clean_file) # aqui tirei os número de página pares
clean_file = re.sub(r'</b>\n<b>', ' ', clean_file)
clean_file = re.sub(r'U\n(.*)\n(.*)\nE\n', r'U\n\1 \2\nE\n', clean_file) # se o U tiver 2 linhas
clean_file = re.sub(r'U\n(.*)\n(.*)\n(.*)\nE\n', r'U\n\1 \2 \3\nE\n', clean_file) # se o U tiver 3 linhas
clean_file = re.sub(r'U\n(.*)\n(.*)\n(.*)\n(.*)\nE\n', r'U\n\1 \2 \3 \4\nE\n', clean_file) # se o U tiver 4 linhas
clean_file = re.sub(r'E\n(.*)\n(.*)\n<b>', r'E\n\1 \2\n<b>', clean_file) # se o E tiver 2 linhas
clean_file = re.sub(r'E\n(.*)\n(.*)\n(.*)\n<b>', r'E\n\1 \2 \3\n<b>', clean_file) # se o E tiver 3 linhas
clean_file = re.sub(r'E\n(.*)\n(.*)\n(.*)\n(.*)\n<b>', r'E\n\1 \2 \3 \4\n<b>', clean_file) # se o E tiver 4 linhas
clean_file = re.sub(r'E\ndesabrigado(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n', r'E\ndesabrigado \1 \2 \3 \4 \5 \6\n', clean_file) # se o E tiver 6 linhas
clean_file = re.sub(r'E\nzumbido', r'E\nzumbido\n<b>', clean_file)
clean_file = re.sub(r'</b>\n\)\n', r')</b>\n', clean_file)
clean_file = re.sub(r'<b>(.*)</b>(.*)\n<b>(.*)</b>', r'\n<b> \1 \2 \3</b>', clean_file)


pattern1 = r'<b>(.*)</b>'
pattern2 = r'U\n(.*)\nE'
pattern3 = r'E\n(.*)\n<b>'

matches1 = re.findall(pattern1, clean_file)
matches2 = re.findall(pattern2, clean_file)
matches3 = re.findall(pattern3, clean_file)

dicionario = {}

for i, term in enumerate(matches1):
    if i < len(matches2) and i < len(matches3):
        translation_en = matches2[i]
        translation_es = matches3[i]
        dicionario[term] = (translation_en, translation_es)

# Organização no ficheiro json
for termo, traducao in dicionario.items():
    en = traducao[0]
    Spanish = traducao[1]
    dicionario[termo] = {
        "ingles": en,
        "espanhol": Spanish
    }

file_out = open("Output/dicionario_termos_medicos_pt_es_en.json", "w", encoding="utf-8")
json.dump(dicionario, file_out, ensure_ascii=False, indent=4)

file_out.close()