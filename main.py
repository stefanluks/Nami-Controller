from flask import Flask, request, render_template, redirect
from Jimbe import GetAllGames, NovoJogo

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', context={
        "jogos":GetAllGames(),
    })

def GetParams():
    items = []
    dados = str(request.get_data()).replace("b'","").replace("+"," ").split("&")
    for i in dados: items.append(i.split("="))
    objeto = {}
    for i in items:
        objeto[i[0]] = i[1]
    return objeto

@app.route("/jogo/", methods=['POST'])
def Jogo():
    dados = GetParams()
    NovoJogo(dados)
    return redirect("/")

