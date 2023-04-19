import re
import json

# NOTA: ao passar de .pdf para .xml, algumas palavras com acentos ficaram separadas, por exemplo, 'epífise' ficou 'epífi se', 'metátese' ficou 'metáte se'. Contudo, são probelmas que nos ultrapassam, e sendo a uníca solução possível a junção manual dos sufixos, optamos por manter, dado que é percetível a leitura da palavra.

def clean(text):
    text = re.sub(r"\s+", " ", text)   # \s* substitui todos os espaços e \n por apenas 1 espaço
    return text.strip() # Strip() retira o \n no início e no fim da frase

file = open("Ficheiros/anatomiageral.xml", "r", encoding="utf-8")
text = file.read()

text = re.sub(r"</?page.*>","", text)  # Remover <page> e </page>
text = re.sub(r"</?image.*?>", "", text) # Remover <image> e </image>
text = re.sub(r"</?fontspec.*?>", "", text) # Remover <fontspec> e </fontspec>
text = re.sub(r"<[?]xml(.*)?>", "", text) # Remover <xml> e </xml>
text = re.sub(r"<[!]DOCTYPE(.*)?>","", text) # Remover <DOCTYPE> e </DOCTYPE>
text = re.sub(r"</?pdf(.*)?>", "", text) # Remover <pdf> e </pdf>
text = re.sub(r"<text(.*)>\s*(\*)(.*)</text>", "", text) # Remover frases inicializadas com *, ** e ***
text = re.sub(r'<text[^>]*><b>[A-Z]</b>\s*</text>\n', '', text) # Remover letras isoladas s/ espaços
text = re.sub(r'<text[^>]*>\s*(<b>)?[ABC](,\s*[ABC])*(</b>)?\s*</text>', '', text) # Remover letras e combinações de letras c/ espaços
text = re.sub(r"A, F", r"", text)
text = re.sub(r"C VII", r"", text)
text = re.sub(r"Ver pág. 40", r"", text)
text = re.sub(r"\*+", "", text) # Remover 1 ou mais *
text = re.sub(r'<text.*?>\s*\d(\.?)+(\.\d+)?([;,]?\s*\d+(\.\d+)?)*\s*</text>', '#', text) # Substituir números por marcador #
text = re.sub(r"#\n<text(.*)>(.*)</text>", r"<text\1><b>\2</b></text>", text)
text = re.sub(r"><b></b>", ">", text) # Remover os <b></b> que ficaram a mais
text = re.sub(r"#+(.*)", "", text) # Remover os # que ficaram a mais
text = re.sub(r"-</b></text>\n<text(.*)><b>", "", text)  # Juntar as expressões que estão separadas pelas regras de translineação
text = re.sub(r"\[\[(.*)\]\]",r"\1", text)
text = re.sub(r"<i><b>(.*)</b></i>([^<]*)", r"<t>\1</t>\2", text) # Substituir o marcador b|i
text = re.sub(r"<i>(.*)</i>([^<]*)", r"<b>\1</b>\2", text) # Substituir o marcador i
text = re.sub(r"</?text.*?>", "", text) # Remover <text> e </text>
text = re.sub(r"-\n", "", text) # Remover os -\n que resulta da translineação
text = re.sub(r"\bm+\.", "", text) # Remover marca m. e mm.
text = re.sub(r"<b> </b>", "", text) # Remover marca <b> </b>
text = re.sub(r"<b>\.</b>", "", text)
text = re.sub(r"<b>(I+)</b>", r"\1", text)
text = re.sub(r"\bIII\b\n\bII\b\n\bI\b\n\bI\b\n\bV\b", "", text) # Remover numeração romana extra 
text = re.sub(r"\n(\s*)\n", "\n", text) # Remover espaços


# Pesquisar a expressão
list = re.findall(r"<b>(.*)</b>([^<]*)", text) # Pesquisar a expressão

# Cria um novo dicionário com as modificações desejadas
dicionario_modificado = {}
for termo, designacao in list:
    chave_modificada = termo.strip().replace('\n', '').lower() # Remover tudo depois do último '.' na chave
    ultimo_ponto_chave = chave_modificada.rfind('.')
    if ultimo_ponto_chave != -1:
        chave_modificada = chave_modificada[:ultimo_ponto_chave]
    valor_modificado = designacao.strip().replace('\n', '') # Remover tudo depois do último '.' no valor
    ultimo_ponto_valor = valor_modificado.rfind('.')
    if ultimo_ponto_valor != -1:
        valor_modificado = valor_modificado[:ultimo_ponto_valor]
    dicionario_modificado[chave_modificada] = {"descricao": valor_modificado}


output = open("Output/anatomiageral.json", "w", encoding="utf-8")
json.dump(dicionario_modificado, output, ensure_ascii=False, indent=4)

output.close()

file.close()