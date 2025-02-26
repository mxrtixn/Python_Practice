# Définition d'une fonction qui permet de classer les étudiants selon leurs notes
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


# Spécifier le nombre d'étudiants
nombre_etudiants = int(input("Entrez le nombre d'étudiants : "))

# Création d'une liste pour stocker les informations des étudiants
etudiants = []

# La saisie des informations des étudiants
for i in range(nombre_etudiants):
    print(f"Étudiant {i + 1}:")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    note = float(input("Note : "))

    # Ajouter l'étudiant avec son nom, prénom et sa note
    etudiants.append([nom, prenom, note, classification(note)])

# Tri des étudiants par note (Tri par sélection)
n = len(etudiants)
for i in range(n):
    max_index = i
    for j in range(i + 1, n):
        if etudiants[j][2] > etudiants[max_index][2]:  # Comparaison des notes
            max_index = j
    # Échange des éléments
    etudiants[i], etudiants[max_index] = etudiants[max_index], etudiants[i]

# Affichage des résultats
print("\nListe des étudiants classés par note:")
for etudiant in etudiants:
    print(f"{etudiant[0]} {etudiant[1]} - Note: {etudiant[2]} - Classification: {etudiant[3]}")
