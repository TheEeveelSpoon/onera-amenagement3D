#python3 hape3D_V0.py < genere1.txt

# TO DO :
# fonction tasser()
# fonction collision(v1,v2)
# vérifier heuristique : dans le fichier il parle de trier les objets en fonction du volume au départ il me semble, mais j'ai fait en fonction du poids car d'après ce que j'ai compris, cet algo place les objets dans l'ordre qui vient le plus bas possible. Donc les objets les plus lours seront ainsi automatiquement placés le plus bas. Enfin ça, c'est ce que j'espère.

cx, cy, cz = list(map(int, input().split())) #dimensions du container
nb_boxes = int(input())

container = [] #Contiendra des tuples ((a,b,c,d,e,f,g,h),p) des boîtes placées
leftovers = [] #Contiendra la liste des cubes n'ayant pu être placés

boites = [list(map(float,input().split())) for _ in range(nb_boxes)]
# On récupère les boîtes sous format (x,y,z,p)
boites.sort(key = lambda x : x[3]) # On trie en fonction du poids
# Comme ça les boîtes les plus lourdes sont placées en premier vers le bas

#Packing point number : quadrillage du cube pour placement des boîtes
#Avec des trous, on tasse après
PPN = [(0.1*i,0.1*j,0.1*k) for i in range(-cx*10,cx*10) for j in range(-cy*10,cy*10) for k in range(-cz*10,cz*10)]

def collision(cube1,cube2) :
    # Les objets v1 et v2 entrent-ils en collision ?
    cube1cote1 = abs(cube1[3][0] - cube1[0][0])
    cube1cote2 = abs(cube1[4][2] - cube1[0][2])
    cube1hauteur = abs(cube1[1][1] - cube1[0][1])

    cube2cote1 = abs(cube2[3][0] - cube2[0][0])
    cube2cote2 = abs(cube2[4][2] - cube2[0][2])
    cube2hauteur = abs(cube2[1][1] - cube2[0][1])

    a=0	

    for i in range(0,len(cube1)) :
    # trop à droite # trop à gauche # trop en bas # trop en haut # trop derrière # trop devant
        if((cube2[i][0] >= cube1[i][0] + cube1cote1)	
        or (cube1[i][0] >= cube2[i][0] + cube2cote1)		
        or (cube2[i][1] >= cube1[i][1] + cube1hauteur) 		
        or (cube1[i][1] >= cube2[i][1] + cube2hauteur)  	    
        or (cube2[i][2] >= cube1[i][2] + cube1cote2)   		
        or (cube1[i][2] >= cube2[i][2] + cube2cote2)) :
            a = a+1

    # il n'y a pas collision
    if(a==len(cube1)) :
        varReturn = False
        #print(varReturn," : pas de collision")

    # il y a collision
    else :
        varReturn = True
        #print(varReturn," : collision")
    return varReturn
    
def enDehorsDuContainer(verticies) :
    #print("Attention !")
    ret = False
    for coin in verticies :
        #print(coin, ":",coin[0],">",cx," et ", coin[0],"<",-cx," et ", coin[1],">",cy," et ", coin[1],"<",-cy," et ", coin[2],">",cz," et ", coin[2],"<",-cz)
        ret = ret or (coin[0]>cx or coin[0]<-cx or coin[1]>cy or coin[1]<-cy or coin[2]>cz or coin[2]<-cz)
    return ret
def placer(boite, point) :
    # On place la boite (x,y,z,p) au point posx, posy, posz dans le container
    posx, posy, posz = point
    x,y,z,p = boite
    container.append((coins(posx,posy,posz,x,y,z),p))

def canPlace(boite, details=False) :
    # Est-ce qu'on peut placer la boîte de coords (a,b,c,d,e,f,g) dans le container ?
    collide = [1 for v in container if collision(v[0],boite)]
    if details :
        print("Boîte en dehors du container ?",enDehorsDuContainer(boite))
        print("Boite en collision ?",bool(collide))
    return (not enDehorsDuContainer(boite)) and (not collide)

def tasser() :
    # Slide objets to remove spaces between boxes
    pasEncoreFait = True

