
def gerar_resposta(categoria, nome=None):
    saudacao = f"Prezado(a) {nome},\n\n" if nome else "Prezado(a),\n\n"

    if categoria == "Produtivo":
        return (
            saudacao +
            "Agradecemos o seu contato. Recebemos sua mensagem e daremos o devido seguimento à sua solicitação.\n\n"
            "Retornaremos em breve, se necessário.\n\n"
            "Atenciosamente,\n"
            "Equipe AutoU"
        )
    elif categoria == "Improdutivo":
        return (
            saudacao +
            "Agradecemos pela sua mensagem.\n\n"
            "Atenciosamente,\n"
            "Equipe AutoU"
        )
    else:
        return "Não foi possível determinar uma resposta para este e-mail."