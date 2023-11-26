import math
from PyQt5 import  QtGui
from PyQt5.QtCore import QSize, Qt, QUrl
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QLabel, \
    QGridLayout, QPushButton, QHBoxLayout, QScrollArea, QButtonGroup, QTextEdit

from manualLista import Lista

class Manual(QMainWindow):
    def __init__(self, anterior):
        super(Manual, self).__init__(anterior)
        # Se crea la ventana principal junto a sus modificaciones
        self.ventanaAnterior = anterior

        self.colorFondo1 = anterior.colorFondo1
        self.colorFondo2 = anterior.colorFondo2
        self.colorFondo3 = anterior.colorFondo3
        self.colorLetra1 = anterior.colorLetra1
        self.colorLetra2 = anterior.colorLetra2
        self.colorLetra3 = anterior.colorLetra3
        self.colorBotones1 = anterior.colorBotones1
        self.colorBotones2 = anterior.colorBotones2
        self.colorBotones3 = anterior.colorBotones3
        self.colorLogo = anterior.colorLogo

        self.setWindowTitle("Manual")

        self.ancho = 1000
        self.alto = 563
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Creamos la ventana de fondo para establecer las ventanas de forma vertical
        self.fondo = QWidget()
        self.vertical = QVBoxLayout()
        self.fondo.setStyleSheet("background-color: " + self.colorFondo1 + ";")
        self.setCentralWidget(self.fondo)

        # Creamos una ventana horizontal para establecer el titulo y el botón de regreso
        self.regreso = QLabel()
        self.horizontalP = QHBoxLayout()
        self.regreso.setFixedHeight(60)

        # Creamos el titulo
        self.titulo1 = QLabel("MANUAL")
        self.titulo1.setFont(QFont("Arial", 40))
        self.titulo1.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.titulo1.setAlignment(Qt.AlignCenter)

        self.horizontalP.addWidget(self.titulo1)
        self.horizontalP.addStretch()

        # Creamos el botón para volver a la ventana administrador
        self.devolver = QPushButton()
        self.devolver.setFixedWidth(50)
        self.devolver.setFixedHeight(50)
        self.devolver.setStyleSheet("background-color: " + self.colorBotones1 + ";")
        self.devolver.setIcon(QtGui.QIcon('Imagenes/iconos/casa.png'))
        self.devolver.setIconSize(QSize(40, 40))
        self.devolver.clicked.connect(self.ir_administrador)

        self.horizontalP.addWidget(self.devolver)

        self.regreso.setLayout(self.horizontalP)
        self.vertical.addWidget(self.regreso)
        self.vertical.addStretch()

        #- SE CREA LABEL PARA AGREGAR INFORMACION -
        self.vA = QLabel()
        self.horizontalA = QHBoxLayout()
        self.vA.setStyleSheet("background-color: " + self.colorFondo3 + ";")
        self.vA.setFixedHeight(400)

        #---- AQUI VA EL TEXTO RELACIONADO CON LA INFORMACION
        self.textoIzquierda = QLabel()
        self.verticalI = QVBoxLayout()
        self.textoIzquierda.setFixedWidth(600)
        self.verticalI.setAlignment(Qt.AlignTop)

        self.tituloDescripcion = QLabel()
        self.tituloDescripcion.setAlignment(Qt.AlignCenter)
        self.tituloDescripcion.setFont(QFont("Arial", 15))
        self.tituloDescripcion.setStyleSheet("color: " + self.colorLetra3 + ";")


        self.verticalI.addWidget(self.tituloDescripcion)

        self.textoDescripcion = QWebEngineView()
        self.textoDescripcion.setContextMenuPolicy(Qt.NoContextMenu)
        self.textoDescripcion.setFixedHeight(291)

        self.verticalI.addWidget(self.textoDescripcion)

        self.textoIzquierda.setLayout(self.verticalI)
        self.horizontalA.addWidget(self.textoIzquierda)

        #---- AQUI VAN LAS IMAGENES RELACIONADAS CON AL INFORMACION ----
        self.imagenInfomacion = QLabel()
        self.imagenInfomacion.setFixedWidth(300)
        self.imagenInfomacion.setFixedHeight(300)
        self.imagenInfomacion.setScaledContents(True)

        self.horizontalA.addWidget(self.imagenInfomacion)

        self.vA.setLayout(self.horizontalA)
        self.vertical.addWidget(self.vA)

        #- SE AGREGA LABEL PARA COLOCAR LOS BOTONES -
        self.vB = QLabel()
        self.horizontalB = QHBoxLayout()
        self.vB.setFixedHeight(60)

        self.botonIzquierda = QPushButton()
        self.botonIzquierda.setFixedWidth(90)
        self.botonIzquierda.setFixedHeight(40)
        self.botonIzquierda.setStyleSheet("background-color: " + self.colorBotones1 + ";")
        self.botonIzquierda.setIcon(QtGui.QIcon('Imagenes/iconos/flechaIzquierda.png'))
        self.botonIzquierda.setIconSize(QSize(60, 20))
        self.botonIzquierda.setFont(QFont("Arial", 12))
        self.botonIzquierda.clicked.connect(self.boton_izquierda)

        self.botonDerecha = QPushButton()
        self.botonDerecha.setFixedWidth(90)
        self.botonDerecha.setFixedHeight(40)
        self.botonDerecha.setStyleSheet("background-color: " + self.colorBotones1 + ";")
        self.botonDerecha.setIcon(QtGui.QIcon('Imagenes/iconos/flechaDerecha.png'))
        self.botonDerecha.setIconSize(QSize(60, 20))
        self.botonDerecha.setFont(QFont("Arial", 12))
        self.botonDerecha.clicked.connect(self.boton_Derecha)

        self.horizontalB.addWidget(self.botonIzquierda)
        self.horizontalB.addStretch()
        self.horizontalB.addWidget(self.botonDerecha)

        self.vB.setLayout(self.horizontalB)
        self.vertical.addWidget(self.vB)

        # -- SE COLOCA AL FINAL --
        self.fondo.setLayout(self.vertical)

        self.contador = 1

        self.manual1 = open("manual/1.html", "rb"); self.pag1 = self.manual1.read().decode("UTF-8"); self.manual1.close()
        self.manual2 = open("manual/2.html", "rb"); self.pag2 = self.manual2.read().decode("UTF-8"); self.manual2.close()
        self.manual3 = open("manual/3.html", "rb"); self.pag3 = self.manual3.read().decode("UTF-8"); self.manual3.close()
        self.manual4 = open("manual/4.html", "rb"); self.pag4 = self.manual4.read().decode("UTF-8"); self.manual4.close()
        self.manual5 = open("manual/5.html", "rb"); self.pag5 = self.manual5.read().decode("UTF-8"); self.manual5.close()
        self.manual6 = open("manual/6.html", "rb"); self.pag6 = self.manual6.read().decode("UTF-8"); self.manual6.close()
        self.manual7 = open("manual/7.html", "rb"); self.pag7 = self.manual7.read().decode("UTF-8"); self.manual7.close()
        self.manual8 = open("manual/8.html", "rb"); self.pag8 = self.manual8.read().decode("UTF-8"); self.manual8.close()


        self.informacion = [self.pag1, self.pag2, self.pag3, self.pag4, self.pag5, self.pag6, self.pag7, self.pag8]

        self.file = open('datos/manual.txt', 'rb')
        self.manuales = []

        self.imagen1 = QPixmap('Imagenes/Imagenes manual/1.png')
        self.imagen2 = QPixmap('Imagenes/Imagenes manual/2.jpg')
        self.imagen3 = QPixmap('Imagenes/Imagenes manual/3.png')
        self.imagen4 = QPixmap('Imagenes/Imagenes manual/4.jpg')
        self.imagen5 = QPixmap('Imagenes/Imagenes manual/5.png')
        self.imagen6 = QPixmap('Imagenes/Imagenes manual/6.png')
        self.imagen7 = QPixmap('Imagenes/Imagenes manual/7.png')
        self.imagen8 = QPixmap('Imagenes/Imagenes manual/8.png')

        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")
            if linea == '':
                break
            self.m = Lista(
                lista[0],
                lista[1],
                lista[2]
            )
            self.manuales.append(self.m)
        self.file.close()

        #varible para cargar informacion cuando ingrese a la ventana manual
        self.botonIzquierda.hide()
        self.actualizar_manual()

    def actualizar_manual(self):
        for self.m in self.manuales:
            if self.m.idPosicion == str(self.contador):

                self.tituloDescripcion.setText(self.m.titulo)
                self.textoDescripcion.setHtml(self.informacion[int(self.m.idtexto) - 1])

                if self.m.idPosicion == str(1):
                    self.imagenInfomacion.setPixmap(self.imagen1)
                if self.m.idPosicion == str(2):
                    self.imagenInfomacion.setPixmap(self.imagen2)
                if self.m.idPosicion == str(3):
                    self.imagenInfomacion.setPixmap(self.imagen3)
                if self.m.idPosicion == str(4):
                    self.imagenInfomacion.setPixmap(self.imagen4)
                if self.m.idPosicion == str(5):
                    self.imagenInfomacion.setPixmap(self.imagen5)
                if self.m.idPosicion == str(6):
                    self.imagenInfomacion.setPixmap(self.imagen6)
                if self.m.idPosicion == str(7):
                    self.imagenInfomacion.setPixmap(self.imagen7)
                if self.m.idPosicion == str(8):
                    self.imagenInfomacion.setPixmap(self.imagen8)

    def ir_administrador(self):
        # Metodo para volver a la ventana del administrador
        self.hide()
        self.ventanaAnterior.escanear_alertas()
        self.ventanaAnterior.notificacion_alertas()
        self.ventanaAnterior.show()
        self.ventanaAnterior.show()

    def boton_izquierda(self):
        if self.contador == 2:
            self.contador -= 1
            self.botonIzquierda.hide()
            self.actualizar_manual()
        elif not self.contador == 0:
            self.contador -= 1
            self.actualizar_manual()
            self.botonDerecha.show()
            self.botonIzquierda.show()
        elif self.contador == 1:
            pass

    def boton_Derecha(self):
        if self.contador < len(self.informacion) - 1:
            self.contador += 1
            self.actualizar_manual()
            self.botonIzquierda.show()
            self.botonDerecha.show()
        elif self.contador == len(self.informacion) - 1:
            self.contador += 1
            self.actualizar_manual()
            self.botonDerecha.hide()