# ----Fonctions----
def calculIMC(height, weight) :
	imc = float(weight)/((float(height)/100) ** 2)
	return imc


def main() :
	global name
	tab = []
	while name != "" :
		name = input("Nom? ")
		if name != "" :
			per = []
			height = input("Taille? cm ")
			while float(height) > 250 or float(height) < 100 :
				height = input("Veuillez ressaisir la taille en cm. ")
			weight = input("Poids? kg ")
			while float(weight) > 300 or float(weight) < 30 :
				weight = input("Veuillez ressaisir le poids en kilo. ")
			sexe = input("Sexe? H/F ")
			while sexe not in {"H", "F"} :
				sexe = input("Veuillez ressaisir le sexe H/F ")
			imc = calculIMC(height, weight)
			per.append(name)
			per.append(imc)
			tab.append(per)
	print(tab)
	cat = {}
	cat["Obésité morbide (ou massive)"] = 40
	cat["Obesité sévère"] = 35
	cat["Obésité modérée"] = 30
	cat["Surpoids"] = 25
	cat["Corpulence normale"] = 18.5
	cat["Maigreur"] = 16.5
	cat["famine"] = 4.7
	for i in cat:
		for j in range(len(tab)):
			print(cat[i], "cat")
			if tab[j][1] > cat[i]:
				print(tab[j][0], tab[j][1])
				tab.pop(j)
				print(tab)
				print("------------")





# ---Variables Globales---
name = "jceirb"

# ----Programme---
if __name__ == "__main__" :
	main()
