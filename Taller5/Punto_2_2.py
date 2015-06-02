from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import random


def main():
    global window
    global r, g, b
    r = 0
    g = 1
    b = 0
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)

    window = glutCreateWindow('Circulo')

    glutDisplayFunc(mostrarEscena)
    glutIdleFunc(mostrarEscena)
    glutKeyboardFunc(keyPressed)
    glutMouseFunc(mousePressed);
    InitGL(500, 500)
    glutMainLoop()


def InitGL(Width, Heigth):
    glClearColor(0.53, 0.53, 0.53, 0)
    glMatrixMode(GL_PROJECTION)


def mostrarEscena():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(r, g, b)
    circleSections = 100;
    sides = 32
    radius = 0.5
    for i in range(circleSections):
        cosine = radius * cos(i * 2 * pi / sides) + 0
        sine = radius * sin(i * 2 * pi / sides) + 0
        glVertex2f(cosine, sine)

    glEnd()

    glutSwapBuffers();


def keyPressed(*args):
    global r, g, b
    key = args[0];
    if (key == "r" or key == "R"):
        r = 1
        g = 0
        b = 0
        matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        print matrix
    elif (key == "g" or key == "G"):
        r = 0
        g = 1
        b = 0
        matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        print matrix
    elif (key == "b" or key == "B"):
        r = 0
        g = 0
        b = 1
        matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        print matrix

#Se escoge la variacion de tonalidad en verde
def mousePressed(button, status, x, y):
    global r, g, b
    if (button == GLUT_LEFT_BUTTON):

        k = g*0.5
        if(k<0):
            g = 0.1
        else:
            g = k
        matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        print matrix

    elif(button == GLUT_RIGHT_BUTTON):

        k = g*2
        if(k>1):
            g = 1
        else:
            g = k
        matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        print matrix

if __name__ == "__main__":
    main()