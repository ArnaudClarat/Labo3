# ----Fonctions----
def isfloat(value):
	# Verification du type de la valeur
	# source: stackoverflow
	try:
		float(value)
		return True
	except:
		return False

def calculIMC(height, weight):
	imc = float(weight)/((float(height)/100) ** 2)
	return imc

def entree():
	per = []
	taille = input("Taille? cm ")
	while (not taille.isdigit() or (taille.isdigit()) and (int(taille) < 100 or int(taille) > 300)):
		taille = ("Veuillez entrer une taille en centimetre ")
	poids = input("Poids? kg ")
	while (not isfloat(poids) or (isfloat(poids)) and (float(poids) < 30 or float(poids) > 500)):
		poids = input("Veuillez rentrer un poids en kilo ")
	sexe = input("Sexe? H/F/NB ").upper
	while sexe not in {"H", "F", "NB"}:
		sexe = input("Veuillez rentrer un sexe (Homme/Femme/Non-Binaire) ")
	per.append(name)
	per.append(calculIMC(taille, poids))
	return per



def main():
	# Fonction principale.
	name = "jceirb"
	tab = []
	while name != "":
		name = input("Nom? ")
		if name != "":
			entree()




if __name__ == "__main__":
	main()
