def entrer(i):
    nom = input("Entrez le nom du produit : ")
    pu = float(input("Entrez le prix du produit : "))
    quantite = int(input("Entrez la quantité du produit : "))
    return nom, pu, quantite

def pt_chaque_produit(pu, quantite):
    return pu * quantite


nombre_du_produit = int(input("Veuillez entrer le nombre des produits: "))

facture =""

for i in range(1, nombre_du_produit + 1):
    nom, pu, quantite = entrer(i)
    pt = pt_chaque_produit(pu, quantite)
    facture += f"produit: {nom}, Prix: {pu}, Quantité: {quantite}\n"

print("\n\n" + facture)