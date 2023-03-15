import re

file = open('dicionario_medico.txt')
text = file.read()

text = re.sub(r'\n\n\f(.+\n\n)', r'\n\1', text)
text = re.sub(r'\n\n\f((?:.+))\n[A-ZÁÀÂÃÉÍÓÕÚ]', r'\n\n\1', text)
text = re.sub(r'\n\n\f', r'\n', text)
text = re.sub(r'\f','',text)
capture_words = re.sub(r'\n\n(.+)', r"\n\n@\1", text)
capture_description = re.sub(r'\n([^@\n].+)', r'\n€\1', capture_words)
new_description = re.sub(r'(@.+)\n\n@(.+)', r'\1\n€\2', capture_description)
remove_lines = re.sub(r'(€.+)(?:\n€(.+))+', r'\1\2', new_description)
remove = re.sub(r'[@€]', r'', remove_lines)

new_entries = re.findall(r"\n\n(.+)\n(.+)", remove)
# print(new_entries)

file.close()

html = open('dicionario_medico.html','w', encoding='utf-8')
head = '''
<html>
<head> 
<meta charset='utf-8'/>
<title> Dicionário Médico </title>
</head> 
<body style = "background-color:lavender;">
<h1 style = "text-align:center; color:darkred;"> <br> Dicionário Médico </h1>

'''
entries=list(new_entries)
entries.insert(0,("Designação", "Descrição"))

# Create the HTML table

table = '<table style="border: 1px solid black; border-collapse: collapse; table-layout: auto;">\n'
for i, row in enumerate(entries):
    table += '<tr style="border: 1px solid black; border-collapse: collapse;">'
    for j, item in enumerate(row):
        if i == 0: 
            table += '<th style="font-weight:bold;border-right: 1px solid black;">{}</th>'.format(item)
        else:
            table += '<td style="border-right: 1px solid black;">{}</td>'.format(item)
    table += "</tr>\n"
table += "</table>"

footer = '''

</body>
</html>
'''

html.write(head+table+footer)

html.close()
