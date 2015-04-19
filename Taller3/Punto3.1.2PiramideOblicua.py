from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import * 
import random

global r
r=0.901
global g
g=0.372
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
	glutSpecialFunc(keyPressed)
	glutMouseFunc(clickPressed)
	InitGL(500,500)
	print "La matriz de proyeccion es:"
	print glGetFloatv(GL_PROJECTION_MATRIX)
	
	glutMainLoop()
	
	
def InitGL(Width, Height):
	glClearColor(0.529, 0.529, 0.529,0.529)
	glMatrixMode(GL_PROJECTION)
	
def mostrarEscena():
	glClear(GL_COLOR_BUFFER_BIT)
	
	glBegin(GL_TRIANGLES)
	#left
	glColor3f(0,0,0)
	glVertex3f(0.0, 0.5, 1.0)
	glVertex3f(0.0, 0.0, 0.5)
	glVertex3f(0.0, 0.0, 0.5)
	#front
	glColor3f(1,0,0)
	glVertex3f(0.0, 0.5, 1.0)
	glVertex3f(1, 0.0, 1.5)
	glVertex3f(0.0, 0.0, 1.5)
	#back
	glColor3f(0,1,0)
	glVertex3f(0.0, 0.5, 1.0)
	glVertex3f(1, 0.0, 0.5)
	glVertex3f(0.0, 0.0, 0.5)
	#top
	glColor3f(0,0,1)
	glVertex3f(0.0, 0.5, 1.0)
	glVertex3f(1, 0.0, 0.5)
	glVertex3f(1, 0.0, 1.5)
		
	glEnd()
	
	glBegin(GL_QUADS)
	#bottom
	glColor3f(1,1,0)
	glVertex3f(0.0, 0.0, 1.5)
	glVertex3f(1.0, 0.0, 1.5)
	glVertex3f(1.0, 0.0, 0.5)
	glVertex3f(0.0, 0.0, 0.5)
	
	glEnd()
	
	glutSwapBuffers()
	
def keyPressed(*args):
	key = args[0]
	if(key=="o" or key=="O"):
		#glOrtho(-1,1,-1,1,1,-2) #con esta proyeccion no se agranda ni se encoge el plano visual, al menos no en el plano xy.
		#glOrtho(0,2,0,1,1,-1) #con esta proyeccion se ve una esquina no mas de la piramide, debido a la traslacion del campo visual.
		glOrtho(-2,2,-2,2,2,-2) #como el campo visual se hace mas grande con esta proyeccion la piramide se va haciendo mas pequeno.
		print "La matriz de proyeccion es:"
		print glGetFloatv(GL_PROJECTION_MATRIX)
		print "La matriz de modelado es:"
		print glGetFloatv(GL_MODELVIEW_MATRIX)
	elif(key=="l" or key=="L"):
		#gluLookAt(0,0,0,0,0,1,0,1,0) #con esta ubicacion la proyeccion se refleja en el eje zy.
		#gluLookAt(0,0,2,0,0,0,0,1,0) #con esta ubicacion la camara se traslada hacia la cara frontal pero a la segunda vez, no se logra ver nada.
		gluLookAt(0,0,0,1,0,0.5,0,1,0) #con este centro de referencia se ven las caras rojo, verde y azul de la piramide, caras que se muestran en el punto al que se esta apuntando.
		print "La matriz de proyeccion es:"
		print glGetFloatv(GL_PROJECTION_MATRIX)
		print "La matriz de modelado es:"
		print glGetFloatv(GL_MODELVIEW_MATRIX)
	elif(key=="f" or key=="F"):
		#glFrustum(1.0,1.02,0.0,0.03,0.2,2) #con esta proyeccion no se ve la piramide.
		print "La matriz de proyeccion es:"
		print glGetFloatv(GL_PROJECTION_MATRIX)
		print "La matriz de modelado es:"
		print glGetFloatv(GL_MODELVIEW_MATRIX)
	elif(key=="r"):
		glRotatef(35,1,3,5)
		print "La matriz de proyeccion es:"
		print glGetFloatv(GL_PROJECTION_MATRIX)
		print "La matriz de modelado es:"
		print glGetFloatv(GL_MODELVIEW_MATRIX)
	elif( key=="R"):
		glRotatef(-35,1,3,5)
		print "La matriz de proyeccion es:"
		print glGetFloatv(GL_PROJECTION_MATRIX)
		print "La matriz de modelado es:"
		print glGetFloatv(GL_MODELVIEW_MATRIX)
		
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
