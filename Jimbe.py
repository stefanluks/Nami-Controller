'''Api concect Thounsed Sunny Api [https://thousand-sunny-api.onrender.com] to Nami the App controller [Nami Navegadora]'''
import requests as req
import json


def GetRankingGeral(id):
    resposta = req.get("https://thousand-sunny-api.onrender.com/rankingGeral/"+str(id))
    object = json.loads(resposta.content)
    return object["content"]["ranking"]


def GetAllGames():
    resposta = req.get("https://thousand-sunny-api.onrender.com/jogos")
    object = json.loads(resposta.content)
    saida = []
    for jogo in object["content"]:
        saida.append({
            "id":jogo["id"],
            "nome":jogo["nome"],
            "descricao":jogo["descricao"],
            "ranking":GetRankingGeral(jogo["id"])
        })
    return saida


def NovoJogo(objeto):
    resposta = req.post("https://thousand-sunny-api.onrender.com/jogos", json=objeto)
    return json.loads(resposta.content)