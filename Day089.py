from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle = 0.0


def menggambar3d():
    global angle

    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslatef(0, 0, -15)  # harus disertakan jika ingin melihat sisi dari objek
    glRotatef(angle, 0, 1, 0)
    glBegin(GL_TRIANGLES)  # untuk objek segitiga yang bagian atas
    # DEPAN HIJAU
    glColor3f(0, 1, 0)
    glVertex3f(0, 1, 0)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    # MERAH KANAN FACE2
    glColor3f(1, 0, 0)
    glVertex3f(0, 1, 0)  # atas
    glVertex3f(1, -1, 1)  # bawah depan
    glVertex3f(1, -1, -1)  # samping bawah belakang

    # tambahkan 2 face lagi untuk objek segitiga bagian atas
    glEnd()
    # Alas
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)

    glEnd()

    glTranslatef(4, 0, 0)

    # objek segitiga yang kedua cerminan
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 1)
    glVertex3f(-1, -1, 1)
    glColor3f(0, 0, 1)
    glVertex3f(0, -3, 0)
    glVertex3f(1, -1, 1)
    # kanan
    glColor3f(1, 1, 0)
    glVertex3f(1, -1, 1)
    glColor3f(0, 1, 1)
    glVertex3f(0, -3, 0)
    glVertex3f(1, -1, -1)

    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)

    glEnd()

    glutSwapBuffers()


def timer(value):
    global angle
    angle += 1.0
    if angle > 360.0:
        angle -= 360.0

    glutPostRedisplay()
    glutTimerFunc(10, timer, 0)


def bentuk(width, height):
    if height == 0:
        height = 1

    ukuran = float(width) / float(height)

    glViewport(50, 100, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50, ukuran, 1, 100)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(680, 480)
    glutInitWindowPosition(-10, 100)
    glutCreateWindow("segitiga")
    glutDisplayFunc(menggambar3d)
    glutReshapeFunc(bentuk)
    glutTimerFunc(5, timer, 0)
    glutMainLoop()


main()
