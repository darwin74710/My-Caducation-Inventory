import math
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QLabel, \
    QGridLayout, QFormLayout, QPushButton, QHBoxLayout, QScrollArea, QButtonGroup, QDialog, \
    QTextEdit, QComboBox
from datetime import date
import calendar

from productosCrear import ProductosCrear
from productosModificar import ProductosModificar
from productosEliminar import ProductosEliminar
from productosLista import Lista

class Productos(QMainWindow):
    def __init__(self, anterior):
        super(Productos, self).__init__(anterior)
        # Se crea la ventana principal junto a sus modificaciones
        self.ventanaAnterior = anterior
        self.esAdministrador = anterior.esAdministrador

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

        self.fechaActual = date.today()
        self.calendario = calendar

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
        self.ventana.setStyleSheet("background-color: " + self.colorFondo1 + ";")
        self.setCentralWidget(self.ventana)

        # Ventana para la distribución de productos mas los filtros
        self.ventanaListaProductos = QLabel()
        self.verticalProductos = QVBoxLayout()

        self.filtros = QLabel()
        self.horizontalFiltros = QHBoxLayout()
        self.filtros.setFixedHeight(30)

        self.tituloListaProductos = QLabel("LISTA DE PRODUCTOS")
        self.tituloListaProductos.setFont(QFont("Arial", 12))
        self.tituloListaProductos.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.horizontalFiltros.addWidget(self.tituloListaProductos)
        self.horizontalFiltros.addStretch()

        self.tituloFiltros = QLabel("Filtros: ")
        self.tituloFiltros.setFont(QFont("Arial", 12))
        self.tituloFiltros.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.horizontalFiltros.addWidget(self.tituloFiltros)

        self.filtro = QComboBox()
        self.filtro.setFixedHeight(20)
        self.filtro.setStyleSheet("background-color: white;")
        self.filtro.setFont(QFont("Arial", 12))
        self.filtro.addItems(["Granos", "Enlatados", "Lacteos", "Carnicos", "Pescados", "Otros", "Todos", "Caducados"])
        self.horizontalFiltros.addWidget(self.filtro)

        self.filtros.setLayout(self.horizontalFiltros)
        self.verticalProductos.addWidget(self.filtros)

        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("background-color: " + self.colorFondo2 + "; border: none;")
        self.scrollArea.setWidgetResizable(True)

        self.contenedora = QWidget()
        self.cuadricula = QGridLayout(self.contenedora)
        self.cuadricula.setAlignment(Qt.AlignTop)
        self.scrollArea.setWidget(self.contenedora)

        self.verticalProductos.addWidget(self.scrollArea)
        self.ventanaListaProductos.setLayout(self.verticalProductos)
        self.horizontal.addWidget(self.ventanaListaProductos)

        self.filtro.setCurrentIndex(self.ventanaAnterior.actualizadorFiltros)
        self.filtro.currentIndexChanged.connect(self.metodo_actualizarFiltros)
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
        self.letreroP.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.horizontalP.addWidget(self.letreroP)
        self.horizontalP.addStretch()

        self.devolver = QPushButton()
        self.devolver.setFixedWidth(50)
        self.devolver.setFixedHeight(50)
        self.devolver.setStyleSheet("background-color: " + self.colorBotones1 + ";")
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
        self.imagenLacteos = QPixmap("Imagenes/Imagenes Productos/lacteos.png")
        self.imagenCarnicos = QPixmap("Imagenes/Imagenes Productos/carnicos.png")
        self.imagenPescados = QPixmap("Imagenes/Imagenes Productos/pescados.png")
        self.imagenOtros = QPixmap("Imagenes/Imagenes Productos/otros.png")
        self.imagenCaducados = QPixmap("Imagenes/Imagenes Productos/caducados.png")

        self.minihorizontal.addWidget(self.imagenFiltro)

        self.ventanaImg.setLayout(self.minihorizontal)
        self.vertical2.addWidget(self.ventanaImg)

        self.ventanainfo = QLabel()
        self.verticalInfo = QVBoxLayout()
        self.ventanainfo.setFixedHeight(267)
        self.ventanainfo.setStyleSheet("background-color: " + self.colorFondo2 + ";")
        self.verticalInfo.setContentsMargins(10, 0, 10, 10)

        self.textoNombre = QLabel()
        self.textoNombre.setAlignment(Qt.AlignCenter)
        self.textoNombre.setFixedHeight(40)
        self.textoNombre.setStyleSheet("color: " + self.colorLetra1 + ";"
                                  "border: 2px solid " + self.colorLetra3 + ";"
                                  "border-left: none;"
                                  "border-right: none;"
                                  "border-top: none;")
        self.textoNombre.setFont(QFont("Arial", 12))

        self.verticalInfo.addWidget(self.textoNombre)

        self.textoDescripcion = QTextEdit()
        self.textoDescripcion.setReadOnly(True)
        self.textoDescripcion.setContextMenuPolicy(Qt.NoContextMenu)
        self.textoDescripcion.setFixedHeight(100)
        self.textoDescripcion.setFont(QFont("Arial", 12))
        self.textoDescripcion.setStyleSheet("color: " + self.colorLetra1 + ";"
                                  "border: 2px solid " + self.colorLetra3 + ";"
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
        self.caducidadTitulo.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.caducidadTitulo.setFont(QFont("Arial", 12))

        self.horizontalTitulos.addWidget(self.caducidadTitulo)

        self.cantidadTitulo = QLabel("Cantidad: ")
        self.cantidadTitulo.setFixedWidth(90)
        self.cantidadTitulo.setFixedHeight(12)
        self.cantidadTitulo.setStyleSheet("color: " + self.colorLetra1 + ";")
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
        self.caducidad.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.caducidad.setFont(QFont("Arial", 12))

        self.horizontalDatos.addWidget(self.caducidad)

        self.cantidad = QLabel()
        self.cantidad.setFixedWidth(90)
        self.cantidad.setFixedHeight(12)
        self.cantidad.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.cantidad.setFont(QFont("Arial", 12))

        self.horizontalDatos.addWidget(self.cantidad)

        self.ventanaDatos.setLayout(self.horizontalDatos)
        self.verticalInfo.addWidget(self.ventanaDatos)

        # Se crea la ventana para los botones interactuables con los productos
        if self.esAdministrador == True:
            self.ventanaBotones = QLabel()
            self.horizontalBotones = QHBoxLayout()
            self.ventanaBotones.setFixedHeight(35)

            # Botón para crear productos
            self.crear = QPushButton("Crear")
            self.crear.setFixedWidth(85)
            self.crear.setFixedHeight(27)
            self.crear.setStyleSheet("background-color: " + self.colorBotones2 + "; color: white;")
            self.crear.setFont(QFont("Arial", 12))
            self.crear.clicked.connect(self.metodo_crear_producto)

            self.horizontalBotones.addWidget(self.crear)
            self.horizontalBotones.addStretch()

            # Botón para modificar productos
            self.Modificar = QPushButton("Modificar")
            self.Modificar.setFixedWidth(85)
            self.Modificar.setFixedHeight(27)
            self.Modificar.setStyleSheet("background-color: " + self.colorBotones2 + "; color: white;")
            self.Modificar.setFont(QFont("Arial", 12))
            self.Modificar.clicked.connect(self.metodo_modificar_producto)

            self.horizontalBotones.addWidget(self.Modificar)
            self.horizontalBotones.addStretch()

            # Botón para eliminar productos
            self.eliminar = QPushButton("Eliminar")
            self.eliminar.setFixedWidth(85)
            self.eliminar.setFixedHeight(27)
            self.eliminar.setStyleSheet("background-color: " + self.colorBotones2 + "; color: white;")
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
        self.ventanaDialogo.setWindowIcon(QtGui.QIcon("Imagenes/" + self.colorLogo))
        self.ventanaDialogo.setFixedWidth(300)
        self.ventanaDialogo.setFixedHeight(80)
        self.ventanaDialogo.setStyleSheet("background-color: " + self.colorFondo1 + ";")
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        self.formularioValidarModificar = QFormLayout()

        self.mensaje = QLabel()
        self.mensaje.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.mensaje.setFont(QFont("Arial", 12))

        self.formularioValidarModificar.addRow(self.mensaje)

        self.eleccion = QLabel()
        self.eleccion.setFixedHeight(40)
        self.horizontalModificarOk = QHBoxLayout()

        self.botonOk = QPushButton("Ok")
        self.botonOk.setFixedWidth(80)
        self.botonOk.setFixedHeight(25)
        self.botonOk.setStyleSheet("background-color: " + self.colorBotones1 + "; color: white;")
        self.botonOk.setFont(QFont("Arial", 12))
        self.botonOk.clicked.connect(self.metodo_cerrar)

        self.horizontalModificarOk.addStretch()
        self.horizontalModificarOk.addWidget(self.botonOk)

        self.eleccion.setLayout(self.horizontalModificarOk)
        self.formularioValidarModificar.addRow(self.eleccion)

        self.ventanaDialogo.setLayout(self.formularioValidarModificar)

    def ordenar_productos_lista(self):
        self.ventanaAnterior.actualizadorFiltros = int(self.filtro.currentIndex())

        self.diaActual = int(self.fechaActual.day)
        self.mesActual = int(self.fechaActual.month)
        self.anoActual = int(self.fechaActual.year)
        if self.filtro.currentIndex() == 6:
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

                if int(self.u.numeroAno) < int(self.anoActual):
                    self.u.identificadorFiltro = str(7)
                elif (int(self.u.numeroAno) == int(self.anoActual)) and (int(self.u.numeroMes) < int(self.mesActual)):
                    self.u.identificadorFiltro = str(7)
                elif (int(self.u.numeroAno) == int(self.anoActual)) and (int(self.u.numeroMes) == int(self.mesActual)) and (int(self.u.numeroDia) <= int(self.diaActual)):
                    self.u.identificadorFiltro = str(7)

                self.file2 = open('datos/productos.txt', 'wb')
                for self.u in self.usuarios:
                    self.file2.write(bytes(self.u.nombre + ";"
                                           + str(self.u.idPosicion) + ";"
                                           + self.u.identificadorFiltro + ";"
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
                        self.botonAccion.setStyleSheet("color: white; background-color: " + self.colorBotones2 + ";")
                        self.botonAccion.setFixedHeight(50)

                        self.verticalCuadricula.addWidget(self.botonAccion)

                        self.botones.addButton(self.botonAccion, int(self.usuarios[self.contador].idPosicion))

                        self.ventanaAux.setLayout(self.verticalCuadricula)

                        self.cuadricula.addWidget(self.ventanaAux, fila, columna)

                        self.contador += 1
            self.botones.idClicked.connect(self.metodo_accionProductos)

        elif self.filtro.currentIndex() == self.ventanaAnterior.actualizadorFiltros and self.ventanaAnterior.actualizadorFiltros != 6:
            self.file = open('datos/productos.txt', 'rb')
            self.usuarios = []
            self.arrayFiltros = []

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

                if int(self.u.identificadorFiltro) == self.ventanaAnterior.actualizadorFiltros and self.ventanaAnterior.actualizadorFiltros != 6:
                    self.listaFiltros = Lista(
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
                    self.arrayFiltros.append(self.listaFiltros)
                else:
                    pass

                self.file2 = open('datos/productos.txt', 'wb')
                for self.u in self.usuarios:
                    self.file2.write(bytes(self.u.nombre + ";"
                                           + str(self.u.idPosicion) + ";"
                                           + self.u.identificadorFiltro + ";"
                                           + self.u.descripcion + ";"
                                           + self.u.numeroDia + ";"
                                           + self.u.numeroMes + ";"
                                           + self.u.numeroAno + ";"
                                           + self.u.numeroCantidad + ";"
                                           + self.u.espacio, encoding='UTF-8'))
                self.file2.close()
            self.file.close()

            self.numeroProductos = len(self.arrayFiltros)
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

                        self.botonAccion = QPushButton(self.arrayFiltros[self.contador].nombre)
                        self.botonAccion.setFont(QFont("Arial", 12))
                        self.botonAccion.setStyleSheet("color: white; background-color: " + self.colorBotones2 + ";")
                        self.botonAccion.setFixedHeight(50)

                        self.verticalCuadricula.addWidget(self.botonAccion)

                        self.botones.addButton(self.botonAccion, int(self.arrayFiltros[self.contador].idPosicion))

                        self.ventanaAux.setLayout(self.verticalCuadricula)

                        self.cuadricula.addWidget(self.ventanaAux, fila, columna)

                        self.contador += 1
            self.botones.idClicked.connect(self.metodo_accionProductos)
            self.idPosicion = 0

    def metodo_accionProductos(self, idPosicion):
        if self.idPosicion == 0:
            self.botones.button(idPosicion).setStyleSheet("color: white; background-color: " + self.colorBotones3 + ";")
        if self.idPosicion > 0:
            self.botones.button(self.idPosicion).setStyleSheet("color: white; background-color: " + self.colorBotones2 + ";")
            self.botones.button(idPosicion).setStyleSheet("color: white; background-color: " + self.colorBotones3 + ";")

        self.idPosicion = idPosicion

        if self.filtro.currentIndex() == 6:
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
                        self.imagenFiltro.setPixmap(self.imagenLacteos)
                    if self.u.identificadorFiltro == str(3):
                        self.imagenFiltro.setPixmap(self.imagenCarnicos)
                    if self.u.identificadorFiltro == str(4):
                        self.imagenFiltro.setPixmap(self.imagenPescados)
                    if self.u.identificadorFiltro == str(5):
                        self.imagenFiltro.setPixmap(self.imagenOtros)
                    if self.u.identificadorFiltro == str(7):
                        self.imagenFiltro.setPixmap(self.imagenCaducados)

                    self.textoNombre.setText(self.u.nombre)
                    self.textoDescripcion.setText(self.u.descripcion)
                    self.caducidad.setText(self.u.numeroDia + "/" + self.u.numeroMes + "/" + self.u.numeroAno)
                    self.cantidad.setText(self.u.numeroCantidad)
                    break

        elif self.filtro.currentIndex() == self.ventanaAnterior.actualizadorFiltros and self.ventanaAnterior.actualizadorFiltros != 6:
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

            for self.u in self.usuarios:
                if idPosicion == int(self.u.idPosicion):
                    if self.u.identificadorFiltro == str(0):
                        self.imagenFiltro.setPixmap(self.imagenGranos)
                    if self.u.identificadorFiltro == str(1):
                        self.imagenFiltro.setPixmap(self.imagenEnlatados)
                    if self.u.identificadorFiltro == str(2):
                        self.imagenFiltro.setPixmap(self.imagenLacteos)
                    if self.u.identificadorFiltro == str(3):
                        self.imagenFiltro.setPixmap(self.imagenCarnicos)
                    if self.u.identificadorFiltro == str(4):
                        self.imagenFiltro.setPixmap(self.imagenPescados)
                    if self.u.identificadorFiltro == str(5):
                        self.imagenFiltro.setPixmap(self.imagenOtros)
                    if self.u.identificadorFiltro == str(7):
                        self.imagenFiltro.setPixmap(self.imagenCaducados)

                    self.textoNombre.setText(self.u.nombre)
                    self.textoDescripcion.setText(self.u.descripcion)
                    self.caducidad.setText(
                    self.u.numeroDia + "/" + self.u.numeroMes + "/" + self.u.numeroAno)
                    self.cantidad.setText(self.u.numeroCantidad)
                    break

    def metodo_crear_producto(self):
        self.ir_productosCrear = ProductosCrear(self)
        self.ir_productosCrear.show()

    def metodo_modificar_producto(self):
        self.ventanaDialogo.setWindowTitle("Modificar Producto")
        if self.idPosicion <= 0:
            self.ventanaDialogo.setFixedWidth(200)

            self.mensaje.setText("Seleccione un producto.")

            self.ventanaDialogo.exec_()
        elif int(self.u.idPosicion) == self.idPosicion and int(self.u.identificadorFiltro) < 7:
            self.ir_productosModificar = ProductosModificar(self)
            self.ir_productosModificar.show()
        elif int(self.u.identificadorFiltro) == 7:
            self.ventanaDialogo.setFixedWidth(350)
            self.mensaje.setText("No puedes modificar un producto caducado.")

            self.ventanaDialogo.exec_()

    def metodo_eliminar_producto(self):
        # Ventana emergente para aceptar o negar la eliminación del producto seleccionado
        self.ventanaDialogo.setWindowTitle("Eliminar Producto")
        if self.idPosicion <= 0:
            self.ventanaDialogo.setFixedWidth(200)

            self.mensaje.setText("Seleccione un producto.")

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
        self.ventanaAnterior.escanear_alertas()
        self.ventanaAnterior.notificacion_alertas()
        self.ventanaAnterior.show()

    def limpiar(self):
        self.idPosicion = 0
        self.imagenFiltro.setPixmap(self.imagenVacia)
        self.textoNombre.setText("")
        self.textoDescripcion.setText("")
        self.caducidad.setText("")
        self.cantidad.setText("")

    def metodo_actualizarFiltros(self):
        self.ventanaAnterior.actualizadorFiltros = self.filtro.currentIndex()
        self.hide()
        self.ventanaAnterior.hide()
        self.ventanaAnterior.ir_productos()