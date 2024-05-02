def afficher_question(question):
    print("Question:", question)


def afficher_propositions(propositions):
    for p in propositions:
        print(p)


def traiter_reponse(bonne_reponse):
    global score
    reponse = input("Votre réponse: ")
    if reponse == bonne_reponse:
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")
        score -= 1


def poser_question(question, propositions, bonne_reponse):
    afficher_question(question)
    afficher_propositions(propositions)
    traiter_reponse(bonne_reponse)


score = 0
poser_question("Quelle est la capitale de la France", ["(a) Paris", "(b) Marseille", "(c) Lyon"], "a")
print("Score final", score)
