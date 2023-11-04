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

        self.instrucciones()

        self.barraHerramientas = QToolBar("Barra de Herramientas")
        self.barraHerramientas.setStyleSheet("color: white; background-color: #8EA85D;")
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
            self.instrucciones()

        if opcion.text() == "Productos":
            self.lista_productos()

        if opcion.text() == "Manual":
            self.mostrar_manual()

        if opcion.text() == "Alertas":
            self.mostrar_alertas()

        if opcion.text() == "Desconexión":
            self.hide()
            self.ventanaAnterior.show()

    def instrucciones(self):
        self.ventana = QWidget()
        self.ventana.setStyleSheet("background-color: #9AC069;")
        self.setCentralWidget(self.ventana)
        self.vertical = QVBoxLayout()
        self.vacio = QLabel("")

        self.titulo1 = QLabel("Instrucciones")
        self.titulo1.setFont(QFont("Arial", 40))
        self.titulo1.setStyleSheet("color: white;")
        self.titulo1.setAlignment(Qt.AlignCenter)

        self.vertical.addWidget(self.titulo1)

        self.vertical.addStretch()

        self.Fondo = QLabel()
        self.Fondo.setStyleSheet("background-color: white;")
        self.Fondo.setFixedHeight(450)

        self.Horizontal = QHBoxLayout()

        self.ventanai = QLabel()
        self.ventanai.setFixedWidth(600)

        self.Formulario = QFormLayout()

        self.Titulo1 = QLabel()
        self.Titulo1.setText("Instrucciones: ")
        self.Titulo1.setFont(QFont("arial", 15))
        self.Titulo1.setStyleSheet("color: #9AC069;")

        self.descripcion1 = QLabel("En esta pestaña encontraras todas las instrucciones\n"
                                   "de la aplicación.")
        self.descripcion1.setFont(QFont("arial", 12))

        self.Formulario.addRow(self.Titulo1, self.descripcion1)

        self.Formulario.addRow(self.vacio)

        self.Titulo2 = QLabel()
        self.Titulo2.setText("Productos: ")
        self.Titulo2.setFont(QFont("arial", 15))
        self.Titulo2.setStyleSheet("color: #9AC069;")

        self.descripcion2 = QLabel("En esta pestaña encontraras todos los productos que\n"
                                   "tengas almacenados, puedes crear, eliminar, modificar,\n"
                                   "actualizar y visualizar cada producto registrado.")
        self.descripcion2.setFont(QFont("arial", 12))

        self.Formulario.addRow(self.Titulo2, self.descripcion2)

        self.Formulario.addRow(self.vacio)

        self.Titulo3 = QLabel()
        self.Titulo3.setText("Manual: ")
        self.Titulo3.setFont(QFont("arial", 15))
        self.Titulo3.setStyleSheet("color: #9AC069;")

        self.descripcion3 = QLabel("En esta pestaña encontraras el manual en dónde podras\n"
                                   "leer acerca de información adicional que te podria ayudar.")
        self.descripcion3.setFont(QFont("arial", 12))

        self.Formulario.addRow(self.Titulo3, self.descripcion3)

        self.Formulario.addRow(self.vacio)

        self.Titulo4 = QLabel()
        self.Titulo4.setText("Alertas: ")
        self.Titulo4.setFont(QFont("arial", 15))
        self.Titulo4.setStyleSheet("color: #9AC069;")

        self.descripcion4 = QLabel("En esta pestaña recibiras notificaciones acerca de\n"
                                   "productos que se encuentren pronto a caducar.")
        self.descripcion4.setFont(QFont("arial", 12))

        self.Formulario.addRow(self.Titulo4, self.descripcion4)

        self.Formulario.addRow(self.vacio)

        self.Titulo5 = QLabel()
        self.Titulo5.setText("Desconexión: ")
        self.Titulo5.setFont(QFont("arial", 15))
        self.Titulo5.setStyleSheet("color: #9AC069;")

        self.descripcion5 = QLabel("Este es el botón para cerrar la sesión.")
        self.descripcion5.setFont(QFont("arial", 12))

        self.Formulario.addRow(self.Titulo5, self.descripcion5)

        self.Formulario.addRow(self.vacio)

        self.datoextra = QLabel()
        self.datoextra.setFixedWidth(560)
        self.datoextra.setText("\nEn la parte superior de la aplicación podras encontrar botones\n"
                               "para navegar en las diferentes pestañas.\n")
        self.datoextra.setFont(QFont("arial", 15))
        self.datoextra.setStyleSheet("color: #9AC069; border: 2px solid #9AC069;")

        self.Formulario.addRow(self.datoextra)


        self.ventanai.setLayout(self.Formulario)

        self.Horizontal.addWidget(self.ventanai)

        self.ventanad = QLabel()
        self.imagenD = QPixmap("Imagenes/logo blanco.png")
        self.ventanad.setPixmap(self.imagenD)
        self.ventanad.setScaledContents(True)
        self.ventanad.setFixedHeight(350)
        self.ventanad.setFixedWidth(350)

        self.Horizontal.addWidget(self.ventanad)

        self.vertical.addWidget(self.Fondo)

        self.Fondo.setLayout(self.Horizontal)
        self.ventana.setLayout(self.vertical)

    def lista_productos(self):

        self.ventana = QWidget()
        self.ventana.setStyleSheet("background-color: #9AC069;")
        self.setCentralWidget(self.ventana)
        self.horizontal = QHBoxLayout()

        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("background-color: #8EA85D;")
        # Adaptar el scroll a diferentes escaladas
        self.scrollArea.setWidgetResizable(True)
        # Ventana contenedora para la cuadricula
        self.contenedora = QWidget()


        self.cuadricula = QGridLayout(self.contenedora)

        self.scrollArea.setWidget(self.contenedora)

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

        self.horizontal.addWidget(self.scrollArea)

        #Aquí comienza
        self.ventana2 = QLabel()
        self.ventana2.setStyleSheet("background-color: #8EA85D;")
        self.ventana2.setFixedWidth(370)
        self.formulario3 = QFormLayout()
        self.formulario3.setContentsMargins(10, 0, 10, 0)
        self.formulario3.setVerticalSpacing(17)

        self.letreroP = QLabel()
        self.letreroP.setText("Productos")
        self.letreroP.setFont(QFont("Arial", 40))
        self.letreroP.setAlignment(Qt.AlignCenter)
        self.letreroP.setFixedWidth(350)
        self.letreroP.setFixedHeight(70)
        self.letreroP.setStyleSheet("color: white;")
        self.formulario3.addRow(self.letreroP)

        self.imagenP = QLabel()
        self.espacio1 = QLabel("")
        self.espacio1.setFixedWidth(61)
        self.imagenP.setFixedWidth(170)
        self.imagenP.setFixedHeight(170)
        self.imagen = QPixmap("Imagenes/Imagenes Productos/arroz diana.jpg")
        self.imagenP.setPixmap(self.imagen)
        self.imagenP.setScaledContents(True)

        self.formulario3.addRow(self.espacio1, self.imagenP)

        self.texto1 = QLabel("Descripción: ")
        self.texto1.setStyleSheet("color: white;")
        self.texto1.setFont(QFont("Arial", 12))

        self.texto2 = QLabel("Arroz Diana de 5000g\n"
                             "excelente fuente de\n"
                             "vitaminas y minerales\n"
                             "como niacina, vitaminda D,\n"
                             "calcio, fibra, hierro,\n"
                             "tiamina y riboflavina.")
        self.texto2.setFont(QFont("Arial", 12))

        self.formulario3.addRow(self.texto1, self.texto2)

        self.texto3 = QLabel("Caducidad: ")
        self.texto3.setStyleSheet("color: white;")
        self.texto3.setFont(QFont("Arial", 12))

        self.texto4 = QLabel("17/11/2023")
        self.texto4.setFont(QFont("Arial", 12))

        self.formulario3.addRow(self.texto3, self.texto4)

        self.texto5 = QLabel("Cantidad: ")
        self.texto5.setStyleSheet("color: white;")
        self.texto5.setFont(QFont("Arial", 12))

        self.texto6 = QLabel("23 Unidades")
        self.texto6.setFont(QFont("Arial", 12))

        self.formulario3.addRow(self.texto5, self.texto6)

        self.texto7 = QLabel("Precio: ")
        self.texto7.setStyleSheet("color: white;")
        self.texto7.setFont(QFont("Arial", 12))

        self.texto8 = QLabel("$ 22.290")
        self.texto8.setFont(QFont("Arial", 12))

        self.formulario3.addRow(self.texto7, self.texto8)


        self.ventana2.setLayout(self.formulario3)
        self.horizontal.addWidget(self.ventana2)

        self.ventana.setLayout(self.horizontal)

    def mostrar_manual(self):
        self.ventana = QWidget()
        self.ventana.setStyleSheet("background-color: #9AC069;")
        self.setCentralWidget(self.ventana)
        self.horizontal = QVBoxLayout()

        self.titulo1 = QLabel("Manual")
        self.titulo1.setFont(QFont("Arial", 40))
        self.titulo1.setStyleSheet("color: white;")
        self.titulo1.setAlignment(Qt.AlignCenter)

        self.horizontal.addWidget(self.titulo1)

        self.horizontal.addStretch()

        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("background-color: #8EA85D;")
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

        self.ventana.setLayout(self.horizontal)

    def mostrar_alertas(self):
        self.ventana = QWidget()
        self.ventana.setStyleSheet("background-color: #9AC069;")
        self.setCentralWidget(self.ventana)
        self.horizontal = QVBoxLayout()

        self.titulo1 = QLabel("Alertas")
        self.titulo1.setStyleSheet("color: white;")
        self.titulo1.setFont(QFont("Arial", 40))
        self.titulo1.setAlignment(Qt.AlignCenter)

        self.horizontal.addWidget(self.titulo1)

        self.horizontal.addStretch()

        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("background-color: #8EA85D;")
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

        self.ventana.setLayout(self.horizontal)

    def metodo_accion_boton(self, idBoton):
        self.botones.button(self.contador).setStyleSheet("color: white; background-color: #9AC069;")
        self.botones.button(idBoton).setStyleSheet("color: white; background-color: #65783E;")
        self.contador = idBoton
