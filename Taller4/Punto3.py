from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def main():
	global window

	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)

	window = glutCreateWindow('Taller 4-4.1')

	glutDisplayFunc(mostrarEscena)
	glutIdleFunc(mostrarEscena)
	InitGL(500,500)
	glutMainLoop()
	glGetFloatv(GL_MODELVIEW_MATRIX)

def InitGL(Width, Height):
	glClearColor(0.529, 0.529, 0.529,0.529)
	glMatrixMode(GL_PROJECTION)

def mostrarEscena():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    for punto in pun_pintar:
        glVertex2d(float(punto[0])/100, float(punto[1])/100)
    glEnd()
    glutSwapBuffers()

def DDA(x1, y1, x2, y2):

    m = float(calcular_pendiente(x1, y1, x2, y2))

    if(abs(m)>1):
        m=1/m
        if y1>y2:
            x1_p=x2
            x2_p=x1
            y1_p=y2
            y2_p=y1
            x1=x1_p
            x2=x2_p
            y1=y1_p
            y2=y2_p
        y=y1
        x=x1
        lis_pun_pintar = [[round(x1), round(y1)]]
        for y in range(y1+1, y2):
            x=float(x+m)
            print x, y
            lis_pun_pintar.append([round(x),round(y)])
    else:
        if x1>x2:
            x1_p=x2
            x2_p=x1
            y1_p=y2
            y2_p=y1
            x1=x1_p
            x2=x2_p
            y1=y1_p
            y2=y2_p
        y=y1
        x=x1
        lis_pun_pintar = [[round(x1), round(y1)]]
        for x in range(x1+1, x2):
            y=y+m
            lis_pun_pintar.append([round(x),round(y)])
    lis_pun_pintar.append([round(x2),round(y2)])

    return lis_pun_pintar

def calcular_pendiente(x1, y1, x2, y2):
    pen = float(y2-y1)/(x2-x1)
    return  pen


################ PUNTO 3.1.1#######################
print "Punto 3. Los puntos a pintar con el algoritmo DDA y los siguientes puntos (-6, 7) (5, 10)", DDA(-6, 7, 5, 10)
################ PUNTO 3.1.2#######################
print "Punto 3. Los puntos a pintar con el algoritmo DDA y los siguientes puntos (-6, 7) (5, 10)", DDA(-6, 7, 5, 10)

################ PUNTO 3.2.1#######################
#los puntos: (-0,65, -0,45) (0,7, 0,6). Los multiplicamos por 100 para poder que se vuelvan enteros y luego se divide entre el mismo numero para poder a graficar los puntos propuestos.
#pun_pintar = DDA(-65, -45, 70, 60)

################ PUNTO 3.2.2#######################
#Para esta recta: y=0,9x -0,3 desde x=-0,7 a x=0,8. Se evalua los dos x en la ecuacion. Con lo cual tenemos los puntos (-0.7,-0,93) (0.8, 0,42)
#los puntos: (-0.7,-0,93) (0.8, 0,42). Los multiplicamos por 100 para poder que se vuelvan enteros y luego se divide entre el mismo numero para poder a graficar los puntos propuestos.
pun_pintar = DDA(-70,-93, 80, 42)
main()
