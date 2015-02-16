#Taller 1 Daniel Correa 1225622
from OpenGL.GL import *
import OpenGL.GL as gl
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
c11=0.094 
c12= 0.392
c13=0.047

c21=0.047
c22=0.141
c23=0.392

c31=0.482
c32=0.035
c33=0.035

c41=0.698
c42=0.670
c43=0.003

c51=1.0
c52=1.0
c53=1.0

c61=0.0
c62=0.0
c63=0.0


rotate_y=-35; 
rotate_x=5;


def main():
	global window
	
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)
	
	window = glutCreateWindow('Test')
	glEnable(GL_DEPTH_TEST);
	
	glutDisplayFunc(mostrarEscena)
	glutIdleFunc(mostrarEscena)
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mouseClicked);
	glutSpecialFunc(specialKeys);
	InitGL(500,500)
	glutMainLoop()

def InitGL(Width, Height):
	glClearColor(0.53,0.53,0.53,0.0)
	glMatrixMode(GL_PROJECTION)
	
def mostrarEscena():
	
	global rotate_x
	global rotate_y
	
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glLoadIdentity();
	
	glRotatef( rotate_x, 1.0, 0.0, 0.0 );
	glRotatef( rotate_y, 0.0, 1.0, 0.0 );
	#glRotatef(30,0,0,1) #Rotacion 2.6


	#Parte 1 

	#Cara1
	glBegin(GL_QUADS)
	glColor3f( c11, c12, c13 );
	glVertex3f(  0.0, -0.25, -0.25 );
	glVertex3f(  0.25, 0.25, -0.25 );
	glVertex3f(  0.0, 0.25, -0.25 );
	glVertex3f(  -0.25, -0.25, -0.25 );
	glEnd()

	#Cara3
	glBegin(GL_QUADS)
	glColor3f( c31, c32, c33 );
	glVertex3f(  0.0, -0.25, 0.0 );
	glVertex3f(  0.25, 0.25, 0.0 );
	glVertex3f(  0.0, 0.25, 0.0 );
	glVertex3f(  -0.25, -0.25, 0.0 );
	glEnd()

	#Cara4
	glBegin(GL_QUADS)
	glColor3f( c41, c42, c43 );
	glVertex3f(  0.25, 0.25, -0.25 );
	glVertex3f(  0.25, 0.25, 0.0 );
	glVertex3f(  0.0, 0.25, 0.0 );
	glVertex3f(  0.0, 0.25, -0.25 );
	glEnd()

	#Cara5
	glBegin(GL_QUADS)
	glColor3f( c51, c52, c53 );
	glVertex3f(  0.0, -0.25, -0.25 );
	glVertex3f(  0.0, -0.25, 0.0 );
	glVertex3f(  -0.25, -0.25, 0.0 );
	glVertex3f(  -0.25, -0.25, -0.25 );
	glEnd()	

	#Cara2
	glBegin(GL_QUADS)
	glColor3f( c21, c22, c23 );
	glVertex3f(  0.0, -0.25, 0.0 );
	glVertex3f(  0.25, 0.25, 0.0 );
	glVertex3f(  0.25, 0.25, -0.25 );
	glVertex3f(  0.0, -0.25, -0.25 );
	glEnd()

	#Cara6
	glBegin(GL_QUADS)
	glColor3f( c61, c62, c63 );
	glVertex3f(  -0.25, -0.25, 0.0 );
	glVertex3f(  0.0, 0.25, 0.0 );
	glVertex3f(  0.0, 0.25, -0.25 );
	glVertex3f(  -0.25, -0.25, -0.25 );
	glEnd()


	#Parte 2

	#Cara1
	glBegin(GL_QUADS)
	glColor3f( c11, c12, c13 );
	glVertex3f(  0.50, -0.25, -0.25 );
	glVertex3f(  0.25, 0.25, -0.25 );
	glVertex3f(  0.0, 0.25, -0.25 );
	glVertex3f(  0.25, -0.25, -0.25 );
	glEnd()

	#Cara3
	glBegin(GL_QUADS)
	glColor3f( c31, c32, c33 );
	glVertex3f(  0.50, -0.25, 0.0 );
	glVertex3f(  0.25, 0.25, 0.0 );
	glVertex3f(  0.0, 0.25, 0.0 );
	glVertex3f(  0.25, -0.25, 0.0 );
	glEnd()

	#Cara5
	glBegin(GL_QUADS)
	glColor3f( c51, c52, c53 );
	glVertex3f(  0.50, -0.25, -0.25 );
	glVertex3f(  0.50, -0.25, 0.0 );
	glVertex3f(  0.25, -0.25, 0.0 );
	glVertex3f(  0.25, -0.25, -0.25 );
	glEnd()	

	#Cara2
	glBegin(GL_QUADS)
	glColor3f( c21, c22, c23 );
	glVertex3f(  0.50, -0.25, 0.0 );
	glVertex3f(  0.25, 0.25, 0.0 );
	glVertex3f(  0.25, 0.25, -0.25 );
	glVertex3f(  0.50, -0.25, -0.25 );
	glEnd()

	#Cara 6 
	glBegin(GL_QUADS)
	glColor3f( c61, c62, c63 );
	glVertex3f(  0.25, -0.25, 0.0 );
	glVertex3f(  0.0, 0.25, 0.0 );
	glVertex3f(  0.0, 0.25, -0.25 );
	glVertex3f(  0.25, -0.25, -0.25 );
	glEnd()

	glFlush()
	glutSwapBuffers();


