# coding=utf-8
# ----Fonctions----
# noinspection PyBroadException


def isfloat(value):
    # Verification du type de la valeur
    # source: stackoverflow
    try:
        float(value)
        return True
    except:
        return False


def calculIMC(height, weight):
    height = float(height)
    weight = float(weight)
    if height > 3:
        height_m = height / 100
    else:
        height_m = height
    imc = weight / height_m ** 2
    return imc


def entree():
    taille = input("Taille? cm ")
    while not taille.isdigit() or (taille.isdigit()) and (int(taille) < 100 or int(taille) > 300):
        taille = input("Veuillez entrer une taille en centimetre ")
    poids = input("Poids? kg ")
    while not isfloat(poids) or (isfloat(poids)) and (float(poids) < 30 or float(poids) > 500):
        poids = input("Veuillez rentrer un poids en kilo ")
    sexe = input("Sexe? H/F/NB ").upper()
    while sexe not in {"H", "F", "NB"}:
        sexe = input("Veuillez rentrer un sexe (Homme/Femme/Non-Binaire) ").upper()
    return calculIMC(taille, poids)


def affichage(tab):
    cat = [["Obésité morbide (ou massive)", 40], ["Obesité sévère", 35], ["Obésité modérée", 30], ["Surpoids", 25],
           ["Corpulence normale", 18.5], ["Maigreur", 16.5], ["Famine", 4.7]]
    print("\nAffichage des données\n")
    for i in range(len(cat)):
        for j in range(len(tab) - 1):
            if tab[j][1] > cat[i][1]:
                print(cat[i][0], i)
                print("\t", tab[j][0], j)
                tab.pop(j)
                print(tab, "tab")


def main():
    # Fonction principale.
    name = "bonjour"
    tab = []
    while name != "":
        name = input("Nom? ")
        if name != "":
            per = [name, entree()]
            tab.append(per)
    affichage(tab)


if __name__ == "__main__":
    main()
