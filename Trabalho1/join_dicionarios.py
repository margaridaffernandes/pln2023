import json

# Ler os arquivos JSON
with open('Output/dicionario_termos_medicos_pt_es_en.json', 'r') as f:
    json1 = json.load(f)

with open('Output/anatomiageral.json', 'r') as f:
    json2 = json.load(f)

with open('Output/Dicionario_de_termos_medicos_e_de_enfermagem.json', 'r') as f:
    json3 = json.load(f)

resultado = {}

termos_json1 = set(json1.keys())
termos_json2 = set(json2.keys())
termos_json3 = set(json3.keys())

# Chaves em comum em json1 e json2
termos_comuns = termos_json1.intersection(termos_json2)

# Chaves em json1 mas não em json2
termos_1 = termos_json1.difference(termos_json2)

# Chaves em json2 mas não em json1
termos_2 = termos_json2.difference(termos_json1)

for termo in termos_comuns:
    resultado[termo] = {
        "descricao": json2[termo]["descricao"],
        "ingles": json1[termo]["ingles"],
        "espanhol": json1[termo]["espanhol"]
    }

for termo in termos_1:
    resultado[termo] = {
        "ingles": json1[termo]["ingles"],
        "espanhol": json1[termo]["espanhol"]
    }

for termo in termos_2:
    resultado[termo] = {
        "descricao": json2[termo]["descricao"],
    }

for termo in termos_json3:
    info = {"designacao": json3[termo]["designacao"]}
    
    if termo in termos_comuns:
        info["ingles"] = json1[termo]["ingles"]
        info["espanhol"] = json1[termo]["espanhol"]
        info["descricao"] = json2[termo]["descricao"]
    elif termo in termos_1:
        info["ingles"] = json1[termo]["ingles"]
        info["espanhol"] = json1[termo]["espanhol"]
    elif termo in termos_2:
        info["descricao"] = json2[termo]["descricao"]
    
    resultado[termo] = info
              
                 
with open('Output/join_resultado.json', 'w') as f:
    json.dump(resultado, f, indent=4, ensure_ascii=False)