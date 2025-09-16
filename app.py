# -*- coding: utf-8 -*-

# --- Importações de Bibliotecas Padrão ---
import sys
import os
import io

# --- Importações de Terceiros (Libs externas) ---
from flask import Flask, request, jsonify, render_template

# --- Importações Locais (do seu próprio projeto) ---
# Adiciona a raiz do projeto ao path para garantir que os imports funcionem
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from core.logica_ia import classificar_email, extrair_nome
from core.respostas import gerar_resposta_produtiva, gerar_resposta
from core.utils import extrair_texto_pdf

# --- Configuração da Aplicação Flask ---
app = Flask(__name__)

# --- Funções Auxiliares ---

def _extrair_texto_da_requisicao(req):
    """
    Função auxiliar para extrair o texto do e-mail a partir da requisição.
    Lida tanto com texto direto quanto com upload de arquivos (.txt, .pdf).
    Retorna o texto extraído ou None em caso de falha ou formato inválido.
    """
    texto_email = ""
    
    # Prioridade 1: Tenta pegar o texto do campo de formulário
    if 'email_text' in req.form and req.form['email_text'].strip():
        return req.form['email_text']

    # Prioridade 2: Tenta pegar o texto de um arquivo enviado
    arquivo = req.files.get('email_file')
    if arquivo and arquivo.filename != '':
        filename = arquivo.filename.lower()
        if filename.endswith('.txt'):
            texto_email = arquivo.read().decode('utf-8')
        elif filename.endswith('.pdf'):
            # Usa um stream de bytes para ler o arquivo PDF em memória
            file_stream = io.BytesIO(arquivo.read())
            texto_email = extrair_texto_pdf(file_stream)
        
        return texto_email
    
    # Retorna None se nenhum texto ou arquivo válido foi encontrado
    return None

# --- Rotas da Aplicação ---

@app.route('/')
def index():
    """ Rota principal que renderiza a página inicial (index.html). """
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar_email():
    """
    Rota principal da API. Recebe o texto, processa com a IA e retorna
    a classificação e uma sugestão de resposta em formato JSON.
    """
    texto_email = _extrair_texto_da_requisicao(request)

    if not texto_email:
        return jsonify({'error': 'Nenhum texto, arquivo válido ou conteúdo extraível fornecido.'}), 400

    # --- Coração da Lógica de IA ---
    # 1. Classificar a categoria do e-mail
    categoria = classificar_email(texto_email)
    
    # 2. Tentar extrair o nome do remetente
    nome_remetente = extrair_nome(texto_email)

    # 3. Gerar a resposta sugerida com base na categoria
    if categoria == 'produtivo':
        # Se for produtivo, usa a nova função inteligente que analisa o texto
        resposta_sugerida = gerar_resposta_produtiva(texto_email, nome_remetente)
    else:
        # Para outras categorias (improdutivo), usa a função simples
        resposta_sugerida = gerar_resposta(categoria, nome_remetente)

    # 4. Montar e retornar a resposta final em JSON
    return jsonify({
        'categoria': categoria,
        'resposta_sugerida': resposta_sugerida,
        'nome_detectado': nome_remetente or "Nenhum nome detectado"
    })

# --- Ponto de Entrada da Aplicação ---

if __name__ == '__main__':
    # Roda o servidor de desenvolvimento do Flask
    # O debug=True é ótimo para desenvolver, pois o servidor reinicia a cada alteração no código.
    app.run(debug=True)