import json
import re
from deep_translator import GoogleTranslator


file_in = open('dicionario_medico.json', 'r', encoding='utf-8')
dic = json.load(file_in)


def translate(entrie):
    with open('termos_traduzidos.txt', 'r', encoding='utf-8') as read_file:
        lines = read_file.readlines()
    translations = {}
    for line in lines:
        line = line.strip()
        key, value = line.split(" @ ")
        translations[key] = value
    try:
        return translations[entrie]
    except KeyError:
        return entrie


new_dic = {}
for key, value in dic.items():
    en_translation = translate(key)
    new_dic[key] = {
        "description": value,
        "en": en_translation
    }


file_out = open('result_ficheiro.json', 'w')
json.dump(new_dic, file_out, ensure_ascii=False, indent=4)

file_in.close()
file_out.close()