####################################
#### LABO 3 ########################
##### CALCULATEUR IMC ##############
####################################
#### Jim Ocket #####################
####################################

def isfloat(value):
	''' Fonction de vérification:
est-ce que la valeur en paramètre est un float ou non.
source: stackoverflow
'''
	try:
		float(value)
		return True
	except:
		return False



def validation_donnees(infos_personnes):
	''' Fonction qui traite les différentes
informations enregistrées grâce à la fonction
'reception_donnees',  fais le calcul de l'IMC et
retourne un dictionnaire.
'''
	dico_personne = {} # creation d'un dictionnaire
	for info in infos_personnes: # itération sur les différentes listes reçues
		# le calcul est poids au kg / taille en m2 donc on met la taille en mètres
		taille_m = float(info[1]) / 100
		taille_carre = taille_m**2 # on fait le carré de la taille en mètre
		# on fait le calcul en tant que tel et on arrondi à 2 chiffres derrière la virgule
		imc = round((info[2] / taille_carre),2)
		dico_personne[info[0]] = imc # on enrigstre le nom comme clé et l'imc comme valeur

	return dico_personne



def affichage_donnees(categ_poids, liste_poids):
	''' Fonction d'affichage par catégorie.
On reçoit une liste en paramètre, on récupère ses valeurs
et on les affiche.
'''
	print(categ_poids)
	for i in liste_poids:
		print(i[0].capitalize(), "- IMC de:", i[1])
	print("-------------------------------------")
	print("\n")



def utilisation_donnees(dico):
	''' Creation de listes pour chaque catégorie.
La fonction reçoit un dictionnaire et sépare les valeurs
par rapport aux différentes catégories.
Elle affiche enfin les catégories qui contiennent une valeur
ainsi que les différentes valeurs.
'''
	# creation des listes en fonction des catégories
	obese_morbide = []
	obese_severe = []
	obese_modere = []
	surpoids = []
	corpulence_normale = []
	maigreur = []
	famine = []
	categories_imc = ["+ de 40: obésité morbide ou massive",
		"35 à 40: obésité sévère","30 à 35: obésité modérée",
		"25 à 30: surpoids","18.5 à 25: corpulence normale","- de 16.5: famine"]

	# récupération des clés et des valeurs du dictionnaire
	# et insertion des celles-ci dans les listes correspondantes
	for cle,valeur in dico.items():
		if valeur > 40:
			obese_morbide.append([cle, valeur])
		elif valeur > 35 and valeur <= 40:
			obese_severe.append([cle, valeur])
		elif valeur > 30 and valeur <= 35:
			obese_modere.append([cle, valeur])
		elif valeur > 25 and valeur <= 30:
			surpoids.append([cle, valeur])
		elif valeur > 18.5 and valeur <= 25:
			corpulence_normale.append([cle, valeur])
		elif valeur >= 16.5 and valeur <= 18.5:
			maigreur.append([cle, valeur])
		elif valeur < 16.5:
			famine.append([cle, valeur])
		else:
			print("c'est une grossière erreur !")



	# categories
	print("-------------------------------------")
	print("-------------------------------------")
	if obese_morbide:
		affichage_donnees(categories_imc[0], obese_morbide)
	if obese_severe:
		affichage_donnees(categories_imc[1], obese_severe)
	if obese_modere:
		affichage_donnees(categories_imc[2], obese_modere)
	if surpoids:
		affichage_donnees(categories_imc[3], surpoids)
	if corpulence_normale:
		affichage_donnees(categories_imc[4], corpulence_normale)
	if maigreur:
		affichage_donnees(categories_imc[5], maigreur)
	if famine:
		affichage_donnees(categories_imc[6], famine)



def reception_donnees():
	''' Fonction demandant à l'utilisateur de rentrer
différentes données (nom, taille, poids, sexe)
afin de les enregistrer dans une liste et de
renvoyer cette liste. Celle-ci est récupérée par
le programme principal (dans la fonction 'main')
'''
	first_list = [] # creation d'une liste dans laquelle on enrgistre les donnees
	nom_pers = input("Entrer le nom: ")
	if nom_pers.isdigit():
		nom_pers = input("Entrer le nom: ")
	if nom_pers == '': # verification que l'input ne soit pas vide.
		return '' # si il est vide on renvoie une chaine de caractères vide et on arrête la fonction
	first_list.append(nom_pers) # on ajoute le nom dans la liste

	taille_pers = "0"
	# vérification que la taille soit plausible (pas un string, pas un float et entre 30 et 280)
	while taille_pers == "0" or not taille_pers.isdigit() or (taille_pers.isdigit()
	                                                          and (int(taille_pers) < 30 or int(taille_pers) > 280)):
		taille_pers = input("Entrer la taille en cm: ")
	first_list.append(int(taille_pers)) # on ajoute la taille dans la liste


	poids_pers = "0"
	# vérification que le poids soit plausible. On le met en float car certaines personnes
	# pourraient mettre un poids précis
	while poids_pers == "0" or not isfloat(poids_pers) or (isfloat(poids_pers)
	                                                       and (float(poids_pers) < 20 or float(poids_pers) > 1000)):
		poids_pers = input("Entrer le poids en kilo: ")
	first_list.append(float(poids_pers)) # on ajoute le poids à la liste


	sexe_pers = str(input("Entrer le sexe (M)âle, (F)emelle: "))
	# vérification que ce soit bien un homme ou une femme et pas autre chose
	while sexe_pers.lower() != 'f' and sexe_pers.lower() != 'm':
		sexe_pers = str(input("Entrer le sexe (M)âle, (F)emelle: "))
	first_list.append(sexe_pers) # on ajoute le sexe à la liste

	return first_list # la fonction retourne la liste



def main():
	''' Fonction principale.
On boucle tant que l'input n'est pas vide.
Tant que ça boucle, on reçoit les données de la fonction
'reception_donnees' et on les ajoute à une liste.
Lorsque la boucle est finie, on envoie cette liste dans la fonction
'validation_donnees', elle même paramètre de la fonction 'utilisation_donnees'.
'''
	end_game = 'o'
	test_list = []
	print("-------------------")
	print("| CALCULATEUR IMC |")
	print("-------------------\n")
	while end_game != '': # boucle tant que input n'est pas vide
		end_game = reception_donnees() # si vide, retourne vide, sinon retourne liste de données
		if end_game != '': # si pas vide on ajoute les données à la liste
			test_list.append(end_game)
			print("\n ################ \n")
	if test_list: # si la liste n'est pas vide, on travaille dessus, sinon on arrête le programme
		utilisation_donnees(validation_donnees(test_list))

	print("--------------------")
	print("| FIN DU PROGRAMME |")
	print("--------------------")


if __name__ == "__main__":
	main()