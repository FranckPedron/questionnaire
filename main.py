class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def fromData(data):
        quest = Question(data[0], data[1], data[2])
        return quest

    def afficher_titre_question(self):
        print("Question:", self.titre)

    def afficher_propositions(self):
        propositions = self.choix
        for i in range(len(propositions)):
            print(i+1, "-", propositions[i])

    def traiter_reponse(self):
        reponse_correcte = False
        # choix = self.choix
        reponse_choisie = Question.demander_reponse_numerique(1, len(self.choix))
        if self.choix[reponse_choisie].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            reponse_correcte = True
        else:
            print("Mauvaise réponse")

        return reponse_correcte

    def demander_reponse_numerique(mini, maxi):
        reponse = input(f"Votre réponse (entre {mini} et {maxi}) : ")
        try:
            reponse_int = int(reponse)
            if mini <= reponse_int <= maxi:
                return reponse_int-1
            print(f"ERREUR: Vous devez entrer un nombre entre {mini} et {maxi}")
        except:
            print("ERREUR: Vous devez entrer uniquement des chiffres")
        return demander_reponse_numerique(mini, maxi)

    def poser_question(self):
        self.afficher_titre_question()
        self.afficher_propositions()
        return self.traiter_reponse()


class Questionnaire:
    SCORE = 0

    def __init__(self, questions):
        self.questions = questions

    def lancer_questionnaire(self):
        for question in self.questions:
            if question.poser_question():
                Questionnaire.SCORE += 1
        self.afficher_score()

    def afficher_score(self):
        print()
        print("Score final", self.SCORE, "/", len(self.questions))


Questionnaire((
    Question("Quelle est la capitale de la France ?", ("Paris", "Marseille", "Lyon"), "Paris"),
    Question("Quelle est la capitale de l'Italie ?", ("Turin", "Naple", "Rome", "Milan"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ("liège", "Bruxelle", "Bruges", "Ostende", "Anvers"), "Bruxelle")
)).lancer_questionnaire()
