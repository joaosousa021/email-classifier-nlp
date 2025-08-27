# Classificador Inteligente de E-mails - Desafio AutoU 🚀

![Status](https://img-shields-io.translate.goog/badge/status-concluído-brightgreen?_x_tr_sl=pt&_x_tr_tl=en&_x_tr_hl=pt-BR&_x_tr_pto=wapp)

Uma aplicação web que usa Inteligência Artificial para classificar e-mails e sugerir respostas personalizadas, automatizando o fluxo de trabalho e liberando tempo para o que realmente importa.

## 🔗 Links

- **Acesse a aplicação aqui:** `[COLOQUE AQUI O LINK DA SUA APLICAÇÃO NA NUVEM]`
- **Assista ao vídeo de demonstração:** `[COLOQUE AQUI O LINK DO SEU VÍDEO NO YOUTUBE]`

## 👨‍💻 A Jornada do Desenvolvimento (E os Desafios no Caminho)

Construir este projeto foi uma jornada incrível de aprendizado e, como em todo projeto de IA, cheia de desafios interessantes. A ideia inicial era simples, mas garantir que a IA se comportasse de forma profissional e consistente exigiu várias iterações.

### O Primeiro Grande Desafio: A IA "Criativa Demais"

Meu plano inicial para as respostas era usar um modelo de linguagem generativo (como o `T5` e o `mT0`). A ideia era que a IA "escrevesse" uma resposta única para cada e-mail.

**O que aconteceu?** Caos criativo! 😂

- O modelo começou a "alucinar", inventando informações que não estavam no e-mail original (como o infame "tickle de ouro").
- Em outros testes, ele entrava em loops de repetição ou simplesmente copiava trechos do e-mail de entrada.

**A Solução:** Percebi que, para um ambiente de negócios, **confiabilidade é mais importante que criatividade.** Tomei a decisão de engenharia de pivotar a estratégia: usar a IA para a tarefa mais complexa (classificação) e usar templates robustos em Python para as respostas. Isso garante respostas 100% precisas, profissionais e alinhadas com o tom de voz da empresa.

### O Segundo Desafio: A Ambiguidade da Classificação

O classificador inicial, um modelo `zero-shot`, funcionava bem para casos óbvios, mas falhava em e-mails mais sutis, gerando um "pingue-pongue":

1.  Com `labels` mais genéricas, ele não conseguia identificar e-mails produtivos que usavam linguagem indireta.
2.  Com `labels` mais fortes e focadas em "ação", ele se tornava sensível demais e classificava e-mails informativos (FYI) como produtivos por causa de palavras-chave como "próximos passos".

**A Solução:** A abordagem `zero-shot` se mostrou inconsistente para os casos de borda. A solução definitiva foi trocar de ferramenta e adotar um **modelo especialista**, treinado especificamente para análise de sentimento (`nlptown/bert-base-multilingual-uncased-sentiment`). Combinado com uma lógica de palavras-chave para os casos neutros, ele se mostrou muito mais robusto e consistente para entender a real intenção do texto.

### O Toque Final: Personalização Inteligente

Para ir além do básico, decidi que a aplicação deveria personalizar a saudação. Isso me levou ao mundo do **NER (Named Entity Recognition)**. O desafio era extrair _apenas_ o nome, ignorando cargos e outras informações da assinatura. Após alguns testes, desenvolvi uma função que:

1.  Foca apenas nas últimas linhas do e-mail.
2.  Usa o modelo NER para encontrar entidades de "Pessoa".
3.  Aplica uma "blacklist" de cargos comuns para limpar o resultado, garantindo que a saudação seja sempre natural e profissional.

## 🛠️ Tecnologias Utilizadas

- **Backend:**
  - **Python 3.11+**
  - **Flask:** Para criar o servidor e a API.
- **Inteligência Artificial:**
  - **Hugging Face Transformers:** A biblioteca principal para acessar os modelos de IA.
  - **`nlptown/bert-base-multilingual-uncased-sentiment`:** Modelo especialista para a classificação de e-mails.
  - **`dslim/bert-base-NER`:** Modelo especialista para extração de nomes de pessoas.
- **Frontend:**
  - **HTML5, CSS3, JavaScript (puro)**
  - **Fetch API:** Para a comunicação assíncrona com o backend.
- **Utilitários:**
  - **PyPDF2:** Para a extração de texto de arquivos PDF.

## 🚀 Como Executar Localmente

Siga os passos abaixo para ter o projeto rodando em sua máquina.

**Pré-requisitos:**

- Python 3.8 ou superior
- Git

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd [NOME_DA_PASTA_DO_PROJETO]
    ```
2.  **Crie e ative um ambiente virtual:**

    ```bash
    # Cria o ambiente
    python -m venv venv

    # Ativa no Windows (PowerShell)
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências do projeto:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Execute a aplicação Flask:**
    ```bash
    python -m flask run
    ```
5.  Pronto! Agora é só acessar **`http://127.0.0.1:5000`** no seu navegador.
