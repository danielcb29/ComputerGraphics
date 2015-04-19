from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import * 
import random

global r
r=0
global g
g=1
global b
b=0

transCounter = 0
def main():
	global window
	
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)
	
	window = glutCreateWindow('Prueba')
	
	glutDisplayFunc(mostrarEscena)
	glutIdleFunc(mostrarEscena)
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(clickPressed)
	InitGL(500,500)
	
	matriz = glGetFloatv(GL_PROJECTION_MATRIX)
	print matriz
	
	glutMainLoop()
	
	
def InitGL(Width, Height):
	glClearColor(0.529, 0.529, 0.529,0.529)
	
def mostrarEscena():
	glClear(GL_COLOR_BUFFER_BIT)
	
	glLoadIdentity()
	
	
	
	
	
	
	
	glBegin(GL_QUADS)
	
	
	
	glColor3f(r,g,b)
	glVertex2f( 15, 15)
	glVertex2f( 15, -15)
	glVertex2f( -15, -15)
	glVertex2f( -15, 15)
 
	glEnd()
	
	glViewport(150, 150, 200, 200)
	
	glMatrixMode(GL_PROJECTION)
	
	glutSwapBuffers()
	
def keyPressed(*args):
	key = args[0]
	print glGetFloatv(GL_PROJECTION_MATRIX)
		
def clickPressed(*args):
	button = args[0]
	global r
	global g
	global b
	if (button == GLUT_LEFT_BUTTON):
		r=random.random()
		g=random.random()
		b=random.random()
		mostrarEscena()
		

main()