def keyPressed(*args):
	key = args[0];
	global c11
	global c12
	global c13
	global c21
	global c22
	global c23
	global c31
	global c32
	global c33
	global c41
	global c42
	global c43
	global c51
	global c52
	global c53
	global c61
	global c62
	global c63
	if key=="r" or key=="R":
		
		c11=1.0
		c12=0.0
		c13=0.0
		c21=1.0
		c22=0.0
		c23=0.0
		c31=1.0
		c32=0.0
		c33=0.0
		c41=1.0
		c42=0.0
		c43=0.0
		c51=1.0
		c52=0.0
		c53=0.0
		c61=1.0
		c62=0.0
		c63=0.0
		mostrarEscena()
	elif key=="g" or key=="G":
		
		c11=0.0
		c12=1.0
		c13=0.0
		c21=0.0
		c22=1.0
		c23=0.0
		c31=0.0
		c32=1.0
		c33=0.0
		c41=0.0
		c42=1.0
		c43=0.0
		c51=0.0
		c52=1.0
		c53=0.0
		c61=0.0
		c62=1.0
		c63=0.0
		mostrarEscena()
	elif key=="b" or key=="B":
		
		c11=0.0
		c12=0.0
		c13=1.0
		c21=0.0
		c22=0.0
		c23=1.0
		c31=0.0
		c32=0.0
		c33=1.0
		c41=0.0
		c42=0.0
		c43=1.0
		c51=0.0
		c52=0.0
		c53=1.0
		c61=0.0
		c62=0.0
		c63=1.0
		mostrarEscena()
	
	
def mouseClicked(*args):
	key = args[0];
	global c11
	global c12
	global c13
	global c21
	global c22
	global c23
	global c31
	global c32
	global c33
	global c41
	global c42
	global c43
	global c51
	global c52
	global c53
	global c61
	global c62
	global c63
	if key == GLUT_LEFT_BUTTON:
		c11= random.random()
		c12= random.random()
		c13= random.random()
		c21= random.random()
		c22= random.random()
		c23= random.random()
		c31= random.random()
		c32= random.random()
		c33= random.random()
		c41= random.random()
		c42= random.random()
		c43= random.random()
		c51= random.random()
		c52= random.random()
		c53= random.random()
		c61= random.random()
		c62= random.random()
		c63= random.random()
		mostrarEscena()
	


		
def specialKeys( *args):
	key = args[0]
	global rotate_x
	global rotate_y

	if (key == GLUT_KEY_RIGHT):
		rotate_y += 5;

	elif (key == GLUT_KEY_LEFT):
		rotate_y -= 5;

	elif (key == GLUT_KEY_UP):
		rotate_x += 5;

 
	elif (key == GLUT_KEY_DOWN):
		rotate_x -= 5;

	#print "X: "+str(rotate_x)
	#print "Y: "+str(rotate_y)
 
		
		
		
if __name__=="__main__":
	main()
