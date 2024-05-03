def afficher_titre_question(question):
    print("Question:", question[0])


def afficher_propositions(question):
    propositions = question[1]
    for i in range(len(propositions)):
        print(i+1, "-", propositions[i])


def traiter_reponse(question):
    global score
    choix = question[1]
    reponse_choisie = demander_reponse_numerique(1, len(question[1]))
    if choix[reponse_choisie].lower() == question[2].lower():
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")
        score -= 1


def demander_reponse_numerique(min, max):
    reponse = input(f"Votre réponse (entre {min} et {max}) : ")
    try:
        reponse_int = int(reponse)
        if min <= reponse_int <= max:
            return reponse_int-1
        print(f"ERREUR: Vous devez entrer un nombre entre {min} et {max}")
    except:
        print("ERREUR: Vous devez entrer uniquement des chiffres")
    return demander_reponse_numerique(min, max)


def poser_question(question):
    afficher_titre_question(question)
    afficher_propositions(question)
    traiter_reponse(question)
    print()


def afficher_score(s):
    print("Score final", s)


score = 0

question1 = ("Quelle est la capitale de la France ?", ("Paris", "Marseille", "Lyon"), "Paris")
question2 = ("Quelle est la capitale de l'Italie ?", ("Turin", "Naple", "Rome", "Milan"), "Rome")

poser_question(question1)
poser_question(question2)

afficher_score(score)
