def transform(users):
    for user in users:
        score = user["score"]

        if score >= 700:
            user["message"] = "Seu perfil é VIP. Que tal desbloquear oportunidades exclusivas de rendimento hoje?"
        elif score >= 500:
            user["message"] = "Vamos fazer seu dinheiro trabalhar para você agora?"
        else:
            user["message"] = "Vamos organizar sua vida financeira e conquistar sua liberdade?"

    return users
