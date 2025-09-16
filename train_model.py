import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib 

print("Iniciando o treinamento do modelo...")


df = pd.read_csv('emails.csv')


if df.empty:
    print("Erro: O arquivo emails.csv está vazio ou não foi encontrado.")
else:
    print(f"Dataset carregado com {len(df)} exemplos.")
    X = df['texto']
    y = df['categoria']


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LinearSVC())
    ])

    print("Treinando o modelo com os dados...")
    pipeline.fit(X_train, y_train)

    print("\nAvaliação do modelo no conjunto de teste:")
    y_pred = pipeline.predict(X_test)
    print(classification_report(y_test, y_pred))

    joblib.dump(pipeline, 'modelo_email.joblib')
    print("\nModelo treinado e salvo com sucesso como 'modelo_email.joblib'!")