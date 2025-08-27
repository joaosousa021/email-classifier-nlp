# Classificador Inteligente de E-mails - Desafio AutoU 🚀

![Status](https://img.shields.io/badge/status-finalizado-brightgreen)
![Tecnologia](https://img.shields.io/badge/tecnologia-Python%20%7C%20Flask%20%7C%20IA-blue)

Uma aplicação web full-stack que utiliza Inteligência Artificial para automatizar a triagem e resposta de e-mails, transformando um processo manual e demorado em uma tarefa inteligente e instantânea.

---

## 🎯 Links Essenciais

- **Acesse a Aplicação ao Vivo:** `[COLOQUE AQUI O LINK DA SUA APLICAÇÃO NA NUVEM]`
- **Assista ao Vídeo de Demonstração (5 min):** `[COLOQUE AQUI O LINK DO SEU VÍDEO NO YOUTUBE]`

---

## 💡 O Problema a Ser Resolvido

Empresas do setor financeiro lidam com um volume altíssimo de e-mails diariamente. Uma equipe gasta horas preciosas lendo, priorizando e respondendo a cada mensagem, muitas das quais são informativas e não exigem ação. Esse processo manual é lento, caro e propenso a erros.

## ✨ A Solução

Este projeto ataca o problema com uma abordagem de duas camadas de Inteligência Artificial:

1.  **Classificação de Intenção:** A aplicação lê o conteúdo do e-mail (texto ou PDF) e o classifica automaticamente como **Produtivo** (exige uma ação, como um pedido de suporte) ou **Improdutivo** (um agradecimento ou aviso).
2.  **Extração de Dados:** Para e-mails que exigem uma resposta, a IA identifica e extrai o **nome do remetente** na assinatura para personalizar a comunicação.
3.  **Resposta Inteligente:** Com base na classificação e nos dados extraídos, o sistema sugere uma resposta profissional, consistente e personalizada, pronta para ser enviada.

O resultado é uma ferramenta que economiza tempo, padroniza a comunicação e permite que a equipe foque em tarefas de maior valor.

---

## 👨‍💻 Minha Jornada e Decisões Técnicas

Construir uma solução de IA robusta envolve mais do que apenas escolher um modelo. A jornada neste projeto foi um ciclo de testes, aprendizados e decisões de engenharia para garantir a melhor performance.

#### Desafio 1: A Inconsistência do Classificador `Zero-Shot`
Inicialmente, optei por um modelo de classificação *zero-shot* pela sua flexibilidade. No entanto, em testes com e-mails mais complexos e ambíguos, sua performance oscilava muito. Um e-mail informativo com palavras como "próximos passos" era classificado como produtivo, enquanto um pedido real com um tom muito sutil era ignorado.

**➡️ Decisão:** Troquei o modelo generalista por um **especialista em análise de sentimento** (`nlptown/bert-base-multilingual-uncased-sentiment`). A abordagem mudou de "adivinhar a categoria" para "analisar a intenção (positiva, negativa, neutra)". Combinei isso com uma lógica de palavras-chave para os casos neutros, o que tornou a classificação muito mais estável e confiável.

#### Desafio 2: A imprevisibilidade da Geração de Texto
Para as respostas, testei modelos generativos como `T5` e `mT0`. Os resultados eram imprevisíveis: às vezes a IA "alucinava" e inventava informações, outras vezes entrava em loops de repetição.

**➡️ Decisão:** Para uma aplicação de negócios, a consistência é rei. Abandonei a geração de texto via IA e implementei um sistema de **templates inteligentes em Python**. A IA faz a parte difícil (classificar e extrair o nome), e o sistema garante que a resposta seja sempre 100% correta, profissional e segura, eliminando qualquer risco de erro.

#### Desafio 3: A Personalização da Saudação
Para ir além, adicionei a extração de nomes com um modelo **NER (Named Entity Recognition)**. O desafio era capturar apenas o nome, ignorando cargos ("Gerente de Vendas") e outras informações.

**➡️ Decisão:** Implementei uma função com uma lógica de "limpeza" em duas etapas: ela primeiro remove saudações comuns ("Atenciosamente,") e depois aplica uma "blacklist" de cargos sobre o nome extraído pela IA. O resultado é uma saudação limpa e natural.

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia | Descrição |
| :--- | :--- | :--- |
| **Backend** | Python & Flask | Servidor web leve e API para processar as requisições. |
| **IA (Classificação)** | Transformers (Hugging Face) | `nlptown/bert-base-multilingual-uncased-sentiment` para análise de intenção. |
| **IA (Extração)** | Transformers (Hugging Face) | `dslim/bert-base-NER` para reconhecimento de nomes de pessoas. |
| **Frontend** | HTML, CSS, JavaScript | Interface de usuário limpa e interativa, sem a necessidade de frameworks. |
| **Utilitários** | PyPDF2 | Extração de texto de documentos PDF enviados pelos usuários. |

---

## 🚀 Como Executar Localmente

Siga os passos abaixo para ter o projeto rodando em sua máquina.

**Pré-requisitos:**
-   Python 3.8+
-   Git

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
4.  **Execute a aplicação:**
    ```bash
    python -m flask run
    ```
5.  Pronto! Acesse **`http://1227.0.0.1:5000`** no seu navegador.
