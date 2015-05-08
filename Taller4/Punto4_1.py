from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import * 
import random

r=0
g=1
b=0

transCounter = 0
def main():
	global window
	
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)
	
	window = glutCreateWindow('Taller 4-4.1')

	glutDisplayFunc(mostrarEscena)
	glutIdleFunc(mostrarEscena)
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mouseClicked)
	InitGL(500,500)
	glutMainLoop()
	glGetFloatv(GL_MODELVIEW_MATRIX)
	
def InitGL(Width, Height):
	glClearColor(0.529, 0.529, 0.529,0.529)
	glMatrixMode(GL_PROJECTION)
	
def mostrarEscena():
	glClear(GL_COLOR_BUFFER_BIT)
	
	#EJERCICIO 4.1 , PRIMER EJERCICIO RECTA 
	glBegin(GL_LINES)
	glColor3f(r,g,b)
	p1=[-0.8,-0.71]
	p2=[0.9,0.48]
	vertices = punto_medio(p1,p2,False)
	for v in vertices:
		v
	glEnd()
	
	#EJERCICIO 4.1 , SEGUNDO EJERCICIO PUNTOS
	glBegin(GL_LINES)
	glColor3f(r,g,b)
	p3=[-0.6,-0.75]
	p4=[0.8,0.69]
	vertices = punto_medio(p3,p4,False)
	for v in vertices:
		v
	glEnd()
	
	glutSwapBuffers()

def punto_medio(pto1, pto2,print_line):
	vertices = []
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
	if print_line:
		print 'Dibuja: (' + str(x) + ',' + str(y) + ')'
	vertices.append(glVertex2f(x,y))
	while x < x1:
		if d <= 0:
			d+=incrE
			x+=1
		else:
			d+=increNE
			x+=1
			y+=1
		if print_line:
			print 'Dibuja: (' + str(x) + ',' + str(y) + ')'
		vertices.append(glVertex2f(x,y))
	return vertices
	
def keyPressed(*args):
	key = args[0]
	#print glGetFloatv(GL_PROJECTION_MATRIX)
	#Un punto es un arreglo bidimensional donde la posicion 0 es X y la posicion q es Y
	if key == 'p':
		p1 = [-4,-6]
		p2 = [9,6]
		print 'ALGORIMO PUNTO MEDIO PARA: ('  + str(p1[0]) + ',' + str(p1[1]) + ') hasta (' + str(p2[0]) + ',' + str(p2[1]) + ')'
		punto_medio(p1,p2,True)
	if key == 'P':
		p1 = [-9,2]
		p2 = [8,6]
		print 'ALGORIMO PUNTO MEDIO PARA: ('  + str(p1[0]) + ',' + str(p1[1]) + ') hasta (' + str(p2[0]) + ',' + str(p2[1]) + ')'
		punto_medio(p1,p2,True)

def mouseClicked(*args):
	key = args[0];
	global r
	global g
	global b
	if key == GLUT_LEFT_BUTTON:
		r= random.random()
		g= random.random()
		b= random.random()
		mostrarEscena()
main()

