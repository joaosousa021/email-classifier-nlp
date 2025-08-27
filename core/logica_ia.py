
import re
from transformers import pipeline
import gc 

def classificar_email(texto):
   
    classifier = None 
    try:
        print("Carregando modelo de classificação para uso...")
        classifier = pipeline(
            "sentiment-analysis",
            model="nlptown/bert-base-multilingual-uncased-sentiment"
        )
        
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
    finally:
        del classifier
        gc.collect()
        print("Modelo de classificação liberado da memória.")


def extrair_nome(texto):
    ner_pipeline = None 
    try:
        print("Carregando modelo NER para uso...")
        ner_pipeline = pipeline(
            "ner",
            model="dslim/bert-base-NER"
        )
        
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
    finally:
        del ner_pipeline
        gc.collect()
        print("Modelo NER liberado da memória.")