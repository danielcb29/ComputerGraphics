# Practica 1 Daniel Correa 1225622
from OpenGL.GL import *
import OpenGL.GL as gl
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

r = 0.0
g = 0.0
b = 0.0


def main():
    global window

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(200, 200)

    window = glutCreateWindow('Test')

    global r
    global g
    global b

    r = 0.0
    g = 0.0
    b = 0.0

    glutDisplayFunc(mostrarEscena)
    glutIdleFunc(mostrarEscena)
    glutKeyboardFunc(keyPressed)
    glutMouseFunc(mouseClicked);
    InitGL(500, 500)
    glutMainLoop()
    matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    print matrix


def InitGL(Width, Height):
    glClearColor(0.53, 0.53, 0.53, 0.0)
    glMatrixMode(GL_PROJECTION)


def mostrarEscena():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_QUADS)
    glColor3f(r, g, b)
    glVertex2f(0.25, 0.25)
    glVertex2f(0.25, -0.25)
    glVertex2f(-0.25, -0.25)
    glVertex2f(-0.25, 0.25)
    glEnd()

    glutSwapBuffers();


def keyPressed(*args):
    key = args[0];
    global r
    global g
    global b
    #Color rojo
    if key == "1" :

        h = 0
        s = 1
        v = 1
        transformarHSVRGB(h, s ,v)

    #Colo amarillo
    elif key == "2":

        h = 60
        s = 1
        v = 1
        transformarHSVRGB(h, s ,v)

    #Color verde
    elif key == "3":
        h = 120
        s = 1
        v = 1
        transformarHSVRGB(h, s ,v)
    matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    print matrix


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
    matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    print matrix

def transformarHSVRGB(h, s, v):

    global r, g, b
    hi = math.floor(h/60)%6
    f = ((h/60)%6)-hi
    p = v*(1-s)
    q = v*(1-(f*s))
    t = v*(1-((1-f)*s))
    if (hi == 0):
        r = v
        g = t
        b = p
    elif(hi==1):
        r = q
        g = v
        b = p
    elif(hi==2):
        r = p
        g = v
        b = t
    elif(hi==3):
        r = p
        g = q
        b = v
    elif(hi==4):
        r = t
        g = p
        b = v
    elif(hi==5):
        r = v
        g = p
        b = q


if __name__ == "__main__":
    main()
