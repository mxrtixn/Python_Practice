# Définition d'une fonctionqui permet de classer les étudiants selon leurs notes
def classification(note):
    if note >= 16:
        return "Très Bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez Bien"
    elif note >= 10:
        return "Passable"
    else:
        return "Insuffisant"


# Specifier le nombre d'étudiants
nombre_etudiants = int(input("Entrez le nombre d'étudiants : "))

# Creation d'une liste pour stocker les informations des étudiants
etudiants = []

# La saisie des informations des étudiants
for i in range(nombre_etudiants):
    print(f"Étudiant {i + 1}:")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    note = float(input("Note : "))

    # Ajouter l'étudiant avec son nom, prénom et sa note
    etudiants.append({
        "Nom": nom,
        "Prénom": prenom,
        "Note": note,
        "Classification": classification(note)
    })

# Le classemnt des étudiants par leur note en utilisant le tri de la liste
etudiants_triees = sorted(etudiants, key=lambda x: x["Note"], reverse=True)

# Affichage des résultats
print("\nListe des étudiants classés par note:")
for etudiant in etudiants_triees:
    print(
        f"{etudiant['Nom']} {etudiant['Prénom']} - Note: {etudiant['Note']} - Classification: {etudiant['Classification']}")
