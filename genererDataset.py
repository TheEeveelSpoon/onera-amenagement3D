from random import random

NB_BOX = 25
RAPPORT = 10

"""
# Sous Linux avec python3 genererDataset.py > fichier_conteneur_généré.txt

#TAILLE DU CONTENEUR PRINCIPAL
print("100 100 100")
#print(str(int(random()*100)+1)+" "+str(int(random()*100)+1)+" "+str(int(random()*100)+1))

#Pour itérer en fonction du nombre de boîtes
print(str(NB_BOX))

#Pour générer les tailles des boîtes
for i in range(NB_BOX) :
	print(str(int(random()*100/NB_BOX)+1)+" "+str(int(random()*100/NB_BOX)+1)+" "+str(int(random()*100/NB_BOX)+1))
"""

# Sous windows avec enregistrement automatique dans le fichier indiqué ligne suivante :
fichier = open("genere100.txt", "w")

#TAILLE DU CONTENEUR PRINCIPAL
fichier.write("100 100 100\n")
#print(str(int(random()*100)+1)+" "+str(int(random()*100)+1)+" "+str(int(random()*100)+1))

#Pour itérer en fonction du nombre de boîtes
fichier.write(str(NB_BOX)+"\n")

#Pour générer les tailles des boîtes
for i in range(NB_BOX) :
	fichier.write(str(int(random()*100/RAPPORT)+1)+" "+str(int(random()*100/RAPPORT)+1)+" "+str(int(random()*100/RAPPORT)+1)+"\n")

fichier.close()



# CONTAINER TAILLE 1


# Sous windows avec enregistrement automatique dans le fichier indiqué ligne suivante :
fichier = open("genere1.txt", "w")

#TAILLE DU CONTENEUR PRINCIPAL
fichier.write("1 1 1\n")
#print(str(int(random()*100)+1)+" "+str(int(random()*100)+1)+" "+str(int(random()*100)+1))

#Pour itérer en fonction du nombre de boîtes
fichier.write(str(NB_BOX)+"\n")

boxes = []

#Pour générer les tailles des boîtes
for i in range(NB_BOX) :
	x = round(int((random()*100/RAPPORT)+1)/10,2)
	y = round(int((random()*100/RAPPORT)+1)/10,2)
	z = round(int((random()*100/RAPPORT)+1)/10,2)
	p = round(int((random()*100)+1),2)#poids
	boxes.append((x,y,z,p))
	fichier.write(str(x)+" "+str(y)+" "+str(z)+" "+str(p)+"\n")

fichier.close()


print(boxes)


# Répartition en ligne

fichier = open("repartitionLigne.txt", "w")

#TAILLE DU CONTENEUR PRINCIPAL
fichier.write("1 1 1\n")
#print(str(int(random()*100)+1)+" "+str(int(random()*100)+1)+" "+str(int(random()*100)+1))

#Pour itérer en fonction du nombre de boîtes
fichier.write(str(NB_BOX)+"\n")

posx, posy, posz = (-1,-1,-1)
for (x,y,z,p) in boxes :
	fichier.write(str(p)+"\n")
	vertice = ((posx+x,posy,posz), (posx+x,posy+y,posz), (posx,posy+y,posz), (posx, posy, posz), (posx+x,posy,posz+z), (posx+x,posy+y,posz+z), (posx,posy,posz+z), (posx,posy+y, posz+z))
	for c in vertice :
		fichier.write(str(round(c[0],2))+","+str(round(c[1],2))+","+str(round(c[2],2))+"\n")
	posx+=x
	#posy+=y
	#posz+=z

fichier.close()




