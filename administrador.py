import math
import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QToolBar, QAction, QWidget, QVBoxLayout, QLabel, \
    QGridLayout, QFormLayout, QPushButton, QHBoxLayout, QLineEdit, QScrollArea, QButtonGroup


class Administrador(QMainWindow):
    def __init__(self, anterior):
        super(Administrador, self).__init__(anterior)

        self.ventanaAnterior = anterior

        self.setWindowTitle("Administrador")

        self.ancho = 1000
        self.alto = 563

        self.resize(self.ancho, self.alto)

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.instrucciones = QLabel()
        self.imgins = QPixmap("Imagenes/instrucciones-admin.png")
        self.instrucciones.setPixmap(self.imgins)

        #Escalamiento de las imagenes a la ventana.
        self.instrucciones.setScaledContents(True)
        self.resize(self.imgins.width(), self.imgins.height())

        self.setCentralWidget(self.instrucciones)

        self.barraHerramientas = QToolBar("Barra de Herramientas")
        self.barraHerramientas.setStyleSheet("background-color: white;")
        # Agregar la barra de herramientas
        self.addToolBar(self.barraHerramientas)

        # Crear una opción de la barra de herramientas
        self.ventana_instrucciones = QAction("Instrucciones", self)
        self.barraHerramientas.addAction(self.ventana_instrucciones)

        self.ventana_productos = QAction("Productos", self)
        self.barraHerramientas.addAction(self.ventana_productos)

        self.modificar_productos = QAction("Manual", self)
        self.barraHerramientas.addAction(self.modificar_productos)

        self.alertas = QAction("Alertas", self)
        self.barraHerramientas.addAction(self.alertas)

        self.desconexión = QAction("Desconexión", self)
        self.barraHerramientas.addAction(self.desconexión)

        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraHerramientas)


    def accion_barraHerramientas(self, opcion):

        #Validar cual opción se está pulsando.
        if opcion.text() == "Instrucciones":

            # Crear una ventana dentro de la principal.
            self.vp = QLabel()
            self.vp.setPixmap(self.imgins)

            self.vp.setScaledContents(True)
            self.resize(self.imgins.width(), self.imgins.height())

            self.setCentralWidget(self.vp)


        if opcion.text() == "Productos":
            self.lista_productos()


        if opcion.text() == "Manual":
            self.mostrar_manual()


        if opcion.text() == "Alertas":
            self.mostrar_alertas()


        if opcion.text() == "Desconexión":
            self.hide()
            self.ventanaAnterior.show()


    def lista_productos(self):

        self.ventana = QWidget()
        self.ventana.setStyleSheet("background-color: #739f6e;")
        self.setCentralWidget(self.ventana)
        self.horizontal = QHBoxLayout()

        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("background-color: #e86868;")
        # Adaptar el scroll a diferentes escaladas
        self.scrollArea.setWidgetResizable(True)
        # Ventana contenedora para la cuadricula
        self.contenedora = QWidget()


        self.cuadricula = QGridLayout(self.contenedora)

        self.scrollArea.setWidget(self.contenedora)

        self.horizontal.addWidget(self.scrollArea)

        # Establecemos el numero de elementos
        self.numeroElementos = 12

        # Creamos el contador de elementos que se muestran en el Layout
        self.contador = 0

        # Para establecer los elementos por fila
        self.elementosPorColumna = 1
        # Redondeamos al entero superior + 1, mostraremos 3 columnas por fila
        # por eso dividimos por 3
        self.numeroFilas = math.ceil(self.numeroElementos / self.elementosPorColumna) + 1

        self.ventana.setLayout(self.horizontal)

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

                    self.botonAccion = QPushButton("Arroz Diana " + str(self.contador + 1))
                    self.botonAccion.setStyleSheet("background-color: #E16262;")
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

        #Aquí comienza
        self.ventana2 = QWidget()
        self.horizontal2 = QVBoxLayout()

        self.letreroP = QLabel()
        self.letreroP.setText("PRODUCTO")
        self.letreroP.setFont(QFont("Arial", 20))
        self.letreroP.setAlignment(Qt.AlignCenter)
        self.letreroP.setFixedWidth(380)
        self.horizontal2.addWidget(self.letreroP)

        self.imagenP = QLabel("subir imagen")
        self.imagenP.setAlignment(Qt.AlignCenter)
        self.horizontal2.addWidget(self.imagenP)

        self.horizontal2.addStretch()

        self.ventanaInfo = QWidget()
        self.formulario2 = QFormLayout()
        self.ventanaInfo.setLayout(self.formulario2)

        self.texto1 = QLabel("ola")
        self.texto2 = QLabel("nospirin")
        self.formulario2.addRow(self.texto1, self.texto2)

        self.horizontal2.addWidget(self.ventanaInfo)



        self.ventana2.setLayout(self.horizontal2)
        self.horizontal.addWidget(self.ventana2)
        self.ventana.setLayout(self.horizontal)

    def mostrar_manual(self):
        self.ventana = QWidget()
        self.ventana.setStyleSheet("background-color: #739f6e;")
        self.setCentralWidget(self.ventana)
        self.horizontal = QVBoxLayout()

        self.titulo1 = QLabel("Manual")
        self.titulo1.setFont(QFont("Arial", 40))
        self.titulo1.setAlignment(Qt.AlignCenter)

        self.horizontal.addWidget(self.titulo1)

        self.horizontal.addStretch()

        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("background-color: #e86868;")
        self.scrollArea.setFixedHeight(450)
        # Adaptar el scroll a diferentes escaladas
        self.scrollArea.setWidgetResizable(True)
        # Ventana contenedora para la cuadricula
        self.contenedora = QWidget()

        self.cuadricula = QGridLayout(self.contenedora)

        self.scrollArea.setWidget(self.contenedora)

        self.horizontal.addWidget(self.scrollArea)

        # Establecemos el numero de elementos
        self.numeroElementos = 12

        # Creamos el contador de elementos que se muestran en el Layout
        self.contador = 0

        # Para establecer los elementos por fila
        self.elementosPorColumna = 1
        # Redondeamos al entero superior + 1, mostraremos 3 columnas por fila
        # por eso dividimos por 3
        self.numeroFilas = math.ceil(self.numeroElementos / self.elementosPorColumna) + 1

        self.ventana.setLayout(self.horizontal)

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

                    self.botonAccion = QPushButton("Manual número " + str(self.contador + 1))
                    self.botonAccion.setStyleSheet("background-color: #E16262;")
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

        self.ventana.setLayout(self.horizontal)

    def mostrar_alertas(self):
        self.ventana = QWidget()
        self.ventana.setStyleSheet("background-color: #739f6e;")
        self.setCentralWidget(self.ventana)
        self.horizontal = QVBoxLayout()

        self.titulo1 = QLabel("Alertas")
        self.titulo1.setFont(QFont("Arial", 40))
        self.titulo1.setAlignment(Qt.AlignCenter)

        self.horizontal.addWidget(self.titulo1)

        self.horizontal.addStretch()

        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("background-color: #e86868;")
        self.scrollArea.setFixedHeight(450)
        # Adaptar el scroll a diferentes escaladas
        self.scrollArea.setWidgetResizable(True)
        # Ventana contenedora para la cuadricula
        self.contenedora = QWidget()

        self.cuadricula = QGridLayout(self.contenedora)

        self.scrollArea.setWidget(self.contenedora)

        self.horizontal.addWidget(self.scrollArea)

        # Establecemos el numero de elementos
        self.numeroElementos = 12

        # Creamos el contador de elementos que se muestran en el Layout
        self.contador = 0

        # Para establecer los elementos por fila
        self.elementosPorColumna = 1
        # Redondeamos al entero superior + 1, mostraremos 3 columnas por fila
        # por eso dividimos por 3
        self.numeroFilas = math.ceil(self.numeroElementos / self.elementosPorColumna) + 1

        self.ventana.setLayout(self.horizontal)

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
                    self.botonAccion.setStyleSheet("background-color: #E16262;")
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

        self.ventana.setLayout(self.horizontal)

    def metodo_accion_boton(self, idBoton):
        self.botones.button(self.contador).setStyleSheet("background-color: #E16262;")
        self.botones.button(idBoton).setStyleSheet("background-color: #CA4141;")
        self.contador = idBoton


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
