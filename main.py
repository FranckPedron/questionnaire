def afficher_titre_question(question):
    print("Question:", question[0])


def afficher_propositions(question):
    propositions = question[1]
    for p in propositions:
        print(p)


def traiter_reponse(question):
    global score
    reponse = input("Votre réponse: ")
    if reponse == question[2]:
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")
        score -= 1


def poser_question(question):
    afficher_titre_question(question)
    afficher_propositions(question)
    traiter_reponse(question)


score = 0

question1 = ("Quelle est la capitale de la France", ("(a) Paris", "(b) Marseille", "(c) Lyon"), "a")

poser_question(question1)

print("Score final", score)
