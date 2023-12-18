import tkinter as tk
import Transformaciones as tr
import Reprint as rp
from OpenGL.GL import *
from OpenGL.GLU import *
from pyopengltk import OpenGLFrame
import pygame

bandera = 0

class frame(OpenGLFrame):
    def initgl(self):
        glViewport(0, 0, self.width, self.height)
        glClearColor(0.0, 0.0, 0.0, 0.0)

        # setup projection matrix
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-40, 40, -40, 40)

        # setup identity model view matrix
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def redraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        if bandera == 1:
            rp.imprimir(tr.multiplicacion(tr.matTraslado))
        if bandera == 2:
            rp.imprimir(tr.multiplicacion(tr.matEscAumento))
        if bandera == 3:
            rp.imprimir(tr.multiplicacion(tr.matEscDisminucion))
        if bandera == 4:
            rp.imprimir(tr.multiplicacion(tr.matEscPunFijAumento))
        if bandera == 5:
            rp.imprimir(tr.multiplicacion(tr.matEscPunFijDismin))
        if bandera == 6:
            rp.imprimir(tr.multiplicacion(tr.matRotIzq))
        if bandera == 7:
            rp.imprimir(tr.multiplicacion(tr.matRotDer))
        if bandera == 8:
            rp.imprimir(tr.multiplicacion(tr.matRotPunFijIzq))
        if bandera == 9:
            rp.imprimir(tr.multiplicacion(tr.matRotPunFijDer))
        if bandera == 10:
            rp.imprimir(tr.multiplicacion(tr.matCorH))
        if bandera == 11:
            rp.imprimir(tr.multiplicacion(tr.matCorV))
        if bandera == 12:
            rp.imprimir(tr.multiplicacion(tr.matRefX))
        if bandera == 13:
            rp.imprimir(tr.multiplicacion(tr.matRedY))
        if bandera == 14:
            rp.imprimir(tr.multiplicacion(tr.marRefO))
        if bandera == 15:
            rp.imprimir(tr.multiplicacion(tr.matRefR))
        if bandera == 17 or bandera == 18 or bandera == 16 or bandera == 0:
            rp.imprimir(tr.matOriginal)

        glFlush()


def refresh():
    etiquetaI.pack_forget()
    etiqueta = tk.Label(ventana, text="")
    etiqueta.pack()
    etiqueta.destroy()


def original():
    global bandera
    bandera = 0
    refresh()
    app.redraw()


def traslacion():
    global bandera
    bandera = 1
    refresh()
    app.redraw()


def escAumento():
    global bandera
    bandera = 2
    refresh()
    app.redraw()


def escDism():
    global bandera
    bandera = 3
    refresh()
    app.redraw()


def escAumPF():
    global bandera
    bandera = 4
    refresh()
    app.redraw()


def escDisPF():
    global bandera
    bandera = 5
    refresh()
    app.redraw()


def rotIzq():
    global bandera
    bandera = 6
    refresh()
    app.redraw()


def rotDer():
    global bandera
    bandera = 7
    refresh()
    app.redraw()


def rotIzqPF():
    global bandera
    bandera = 8
    refresh()
    app.redraw()


def rotDerPF():
    global bandera
    bandera = 9
    refresh()
    app.redraw()


def corteH():
    global bandera
    bandera = 10
    refresh()
    app.redraw()


def corteV():
    global bandera
    bandera = 11
    refresh()
    app.redraw()


def refX():
    global bandera
    bandera = 12
    refresh()
    app.redraw()


def refY():
    global bandera
    bandera = 13
    refresh()
    app.redraw()


def refO():
    global bandera
    bandera = 14
    refresh()
    app.redraw()


def refR():
    global bandera
    bandera = 15
    refresh()
    app.redraw()


def info():
    global bandera
    bandera = 16
    etiquetaI.pack()
    app.redraw()


def sonidoOn():
    global bandera
    bandera = 17
    refresh()
    sound.play()
    app.redraw()


def sonidoOff():
    global bandera
    bandera = 18
    refresh()
    sound.stop()
    app.redraw()


def menu():
    # MenuBar
    menuBar = tk.Menu(ventana)
    ventana.config(menu=menuBar)

    # Creación de menús
    menu_escalacion = tk.Menu(menuBar, tearoff=0)
    menu_escPF = tk.Menu(menu_escalacion, tearoff=0)
    menu_rotacion = tk.Menu(menuBar, tearoff=0)
    menu_rotPF = tk.Menu(menu_rotacion, tearoff=0)
    menu_corte = tk.Menu(menuBar, tearoff=0)
    menu_ref = tk.Menu(menuBar, tearoff=0)
    menu_sonido = tk.Menu(menuBar, tearoff=0)

    # Agregar los menús al menú bar
    menuBar.add_cascade(label="Original", command=original)
    menuBar.add_cascade(label="Traslación", command=traslacion)
    menuBar.add_cascade(label="Escalación", menu=menu_escalacion)
    menuBar.add_cascade(label="Rotación", menu=menu_rotacion)
    menuBar.add_cascade(label="Corte", menu=menu_corte)
    menuBar.add_cascade(label="Reflexión", menu=menu_ref)
    menuBar.add_cascade(label="Sonido", menu=menu_sonido)
    menuBar.add_cascade(label="Acerca de", command=info)

    menu_escalacion.add_cascade(label="Aumentar", command=escAumento)
    menu_escalacion.add_cascade(label="Disminuir", command=escDism)
    menu_escalacion.add_separator()
    menu_escalacion.add_cascade(label="Punto Fijo", menu=menu_escPF)
    menu_escPF.add_cascade(label="Aumentar", command=escAumPF)
    menu_escPF.add_cascade(label="Disminuir", command=escDisPF)

    menu_rotacion.add_cascade(label="Izquierda", command=rotIzq)
    menu_rotacion.add_cascade(label="Derecha", command=rotDer)
    menu_rotacion.add_separator()
    menu_rotacion.add_cascade(label="Punto Fijo", menu=menu_rotPF)
    menu_rotPF.add_cascade(label="Izquierda", command=rotIzqPF)
    menu_rotPF.add_cascade(label="Derecha", command=rotDerPF)

    menu_corte.add_cascade(label="Vertical", command=corteV)
    menu_corte.add_cascade(label="Horizontal", command=corteH)

    menu_ref.add_cascade(label="Reflexión X", command=refX)
    menu_ref.add_cascade(label="Reflexión Y", command=refY)
    menu_ref.add_cascade(label="Reflexión Recta", command=refR)
    menu_ref.add_cascade(label="Reflexión Origen", command=refO)

    menu_sonido.add_cascade(label="Encender", command=sonidoOn)
    menu_sonido.add_cascade(label="Apagar", command=sonidoOff)


if __name__ == "__main__":
    ventana = tk.Tk()
    pygame.init()
    ventana.title("Cisne")
    menu()
    etiquetaI = tk.Label(ventana, text="Axel Lara Madero 19280766")
    sound = pygame.mixer.Sound("HomeSweetHome.wav")
    app = frame(ventana, width=500, height=500)
    app.pack(fill=tk.BOTH, expand=tk.YES)
    app.mainloop()
