#Practica 5 Daniel Correa, Brayan Rodriguez, Alvaro Martinez
#Para este punto una la tecla 'p' o 'P' para poder ejecutar la funcion de cambio de color CMY to RGB o RGB to CMY 
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
c1=0.81
c2=0.61
c3=1.0
cmy = True
def main():
	global window
	
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)
	
	window = glutCreateWindow('Espacio de Color')
	
	glutDisplayFunc(mostrarEscena)
	glutIdleFunc(mostrarEscena)
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mouseClicked);
	InitGL(500,500)
	glutMainLoop()
	glGetFloatv(GL_MODELVIEW_MATRIX)
	
	
def InitGL(Width, Height):

	glClearColor(0.53,0.53,0.53,0.0)
	glMatrixMode(GL_PROJECTION)
	
def mostrarEscena():
	
	glClear(GL_COLOR_BUFFER_BIT)
	
	glBegin(GL_TRIANGLES)
	glColor3f(c1,c2,c3)
	glVertex2f(0.25,0)
	glVertex2f(-0.25,0)
	glVertex2f(0,0.25)
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
	if key == 'p' or key=='P':
		if cmy: 
			print 'COLORES EN CMY'
			print c1,c2,c3
			convertir()
			print 'COLORES EN RGB'
			print c1,c2,c3

		else: 
			print 'COLORES EN RGB'
			print c1,c2,c3
			convertir()
			print 'COLORES EN CMY'
			print c1,c2,c3
		mostrarEscena()

def convertir():
	global c1
	global c2
	global c3
	global cmy
	
	c1 = 1-c1
	c2 = 1-c2
	c3 = 1-c3
	if cmy: 
		cmy=False
	else: 
		cmy=True
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
