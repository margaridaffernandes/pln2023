from flask import Flask, render_template, request
import json

app = Flask(__name__)

file = open("Output/join_resultado.json")
db = json.load(file)

@app.route("/")
def home():
    return render_template("home.html", title="Dicionário Multilíngue - Multilingual Dictionary - Diccionario Multilingüe")


@app.route('/terms/search')
def search_term():
    term = request.args.get('search-box')
    result = db.get(term)
    return render_template('search.html', title="Dicionário - Dictionary - Diccionario", result=result, term=term)


@app.route("/terms")
def terms():
    return render_template("terms.html",title="Termos médicos (PT - EN - ES)", designations=db.keys())

@app.route("/term/<t>")
def term(t):
    return render_template("term.html", designation=t, value=db.get(t, "None"))


app.run(host="localhost", port=3000, debug=True)