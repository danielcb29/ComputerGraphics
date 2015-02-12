from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import random
c1=0.0
c2=0.0
c3=0.0
def main():
	global window
	
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)
	
	window = glutCreateWindow('Test')
	
	global c1
	global c2
	global c3
	
	c1=0.0
	c2=0.0
	c3=0.0
	
	glutDisplayFunc(mostrarEscena)
	glutIdleFunc(mostrarEscena)
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mouseClicked)
	InitGL(500,500)
	glutMainLoop()
	matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
	print matrix
	
def InitGL(Width, Height):
	glClearColor(0.53,0.53,0.53,0.0)
	glMatrixMode(GL_PROJECTION)
	
def mostrarEscena():
	
	glClear(GL_COLOR_BUFFER_BIT)
	
	glBegin(GL_POLYGON)
	glColor3f(c1,c2,c3)
	
	posx, posy = 0,0    
	sides = 64    
	radius = 0.5    
 
	for i in range(sides):    
		cosine= radius * cos(i*2*pi/sides) + posx    
		sine  = radius * sin(i*2*pi/sides) + posy    
		glVertex2f(cosine,sine)
	
	glEnd()
	
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
	if key=="g" or key=="G":
		
		c1=0.0
		c2=1.0
		c3=0.0
		mostrarEscena()
	if key=="b" or key=="B":
		
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
	matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
	print matrix			
if __name__=="__main__":
	main()
