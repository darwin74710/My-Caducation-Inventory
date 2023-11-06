import math
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QToolBar, QAction, QWidget, QVBoxLayout, QLabel, \
    QGridLayout, QFormLayout, QPushButton, QHBoxLayout, QLineEdit, QScrollArea, QButtonGroup, QDialog, QDialogButtonBox, \
    QTextEdit

class Alertas(QMainWindow):
    def __init__(self, anterior):
        super(Alertas, self).__init__(anterior)

        self.ventanaAnterior = anterior

        self.setWindowTitle("Alertas")

        self.ancho = 1000
        self.alto = 563

        self.resize(self.ancho, self.alto)

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.ventana = QWidget()
        self.ventana.setStyleSheet("background-color: #9AC069;")
        self.setCentralWidget(self.ventana)
        self.vertical = QVBoxLayout()

        self.regreso = QLabel()
        self.regreso.setFixedHeight(60)
        self.horizontalP = QHBoxLayout()

        self.titulo1 = QLabel("ALERTAS")
        self.titulo1.setFont(QFont("Arial", 40))
        self.titulo1.setStyleSheet("color: white;")
        self.titulo1.setAlignment(Qt.AlignCenter)

        self.devolver = QPushButton()
        self.devolver.setFixedWidth(50)
        self.devolver.setFixedHeight(50)
        self.devolver.setStyleSheet("background-color: #8EA85D;")
        self.devolver.setIcon(QtGui.QIcon('Imagenes/iconos/casa.png'))
        self.devolver.setIconSize(QSize(40, 40))
        self.devolver.clicked.connect(self.ir_administrador)

        self.horizontalP.addWidget(self.titulo1)
        self.horizontalP.addStretch()
        self.horizontalP.addWidget(self.devolver)

        self.regreso.setLayout(self.horizontalP)
        self.vertical.addWidget(self.regreso)

        self.vertical.addStretch()

        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("background-color: #8EA85D;")
        self.scrollArea.setFixedHeight(470)
        # Adaptar el scroll a diferentes escaladas
        self.scrollArea.setWidgetResizable(True)
        # Ventana contenedora para la cuadricula
        self.contenedora = QWidget()

        self.cuadricula = QGridLayout(self.contenedora)

        self.scrollArea.setWidget(self.contenedora)

        self.vertical.addWidget(self.scrollArea)

        # Establecemos el numero de elementos
        self.numeroElementos = 12

        # Creamos el contador de elementos que se muestran en el Layout
        self.contador = 0

        # Para establecer los elementos por fila
        self.elementosPorColumna = 1
        # Redondeamos al entero superior + 1, mostraremos 3 columnas por fila
        # por eso dividimos por 3
        self.numeroFilas = math.ceil(self.numeroElementos / self.elementosPorColumna) + 1

        # crear un agrupador de botones
        self.botones = QButtonGroup()
        # Definimos que ningún boton sea exclusivo
        self.botones.setExclusive(False)

        # Ciclos for para crear objetos en la cuadricula.
        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna + 1):
                # Validar el contador
                if self.contador < self.numeroElementos:
                    # En cada celda de la cuadricula se crea una ventana
                    self.ventanaAux = QWidget()

                    # Crear un layout vertical para cada elemento de la cuadricula
                    self.verticalCuadricula = QVBoxLayout()

                    self.botonAccion = QPushButton("Alerta " + str(self.contador + 1))
                    self.botonAccion.setFont(QFont("Arial", 12))
                    self.botonAccion.setStyleSheet("color: white; background-color: #9AC069;")
                    self.botonAccion.setFixedHeight(50)

                    self.verticalCuadricula.addWidget(self.botonAccion)

                    # Agregamos el boton al grupo con el contador como id
                    self.botones.addButton(self.botonAccion, self.contador + 1)

                    self.ventanaAux.setLayout(self.verticalCuadricula)
                    # a la cuadricula le agregamos la ventana en al fila y la columna actual
                    self.cuadricula.addWidget(self.ventanaAux, fila, columna)

                    # Aumentamos el contador
                    self.contador += 1

        self.botones.idClicked.connect(self.metodo_accion_boton)

        self.ventana.setLayout(self.vertical)

    def metodo_accion_boton(self, idBoton):
        self.botones.button(self.contador).setStyleSheet("color: white; background-color: #9AC069;")
        self.botones.button(idBoton).setStyleSheet("color: white; background-color: #65783E;")
        self.contador = idBoton
        print(idBoton)

    def ir_administrador(self):
        self.hide()
        self.ventanaAnterior.show()