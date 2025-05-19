from flask import Flask, request, jsonify
from utils.process_query import procesar_pregunta
import os

app = Flask(__name__)

@app.route("/api/consultar", methods=["POST"])
def consultar()::
    data = request.get_json()
    pregunta = data.get("pregunta")
    if not pregunta:
        return jsonify({"error": "Pregunta requerida"}), 400
    resultado = procesar_pregunta(pregunta)
    return jsonify(resultado)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)