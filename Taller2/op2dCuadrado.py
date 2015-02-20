#Practica 2 Daniel Correa 1225622
from OpenGL.GL import *
import OpenGL.GL as gl
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
from math import *
c1=0.0
c2=1.0
c3=0.0
translateCount=0
translateCount2=0
def main():
	global window
	
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)
	
	window = glutCreateWindow('Test')

	glutDisplayFunc(mostrarEscena)
	glutIdleFunc(mostrarEscena)
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mouseClicked);
	InitGL(500,500)
	glutMainLoop()
	matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
	print matrix
def InitGL(Width, Height):
	glClearColor(0.53,0.53,0.53,0.0)
	glMatrixMode(GL_PROJECTION)
	
def mostrarEscena():
	
	glClear(GL_COLOR_BUFFER_BIT)
	
	glBegin(GL_QUADS)
	glColor3f(c1,c2,c3)
	glVertex2f(0.25,0.25)
	glVertex2f(0.25,-0.25)
	glVertex2f(-0.25,-0.25)
	glVertex2f(-0.25,0.25)
	glEnd()
	
	glutSwapBuffers();


def keyPressed(*args):
	key = args[0];
	global translateCount
	global translateCount2
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
	matrix = glGetFloatv(GL_PROJECTION_MATRIX)
	print matrix
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
	matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
	print matrix
	
if __name__=="__main__":
	main()

