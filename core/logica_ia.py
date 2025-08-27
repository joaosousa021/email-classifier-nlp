import re
from transformers import pipeline


classifier = None
ner_pipeline = None

def _inicializar_modelos_se_necessario():
    global classifier, ner_pipeline

    if classifier is None:
        try:
            print("LAZY LOADING: Carregando modelo de classificação...")
            classifier = pipeline(
                "sentiment-analysis",
                model="nlptown/bert-base-multilingual-uncased-sentiment"
            )
            print("Modelo de classificação carregado.")
        except Exception as e:
            print(f"Erro fatal ao carregar o modelo de classificação: {e}")

    if ner_pipeline is None:
        try:
            print("LAZY LOADING: Carregando modelo NER...")
            ner_pipeline = pipeline(
                "ner",
                model="dslim/bert-base-NER"
            )
            print("Modelo NER carregado.")
        except Exception as e:
            print(f"Erro fatal ao carregar o modelo NER: {e}")


def classificar_email(texto):
    _inicializar_modelos_se_necessario()

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
    _inicializar_modelos_se_necessario()
    
    if not ner_pipeline:
        return None

    try:
        linhas = texto.strip().split('\n')
        linhas_finais = linhas[-4:]
        linhas_finais.reverse()

        blacklist_cargos = [
            'gerente', 'coordenador', 'coordenadora', 'diretor', 'diretora',
            'analista', 'presidente', 'ceo', 'cto', 'cfo', 'desenvolvedor',
            'desenvolvedora', 'de', 'engenheiro', 'engenheira', 'vendas',
            'marketing', 'suporte', 'rh', 'cio'
        ]

        for linha in linhas_finais:
            saudacoes = [
                "Atenciosamente,", "Atenciosamente", "Grato,", "Grato",
                "Obrigado,", "Obrigado", "Abraços,", "Abraços", "Att,"
            ]
            linha_limpa = linha
            for saudacao in saudacoes:
                linha_limpa = re.sub(
                    r'^\s*' + saudacao, '', linha_limpa, flags=re.IGNORECASE
                ).strip()

            if not linha_limpa:
                continue

            entidades = ner_pipeline(linha_limpa)
            nome_tokens = [
                token['word'] for token in entidades
                if token['entity'].startswith(('B-PER', 'I-PER'))
            ]

            if nome_tokens:
                nome_bruto = ""
                for token in nome_tokens:
                    nome_bruto += token.replace('##', '') if token.startswith('##') else f" {token}"
                nome_bruto = nome_bruto.strip()

                palavras_nome = nome_bruto.lower().split()
                if any(palavra in palavras_nome for palavra in blacklist_cargos):
                    continue
                
                if len(nome_bruto) > 2:
                    return nome_bruto
        return None
    except Exception as e:
        print(f"Erro ao extrair nome: {e}")
        return None