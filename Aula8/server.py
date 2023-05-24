from flask import Flask, render_template, request
import json
import re

app = Flask(__name__)

file = open("terms.json")

db = json.load(file)
file.close()


@app.route("/")
def home():
    return render_template("home.html", title="Welcome!!!")


@app.route("/terms")
def terms():
    return render_template("terms.html", designations=db.keys())


@app.route("/term/<t>")
def term(t):
    return render_template("term.html", designation=t, value=db.get(t, "None"))


@app.route("/table")
def searchtable():
    search_term = request.args.get("search_term", "").lower()

    # Load JSON data from file
    with open('terms.json', 'r') as file:
        json_data = file.read()

    # Convert JSON to a Python dictionary
    data = json.loads(json_data)

    results = []  # Lista para armazenar os resultados da pesquisa

    for term, desc in data.items():
        if search_term in term.lower() or search_term in desc['desc'].lower():
            results.append((term, desc['desc']))

    return render_template('table_search.html', results=results)



@app.route("/terms/search")
def search():

    text = request.args.get("text")
    lista = []
    if text:
        for designation, description in db.items():
            # if text in description["desc"] or text in designation:
            # if text.lower() in description["desc"].lower() or text.lower() in designation.lower():
            if re.search(text,designation,flags=re.I) or re.search(text,description["desc"],flags=re.I): 
                lista.append((designation,description))

    return render_template("search.html",matched = lista)

@app.route("/term", methods=["POST"])
def addTerm():
    print(request.form)
    designation = request.form["designation"]
    description = request.form["description"]

    if designation not in db:
        info_message = "Term Added correctly"
    else:
        info_message = "Term Updated correctly!"

    db[designation] = {"desc":description}
    file_save = open("terms.json","w")
    json.dump(db,file_save, ensure_ascii=False, indent=4)
    file_save.close()

    return render_template("terms.html", designations=db.keys(), message = info_message)



@app.route("/term/<designation>", methods=["DELETE"])
def deleteTerm(designation):
    desc = db[designation]
    if designation in db:
        print(designation)
        del db[designation]
        print(db.get(designation))
        file_save = open("terms.json","w")
        json.dump(db,file_save, ensure_ascii=False, indent=4)
        file_save.close()
        
    return {designation: {"desc":desc}}


app.run(host="localhost", port=3000, debug=True)