#Taller1.
#Integrantes:
#Maria Alejandra Pabon 1310263
#Mayerly Suarez        1310284

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
from PIL import Image
import numpy


def InitGL(Width, Height): 
	glClearColor(0.53, 0.53, 0.53, 0.0) 
	glMatrixMode(GL_PROJECTION)


def mostrarEscena():

	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()
	      
	width = 225
	height = 170
	
	#Abrir imagen
	img = Image.open("tux.png")
	data = numpy.array(list(img.getdata()), numpy.uint8)	
	
	texture = glGenTextures(1)
	glPixelStorei(GL_UNPACK_ALIGNMENT,1)
	glBindTexture(GL_TEXTURE_2D, texture)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER)
			
	#activar uso de texturas
	glEnable(GL_TEXTURE_2D)
	
	#cargar textura
	glTexImage2D(GL_TEXTURE_2D,0,3,width, height,0,GL_RGB,GL_UNSIGNED_BYTE,data)

	
	#Aplicar textura a poligono
	#si se cambian corrdenadas del medio, hace efecto espejo imagen, o se rota dentro del poligono
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




def main():

	global window	
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)	
	glutInitWindowPosition(200,200)
	window = glutCreateWindow('Punto4.1')
	glutDisplayFunc(mostrarEscena)	
	glutIdleFunc(mostrarEscena)	
	InitGL(500, 500)
	glutMainLoop()
	

if __name__ == "__main__":
	main() 
