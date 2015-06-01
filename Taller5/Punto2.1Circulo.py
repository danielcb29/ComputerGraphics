from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import * 
import random

#se escoge el negro
r=1
g=0
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
	
	glBegin(GL_POLYGON)
	glColor3f(r,g,b)
	
	posx, posy = 0,0
	sides = 100
	radius = 0.5
	
	for i in range(100):
		cosine=radius*cos(i*2*pi/sides)+posx
		sine=radius*sin(i*2*pi/sides)+posy
		glVertex2f(cosine,sine)
	glEnd()
	
	
	
	glutSwapBuffers()
	
def keyPressed(*args):
	key = args[0]
	global r
	global g
	global b
	if(key=="s" or key=="S"):
		r=1-r
		g=1-g
		b=1-b
		mostrarEscena()
	elif(key=="a" or key=="A"):
		r=random.random()
		g=random.random()
		b=random.random()
		mostrarEscena()
	elif(key=="b" or key=="B"):
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
