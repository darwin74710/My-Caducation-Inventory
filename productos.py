import math
import sys
import time

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QToolBar, QAction, QWidget, QVBoxLayout, QLabel, \
    QGridLayout, QFormLayout, QPushButton, QHBoxLayout, QLineEdit, QScrollArea, QButtonGroup, QDialog, QDialogButtonBox, \
    QTextEdit, QComboBox

from productosCrear import ProductosCrear
from productosModificar import ProductosModificar
from productosEliminar import ProductosEliminar
from productosLista import Lista

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

        # Ventana para la distribución de productos mas los filtros
        self.ventanaListaProductos = QLabel()
        self.verticalProductos = QVBoxLayout()

        self.filtros = QLabel()
        self.horizontalFiltros = QHBoxLayout()
        self.filtros.setFixedHeight(30)
        self.filtros.setStyleSheet("background-color: #9AC069;")

        self.tituloListaProductos = QLabel("LISTA DE PRODUCTOS")
        self.tituloListaProductos.setFont(QFont("Arial", 12))
        self.tituloListaProductos.setStyleSheet("color: white;")
        self.horizontalFiltros.addWidget(self.tituloListaProductos)
        self.horizontalFiltros.addStretch()

        self.tituloFiltros = QLabel("Filtros: ")
        self.tituloFiltros.setFont(QFont("Arial", 12))
        self.tituloFiltros.setStyleSheet("color: white;")
        self.horizontalFiltros.addWidget(self.tituloFiltros)

        self.filtro = QComboBox()
        self.filtro.setFixedHeight(20)
        self.filtro.setStyleSheet("background-color: white;")
        self.filtro.setFont(QFont("Arial", 12))
        self.filtro.addItems(["Todos", "Granos", "Enlatados", "Parva", "Lacteos", "Carnicos", "Pescados"])
        self.horizontalFiltros.addWidget(self.filtro)

        self.actualizarFiltros = QPushButton()
        self.actualizarFiltros.setFixedWidth(20)
        self.actualizarFiltros.setFixedHeight(20)
        self.actualizarFiltros.clicked.connect(self.ordenar_productos_lista)
        self.horizontalFiltros.addWidget(self.actualizarFiltros)

        self.filtros.setLayout(self.horizontalFiltros)
        self.verticalProductos.addWidget(self.filtros)

        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("background-color: #8EA85D;")
        self.scrollArea.setWidgetResizable(True)

        self.contenedora = QWidget()
        self.cuadricula = QGridLayout(self.contenedora)
        self.cuadricula.setAlignment(Qt.AlignTop)
        self.scrollArea.setWidget(self.contenedora)

        self.verticalProductos.addWidget(self.scrollArea)
        self.ventanaListaProductos.setLayout(self.verticalProductos)
        self.horizontal.addWidget(self.ventanaListaProductos)

        self.ordenar_productos_lista()

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

        self.imagenFiltro = QLabel()
        self.imagenFiltro.setFixedWidth(170)
        self.imagenFiltro.setFixedHeight(170)
        self.imagenFiltro.setScaledContents(True)
        self.imagenVacia = QPixmap("Imagenes/Imagenes Productos/vacio.png")
        self.imagenGranos = QPixmap("Imagenes/Imagenes Productos/granos.png")
        self.imagenEnlatados = QPixmap("Imagenes/Imagenes Productos/enlatados.png")
        self.imagenParva = QPixmap("Imagenes/Imagenes Productos/parva.png")
        self.imagenLacteos = QPixmap("Imagenes/Imagenes Productos/lacteos.png")
        self.imagenCarnicos = QPixmap("Imagenes/Imagenes Productos/carnicos.png")
        self.imagenPescados = QPixmap("Imagenes/Imagenes Productos/pescados.png")

        self.minihorizontal.addWidget(self.imagenFiltro)

        self.ventanaImg.setLayout(self.minihorizontal)
        self.vertical2.addWidget(self.ventanaImg)

        self.ventanainfo = QLabel()
        self.verticalInfo = QVBoxLayout()
        self.ventanainfo.setFixedHeight(267)
        self.ventanainfo.setStyleSheet("background-color: #8EA85D;")
        self.verticalInfo.setContentsMargins(10, 0, 10, 10)

        self.textoNombre = QLabel()
        self.textoNombre.setAlignment(Qt.AlignCenter)
        self.textoNombre.setFixedHeight(40)
        self.textoNombre.setStyleSheet("color: white;"
                                  "border: 2px solid #9AC069;"
                                  "border-left: none;"
                                  "border-right: none;"
                                  "border-top: none;")
        self.textoNombre.setFont(QFont("Arial", 12))

        self.verticalInfo.addWidget(self.textoNombre)

        self.textoDescripcion = QTextEdit()
        self.textoDescripcion.setReadOnly(True)
        self.textoDescripcion.setFixedHeight(100)
        self.textoDescripcion.setFont(QFont("Arial", 12))
        self.textoDescripcion.setStyleSheet("border: 2px solid #9AC069;"
                                  "border-left: none;"
                                  "border-right: none;"
                                  "border-top: none;")

        self.verticalInfo.addWidget(self.textoDescripcion)

        self.ventanaTitulos = QLabel()
        self.horizontalTitulos = QHBoxLayout()
        self.ventanaTitulos.setFixedHeight(22)

        self.caducidadTitulo = QLabel("Caducidad: ")
        self.caducidadTitulo.setFixedWidth(90)
        self.caducidadTitulo.setFixedHeight(12)
        self.caducidadTitulo.setStyleSheet("color: white;")
        self.caducidadTitulo.setFont(QFont("Arial", 12))

        self.horizontalTitulos.addWidget(self.caducidadTitulo)

        self.cantidadTitulo = QLabel("Cantidad: ")
        self.cantidadTitulo.setFixedWidth(90)
        self.cantidadTitulo.setFixedHeight(12)
        self.cantidadTitulo.setStyleSheet("color: white;")
        self.cantidadTitulo.setFont(QFont("Arial", 12))

        self.horizontalTitulos.addWidget(self.cantidadTitulo)

        self.ventanaTitulos.setLayout(self.horizontalTitulos)
        self.verticalInfo.addWidget(self.ventanaTitulos)

        self.ventanaDatos = QLabel()
        self.horizontalDatos = QHBoxLayout()
        self.ventanaDatos.setFixedHeight(22)

        self.caducidad = QLabel()
        self.caducidad.setFixedWidth(90)
        self.caducidad.setFixedHeight(12)
        self.caducidad.setFont(QFont("Arial", 12))

        self.horizontalDatos.addWidget(self.caducidad)

        self.cantidad = QLabel()
        self.cantidad.setFixedWidth(90)
        self.cantidad.setFixedHeight(12)
        self.cantidad.setFont(QFont("Arial", 12))

        self.horizontalDatos.addWidget(self.cantidad)

        self.ventanaDatos.setLayout(self.horizontalDatos)
        self.verticalInfo.addWidget(self.ventanaDatos)

        # Se crea la ventana para los botones interactuables con los productos
        self.ventanaBotones = QLabel()
        self.horizontalBotones = QHBoxLayout()
        self.ventanaBotones.setFixedHeight(35)

        # Botón para crear productos
        self.crear = QPushButton("Crear")
        self.crear.setFixedWidth(85)
        self.crear.setFixedHeight(27)
        self.crear.setStyleSheet("background-color: #9AC069; color: white;")
        self.crear.setFont(QFont("Arial", 12))
        self.crear.clicked.connect(self.metodo_crear_producto)

        self.horizontalBotones.addWidget(self.crear)
        self.horizontalBotones.addStretch()

        # Botón para modificar productos
        self.Modificar = QPushButton("Modificar")
        self.Modificar.setFixedWidth(85)
        self.Modificar.setFixedHeight(27)
        self.Modificar.setStyleSheet("background-color: #9AC069; color: white;")
        self.Modificar.setFont(QFont("Arial", 12))
        self.Modificar.clicked.connect(self.metodo_modificar_producto)

        self.horizontalBotones.addWidget(self.Modificar)
        self.horizontalBotones.addStretch()

        # Botón para eliminar productos
        self.eliminar = QPushButton("Eliminar")
        self.eliminar.setFixedWidth(85)
        self.eliminar.setFixedHeight(27)
        self.eliminar.setStyleSheet("background-color: #9AC069; color: white;")
        self.eliminar.setFont(QFont("Arial", 12))
        self.eliminar.clicked.connect(self.metodo_eliminar_producto)

        self.horizontalBotones.addWidget(self.eliminar)

        self.ventanaBotones.setLayout(self.horizontalBotones)

        self.verticalInfo.addStretch()
        self.verticalInfo.addWidget(self.ventanaBotones)

        self.ventanainfo.setLayout(self.verticalInfo)
        self.vertical2.addWidget(self.ventanainfo)

        self.ventana2.setLayout(self.vertical2)
        self.horizontal.addWidget(self.ventana2)
        self.ventana.setLayout(self.horizontal)

        self.idPosicion = 0

        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaDialogo.setWindowIcon(QtGui.QIcon("Imagenes/logo sin fondo.png"))
        self.ventanaDialogo.setFixedWidth(300)
        self.ventanaDialogo.setFixedHeight(100)
        self.ventanaDialogo.setStyleSheet("background-color: #9AC069;")
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

    def ordenar_productos_lista(self):
        if self.filtro.currentIndex() == 0:

            self.file = open('datos/productos.txt', 'rb')
            self.usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                self.idPosicion = len(self.usuarios) + 1
                lista = linea.split(";")
                if linea == '':
                    break
                self.u = Lista(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8]
                )
                self.usuarios.append(self.u)
                self.u.idPosicion = self.idPosicion

                self.file2 = open('datos/productos.txt', 'wb')
                for self.u in self.usuarios:
                    self.file2.write(bytes(str(self.u.idPosicion) + ";"
                                           + self.u.identificadorFiltro + ";"
                                           + self.u.nombre + ";"
                                           + self.u.descripcion + ";"
                                           + self.u.numeroDia + ";"
                                           + self.u.numeroMes + ";"
                                           + self.u.numeroAno + ";"
                                           + self.u.numeroCantidad + ";"
                                           + self.u.espacio, encoding='UTF-8'))
                self.file2.close()
            self.file.close()

            self.numeroProductos = len(self.usuarios)
            self.contador = 0
            self.elementosPorColumna = 1

            self.numeroFilas = math.ceil(self.numeroProductos / self.elementosPorColumna) + 1

            self.botones = QButtonGroup()
            self.botones.setExclusive(True)

            for fila in range(1, self.numeroFilas):
                for columna in range(1, self.elementosPorColumna + 1):
                    if self.contador < self.numeroProductos:
                        self.ventanaAux = QWidget()

                        self.verticalCuadricula = QVBoxLayout()

                        self.botonAccion = QPushButton(self.usuarios[self.contador].nombre)
                        self.botonAccion.setFont(QFont("Arial", 12))
                        self.botonAccion.setStyleSheet("color: white; background-color: #9AC069;")
                        self.botonAccion.setFixedHeight(50)

                        self.verticalCuadricula.addWidget(self.botonAccion)

                        self.botones.addButton(self.botonAccion, int(self.usuarios[self.contador].idPosicion))

                        self.ventanaAux.setLayout(self.verticalCuadricula)

                        self.cuadricula.addWidget(self.ventanaAux, fila, columna)

                        self.contador += 1
            self.botones.idClicked.connect(self.metodo_accionProductos)

        if self.filtro.currentIndex() == 1:
            self.contadorGranos = 0
            self.file = open('datos/productos.txt', 'rb')
            self.usuarios = []
            self.granos = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                self.idPosicion = len(self.usuarios) + 1
                lista = linea.split(";")
                if linea == '':
                    break
                self.u = Lista(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8]
                )
                self.usuarios.append(self.u)
                self.u.idPosicion = self.idPosicion

                if self.u.identificadorFiltro == str(1):
                    self.listaGranos = Lista(
                        lista[0],
                        lista[1],
                        lista[2],
                        lista[3],
                        lista[4],
                        lista[5],
                        lista[6],
                        lista[7],
                        lista[8]
                    )
                    self.contadorGranos += 1
                    self.granos.append(self.listaGranos)
                else:
                    pass

                self.file2 = open('datos/productos.txt', 'wb')
                for self.u in self.usuarios:
                    self.file2.write(bytes(str(self.u.idPosicion) + ";"
                                           + self.u.identificadorFiltro + ";"
                                           + self.u.nombre + ";"
                                           + self.u.descripcion + ";"
                                           + self.u.numeroDia + ";"
                                           + self.u.numeroMes + ";"
                                           + self.u.numeroAno + ";"
                                           + self.u.numeroCantidad + ";"
                                           + self.u.espacio, encoding='UTF-8'))
                self.file2.close()
            self.file.close()

            self.numeroProductos = len(self.granos)
            print("numero de elementos en lista: " + str(len(self.granos)))
            self.contador = 0
            self.elementosPorColumna = 1

            self.numeroFilas = math.ceil(self.numeroProductos / self.elementosPorColumna) + 1

            self.botones = QButtonGroup()
            self.botones.setExclusive(True)

            for fila in range(1, self.numeroFilas):
                for columna in range(1, self.elementosPorColumna + 1):
                    if self.contador < self.numeroProductos:
                        self.ventanaAux = QWidget()

                        self.verticalCuadricula = QVBoxLayout()

                        self.botonAccion = QPushButton(self.granos[self.contador].nombre)
                        self.botonAccion.setFont(QFont("Arial", 12))
                        self.botonAccion.setStyleSheet("color: white; background-color: #9AC069;")
                        self.botonAccion.setFixedHeight(50)

                        self.verticalCuadricula.addWidget(self.botonAccion)

                        self.botones.addButton(self.botonAccion, int(self.usuarios[self.contador].idPosicion))

                        self.ventanaAux.setLayout(self.verticalCuadricula)

                        self.cuadricula.addWidget(self.ventanaAux, fila, columna)

                        self.contador += 1
            self.botones.idClicked.connect(self.metodo_accionProductos)
            self.ventanaAnterior.ir_productos()

    def metodo_accionProductos(self, idPosicion):
        self.botones.button(self.contador).setStyleSheet("color: white; background-color: #9AC069;")
        self.botones.button(idPosicion).setStyleSheet("color: white; background-color: #65783E;")
        self.contador = idPosicion

        self.idPosicion = idPosicion

        if self.filtro.currentIndex() == 0:
            self.file = open('datos/productos.txt', 'rb')

            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                lista = linea.split(";")
                if linea == '':
                    break
                self.u = Lista(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8]
                )
                usuarios.append(self.u)
            self.file.close()

            for self.u in usuarios:
                if int(self.u.idPosicion) == self.idPosicion:

                    if self.u.identificadorFiltro == str(0):
                        self.imagenFiltro.setPixmap(self.imagenGranos)
                    if self.u.identificadorFiltro == str(1):
                        self.imagenFiltro.setPixmap(self.imagenEnlatados)
                    if self.u.identificadorFiltro == str(2):
                        self.imagenFiltro.setPixmap(self.imagenParva)
                    if self.u.identificadorFiltro == str(3):
                        self.imagenFiltro.setPixmap(self.imagenLacteos)
                    if self.u.identificadorFiltro == str(4):
                        self.imagenFiltro.setPixmap(self.imagenCarnicos)
                    if self.u.identificadorFiltro == str(5):
                        self.imagenFiltro.setPixmap(self.imagenPescados)

                    self.textoNombre.setText(self.u.nombre)
                    self.textoDescripcion.setText(self.u.descripcion)
                    self.caducidad.setText(self.u.numeroDia + "/" + self.u.numeroMes + "/" + self.u.numeroAno)
                    self.cantidad.setText(self.u.numeroCantidad)
                    break

        if self.filtro.currentIndex() == 1:
            self.file = open('datos/productos.txt', 'rb')
            print(self.u.idPosicion)

            usuarios = []
            self.granos = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                lista = linea.split(";")
                if linea == '':
                    break
                self.u = Lista(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8]
                )
                usuarios.append(self.u)

                if self.u.identificadorFiltro == str(1):
                    self.listaGranos = Lista(
                        lista[0],
                        lista[1],
                        lista[2],
                        lista[3],
                        lista[4],
                        lista[5],
                        lista[6],
                        lista[7],
                        lista[8]
                    )
                    self.granos.append(self.listaGranos)
            self.file.close()

            for self.u in self.usuarios:
                if int(self.u.idPosicion) == self.idPosicion:

                    if self.listaGranos.identificadorFiltro == str(0):
                        self.imagenFiltro.setPixmap(self.imagenGranos)
                    if self.listaGranos.identificadorFiltro == str(1):
                        self.imagenFiltro.setPixmap(self.imagenEnlatados)
                    if self.listaGranos.identificadorFiltro == str(2):
                        self.imagenFiltro.setPixmap(self.imagenParva)
                    if self.listaGranos.identificadorFiltro == str(3):
                        self.imagenFiltro.setPixmap(self.imagenLacteos)
                    if self.listaGranos.identificadorFiltro == str(4):
                        self.imagenFiltro.setPixmap(self.imagenCarnicos)
                    if self.listaGranos.identificadorFiltro == str(5):
                        self.imagenFiltro.setPixmap(self.imagenPescados)

                    self.textoNombre.setText(self.listaGranos.nombre)
                    self.textoDescripcion.setText(self.listaGranos.descripcion)
                    self.caducidad.setText(
                    self.listaGranos.numeroDia + "/" + self.listaGranos.numeroMes + "/" + self.listaGranos.numeroAno)
                    self.cantidad.setText(self.listaGranos.numeroCantidad)
                    break

    def metodo_crear_producto(self):
        self.ir_productosCrear = ProductosCrear(self)
        self.ir_productosCrear.show()

    def metodo_modificar_producto(self):
        self.ventanaDialogo.setWindowTitle("Modificar Producto")
        if self.idPosicion <= 0:

            self.formularioValidarModificar = QFormLayout()

            self.mensaje = QLabel("Seleccione un producto.")
            self.mensaje.setFixedHeight(45)
            self.mensaje.setStyleSheet("color: white;")
            self.mensaje.setFont(QFont("Arial", 12))

            self.formularioValidarModificar.addRow(self.mensaje)

            self.eleccion = QLabel()
            self.eleccion.setFixedHeight(40)
            self.horizontalModificarOk = QHBoxLayout()

            self.botonOk = QPushButton("Ok")
            self.botonOk.setFixedWidth(80)
            self.botonOk.setFixedHeight(25)
            self.botonOk.setStyleSheet("background-color: #8EA85D; color: white;")
            self.botonOk.setFont(QFont("Arial", 12))
            self.botonOk.clicked.connect(self.metodo_cerrar)

            self.horizontalModificarOk.addStretch()
            self.horizontalModificarOk.addWidget(self.botonOk)

            self.eleccion.setLayout(self.horizontalModificarOk)
            self.formularioValidarModificar.addRow(self.eleccion)

            self.ventanaDialogo.setLayout(self.formularioValidarModificar)
            self.ventanaDialogo.exec_()

        elif int(self.u.idPosicion) == self.idPosicion:
            self.ir_productosModificar = ProductosModificar(self)
            self.ir_productosModificar.show()

    def metodo_eliminar_producto(self):
        # Ventana emergente para aceptar o negar la eliminación del producto seleccionado
        self.ventanaDialogo.setWindowTitle("Eliminar Producto")
        if self.idPosicion <= 0:

            self.formularioValidarModificar = QFormLayout()

            self.mensaje = QLabel("Seleccione un producto.")
            self.mensaje.setFixedHeight(45)
            self.mensaje.setStyleSheet("color: white;")
            self.mensaje.setFont(QFont("Arial", 12))

            self.formularioValidarModificar.addRow(self.mensaje)

            self.eleccion = QLabel()
            self.eleccion.setFixedHeight(40)
            self.horizontalModificarOk = QHBoxLayout()

            self.botonOk = QPushButton("Ok")
            self.botonOk.setFixedWidth(80)
            self.botonOk.setFixedHeight(25)
            self.botonOk.setStyleSheet("background-color: #8EA85D; color: white;")
            self.botonOk.setFont(QFont("Arial", 12))
            self.botonOk.clicked.connect(self.metodo_cerrar)

            self.horizontalModificarOk.addStretch()
            self.horizontalModificarOk.addWidget(self.botonOk)

            self.eleccion.setLayout(self.horizontalModificarOk)
            self.formularioValidarModificar.addRow(self.eleccion)

            self.ventanaDialogo.setLayout(self.formularioValidarModificar)
            self.ventanaDialogo.exec_()

        elif int(self.u.idPosicion) == self.idPosicion:
            self.ir_productosEliminar = ProductosEliminar(self)
            self.ir_productosEliminar.show()

    def metodo_cerrar(self):
        # Metodo para cerrar las subventanas abiertas en las funciones crear, modificar y eliminar
        self.ventanaDialogo.hide()

    def ir_administrador(self):
        # Metodo para volver a la ventana administrador
        self.hide()
        self.ventanaAnterior.show()

    def limpiar(self):
        self.idPosicion = 0
        self.imagenFiltro.setPixmap(self.imagenVacia)
        self.textoNombre.setText("")
        self.textoDescripcion.setText("")
        self.caducidad.setText("")
        self.cantidad.setText("")