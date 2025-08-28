
import re
from transformers import pipeline


try:
    print("Carregando modelo de classificação do cache...")
    classifier = pipeline(
        "sentiment-analysis",
        model="nlptown/bert-base-multilingual-uncased-sentiment"
    )
    print("Carregando modelo NER do cache...")
    ner_pipeline = pipeline(
        "ner",
        model="dslim/bert-base-NER"
    )
    print("Modelos carregados com sucesso.")
except Exception as e:
    print(f"Erro fatal ao carregar os modelos: {e}")
    classifier = None
    ner_pipeline = None


def classificar_email(texto):
    if not classifier:
        return "Erro: Modelo de classificação não carregado."
    try:
        resultado = classifier(texto)
        rating = resultado[0]['label']

        if rating in ["1 star", "2 stars"]:
            return "Produtivo"
        elif rating == "5 stars":
            return "Improdutivo"
        else:
            palavras_de_acao = [
                'solicitar', 'enviar', 'confirmar', 'ajudar', 'precisamos',
                'dúvida', 'problema', 'verificar', 'revisar', 'aprovação'
            ]
            if any(palavra in texto.lower() for palavra in palavras_de_acao):
                return "Produtivo"
            else:
                return "Improdutivo"
    except Exception as e:
        print(f"Erro na classificação: {e}")
        return "Erro na classificação"


def extrair_nome(texto):
    if not ner_pipeline:
        return "Erro: Modelo NER não carregado."
    try:
        
        linhas = texto.strip().split('\n')
        linhas_finais = linhas[-4:]
        linhas_finais.reverse()
        blacklist_cargos = [
            'gerente', 'coordenador', 'coordenadora', 'diretor', 'diretora', 'analista', 
            'presidente', 'ceo', 'cto', 'cfo', 'desenvolvedor', 'desenvolvedora', 'de',
            'engenheiro', 'engenheira', 'vendas', 'marketing', 'suporte', 'rh', 'cio'
        ]
        for linha in linhas_finais:
            saudacoes = ["Atenciosamente,", "Atenciosamente", "Grato,", "Grato", "Obrigado,", "Obrigado", "Abraços,", "Abraços", "Att,"]
            linha_limpa = linha
            for saudacao in saudacoes:
                linha_limpa = re.sub(r'^\s*' + saudacao, '', linha_limpa, flags=re.IGNORECASE).strip()
            if not linha_limpa:
                continue
            entidades = ner_pipeline(linha_limpa)
            nome_tokens = []
            tem_pessoa = False
            for token in entidades:
                if token['entity'].startswith('B-PER') or token['entity'].startswith('I-PER'):
                    nome_tokens.append(token['word'])
                    tem_pessoa = True
            if tem_pessoa:
                nome_bruto = ""
                for token in nome_tokens:
                    if token.startswith('##'):
                        nome_bruto += token.replace('##', '')
                    else:
                        nome_bruto += " " + token
                nome_bruto = nome_bruto.strip()
                contem_cargo = False
                palavras_nome = nome_bruto.lower().split()
                for palavra in palavras_nome:
                    if palavra in blacklist_cargos:
                        contem_cargo = True
                        break
                if not contem_cargo and len(nome_bruto) > 2:
                    return nome_bruto
        return None
    except Exception as e:
        print(f"Erro ao extrair nome: {e}")
        return None