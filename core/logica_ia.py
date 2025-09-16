import joblib
import re


try:
    modelo = joblib.load('modelo_email.joblib')
    print("Modelo de classificação de e-mail carregado com sucesso.")
except FileNotFoundError:
    print("Erro: Arquivo 'modelo_email.joblib' não encontrado. Treine o modelo primeiro executando train_model.py")
    modelo = None

def classificar_email(texto: str) -> str:
    """
    Usa o modelo de Machine Learning treinado para classificar o texto de um e-mail.
    """
    if modelo is None:
        return "erro_modelo_nao_carregado"

    
    predicao = modelo.predict([texto])

  
    return predicao[0]

def extrair_nome(texto: str) -> str:
    """
    Uma função simples para tentar extrair um nome do texto do e-mail.
    Pode ser melhorada no futuro.
    """
   
    padroes = [
        r"Atenciosamente,?\s*([A-Z][a-z]+(?:\s[A-Z][a-z]+)?)",
        r"Abraços,?\s*([A-Z][a-z]+(?:\s[A-Z][a-z]+)?)",
        r"Obrigado,?\s*([A-Z][a-z]+(?:\s[A-Z][a-z]+)?)"
    ]

    for padrao in padroes:
        match = re.search(padrao, texto, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    return None 