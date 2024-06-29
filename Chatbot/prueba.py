# app.py
from flask import Flask, request, render_template, jsonify
from preguntas import Preguntas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({"error": "Bad Request", "message": "No question provided"}), 400
    
    pregunta_usuario = data['question']
    pPractica = Preguntas()
    dato = pPractica.buscar_pregunta_similar(pregunta_usuario.split())    
    print(dato)
    return jsonify({"response": dato})

if __name__ == '__main__':
    app.run(debug=True)