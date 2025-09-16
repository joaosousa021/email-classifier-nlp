import re


INTENCOES_PRODUTIVO = {
    'agendamento': [r'reunião', r'reuniao', r'call', r'conversar', r'agenda', r'horário', r'horario'],
    'demonstracao': [r'demonstração', r'demonstracao', r'demo', r'apresentação', r'apresentacao'],
    'proposta': [r'proposta', r'orçamento', r'orcamento', r'valores', r'preços', r'precos'],
    'informacao': [r'dúvida', r'duvida', r'informações', r'informacoes', r'detalhes', r'entender melhor']
}

def gerar_resposta(categoria, nome_remetente=None):
    """
    Gera uma resposta sugerida com base na categoria do e-mail.
    Para e-mails 'produtivo', a resposta é adaptada ao conteúdo.
    """
    nome = f"{nome_remetente}, " if nome_remetente else ""

    if categoria == 'improdutivo':
        return "Nenhuma ação é necessária para este e-mail. Sugestão: Arquivar."
    
    if categoria == 'produtivo':
        return f"Olá {nome}agradecemos o seu contato. Nossa equipe já está analisando sua mensagem e retornará em breve."

    return "Resposta padrão para categoria desconhecida."


def gerar_resposta_produtiva(texto_email, nome_remetente=None):
    """
    Analisa o conteúdo de um e-mail produtivo e gera uma resposta contextual.
    """
    texto_email_lower = texto_email.lower()
    nome = f"{nome_remetente}, " if nome_remetente else ""

    for intencao, palavras_chave in INTENCOES_PRODUTIVO.items():
        for palavra in palavras_chave:
            if re.search(r'\b' + palavra + r'\b', texto_email_lower):
                return criar_resposta_por_intencao(intencao, nome)


    return (f"Olá {nome}agradecemos o seu interesse! Sua mensagem foi recebida e nossa equipe "
            "comercial entrará em contato o mais breve possível para dar andamento.")


def criar_resposta_por_intencao(intencao, nome):
    """
    Retorna o texto da resposta com base na intenção detectada.
    """
    respostas = {
        'agendamento': (f"Olá {nome}recebemos sua solicitação de agendamento! Para agilizar, "
                        "nossa equipe entrará em contato em breve com algumas opções de horário. "
                        "Obrigado pelo interesse!"),

        'demonstracao': (f"Olá {nome}que ótimo saber do seu interesse em uma demonstração! "
                         "Já encaminhamos sua solicitação para nossos especialistas, que entrarão em contato "
                         "para marcar a melhor data e horário para você e sua equipe."),

        'proposta': (f"Olá {nome}recebemos seu pedido de proposta comercial. Nossa equipe já está trabalhando "
                     "para preparar um documento alinhado às suas necessidades e o enviará em breve."),
        
        'informacao': (f"Olá {nome}obrigado pela sua pergunta. Sua dúvida foi encaminhada para a equipe técnica/comercial "
                       "responsável, que retornará o mais rápido possível com todos os esclarecimentos.")
    }
    return respostas[intencao]
