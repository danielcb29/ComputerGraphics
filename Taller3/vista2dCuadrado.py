#Practica 3 Daniel Correa 1225622
#NOTA: PARA IMPRIMIR LAS MATRICES UNDIR TECLA M
from OpenGL.GL import *
import OpenGL.GL as gl
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
from math import *
import numpy
c1=0.0
c2=1.0
c3=0.0
translateCount=0
translateCount2=0
mpmatrix = 0;
def main():
	global window
	
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)
	
	window = glutCreateWindow('Test')

	InitGL(500,500)
	glutDisplayFunc(mostrarEscena)
	glutIdleFunc(mostrarEscena)
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mouseClicked);
	
	glutMainLoop()
	
def InitGL(Width, Height):
	glClearColor(0.53,0.53,0.53,0.0)
	glMatrixMode(GL_PROJECTION)
	
def mostrarEscena():
	
	global mpmatrix

	glClear(GL_COLOR_BUFFER_BIT)
	
	glBegin(GL_QUADS)
	glColor3f(c1,c2,c3)
	glVertex2f(15,15)
	glVertex2f(15,-15)
	glVertex2f(-15,-15)
	glVertex2f(-15,15)
	glEnd()
	mpmatrix = glViewport(100, 100, 250, 250);
	#mpmatrix = glViewport(50, 50, 500, 500);
	#mpmatrix = glViewport(250, 100, 300, 250);
	glutSwapBuffers();
	



def keyPressed(*args):
	key = args[0];
	global translateCount
	global translateCount2
	global mpmatrix

	matrixModel = glGetFloatv(GL_MODELVIEW_MATRIX)
	matrixProjection = glGetFloatv(GL_PROJECTION_MATRIX)

	if key=="r":
		glRotatef(30,0,0,1)
	elif key=="R":
		rotationMatrix = (cos(30*(180/pi)),sin(30*(180/pi)),0,0,-sin(30*(180/pi)),cos(30*(180/pi)),0,0,0,0,1,0,0,0,0,1)
		glMultMatrixd(rotationMatrix)
		print "With multMatrix :)"

	elif key=="t" :
		if translateCount==3:
			translateCount=0
			glTranslatef(-0.3,-0.6,0)	
		glTranslatef(0.1,0.2,0)
		translateCount+=1
	elif key=="T":
		translateMatrix=(1,0,0,0,0,1,0,0,0,0,1,0,0.1,0.2,0,1)
		trMinMatrix=(1,0,0,0,0,1,0,0,0,0,1,0,-0.3,-0.6,0,1)
		if translateCount2==3:
			glMultMatrixd(trMinMatrix)
			translateCount2=0
		glMultMatrixd(translateMatrix)
		translateCount2+=1
		print "With multMatrix :)"
	elif key=="S" or key=="s": 
		shMatrix=(1,0,0,0,0.3,1,0,0,0,0,1,0,0,0,0,1)
		glMultMatrixd(shMatrix)
		print "With multMatrix :)"
	elif key=="f" or key=="F":
		refMatrix=(1,0,0,0,0,1,0,0,0,0,-1,0,0,0,0,1)
		glMultMatrixd(refMatrix)
		print "With multMatrix :)"
	elif key=="m" or key=="M":
			
		print "Matriz de Modelado",matrixModel
		print "Matriz de Proyeccion",matrixProjection
		print "Matriz de Mapeo",mpmatrix

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
	
if __name__=="__main__":
	main()

