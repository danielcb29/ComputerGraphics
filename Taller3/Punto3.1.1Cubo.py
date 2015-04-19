from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import * 
import random

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
	
	glBegin(GL_QUADS)
	#top
	glColor3f(0,0,0)
	glVertex3f( 0.25, 0.25,-0.25)
	glVertex3f(-0.25, 0.25,-0.25)
	glVertex3f(-0.25, 0.25, 0.25)
	glVertex3f( 0.25, 0.25, 0.25) 
	
	#bottom
	glColor3f(0,0,1)
	glVertex3f( 0.25,-0.25, 0.25)
	glVertex3f(-0.25,-0.25, 0.25)
	glVertex3f(-0.25,-0.25,-0.25)
	glVertex3f( 0.25,-0.25,-0.25) 
	
	#front
	glColor3f(0,1,0)
	glVertex3f( 0.25, 0.25, 0.25)
	glVertex3f(-0.25, 0.25, 0.25)
	glVertex3f(-0.25,-0.25, 0.25)
	glVertex3f( 0.25,-0.25, 0.25)
 
	#back
	glColor3f(1,0,0)
	glVertex3f( 0.25,-0.25,-0.25)
	glVertex3f(-0.25,-0.25,-0.25)
	glVertex3f(-0.25, 0.25,-0.25)
	glVertex3f( 0.25, 0.25,-0.25)
 
	#left
	glColor3f(1,1,0)
	glVertex3f(-0.25, 0.25, 0.25) 
	glVertex3f(-0.25, 0.25,-0.25)
	glVertex3f(-0.25,-0.25,-0.25) 
	glVertex3f(-0.25,-0.25, 0.25) 
 
	#right
	glColor3f(0,1,1)
	glVertex3f( 0.25, 0.25,-0.25) 
	glVertex3f( 0.25, 0.25, 0.25)
	glVertex3f( 0.25,-0.25, 0.25)
	glVertex3f( 0.25,-0.25,-0.25)
	glEnd()
	
	glutSwapBuffers()
	
def keyPressed(*args):
	key = args[0]
	if(key=="o" or key=="O"):
		#glOrtho(-1,1,-1,1,1,-2) #con esta proyeccion no se agranda ni se encoge el plano visual, al menos no en el plano xy.
		#glOrtho(0,2,0,1,1,-1) #con esta proyeccion se ve una esquina no mas del cubo, debido a la traslacion del campo visual.
		glOrtho(-2,2,-2,2,2,-2) #como el campo visual se hace mas grande con esta proyeccion el cubo se va haciendo mas pequeno.
		print "La matriz de proyeccion es:"
		print glGetFloatv(GL_PROJECTION_MATRIX)
		print "La matriz de modelado es:"
		print glGetFloatv(GL_MODELVIEW_MATRIX)
	elif(key=="l" or key=="L"):
		#gluLookAt(0,0,-1,0,0,0,0,1,0) #con esta ubicacion queda igual la proyeccion.
		#gluLookAt(0,0,1,0,0,0,0,1,0) #con esta ubicacion la camara se traslada hacia la cara frontal pero a la segunda vez, no se logra ver nada.
		gluLookAt(0,0,-1,-1,0,0,0,1,0) #con este centro de referencia se ve un poco raro, la camara deberia estar viendo hacia el punto de interseccion entre el plano rojo y el amarillo y en el software se ven los colores cyan, rojo y amarillo.
		print "La matriz de proyeccion es:"
		print glGetFloatv(GL_PROJECTION_MATRIX)
		print "La matriz de modelado es:"
		print glGetFloatv(GL_MODELVIEW_MATRIX)
	elif(key=="f" or key=="F"):
		#glFrustum(-0.1,0.1,-0.1,0.1,0.1,1) #con esta proyeccion se ve la a partir de cierto punto el cubo y tapa toda la vision de la camara.
		#glFrustum(-0.25,0.25,-0.25,0.25,0.25,1) #con esta proyeccion no se ve el cubo porque el campo de visualizacion comienza en 0.25 en z, lugar donde se termina el cubo.
		glFrustum(-0.01,0.01,-0.01,0.01,0.01,0.25) #con esta proyeccion tambien se tapa todo el campo visual con el cubo.
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
		
def clickPressed(*args):'''
	button = args[0]
	global r
	global g
	global b
	if (button == GLUT_LEFT_BUTTON):
		r=random.random()
		g=random.random()
		b=random.random()
		mostrarEscena()
'''		

main()
