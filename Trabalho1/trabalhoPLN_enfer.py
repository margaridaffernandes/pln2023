# + ler o output1 filtrado e eliminar as frases perdidas no meio "português - inglês - espanhol"
import re
import json

file = open('Ficheiros/Dicionario_de_termos_medicos_e_de_enfermagem.xml', 'r', encoding="utf-8")
text = file.read()

def limpa(text):
    if not isinstance(text, str):
        return ""
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


index = text.find("<b>A, AN</b>")
if index != -1:
    remove_text = text[index:]
    
    remove_text = re.sub(r'</?text.*?>','', remove_text) # limpa tudo o que diz texto
    remove_text = re.sub(r'\n[\s*○\s*]+','\n', remove_text) # limpa as bolinhas
    remove_text = re.sub(r'[ÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑA-Z]{3}\s?\n[ÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑA-Z]{3}\nSou.*\n(.*\n){1,5}\d{2,3}\n',' ', remove_text)
    remove_text = re.sub(r'Sou.*\n(.*\n){1,5}\d{2,3}\n', '', remove_text) #limpa as quebras de pagina que contem numero das paginas
    remove_text = re.sub(r'Sou En.*\n(.*\n){2}', '', remove_text) #limpa as quebras de pagina aleatorias sem numero de paginas
    remove_text = re.sub(r'-\n','',remove_text) #limpa os hifens qd há paragrafo nas descrições
    remove_text = re.sub(r'-</i>\n<i>(.*)</i>', r'\1</i>', remove_text) #limpa os <i> e os hifens entre <i>'s, mantendo apenas a palavra lá dentro, juntandos os 2 <i>'s
    remove_text = re.sub(r'\n?<i>(.*)</i>\n', r'\1', remove_text) #limpa <i> mantendo apenas as palavras no seu interior
    remove_text = re.sub(r'([A-Z])\1<b>', r'<b>', remove_text)
    remove_text = re.sub(r'<item .*\n(.*\n)*</pdf2xml>', ' ', remove_text) #limpa a parte final do xml dps do dicionario em si
    remove_text = re.sub(r'-</b>\n<b>', r'', remove_text) #limpa hifens dentro dos termos
    remove_text = re.sub(r'</b>\n\s?<b>', r'', remove_text)
    remove_text = re.sub(r'<b>\s</b>', r' ', remove_text)
    remove_text = re.sub(r'<b>([A-Z][^ÁÉÍÓÚÁÂÊÎÔÛÃÕÇA-Z]*?)</b>', r'\1', remove_text)
    remove_text = re.sub(r'<b>(\d.*)</b>', r'\1', remove_text)
    remove_text = re.sub(r'<b>([^ÁÉÍÓÚÁÂÊÎÔÛÃÕÇA-Z]*?)</b>', r'\1', remove_text)
    remove_text = re.sub(r'<b>(.*)</b>[\n\s][^-]', r'<b>\1</b> - ', remove_text)
    remove_text = re.sub(r'</b>[\n\s]?-', r'</b>', remove_text)
    remove_text = re.sub(r'[^\n]<b>', r'\n<b>', remove_text)
    remove_text = re.sub(r'Vertigens\.\)', r'Vertigens.)\n<b>', remove_text)
    
    
    matches = re.findall(r'<b>(.*?)</b>\s*(.*?)\s*(?=<b>|$)', remove_text, re.DOTALL)
    result_dict = {}

    for match in matches:
        key = match[0].replace(',', '').lower()
        value = match[1].strip()
        value = limpa(value)
        result_dict[key] = {"designacao": value}
    
    file_out = open("Output/Dicionario_de_termos_medicos_e_de_enfermagem.json", "w", encoding="utf-8")
    json.dump(result_dict, file_out, ensure_ascii=False, indent=4)
    file_out.close()