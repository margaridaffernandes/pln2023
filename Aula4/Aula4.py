import re
import json

def clean(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

file = open('dicionario_medico.xml', 'r')
text = file.read()
text = re.sub(r'</?page.*>','',text)
text = re.sub(r'</?text.*?>','',text)

text = re.findall(r'<b>(.*)</b>([^<]*)', text)
text = [(designation, clean(description)) for designation, description in text]

dictionary = dict(text)

out = open('dicionario_medico.json', 'w')
json.dump(dictionary, out, ensure_ascii=False, indent=4)
out.close()

file.close()


dictionary2 = open('dicionario_medico.json', 'r', encoding='utf-8')
d = json.load(dictionary2)

book = open('LIVRO-Doenças-do-Aparelho-Digestivo.txt', 'r', encoding='utf-8')
b = book.read()
paragraphs = b.split('\n\n')

with open('LIVRO-Doenças-do-Aparelho-Digestivo.html', 'w', encoding='utf-8') as new_book:
    new_book.write('<html>\n<head>\n</head>\n<body>\n')

    for p in paragraphs:
        w = p.split()
        for x, y in enumerate(w):
            ws = y.strip('().?!,-\'"')
            if ws.lower() in d:
                ad = f'<a href="{d[ws.lower()]}">{ws} </a>'
                w[x] = ad
        p = ' '.join(w)
        new_book.write('<p>' + p + '</p>\n')
    
    new_book.write('</body>\n</html>')
    new_book.close()

dictionary2.close()
book.close()
