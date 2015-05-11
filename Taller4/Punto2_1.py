__author__ = 'alvarom'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import random

global m, b;


def main():
    global window

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(200, 200)

    window = glutCreateWindow('Taller 4-4.1')

    glutDisplayFunc(mostrarEscena)
    glutIdleFunc(mostrarEscena)
    glutKeyboardFunc(keyPressed)
    glutMouseFunc(mouseClicked)
    InitGL(500, 500)
    glutMainLoop()
    glGetFloatv(GL_MODELVIEW_MATRIX)


def InitGL(Width, Height):
    glClearColor(0.529, 0.529, 0.529, 0.529)
    glMatrixMode(GL_PROJECTION)


def mostrarEscena():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_POINTS)
    glColor3f(r, g, b)
    for
        glVertex3f()


    glutSwapBuffers()



def calcularRecta(p1, p2):
    global m, b
    m = (p2[1]- p1[1])/(p2[0]-p1[0])
    if(m<-1|m>1):
        m = 1/m

    b = p2[1]-(m*p2[0])

def keyPressed(*args):
    key = args[0]
    global m, b
    # print glGetFloatv(GL_PROJECTION_MATRIX)
    # Un punto es un arreglo bidimensional donde la posicion 0 es X y la posicion q es Y
    if key == '1':
        p1 = [-1, 3]
        p2 = [4, 4]
        calcularRecta(p1, p2)
        print 'ALGORIMO DE FUERZA BRUTA PARA: (' + str(p1[0]) + ',' + str(p1[1]) + ') hasta (' + str(p2[0]) + ',' + str(
            p2[1]) + ')'
        mostrarEscena()
    if key == 'P':
        p1 = [-3, 6]
        p2 = [6, 6]
        calcularRecta(p1, p2)
        print 'ALGORIMO DE FUERZA BRUTA PARA: (' + str(p1[0]) + ',' + str(p1[1]) + ') hasta (' + str(p2[0]) + ',' + str(
            p2[1]) + ')'
        mostrarEscena()


def mouseClicked(*args):
    key = args[0];
    global r
    global g
    global b
    if key == GLUT_LEFT_BUTTON:
        r = random.random()
        g = random.random()
        b = random.random()
        mostrarEscena()


main()

