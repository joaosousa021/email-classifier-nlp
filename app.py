# app.py
import sys
import os
import io
from flask import Flask, request, jsonify, render_template


project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


from core.logica_ia import classificar_email, extrair_nome
from core.respostas import gerar_resposta
from core.utils import extrair_texto_pdf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar_email():
    texto_email = ""
    arquivo = request.files.get('email_file')

    if 'email_text' in request.form and request.form['email_text'].strip():
        texto_email = request.form['email_text']
    elif arquivo and arquivo.filename != '':
        if arquivo.filename.endswith('.txt'):
            texto_email = arquivo.read().decode('utf-8')
        elif arquivo.filename.endswith('.pdf'):
            file_stream = io.BytesIO(arquivo.read())
            texto_email = extrair_texto_pdf(file_stream)
        else:
            return jsonify({'error': 'Formato de arquivo não suportado.'}), 400
    else:
        return jsonify({'error': 'Nenhum texto ou arquivo de email fornecido.'}), 400

    if not texto_email:
        return jsonify({'error': 'Não foi possível extrair texto do arquivo.'}), 400

    categoria = classificar_email(texto_email)
    nome_remetente = extrair_nome(texto_email)
    resposta_sugerida = gerar_resposta(categoria, nome_remetente)

    return jsonify({
        'categoria': categoria,
        'resposta_sugerida': resposta_sugerida,
        'nome_detectado': nome_remetente or "Nenhum nome detectado"
    })

if __name__ == '__main__':
    app.run(debug=True)