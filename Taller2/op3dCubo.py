#Practica 2 Daniel Correa 1225622
from OpenGL.GL import *
import OpenGL.GL as gl
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
from math import *
c1=0.0
c2=0.0
c3=0.0


def main():
	global window
	
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)
	
	window = glutCreateWindow('Test')
	glEnable(GL_DEPTH_TEST);
	global c1
	global c2
	global c3
	
	c1=0.0
	c2=0.69
	c3=0.96
	
	glutDisplayFunc(mostrarEscena)
	glutIdleFunc(mostrarEscena)
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mouseClicked);

	InitGL(500,500)
	glutMainLoop()

def InitGL(Width, Height):
	glClearColor(0.53,0.53,0.53,0.0)
	glMatrixMode(GL_PROJECTION)
	
def mostrarEscena():
	

	
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

	
	glBegin(GL_POLYGON);
 
	glColor3f( c1, c2, c3 );     
	glVertex3f(  0.25, -0.25, -0.25 );      
    
	glVertex3f(  0.25,  0.25, -0.25 );      
    
	glVertex3f( -0.25,  0.25, -0.25 );      
   
	glVertex3f( -0.25, -0.25, -0.25 );      
 
	glEnd();

	glBegin(GL_POLYGON);
	glColor3f(   c1,  c2, c3 );
	glVertex3f(  0.25, -0.25, 0.25 );
	glVertex3f(  0.25,  0.25, 0.25 );
	glVertex3f( -0.25,  0.25, 0.25 );
	glVertex3f( -0.25, -0.25, 0.25 );
	glEnd();
	 

	glBegin(GL_POLYGON);
	glColor3f(  c1,  c2,  c3 );
	glVertex3f( 0.25, -0.25, -0.25 );
	glVertex3f( 0.25,  0.25, -0.25 );
	glVertex3f( 0.25,  0.25,  0.25 );
	glVertex3f( 0.25, -0.25,  0.25 );
	glEnd();
	 
	
	glBegin(GL_POLYGON);
	glColor3f(   c1,  c2,  c3 );
	glVertex3f( -0.25, -0.25,  0.25 );
	glVertex3f( -0.25,  0.25,  0.25 );
	glVertex3f( -0.25,  0.25, -0.25 );
	glVertex3f( -0.25, -0.25, -0.25 );
	glEnd();
	 
	
	glBegin(GL_POLYGON);
	glColor3f(   c1,  c2, c3 );
	glVertex3f(  0.25,  0.25,  0.25 );
	glVertex3f(  0.25,  0.25, -0.25 );
	glVertex3f( -0.25,  0.25, -0.25 );
	glVertex3f( -0.25,  0.25,  0.25 );
	glEnd();

	glBegin(GL_POLYGON);
	glColor3f(   c1, c2,  c3 );
	glVertex3f(  0.25, -0.25, -0.25 );
	glVertex3f(  0.25, -0.25,  0.25 );
	glVertex3f( -0.25, -0.25,  0.25 );
	glVertex3f( -0.25, -0.25, -0.25 );
	glEnd()
	glFlush()
	glutSwapBuffers();


def keyPressed(*args):
	key = args[0];
	global c1
	global c2
	global c3
	if key=="r":
		glRotatef(30,1,0,0)
		
	elif key=="R":
		rotationMatrix = (1,0,0,0,0,cos(30*(180/pi)),sin(30*(180/pi)),0,0,-sin(30*(180/pi)),cos(30*(180/pi)),0,0,0,0,1)
		glMultMatrixd(rotationMatrix)
		print "With multMatrix :) rot"
	elif key == "S" or key=="s":
		glRotatef(35,1,3,5)
	elif key=="b" or key=="B":
		glRotatef(30,0,0,1)
		print "de rotacion a translacion"
		glTranslatef(0.0,0.1,0.0)
		print "de translacion a escalacion"
		glScalef(1.0,0.95,1.0)
	

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