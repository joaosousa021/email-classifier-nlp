# download_models.py
from transformers import pipeline

print("Iniciando pré-download do modelo de classificação...")
pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)
print("Modelo de classificação baixado.")

print("Iniciando pré-download do modelo NER...")
pipeline(
    "ner",
    model="dslim/bert-base-NER"
)
print("Modelo NER baixado.")

print("Todos os modelos foram baixados e cacheados com sucesso.")