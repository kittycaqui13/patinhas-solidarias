from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de dados em memória simulada
pets_db = [
    {
        "id": 1,
        "nome": "Thor",
        "especie": "Cachorro",
        "porte": "Médio",
        "idade": "2 anos",
        "status": "Disponível",
    },
    {
        "id": 2,
        "nome": "Gatosa",
        "especie": "Gato",
        "porte": "Pequeno",
        "idade": "7 anos",
        "status": "Disponível",
    },
]

doacoes_db = []


@app.route("/")
def home():
    return jsonify(
        {
            "sistema": "API Patinhas Solidárias",
            "versao": "1.0.0",
            "status": "Online",
        }
    )


@app.route("/api/pets", methods=["GET"])
def listar_pets():
    return jsonify(pets_db), 200


@app.route("/api/pets", methods=["POST"])
def cadastrar_pet():
    novo_pet = request.json
    novo_pet["id"] = len(pets_db) + 1
    pets_db.append(novo_pet)
    return (
        jsonify(
            {
                "mensagem": "Pet cadastrado com sucesso!",
                "pet": novo_pet,
            }
        ),
        201,
    )


@app.route("/api/doar", methods=["POST"])
def registrar_doacao():
    dados = request.json
    doacoes_db.append(dados)
    return (
        jsonify(
            {
                "mensagem": "Doação registrada com sucesso. Muito obrigado!",
                "dados": dados,
            }
        ),
        201,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)