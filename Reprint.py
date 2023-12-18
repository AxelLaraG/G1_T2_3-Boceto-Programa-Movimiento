from OpenGL.GL import *

cont = 0


def imprimir(res):
    global cont
    cont = 0
    for i in range(0, 7):
        if i == 1 or i == 2:
            glColor3f(1, 1, 1)
            poligono(4, res)
        else:
            if i == 0:
                glColor3f(1, 1, 0)

            triangulo(res)


def poligono(lados, res):
    global cont
    aux = cont
    glBegin(GL_POLYGON)
    for i in range(aux, (aux + lados)):
        cont += 1
        glVertex2f(res[i][0], res[i][1])
    glEnd()


def triangulo(res):
    global cont
    aux = cont
    glBegin(GL_TRIANGLES)
    for i in range(aux, (aux + 3)):
        cont += 1
        glVertex2f(res[i][0], res[i][1])
    glEnd()
