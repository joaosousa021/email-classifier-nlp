# Classificador Inteligente de E-mails com IA 🚀

![Status](https://img.shields.io/badge/status-finalizado-brightgreen)
![Tecnologia](https://img.shields.io/badge/tecnologia-Python%20%7C%20Flask%20%7C%20Scikit--learn-blue)
![Accuracy](https://img.shields.io/badge/acurácia-98%25-informational)

Uma aplicação web full-stack que utiliza Machine Learning para automatizar a triagem e resposta de e-mails, transformando um processo manual e demorado em uma tarefa inteligente e instantânea com 98% de acurácia.

---

## 🎯 Links Essenciais

- **Acesse a Aplicação ao Vivo:** `[https://huggingface.co/spaces/joaosousa021/email-classifier-nlp]`

---

## 💡 O Problema a Ser Resolvido

Empresas lidam com um volume altíssimo de e-mails diariamente. Uma equipe gasta horas preciosas lendo e priorizando cada mensagem. O desafio é criar uma ferramenta que possa distinguir rapidamente e-mails que exigem ação imediata (produtivos) daqueles que são apenas informativos ou dispensáveis (improdutivos).

## ✨ A Solução

Este projeto ataca o problema com um pipeline de Machine Learning e processamento de linguagem natural:

1.  **Classificação de Intenção:** A aplicação lê o conteúdo do e-mail (texto ou PDF) e o classifica com **98% de acurácia** como **Produtivo** (exige uma ação) ou **Improdutivo** (um aviso, agradecimento ou recusa).
2.  **Resposta Inteligente e Contextual:** Para e-mails produtivos, o sistema vai além. Ele identifica a intenção principal (pedido de reunião, proposta, dúvida técnica) e sugere uma resposta profissional e adaptada ao contexto, pronta para ser enviada.

O resultado é uma ferramenta que economiza tempo, padroniza a comunicação e permite que a equipe foque em e-mails que realmente geram valor.

---

## 👨‍💻 Minha Jornada e Decisões Técnicas

Construir uma solução de IA robusta é um processo iterativo. A jornada neste projeto foi um ciclo de diagnóstico, estratégia e otimização para alcançar a máxima performance.

#### Desafio 1: A Baixa Confiabilidade de um Modelo Generalista

A primeira abordagem foi um modelo que tentava classificar e-mails em 5 categorias diferentes (`interessado`, `dúvida`, `não interessado`, etc.). Os testes mostraram que, com um dataset limitado, o modelo era inconsistente, com uma acurácia de apenas **40%**. Ele tinha grande dificuldade em diferenciar as nuances entre as categorias.

**➡️ Insight e Decisão:** A IA precisava de mais dados para aprender, mas o problema principal era a complexidade da tarefa. A decisão estratégica foi simplificar o problema. Em vez de 5 classes, o foco passou a ser resolver a questão de negócio mais importante: **"Este e-mail precisa de uma ação ou não?"**.

#### Desafio 2: Dados Desbalanceados e Treinamento

Ao focar em duas classes (`produtivo` e `improdutivo`), o próximo desafio era a qualidade dos dados. O dataset inicial era pequeno e desbalanceado, fazendo com que o modelo ficasse "viciado" em uma categoria e ignorasse as outras.

**➡️ Insight e Decisão:** A performance de um modelo é um reflexo direto da qualidade de seus dados. O trabalho foi focado em **aumentar e balancear o dataset**, garantindo que ambas as classes tivessem um número robusto e variado de exemplos (mais de 250 no total). O código de treinamento foi estruturado em um pipeline `Scikit-learn` com `TfidfVectorizer` e `LinearSVC`, permitindo um ciclo rápido de re-treinamento a cada melhoria nos dados.

#### O Resultado: Um Salto para 98% de Acurácia

Após o balanceamento dos dados e a simplificação estratégica do problema, o modelo foi treinado novamente. O resultado foi um salto de performance de 40% para **98% de acurácia**, com métricas de precisão e recall igualmente altas. Isso validou a abordagem e resultou em um classificador confiável e pronto para uso.

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia | Descrição |
| :--- | :--- | :--- |
| **Backend** | Python & Flask | Servidor web leve e API para processar as requisições. |
| **IA (Machine Learning)** | Scikit-learn & Pandas | Pipeline de classificação de texto treinado com `LinearSVC` para máxima performance. |
| **Frontend** | HTML, CSS, JavaScript | Interface de usuário limpa e interativa para uma ótima experiência. |
| **Utilitários** | Joblib, PyPDF2 | Serialização do modelo treinado e extração de texto de documentos PDF. |
| **Deploy** | Docker & Hugging Face Spaces | Conteinerização da aplicação para um deploy robusto e otimizado. |

---

## 🚀 Como Executar Localmente

Siga os passos abaixo para ter o projeto rodando em sua máquina.

**Pré-requisitos:**

- Python 3.8+
- Git

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/joaosousa021/email-classifier-nlp.git](https://github.com/joaosousa021/email-classifier-nlp.git)
    cd email-classifier-nlp
    ```
2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Cria o ambiente
    python -m venv venv

    # Ativa no Windows (PowerShell)
    .\venv\Scripts\activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Treine o modelo (necessário apenas na primeira vez):**
    ```bash
    python train_model.py
    ```
5.  **Execute a aplicação:**
    ```bash
    python app.py
    ```
6.  Pronto! Acesse **`http://12.0.0.1:5000`** no seu navegador.
