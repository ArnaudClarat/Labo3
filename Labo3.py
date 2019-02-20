# ----Fonctions----
def entree() :
	global name
	while name != "" :
		name = input("Nom? ")
		if name != "" :
			# per = []
			height = input("Taille? cm ")
			while int(height) > 250 or int(height) < 100 :
				height = input("Veuillez ressaisir la taille en cm. ")
			weight = input("Poids? kg ")
			while int(weight) > 300 or int(weight) < 30 :
				weight = input("Veuillez ressaisir le poids en kilo. ")
			sexe = input("Sexe? H/F ")
			while sexe not in {"H", "F"} :
				sexe = input("Veuillez ressaisir le sexe H/F ")
			imc = calculIMC()
			print(imc)


def calculIMC() :
	print("On est dans calculcIMC()")
	# imc = int(weight)/((int(height)/100) ^ 2) TODO Check pourquoi ca marche pas avec un float
	return 2


def main() :
	entree()


# ---Variables Globales---
name = "jceirb"

# ----Programme---
if __name__ == "__main__" :
	main()
