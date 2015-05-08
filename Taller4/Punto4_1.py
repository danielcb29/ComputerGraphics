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
	
	window = glutCreateWindow('Taller 4')
	
	glutDisplayFunc(mostrarEscena)
	glutIdleFunc(mostrarEscena)
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(clickPressed)
	InitGL(500,500)
	
	matriz = glGetFloatv(GL_PROJECTION_MATRIX)
	
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

def punto_medio(pto1, pto2):
	x0 = pto1[0]
	y0 = pto1[1]
	x1 = pto2[0]
	y1 = pto2[1] 
	dy = y1 - y0
	dx = x1 - x0
	d = (2*dy) - dx
	incrE = 2*dy
	increNE = 2 * (dy-dx)
	x = x0
	y = y0
	print 'Dibuja: (' + str(x) + ',' + str(y) + ')'
	while x < x1:
		if d <= 0:
			d+=incrE
			x+=1
		else:
			d+=increNE
			x+=1
			y+=1
		print 'Dibuja: (' + str(x) + ',' + str(y) + ')'
	
def keyPressed(*args):
	key = args[0]
	#print glGetFloatv(GL_PROJECTION_MATRIX)
	#Un punto es un arreglo bidimensional donde la posicion 0 es X y la posicion q es Y
	if key == 'p':
		p1 = [-4,-6]
		p2 = [9,6]
		print 'ALGORIMO PUNTO MEDIO PARA: ('  + str(p1[0]) + ',' + str(p1[1]) + ') hasta (' + str(p2[0]) + ',' + str(p2[1]) + ')'
		punto_medio(p1,p2)
	if key == 'P':
		p1 = [-9,2]
		p2 = [8,6]
		print 'ALGORIMO PUNTO MEDIO PARA: ('  + str(p1[0]) + ',' + str(p1[1]) + ') hasta (' + str(p2[0]) + ',' + str(p2[1]) + ')'
		punto_medio(p1,p2)


		
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

