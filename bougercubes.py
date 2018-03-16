import pygame
from pygame.locals import *
from random import *
from OpenGL.GL import *
from OpenGL.GLU import *


cx,cy,cz = [int(e) for e in input().split(" ")]
container = ((cx,-cy,-cz),(cx,cy,-cz),(-cx,cy,-cz),(-cx,-cy,-cz),(cx,-cy,cz),(cx,cy,cz),(-cx,-cy,cz),(-cx,cy,cz))

ANGLE_ROT = 45/2
NB_CUBES = int(input())
NUM_GENERE = 0
ALEAT = [(random(),random(),random()) for _ in range(NB_CUBES*3*4*6)]

cubes = []
for i in range(NB_CUBES) :
	vertice=[]
	for _ in range(8) :
		vertice.append([float(e) for e in input().split(",")])
	cubes.append(vertice)

edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))
surfaces = ((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6))

def Cube(verticies):
    glBegin(GL_QUADS)
    for surface in surfaces:
        #x = 0
        NUM_GENERE = 0
        for vertex in surface:
            #x+=1
            #glColor3fv(colors[randint(0,len(colors)-1)]) # Cube épileptique !
            #glColor3fv((random(),random(),random()))
            glColor3fv(ALEAT[NUM_GENERE])
            NUM_GENERE+=1
            glVertex3fv(verticies[vertex])
    glEnd()

def Cube_lines(verticies):
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP4:
                    glTranslatef(-1,0,0)
                if event.key == pygame.K_KP6:
                    glTranslatef(1,0,0)
                if event.key == pygame.K_KP8:
                    glTranslatef(0,1,0)
                if event.key == pygame.K_KP2:
                    glTranslatef(0,-1,0)
                if event.key == pygame.K_KP1:
                    glTranslatef(0,0,-1)
                if event.key == pygame.K_KP3:
                    glTranslatef(0,0,1)
                    
                if event.key == pygame.K_PAGEDOWN:
                    glRotatef(ANGLE_ROT, 1, 0, 0)
                if event.key == pygame.K_PAGEUP:
                    glRotatef(ANGLE_ROT, -1, 0, 0)
                if event.key == pygame.K_UP:
                    glRotatef(ANGLE_ROT, 0, 1, 0)
                if event.key == pygame.K_DOWN:
                    glRotatef(ANGLE_ROT, 0, -1, 0)
                    
                if event.key == pygame.K_RIGHT:
                    glRotatef(ANGLE_ROT, 0, 0, 1)
                if event.key == pygame.K_LEFT:
                    glRotatef(ANGLE_ROT, 0, 0, -1)

        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #Cube()
        Cube([list(map(lambda x:x,e)) for e in cubes[0] ])
        Cube([list(map(lambda x:x/2,e)) for e in cubes[1]])
        
        
        glClear(GL_DEPTH_BUFFER_BIT)
        
        Cube_lines([list(map(lambda x:x,e)) for e in container])
        Cube_lines([list(map(lambda x:x/2,e)) for e in cubes[0]])
        
        pygame.display.flip()
        #pygame.time.wait(0)

main()
