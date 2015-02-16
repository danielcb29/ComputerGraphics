#Taller 1 Daniel Correa 1225622
from OpenGL.GL import *
import OpenGL.GL as gl
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
c1=0.0
c2=0.0
c3=0.0

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
	glRotatef(30,0,0,1) #Rotacion 2.6
	
	glBegin(GL_POLYGON);
 
	glColor3f( c1, c2, c3 );     
	glVertex3f(  0.25, -0.25, -0.25 );      
	#glColor3f( 0.0, 1.0, 0.0 );     
	glVertex3f(  0.25,  0.25, -0.25 );      
	#glColor3f( 0.0, 0.0, 1.0 );     
	glVertex3f( -0.25,  0.25, -0.25 );      
	#glColor3f( 1.0, 0.0, 1.0 );     
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
	if key=="r" or key=="R":
		
		c1=1.0
		c2=0.0
		c3=0.0
		mostrarEscena()
	elif key=="g" or key=="G":
		
		c1=0.0
		c2=1.0
		c3=0.0
		mostrarEscena()
	elif key=="b" or key=="B":
		
		c1=0.0
		c2=0.0
		c3=1.0
		mostrarEscena()
	matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
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

	print "X: "+str(rotate_x)
	print "Y: "+str(rotate_y)

 
  
	#glutPostRedisplay();
 
		
		
		
if __name__=="__main__":
	main()
