def ajouter_article(liste_courses, article, quantite):
    if article in liste_courses:
        print(f"L'article '{article}' est déjà dans la liste")
    else:
        liste_courses[article] = quantite
        print(f"L'article '{article}' a ete ajoute avec une quantite de {quantite}")
    return article, quantite


def supprimer_article(liste_courses, article):
    if article in liste_courses:
        del liste_courses[article]
        print(f"L'article '{article}' a ete supprime")


def afficher_liste(liste_courses):
    print("\n Liste de courses :")
    if not liste_courses:
        print("La liste est vide")
    else:
        for article, quantite in liste_courses.items():
            print(f"{article} : {quantite}")


def valider_liste(liste_courses):
    print("\n Liste de courses validée")
    return liste_courses


def quitter_programme():
    print("\n À bientôt !")
    exit()


def main():
    liste_courses = {}
    
    while True:
        print("\n Menu :")
        print("1. Ajouter un article")
        print("2. Supprimer un article")
        print("3. Afficher la liste")
        print("4. Valider la liste")
        print("5. Quitter le programme")

        choix = input("\nEntrez votre choix : ")

        match choix:
            case "1":
                article = input("\nEntrez le nom de l'article : ")
                quantite = int(input("Entrez la quantité : "))
                ajouter_article(liste_courses, article, quantite)

            case "2":
                article = input("\nEntrez le nom de l'article : ")
                supprimer_article(liste_courses, article)

            case "3":
                afficher_liste(liste_courses)

            case "4":
                valider_liste(liste_courses)

            case "5":
                quitter_programme()

            case _:
                print("\nchoix invalide!!\n")


main()
