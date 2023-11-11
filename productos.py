import math
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QToolBar, QAction, QWidget, QVBoxLayout, QLabel, \
    QGridLayout, QFormLayout, QPushButton, QHBoxLayout, QLineEdit, QScrollArea, QButtonGroup, QDialog, QDialogButtonBox, \
    QTextEdit

from productosCrear import ProductosCrear
from productosModificar import ProductosModificar

class Productos(QMainWindow):
    def __init__(self, anterior):
        super(Productos, self).__init__(anterior)
        # Se crea la ventana principal junto a sus modificaciones
        self.ventanaAnterior = anterior

        self.setWindowTitle("Productos")

        self.ancho = 1000
        self.alto = 563
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Se crea la ventana de fondo para establecer otras ventanas de forma horizontal
        self.ventana = QWidget()
        self.horizontal = QHBoxLayout()
        self.ventana.setStyleSheet("background-color: #9AC069;")
        self.setCentralWidget(self.ventana)

        # Ventana para la distribución de productos
        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("background-color: #8EA85D;")
        self.scrollArea.setWidgetResizable(True)

        self.contenedora = QWidget()
        self.cuadricula = QGridLayout(self.contenedora)
        self.scrollArea.setWidget(self.contenedora)

        self.numeroElementos = 12
        self.contador = 0
        self.elementosPorColumna = 1

        # Redondeamos al entero superior + 1, mostraremos 3 columnas por fila
        # por eso dividimos por 3
        self.numeroFilas = math.ceil(self.numeroElementos / self.elementosPorColumna) + 1

        self.ventana.setLayout(self.horizontal)

        self.botones = QButtonGroup()
        self.botones.setExclusive(False)

        # Ciclos para la creación de productos según el numero de elementos establecido
        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna + 1):
                if self.contador < self.numeroElementos:
                    # Metodo para crear una ventana cada vez que los numeros de elementos superen al contador
                    self.ventanaAux = QWidget()

                    self.verticalCuadricula = QVBoxLayout()

                    self.botonAccion = QPushButton("Producto " + str(self.contador + 1))
                    self.botonAccion.setFont(QFont("Arial", 12))
                    self.botonAccion.setStyleSheet("color: white; background-color: #9AC069;")
                    self.botonAccion.setFixedHeight(50)

                    self.verticalCuadricula.addWidget(self.botonAccion)

                    # Agregamos el boton al grupo con el contador como id
                    self.botones.addButton(self.botonAccion, self.contador + 1)

                    self.ventanaAux.setLayout(self.verticalCuadricula)
                    # a la cuadricula le agregamos la ventana en posición de la fila y la columna
                    self.cuadricula.addWidget(self.ventanaAux, fila, columna)

                    self.contador += 1
        # Se le otorga un metodo a cada producto
        self.botones.idClicked.connect(self.metodo_accion_boton)
        self.horizontal.addWidget(self.scrollArea)

        # Se crea la ventana derecha en donde se previsualizara la información de los productos
        self.ventana2 = QLabel()
        self.vertical2 = QVBoxLayout()
        self.ventana2.setFixedWidth(370)

        self.regreso = QLabel()
        self.horizontalP = QHBoxLayout()
        self.regreso.setFixedHeight(60)

        self.letreroP = QLabel()
        self.letreroP.setText("PRODUCTOS")
        self.letreroP.setFont(QFont("Arial", 30))
        self.letreroP.setStyleSheet("color: white;")

        self.horizontalP.addWidget(self.letreroP)
        self.horizontalP.addStretch()

        self.devolver = QPushButton()
        self.devolver.setFixedWidth(50)
        self.devolver.setFixedHeight(50)
        self.devolver.setStyleSheet("background-color: #8EA85D;")
        self.devolver.setIcon(QtGui.QIcon('Imagenes/iconos/casa.png'))
        self.devolver.setIconSize(QSize(40, 40))
        self.devolver.clicked.connect(self.ir_administrador)

        self.horizontalP.addWidget(self.devolver)

        self.regreso.setLayout(self.horizontalP)
        self.vertical2.addWidget(self.regreso)

        self.ventanaImg = QLabel()
        self.minihorizontal = QHBoxLayout()

        self.imagenP = QLabel()
        self.imagenP.setFixedWidth(170)
        self.imagenP.setFixedHeight(170)
        self.imagen = QPixmap("Imagenes/Imagenes Productos/arroz diana.jpg")
        self.imagenP.setPixmap(self.imagen)
        self.imagenP.setScaledContents(True)

        self.minihorizontal.addWidget(self.imagenP)

        self.ventanaImg.setLayout(self.minihorizontal)
        self.vertical2.addWidget(self.ventanaImg)

        self.ventanainfo = QLabel()
        self.formulario3 = QVBoxLayout()
        self.ventanainfo.setFixedHeight(267)
        self.ventanainfo.setStyleSheet("background-color: #8EA85D;")
        self.formulario3.setContentsMargins(10, 0, 10, 10)

        self.texto1 = QLabel("Descripción:")
        self.texto1.setAlignment(Qt.AlignCenter)
        self.texto1.setFixedHeight(40)
        self.texto1.setStyleSheet("color: white;"
                                  "border: 2px solid #9AC069;"
                                  "border-left: none;"
                                  "border-right: none;"
                                  "border-top: none;")
        self.texto1.setFont(QFont("Arial", 12))

        self.formulario3.addWidget(self.texto1)

        self.texto2 = QTextEdit()
        self.texto2.setReadOnly(True)
        self.texto2.setFixedHeight(100)
        self.texto2.setFont(QFont("Arial", 12))
        self.texto2.setStyleSheet("border: 2px solid #9AC069;"
                                  "border-left: none;"
                                  "border-right: none;"
                                  "border-top: none;")

        self.formulario3.addWidget(self.texto2)

        self.ventanaTitulos = QLabel()
        self.formulario4 = QHBoxLayout()
        self.ventanaTitulos.setFixedHeight(22)

        self.descripcionTitulo1 = QLabel("Caducidad: ")
        self.descripcionTitulo1.setFixedWidth(90)
        self.descripcionTitulo1.setFixedHeight(12)
        self.descripcionTitulo1.setStyleSheet("color: white;")
        self.descripcionTitulo1.setFont(QFont("Arial", 12))

        self.formulario4.addWidget(self.descripcionTitulo1)

        self.descripcionTitulo2 = QLabel("Cantidad: ")
        self.descripcionTitulo2.setFixedWidth(90)
        self.descripcionTitulo2.setFixedHeight(12)
        self.descripcionTitulo2.setStyleSheet("color: white;")
        self.descripcionTitulo2.setFont(QFont("Arial", 12))

        self.formulario4.addWidget(self.descripcionTitulo2)

        self.ventanaTitulos.setLayout(self.formulario4)
        self.formulario3.addWidget(self.ventanaTitulos)

        self.ventanaDatos = QLabel()
        self.formulario5 = QHBoxLayout()
        self.ventanaDatos.setFixedHeight(22)

        self.descripcionDatos1 = QLabel("05/11/2023")
        self.descripcionDatos1.setFixedWidth(90)
        self.descripcionDatos1.setFixedHeight(12)
        self.descripcionDatos1.setFont(QFont("Arial", 12))

        self.formulario5.addWidget(self.descripcionDatos1)

        self.descripcionDatos3 = QLabel("$ 22.290")
        self.descripcionDatos3.setFixedWidth(90)
        self.descripcionDatos3.setFixedHeight(12)
        self.descripcionDatos3.setFont(QFont("Arial", 12))

        self.formulario5.addWidget(self.descripcionDatos3)

        self.ventanaDatos.setLayout(self.formulario5)
        self.formulario3.addWidget(self.ventanaDatos)

        # Se crea la ventana para los botones interactuables con los productos
        self.ventanaBotones = QLabel()
        self.vertical3 = QHBoxLayout()
        self.ventanaBotones.setFixedHeight(35)

        # Botón para crear productos
        self.crear = QPushButton("Crear")
        self.crear.setFixedWidth(100)
        self.crear.setFixedHeight(27)
        self.crear.setStyleSheet("background-color: #9AC069; color: white;")
        self.crear.setFont(QFont("Arial", 12))
        self.crear.clicked.connect(self.metodo_crear_producto)

        self.vertical3.addWidget(self.crear)
        self.vertical3.addStretch()

        # Botón para modificar productos
        self.Modificar = QPushButton("Modificar")
        self.Modificar.setFixedWidth(100)
        self.Modificar.setFixedHeight(27)
        self.Modificar.setStyleSheet("background-color: #9AC069; color: white;")
        self.Modificar.setFont(QFont("Arial", 12))
        self.Modificar.clicked.connect(self.metodo_modificar_producto)

        self.vertical3.addWidget(self.Modificar)
        self.vertical3.addStretch()

        # Botón para eliminar productos
        self.eliminar = QPushButton("Eliminar")
        self.eliminar.setFixedWidth(100)
        self.eliminar.setFixedHeight(27)
        self.eliminar.setStyleSheet("background-color: #9AC069; color: white;")
        self.eliminar.setFont(QFont("Arial", 12))
        self.eliminar.clicked.connect(self.metodo_eliminar_producto)

        self.vertical3.addWidget(self.eliminar)

        self.ventanaBotones.setLayout(self.vertical3)

        self.formulario3.addStretch()
        self.formulario3.addWidget(self.ventanaBotones)

        self.ventanainfo.setLayout(self.formulario3)
        self.vertical2.addWidget(self.ventanainfo)

        self.ventana2.setLayout(self.vertical2)
        self.horizontal.addWidget(self.ventana2)
        self.ventana.setLayout(self.horizontal)

    def metodo_crear_producto(self):
        self.ir_productosCrear = ProductosCrear(self)
        self.ir_productosCrear.show()

    def metodo_modificar_producto(self):
        self.ir_productosModificar = ProductosModificar(self)
        self.ir_productosModificar.show()

    def metodo_eliminar_producto(self):
        # Ventana emergente para aceptar o negar la eliminación del producto seleccionado
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaDialogo.setWindowIcon(QtGui.QIcon("Imagenes/logo sin fondo.png"))
        self.ventanaDialogo.setFixedWidth(300)
        self.ventanaDialogo.setFixedHeight(100)
        self.ventanaDialogo.setStyleSheet("background-color: #9AC069;")
        self.ventanaDialogo.setWindowTitle("Eliminar Producto")
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        self.formularioMensaje = QFormLayout()

        self.mensaje = QLabel("Desea eliminar el producto " + " ?")
        self.mensaje.setFixedHeight(45)
        self.mensaje.setStyleSheet("color: white;")
        self.mensaje.setFont(QFont("Arial", 12))

        self.formularioMensaje.addRow(self.mensaje)
        self.eleccion = QLabel()
        self.eleccion.setFixedHeight(40)
        self.horizontal1 = QHBoxLayout()

        self.botonSi = QPushButton("Si")
        self.botonSi.setFixedWidth(80)
        self.botonSi.setFixedHeight(25)
        self.botonSi.setStyleSheet("background-color: #8EA85D; color: white;")
        self.botonSi.setFont(QFont("Arial", 12))
        self.botonSi.clicked.connect(self.funcion_eliminar)

        self.botonNo = QPushButton("No")
        self.botonNo.setFixedWidth(80)
        self.botonNo.setFixedHeight(25)
        self.botonNo.setStyleSheet("background-color: #8EA85D; color: white;")
        self.botonNo.setFont(QFont("Arial", 12))
        self.botonNo.clicked.connect(self.metodo_cerrar)

        self.horizontal1.addWidget(self.botonSi)
        self.horizontal1.addStretch()
        self.horizontal1.addWidget(self.botonNo)

        self.eleccion.setLayout(self.horizontal1)
        self.formularioMensaje.addRow(self.eleccion)

        self.ventanaDialogo.setLayout(self.formularioMensaje)

        self.ventanaDialogo.exec_()

    def funcion_eliminar(self):
        # Metodo para eliminar el producto seleccionado
        print("Eliminar")

    def metodo_accion_boton(self, idBoton):
        # Metodo para cambiar el color de los botones al ser pulsados
        self.botones.button(self.contador).setStyleSheet("color: white; background-color: #9AC069;")
        self.botones.button(idBoton).setStyleSheet("color: white; background-color: #65783E;")
        self.contador = idBoton

    def metodo_cerrar(self):
        # Metodo para cerrar las subventanas abiertas en las funciones crear, modificar y eliminar
        self.ventanaDialogo.hide()

    def ir_administrador(self):
        # Metodo para volver a la ventana administrador
        self.hide()
        self.ventanaAnterior.show()