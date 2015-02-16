#Practica 1 Daniel Correa 1225622
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import random
c1=0.2
c2=0.2
c3=0.3
rotate_y=0
rotate_x=0
def main():

    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500,500)
    window = glutCreateWindow("Test")

    
    InitGL(500,500)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    glutDisplayFunc(mostrarEscena)
    glutIdleFunc(mostrarEscena)
    glutKeyboardFunc(keyPressed)
    glutMouseFunc(mouseClicked)
    glMatrixMode(GL_PROJECTION)
    
    glMatrixMode(GL_MODELVIEW)
    glutMainLoop()
    
def InitGL(Width, Height):
    glClearColor(0.53,0.53,0.53,0.0)
    glMatrixMode(GL_PROJECTION)

def mostrarEscena():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glRotatef(30,0,0,1) #Rotacion 2.6

    color = [c1,c2,c3]
    glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
    glutSolidSphere(0.5,20,20)
    glFlush()
    glutSwapBuffers()
    
def keyPressed(*args):
    key = args[0];
    global c1
    global c2
    global c3
    if key=="r" or key=="R":
        
        c1=1.0
        c2=0.0
        c3=0.0
        mostrarEscena()
    if key=="g" or key=="G":
        
        c1=0.0
        c2=1.0
        c3=0.0
        mostrarEscena()
    if key=="b" or key=="B":
        
        c1=0.0
        c2=0.0
        c3=1.0
        mostrarEscena()
    
    
def mouseClicked(*args):
    key = args[0];
    global c1
    global c2
    global c3
    if key == GLUT_LEFT_BUTTON:
        c1= random.random()
        c2= random.random()
        c3= random.random()
        mostrarEscena()



if __name__ == '__main__': main()