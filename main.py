def afficher_titre_question(question):
    print("Question:", question[0])


def afficher_propositions(question):
    propositions = question[1]
    for i in range(len(propositions)):
        print(i+1, "-", propositions[i])


def traiter_reponse(question):
    reponse_correcte = False
    choix = question[1]
    reponse_choisie = demander_reponse_numerique(1, len(question[1]))
    if choix[reponse_choisie].lower() == question[2].lower():
        print("Bonne réponse")
        reponse_correcte = True
    else:
        print("Mauvaise réponse")

    return reponse_correcte


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
    return traiter_reponse(question)


def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    afficher_score(score, questionnaire)


def afficher_score(s, q):
    print()
    print("Score final", s, "/", len(q))


questionnaire = (
    ("Quelle est la capitale de la France ?", ("Paris", "Marseille", "Lyon"), "Paris"),
    ("Quelle est la capitale de l'Italie ?", ("Turin", "Naple", "Rome", "Milan"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("liège", "Bruxelle", "Bruges", "Ostende", "Anvers"), "Bruxelle")
)

lancer_questionnaire(questionnaire)
