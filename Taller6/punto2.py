# Practica 1 Daniel Correa 1225622
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import Image

c1 = 0.5
c2 = 0.5
c3 = 0.5


def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(200, 200)
    window = glutCreateWindow('Test')
    glutDisplayFunc(mostrarEscena)
    glutIdleFunc(mostrarEscena)
    InitGL(500, 500)
    glutKeyboardFunc(keyPressed)
    glutMainLoop()


def InitGL(Width, Height):
    glClearColor(0.53, 0.53, 0.53, 0.0)
    glMatrixMode(GL_PROJECTION)


def mostrarEscena():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    width = 225
    height = 170

    img = Image.open("images.jpg")
    # data = numpy.array(list(img.getdata()), numpy.uint8)
    data = img.tostring()

    texture = glGenTextures(1)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER)

    glEnable(GL_TEXTURE_2D)

    glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data)

    glBegin(GL_QUADS)
    glTexCoord2f(1, 1);
    glVertex2f(-0.5, -0.5)
    glTexCoord2f(1, 0);
    glVertex2f(-0.5, 0.5)
    glTexCoord2f(0, 0)
    glVertex2f(0.5, 0.5)
    glTexCoord2f(0, 1);
    glVertex2f(0.5, -0.5)
    glEnd()

    glutSwapBuffers()


def keyPressed(*args):
    key = args[0];
    global c1
    global c2
    global c3
    # Modificar luz ambiental
    if key == "a" or key == "A":
        c1 += 0.1
        c2 += 0.1
        c3 += 0.1
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [c1, c2, c2, 1])
        glEnable(GL_LIGHTING)
        mostrarEscena()
    # Modificar luz por difusion
    if key == "d" or key == "D":
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0, 0, 0, 1])
        glEnable(GL_LIGHTING)
        c1 += 0.1
        c2 += 0.1
        c3 += 0.1
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [c1, c2, c2, 1])
        glLightfv(GL_LIGHT0, GL_POSITION,[0.5, 0.5, 0.5, 1]);
        glEnable(GL_LIGHT0)
        mostrarEscena()
    #Luz especular
    if key == "s" or key == "S":
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0, 0, 0, 1])
        glEnable(GL_LIGHTING)
        c1 += 0.1
        c2 += 0.1
        c3 += 0.1
        glLightfv(GL_LIGHT1, GL_SPECULAR, [c1, c2, c2, 1])
        glMaterialfv(GL_FRONT, GL_SPECULAR, [c1, c2, c3])
        glMaterialfv(GL_FRONT, GL_SHININESS, 60)
        glLightfv(GL_LIGHT1, GL_POSITION,[0.5, -0.5, 0.5, 1])
        glEnable(GL_LIGHT1)
        mostrarEscena()
    #Luz de emision
    if key == "E" or key == "e":
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0, 0, 0, 1])
        glEnable(GL_LIGHTING)
        c1 += 0.1
        c2 += 0.1
        c3 += 0.1
        glMaterialfv(GL_FRONT, GL_EMISSION, [0.9, 0.3, 0.3, 0])
        glEnable(GL_LIGHT1)
        mostrarEscena()


if __name__ == "__main__":
    main()
