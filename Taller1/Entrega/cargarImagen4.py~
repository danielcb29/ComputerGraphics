#Practica 1 Daniel Correa 1225622
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import Image

def main():

	global window	
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)	
	glutInitWindowPosition(200,200)
	window = glutCreateWindow('Test')
	glutDisplayFunc(mostrarEscena)	
	glutIdleFunc(mostrarEscena)	
	InitGL(500, 500)
	glutMainLoop()

def InitGL(Width, Height): 
	glClearColor(0.53, 0.53, 0.53, 0.0) 
	glMatrixMode(GL_PROJECTION)


def mostrarEscena():

	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()
	      
	width = 225
	height = 170
	
	img = Image.open("chelsea.jpeg")
	#data = numpy.array(list(img.getdata()), numpy.uint8)	
	data = img.tostring()
	
	texture = glGenTextures(1)
	glPixelStorei(GL_UNPACK_ALIGNMENT,1)
	glBindTexture(GL_TEXTURE_2D, texture)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER)

	glEnable(GL_TEXTURE_2D)
	

	glTexImage2D(GL_TEXTURE_2D,0,3,width, height,0,GL_RGB,GL_UNSIGNED_BYTE,data)

	

	glBegin(GL_QUADS)
	glTexCoord2f(1, 1); 
	glVertex2f(-0.5, -0.5)
	glTexCoord2f(1, 0); 
	glVertex2f(-0.5, 0.5)
	glTexCoord2f(0, 0); 
	glVertex2f(0.5, 0.5)
	glTexCoord2f(0, 1); 
	glVertex2f(0.5, -0.5)
	glEnd()

	glutSwapBuffers()

if __name__ == "__main__":
	main() 
