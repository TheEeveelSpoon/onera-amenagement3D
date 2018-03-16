#python3 V4\ readFromFicRedWarning.py < repartitionLigne.txt 

import pygame
from pygame.locals import *
from random import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pprint import pprint

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

def collisions(cube) :
    for c in cubes :
        if collision(c,cube) :
            return True
    return False

def enDehorsDuContainer(verticies) :
    #print("Attention !")
    ret = False
    for coin in verticies :
        #print(coin, ":",coin[0],">",cx," et ", coin[0],"<",-cx," et ", coin[1],">",cy," et ", coin[1],"<",-cy," et ", coin[2],">",cz," et ", coin[2],"<",-cz)
        ret = ret or (coin[0]>cx or coin[0]<-cx or coin[1]>cy or coin[1]<-cy or coin[2]>cz or coin[2]<-cz)
    return ret

cx,cy,cz = [int(e) for e in input().split(" ")]
container = ((cx,-cy,-cz),(cx,cy,-cz),(-cx,cy,-cz),(-cx,-cy,-cz),(cx,-cy,cz),(cx,cy,cz),(-cx,-cy,cz),(-cx,cy,cz))

ANGLE_ROT = 1
AVANCE = 0.1
NB_CUBES = int(input())
NUM_GENERE = 0
AL = [(random()/2,random(),random()) for _ in range(NB_CUBES*2)]
#print(ALEAT)

cubes = []
poids = []
for i in range(NB_CUBES) :
    poids.append(int(input()))
    vertice=[]
    for _ in range(8) :
        vertice.append([float(e) for e in input().split(",")])
    cubes.append(vertice)

edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))
surfaces = ((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6))

def Cube(verticies, color):
    glBegin(GL_QUADS)
    for surface in surfaces:
        #x = 0
        NUM_GENERE = 0
        for vertex in surface:
            #x+=1
            #glColor3fv(colors[randint(0,len(colors)-1)]) # Cube épileptique !
            #glColor3fv((random(),random(),random()))
            glColor3fv(color)#ALEAT[NUM_GENERE])#4f(color[0],color[1],color[2],0.9)#
            NUM_GENERE+=1
            glVertex3fv(verticies[vertex])
    glEnd()

def Cube_lines(verticies):
    #glPointSize(15)#largeur des lignes mais fonctionne pas
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)#DEPTH BUFFER
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    #glTranslatef(-150,-150, -150)
    glTranslatef(0,0, -10)
    glRotatef(25, 2, 1, 0)

    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            glRotatef(ANGLE_ROT, 0, AVANCE, 0)
        if keys[pygame.K_KP4]:
            glTranslatef(-AVANCE,0,0)
        if keys[pygame.K_KP6]:
            glTranslatef(AVANCE,0,0)
        if keys[pygame.K_KP8]:
            glTranslatef(0,AVANCE,0)
        if keys[pygame.K_KP2]:
            glTranslatef(0,-AVANCE,0)
        if keys[pygame.K_KP1]:
            glTranslatef(0,0,-AVANCE)
        if keys[pygame.K_KP3]:
            glTranslatef(0,0,AVANCE)
        
        if keys[pygame.K_PAGEDOWN]:
            glRotatef(ANGLE_ROT, 1, 0, 0)
        if keys[pygame.K_PAGEUP]:
            glRotatef(ANGLE_ROT, -1, 0, 0)
        if keys[pygame.K_UP]:
            glRotatef(ANGLE_ROT, 0, 1, 0)
        if keys[pygame.K_DOWN]:
            glRotatef(ANGLE_ROT, 0, -1, 0)
                    
        if keys[pygame.K_RIGHT]:
            glRotatef(ANGLE_ROT, 0, 0, 1)
        if keys[pygame.K_LEFT]:
            glRotatef(ANGLE_ROT, 0, 0, -1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #Cube()
        #pprint(cubes)
        for i in range(NB_CUBES) :
            if not enDehorsDuContainer(cubes[i]) :#and not collisions(cubes[i]) :
                #print("Cube :", cubes[i])
                Cube(cubes[i],color=(0,1-poids[i]/100,1))#AL[i])
            else :
                #print("Je suis hors la loi")
                Cube(cubes[i],color=(1,1-poids[i]/100,0))
        
        # COULEUR DES ARETES
        #Cube([(0,0,0)]*8, color = (0,1,1))
        glColor3fv((1,1,1))
        
        
        glClear(GL_DEPTH_BUFFER_BIT)
        Cube_lines(container)
        glColor3fv((0.5,0,1))
        #Cube_lines([[e[0]+0.005,e[1]+0.005,e[2]+0.005] for e in container])
        #Cube_lines([[e[0]+0.01,e[1]+0.01,e[2]+0.01] for e in container])
        for i in range(NB_CUBES) :
        	Cube_lines(cubes[i])
        
        pygame.display.flip()
        #pygame.time.wait(0)

main()
