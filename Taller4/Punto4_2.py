
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

	glBegin(GL_POLYGON)
	#vertices = punto_medio(0.3,False)
	#for v in vertices:
	#	v

	glVertex2f(0,0.3)
	glVertex2f(0,-0.3)
	glVertex2f(0.3,0)
	glVertex2f(-0.3,0)

	glVertex2f(0.1,0.3)
	glVertex2f(0.1,-0.3)
	glVertex2f(-0.1,0.3)
	glVertex2f(-0.1,-0.3)
	glVertex2f(0.3,0.1)
	glVertex2f(0.3,-0.1)
	glVertex2f(-0.3,0.1)
	glVertex2f(-0.3,-0.1)
	
	glVertex2f(0.2,0.2)
	glVertex2f(0.2,-0.2)
	glVertex2f(-0.2,0.2)
	glVertex2f(-0.2,-0.2)
	glColor3f(r,g,b)

	glEnd()

	'''#EJERCICIO 4.1 , PRIMER EJERCICIO RECTA 
	glBegin(GL_QUADS)
	glColor3f(r,g,b)
	glVertex2f(0.25,0.25)
	glVertex2f(0.25,-0.25)
	glVertex2f(-0.25,-0.25)
	glVertex2f(-0.25,0.25)
	glEnd()
	

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
	glEnd()'''
	
	glutSwapBuffers()

def punto_medio(r,print_pto):
	vertices = []
	x = 0
	y = r
	d = 1-r
	if print_pto:
		print 'Dibuja: (' + str(x) + ',' + str(y) + ')'
	vertices.append([x,y])
	while y>x:
		if d<0:
			d+= (2*x)+3
			x+=1
		else:
			d+=(2*(x-y)) + 5
			x+=1
			y-=1
		if print_pto:
			print 'Dibuja: (' + str(x) + ',' + str(y) + ')'
		vertices.append([x,y])
	vertices = calcular_simetricos(vertices,print_pto)
	return vertices

def search_vert(v,verts):
	r = False
	for in_v in verts:
		if in_v==v:
			r = True
			break
	return r

def calcular_simetricos(vert,print_pto):
	new_vert = vert
	for ve in vert:
		temp_vert = []
		temp_vert.append([ve[0],(ve[1]*-1)])
		temp_vert.append([(ve[0]*-1),ve[1]])
		temp_vert.append([(ve[0]*-1),(ve[1]*-1)])
		temp_vert.append([ve[1],ve[0]])
		temp_vert.append([ve[1],(ve[0]*-1)])
		temp_vert.append([(ve[1]*-1),ve[0]])
		temp_vert.append([(ve[1]*-1),(ve[0]*-1)])
		for v in temp_vert:
			if search_vert(v,new_vert) != True:
				new_vert.append(v)
				if print_pto:
					print 'Dibuja: (' + str(v[0]) + ',' + str(v[1]) + ')'
	return_vert = []
	for n in new_vert:
		return_vert.append(glVertex2f(n[0],n[1]))
	return return_vert
	
def keyPressed(*args):
	key = args[0]
	if key == 'p':
		r=3
		print 'ALGORIMO PUNTO MEDIO PARA: r='+str(r)
		punto_medio(r,True)
	if key == 'P':
		r=7
		print 'ALGORIMO PUNTO MEDIO PARA: r='+str(r)
		punto_medio(r,True)

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


