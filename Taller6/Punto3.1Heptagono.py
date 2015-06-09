from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import * 
import random

global r
r=0
global g
g=0
global b
b=0
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
	glMatrixMode(GL_PROJECTION)
	
def mostrarEscena():
	glClear(GL_COLOR_BUFFER_BIT)
	glShadeModel(GL_SMOOTH)
	glBegin(GL_POLYGON)
	
	
	posx, posy = 0,0
	sides = 7
	radius = 0.5
	
	glColor3f(0, 0, 0)
	cosine=radius*cos(0*2*pi/sides)+posx
	sine=radius*sin(0*2*pi/sides)+posy
	glVertex2f(cosine,sine)
	
	glColor3f(1, 0, 0)
	cosine=radius*cos(1*2*pi/sides)+posx
	sine=radius*sin(1*2*pi/sides)+posy
	glVertex2f(cosine,sine)
	
	glColor3f(0, 0, 1)
	cosine=radius*cos(2*2*pi/sides)+posx
	sine=radius*sin(2*2*pi/sides)+posy
	glVertex2f(cosine,sine)
	
	glColor3f(0, 1, 0)
	cosine=radius*cos(3*2*pi/sides)+posx
	sine=radius*sin(3*2*pi/sides)+posy
	glVertex2f(cosine,sine)
	
	glColor3f(0, 1, 1)
	cosine=radius*cos(4*2*pi/sides)+posx
	sine=radius*sin(4*2*pi/sides)+posy
	glVertex2f(cosine,sine)
	
	glColor3f(1, 1, 0)
	cosine=radius*cos(5*2*pi/sides)+posx
	sine=radius*sin(5*2*pi/sides)+posy
	glVertex2f(cosine,sine)
	
	glColor3f(1, 1, 1)
	cosine=radius*cos(6*2*pi/sides)+posx
	sine=radius*sin(6*2*pi/sides)+posy
	glVertex2f(cosine,sine)
	
	glColor3f(1, 0, 1)
	cosine=radius*cos(7*2*pi/sides)+posx
	sine=radius*sin(7*2*pi/sides)+posy
	glVertex2f(cosine,sine)
	
	glEnd()
	
	glutSwapBuffers()
	
def keyPressed(*args):
	key = args[0]
	global r
	global g
	global b
	if(key=="1"):
		r=1
		g=0
		b=0
		mostrarEscena()
	elif(key=="2"):
		r=0
		g=1
		b=0
		mostrarEscena()
	elif(key=="3"):
		r=0
		g=0
		b=1
		mostrarEscena()
		
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
