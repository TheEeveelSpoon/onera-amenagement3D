import pygame
from pygame.locals import *
from random import *
from OpenGL.GL import *
from OpenGL.GLU import *

ANGLE_ROT = 20
NB_CUBES = 2
NUM_GENERE = 0
NO_CUBE = 0
ALEAT = [[(random(),random(),random()) for _ in range(NB_CUBES*3*4*6)] for _ in range(NB_CUBES)]

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))
surfaces = ((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6))

def Cube(verticies=verticies):
    global NO_CUBE
    glBegin(GL_QUADS)
    for surface in surfaces:
        #x = 0
        NUM_GENERE = 0
        for vertex in surface:
            #x+=1
            #glColor3fv(colors[randint(0,len(colors)-1)]) # Cube épileptique !
            #glColor3fv((random(),random(),random()))
            #print(ALEAT)
            print(NO_CUBE,NUM_GENERE)
            glColor3fv(ALEAT[NO_CUBE][NUM_GENERE])
            NUM_GENERE+=1
            glVertex3fv(verticies[vertex])
    glEnd()
    NO_CUBE+=1
    print(NO_CUBE,"END FUNCTION CUBE")

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0,0, -10)

    glRotatef(25, 2, 1, 0)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP4:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_KP6:
                    glTranslatef(0.5,0,0)
                if event.key == pygame.K_KP8:
                    glTranslatef(0,1,0)
                if event.key == pygame.K_KP2:
                    glTranslatef(0,-1,0)
                    
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
        Cube()
        #Cube([list(map(lambda x:x/2,e)) for e in verticies])
        pygame.display.flip()
        #pygame.time.wait(0)

main()