def coins(posx,posy,posz,x,y,z) :
    # Retourne les coords (a,b,c,d,e,f,g,h) de l'objet de taille x,y,z
    # placé au point posx, posy, posz
    return ((posx+x,posy,posz), (posx+x,posy+y,posz), (posx,posy+y,posz), (posx, posy, posz), (posx+x,posy,posz+z), (posx+x,posy+y,posz+z), (posx,posy,posz+z), (posx,posy+y, posz+z))

def orientations(boite, place) :
    # Donne les vertices de boîte, coin placé à place, 
    # pour les 6 orientations possibles de la boîte
    posx, posy, posz = place
    x,y,z,p = boite
    pos1 = coins(posx,posy,posz,x,y,z)
    pos2 = coins(posx,posy,posz,x,z,y)
    pos3 = coins(posx,posy,posz,y,x,z)
    pos4 = coins(posx,posy,posz,y,z,x)
    pos5 = coins(posx,posy,posz,z,x,y)
    pos6 = coins(posx,posy,posz,z,y,x)
    return (pos1, pos2, pos3, pos4, pos5, pos6)

# Pour toutes les boîtes :
for i in range(len(boites)) :
    #print()
    print("BOX",i)
    # z_min = le plus bas qu'on puisse placer cette boîte 
    # dans l'état actuel du container
    z_min = 100000
    # changed : est-ce qu'on a trouvé un vrai emplacement pour la boîte ?
    changed = False
    # Pour tous les points du quadrillage :
    for p in PPN :
        #Pour toutes les orientations possibles de la boîte :
        for coordBoite in orientations(boites[i],p) :
            z = p[2]
            # Si on peut placer la boîte (canPlace) plus bas qu'avant (z<z_min) :
            if z < z_min and canPlace(coordBoite) :
                # On met à jour z_min et le point optimal,
                # et on dit qu'on a bien trouvé une vraie place
                z_min = z
                point_opt = p
                changed = True
                v_opt = coordBoite
                #print(v_opt, canPlace(v_opt))
    #Si on a bien trouvé une vraie place :
    if changed :
        # On met la boîte courrante au point optimal qu'on a trouvé avant
        #placer(boites[i], point_opt)
        container.append((v_opt, boites[i][3]))
        #print(v_opt,canPlace(v_opt, True))
        # Et on tasse, parce qu'avec la méthode du quadrillage,
        # On peut se retrouver avec des trous !
        tasser()
    else :
        # Sinon, on dit qu'on a pas pu placer la boîte
        leftovers.append(boites[i])

# Résultat :
print("Sur", nb_boxes, "boîtes données :")
print(len(container),"placées")
print(len(leftovers),"non placées")

# Rappel : container contient des tuples ((a,b,c,d,e,f,g,h),p) des boîtes placées


# Maintenant, on enregistre le résultat dans le fichier pour la modélisation :
fichier = open("hape3D_V0.txt", "w")

fichier.write("1 1 1\n") # TAILLE DU CONTENEUR PRINCIPAL

fichier.write(str(len(container))+"\n") # nb de boîtes

# Pour les boîtes, représentées par les tuples ((a,b,c,d,e,f,g,h),p), du container :
for vertices, p in container : 
    fichier.write(str(int(p))+"\n") # On écrit le poids
    for c in vertices : # Pour chaque coin de la boîte, on écrit ses coords x,y,z dans le fichier
        fichier.write(str(round(c[0],2))+","+str(round(c[1],2))+","+str(round(c[2],2))+"\n")


fichier.close()
posx, posy, posz = -1, -1, -1
x,y,z  = 1,1,1
container = ((posx+x,posy,posz), (posx+x,posy+y,posz), (posx,posy+y,posz), (posx, posy, posz), (posx+x,posy,posz+z), (posx+x,posy+y,posz+z), (posx,posy,posz+z), (posx,posy+y, posz+z))

cube1 = ((posx+x,posy,posz), (posx+x,posy+y,posz), (posx,posy+y,posz), (posx, posy, posz), (posx+x,posy,posz+z), (posx+x,posy+y,posz+z), (posx,posy,posz+z), (posx,posy+y, posz+z))

print(collision(container, cube1)) #True
