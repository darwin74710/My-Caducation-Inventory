import math
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QLabel, \
    QGridLayout, QFormLayout, QPushButton, QHBoxLayout, QScrollArea, QButtonGroup, QDialog,\
    QTextEdit
from datetime import date
import calendar
from productosLista import Lista

class Alertas(QMainWindow):
    def __init__(self, anterior):
        super(Alertas, self).__init__(anterior)
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

        self.fechaActual = date.today()
        self.calendario = calendar

        self.setWindowTitle("Alertas")

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

        # Creamos la ventana para almacenar el titulo y el botón de regreso
        self.regreso = QLabel()
        self.horizontalP = QHBoxLayout()
        self.regreso.setFixedHeight(60)

        # Creamos el titulo
        self.titulo1 = QLabel("ALERTAS")
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

        # Creamos la ventana para mostrar los elementos de las alertas
        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("background-color: " + self.colorFondo2 + "; border: none;")
        self.scrollArea.setFixedHeight(470)
        self.scrollArea.setWidgetResizable(True)

        self.contenedora = QWidget()
        self.cuadricula = QGridLayout(self.contenedora)
        self.cuadricula.setAlignment(Qt.AlignTop)
        self.scrollArea.setWidget(self.contenedora)
        self.vertical.addWidget(self.scrollArea)

        self.fondo.setLayout(self.vertical)

        self.ventanaValidar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaValidar.setWindowIcon(QtGui.QIcon("Imagenes/" + self.colorLogo))
        self.ventanaValidar.setWindowTitle("Validación")
        self.ventanaValidar.setStyleSheet("background-color: " + self.colorFondo1 + ";")
        self.ventanaValidar.setWindowModality(Qt.ApplicationModal)

        self.verticalValidar = QVBoxLayout()

        self.ventanaValidar.setFixedWidth(330)
        self.ventanaValidar.setFixedHeight(500)

        self.imagenCentrada = QLabel()
        self.imagenCentrada.setFixedHeight(145)
        self.horizontalImagen = QHBoxLayout()

        self.imagenFiltro = QLabel()
        self.imagenFiltro.setFixedWidth(140)
        self.imagenFiltro.setFixedHeight(140)
        self.imagenFiltro.setScaledContents(True)
        self.imagenVacia = QPixmap("Imagenes/Imagenes Productos/vacio.png")
        self.imagenGranos = QPixmap("Imagenes/Imagenes Productos/granos.png")
        self.imagenEnlatados = QPixmap("Imagenes/Imagenes Productos/enlatados.png")
        self.imagenLacteos = QPixmap("Imagenes/Imagenes Productos/lacteos.png")
        self.imagenCarnicos = QPixmap("Imagenes/Imagenes Productos/carnicos.png")
        self.imagenPescados = QPixmap("Imagenes/Imagenes Productos/pescados.png")
        self.imagenOtros = QPixmap("Imagenes/Imagenes Productos/otros.png")
        self.imagenCaducados = QPixmap("Imagenes/Imagenes Productos/caducados.png")

        self.horizontalImagen.addStretch()
        self.horizontalImagen.addWidget(self.imagenFiltro)
        self.horizontalImagen.addStretch()

        self.imagenCentrada.setLayout(self.horizontalImagen)
        self.verticalValidar.addWidget(self.imagenCentrada)
        self.verticalValidar.addStretch()

        self.informacion = QLabel()
        self.informacion.setStyleSheet("background-color: " + self.colorFondo2 + ";")
        self.informacion.setFixedHeight(260)
        self.formularioInformacion = QFormLayout()

        self.tituloNombre = QLabel("Nombre: ")
        self.tituloNombre.setFixedHeight(30)
        self.tituloNombre.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.tituloNombre.setFont(QFont("Arial", 12))

        self.textoNombre = QLabel()
        self.textoNombre.setFixedHeight(30)
        self.textoNombre.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.textoNombre.setFont(QFont("Arial", 12))

        self.formularioInformacion.addRow(self.tituloNombre, self.textoNombre)

        self.tituloDescripcion = QLabel("Descripción: ")
        self.tituloDescripcion.setFixedHeight(30)
        self.tituloDescripcion.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.tituloDescripcion.setFont(QFont("Arial", 12))

        self.textoDescripcion = QTextEdit()
        self.textoDescripcion.setContextMenuPolicy(Qt.NoContextMenu)
        self.textoDescripcion.setReadOnly(True)
        self.textoDescripcion.setFixedHeight(100)
        self.textoDescripcion.setFont(QFont("Arial", 12))
        self.textoDescripcion.setStyleSheet("border: 2px solid " + self.colorLetra3 + "; color: " + self.colorLetra1 + ";")

        self.formularioInformacion.addRow(self.tituloDescripcion, self.textoDescripcion)

        self.tituloCaducidad = QLabel("Caducidad: ")
        self.tituloCaducidad.setFixedHeight(30)
        self.tituloCaducidad.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.tituloCaducidad.setFont(QFont("Arial", 12))

        self.caducidad = QLabel()
        self.caducidad.setFixedHeight(30)
        self.caducidad.setFont(QFont("Arial", 12))
        self.caducidad.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.formularioInformacion.addRow(self.tituloCaducidad, self.caducidad)

        self.tituloCantidad = QLabel("Cantidad: ")
        self.tituloCantidad.setFixedHeight(30)
        self.tituloCantidad.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.tituloCantidad.setFont(QFont("Arial", 12))

        self.cantidad = QLabel()
        self.cantidad.setFixedHeight(30)
        self.cantidad.setFont(QFont("Arial", 12))
        self.cantidad.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.formularioInformacion.addRow(self.tituloCantidad, self.cantidad)

        self.informacion.setLayout(self.formularioInformacion)
        self.verticalValidar.addWidget(self.informacion)

        self.fechaLimite = QLabel()
        self.fechaLimite.setFixedHeight(50)
        self.fechaLimite.setAlignment(Qt.AlignCenter)
        self.fechaLimite.setStyleSheet("background-color: " + self.colorFondo2 + "; color: " + self.colorLetra1 + ";")
        self.fechaLimite.setFont(QFont("Arial", 12))

        self.verticalValidar.addWidget(self.fechaLimite)

        self.botones = QLabel()
        self.botones.setFixedHeight(35)
        self.horizontalValidacion = QHBoxLayout()

        self.horizontalValidacion.addStretch()
        self.Ok = QPushButton("Ok")
        self.Ok.setFixedWidth(80)
        self.Ok.setFixedHeight(25)
        self.Ok.setStyleSheet("background-color: " + self.colorBotones1 + "; color: white;")
        self.Ok.setFont(QFont("Arial", 12))
        self.horizontalValidacion.addWidget(self.Ok)
        self.Ok.clicked.connect(self.metodo_cerrar_validacion)

        self.botones.setLayout(self.horizontalValidacion)
        self.verticalValidar.addWidget(self.botones)
        self.ventanaValidar.setLayout(self.verticalValidar)

        # Sistema para detectar productos aproximados a 10 días
        self.alertasCaducidad = False
        self.alertas = 0
        self.contadorAproximación = 0

        self.file = open('datos/productos.txt', 'rb')
        self.usuarios = []
        self.arrayAlertas = []
        self.posicionAproximado = []
        self.aproximado = []

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
            self.escanear_alertas()
            self.usuarios.append(self.u)
            self.u.idPosicion = self.idPosicion

            if (self.alertasCaducidad == True):
                self.listaAlertas = Lista(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8],
                )

                self.arrayAlertas.append(self.listaAlertas)
                self.listaAlertas.idPosicion = self.idPosicion
                self.posicionAproximado = [self.idPosicion, self.diaActualizado]
                self.aproximado.append(self.posicionAproximado)
                self.alertas += 1

        self.file.close()

        self.numeroElementos = len(self.arrayAlertas)
        self.contador = 0
        self.elementosPorColumna = 1

        self.cargar_alertas()

    def escanear_alertas(self):
        self.numeroDiaProducto = self.u.numeroDia
        self.numeroMesProducto = self.u.numeroMes
        self.numeroAnoProducto = self.u.numeroAno

        self.diaActual = int(self.fechaActual.day)
        self.mesActual = int(self.fechaActual.month)
        self.anoActual = int(self.fechaActual.year)

        self.ultimoDia = self.calendario.monthrange(int(self.numeroAnoProducto), int(self.numeroMesProducto))
        self.limiteDia = self.ultimoDia[1]

        self.diaActualizado = 0
        self.alertasCaducidad = False

        if ((int(self.numeroAnoProducto) == int(self.anoActual))):
            if (int(self.numeroMesProducto) == int(self.mesActual)):
                if (int(self.numeroDiaProducto) >= int(self.diaActual)):
                    if (int(self.diaActual + 10) > int(self.limiteDia)):
                        self.diaActualizado = int(self.numeroDiaProducto) - int(self.diaActual)
                        if (int(self.mesActual) == 12):
                            self.mesActual = 1
                            self.anoActual += 1
                            if (int(self.diaActualizado) <= 10):
                                self.alertasCaducidad = True
                            if (int(self.diaActualizado) == 0):
                                self.alertasCaducidad = False
                        elif (int(self.mesActual) < 12):
                            self.mesActual += 1
                            if (int(self.diaActualizado) <= 10):
                                self.alertasCaducidad = True
                            if (int(self.diaActualizado) == 0):
                                self.alertasCaducidad = False
                    elif (int(self.diaActual + 10) <= int(self.limiteDia)):
                        while (int(self.diaActual) < int(self.numeroDiaProducto)):
                            self.diaActualizado += 1
                            self.diaActual += 1
                        if (int(self.diaActualizado) <= 10):
                            self.alertasCaducidad = True
                        if (int(self.diaActualizado) == 0):
                            self.alertasCaducidad = False

            elif (int(self.numeroMesProducto) == int(self.mesActual) + 1):
                self.pasarDia = 0
                self.acumularDias = 0
                self.ultimoDia = self.calendario.monthrange(int(self.numeroAnoProducto),
                                                            int(self.numeroMesProducto) - 1)
                self.limiteDia = self.ultimoDia[1]
                self.pasarDia = int(self.limiteDia) + int(self.numeroDiaProducto) - int(self.diaActual)
                if (int(self.pasarDia) < int(self.diaActual)):
                    if (int(self.diaActual + 10) > int(self.limiteDia)):
                        if int(self.pasarDia) <= 10:
                            self.alertasCaducidad = True
                        if int(self.pasarDia) == 0:
                            self.alertasCaducidad = False
        elif int(self.numeroAnoProducto) == int(self.anoActual) + 1:
            if (int(self.mesActual) == 12):
                if (int(self.numeroMesProducto) == 1):
                    self.pasarDia = 0
                    self.acumularDias = 0
                    self.ultimoDia = self.calendario.monthrange(int(self.anoActual),
                                                                int(self.mesActual))
                    self.limiteDia = self.ultimoDia[1]
                    self.pasarDia = int(self.limiteDia) + int(self.numeroDiaProducto) - int(self.diaActual)
                    if (int(self.pasarDia) < int(self.diaActual)):
                        if (int(self.diaActual + 10) > int(self.limiteDia)):
                            if int(self.pasarDia) <= 10:
                                self.alertasCaducidad = True
                            if int(self.pasarDia) == 0:
                                self.alertasCaducidad = False

    def cargar_alertas(self):
        self.numeroFilas = math.ceil(int(self.numeroElementos) / self.elementosPorColumna) + 1

        self.botones = QButtonGroup()
        self.botones.setExclusive(False)

        # Ciclos for para crear las alertas de productos pronto a caducar
        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna + 1):
                if self.contador < self.numeroElementos:
                    # En cada celda de la cuadricula se crea una nueva alerta según el producto pronto a caducar
                    self.ventanaAux = QWidget()

                    self.verticalCuadricula = QVBoxLayout()

                    self.botonAccion = QPushButton(self.arrayAlertas[self.contador].nombre + " - " + self.arrayAlertas[self.contador].numeroDia + "/" +self.arrayAlertas[self.contador].numeroMes + "/" + self.arrayAlertas[self.contador].numeroAno)
                    self.botonAccion.setFont(QFont("Arial", 12))
                    self.botonAccion.setStyleSheet("color: white; background-color: " + self.colorBotones2 + ";")
                    self.botonAccion.setFixedHeight(50)

                    self.verticalCuadricula.addWidget(self.botonAccion)

                    # Agregamos el boton al grupo con el contador como id
                    self.botones.addButton(self.botonAccion, int(self.arrayAlertas[self.contador].idPosicion))

                    self.ventanaAux.setLayout(self.verticalCuadricula)
                    # a la cuadricula le agregamos la ventana en la posicion de la fila y la columna
                    self.cuadricula.addWidget(self.ventanaAux, fila, columna)

                    self.contador += 1

        self.botones.idClicked.connect(self.metodo_accionProductos)
        self.idPosicion = 0

    def metodo_accionProductos(self, idPosicion):
        # Metodo para cambiar los colores del botón seleccionado
        if self.idPosicion == 0:
            self.botones.button(idPosicion).setStyleSheet("color: white; background-color: " + self.colorBotones3 + ";")
        if self.idPosicion > 0:
            self.botones.button(self.idPosicion).setStyleSheet("color: white; background-color: " + self.colorBotones2 + ";")
            self.botones.button(idPosicion).setStyleSheet("color: white; background-color: " + self.colorBotones3 + ";")
        self.idPosicion = idPosicion
        if self.idPosicion == self.idPosicion:
            self.file = open('datos/productos.txt', 'rb')

            alertas = []

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
                alertas.append(self.u)
            self.file.close()

            for self.u in alertas:
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
                    self.textoNombre.setText(self.u.nombre)
                    self.textoDescripcion.setText(self.u.descripcion)
                    self.caducidad.setText(self.u.numeroDia + "/" + self.u.numeroMes + "/" + self.u.numeroAno)
                    self.cantidad.setText(self.u.numeroCantidad)
                    for self.posicionAproximado in self.aproximado:
                        if self.idPosicion == self.posicionAproximado[0]:
                            if int(self.posicionAproximado[1]) != 1:
                                self.fechaLimite.setText("Faltan " + str(self.posicionAproximado[1]) + " días para expirar.")
                            if int(self.posicionAproximado[1]) == 1:
                                self.fechaLimite.setText(
                                    "Falta " + str(self.posicionAproximado[1]) + " día para expirar.")
                    break
            self.ventanaValidar.exec_()

    def metodo_cerrar_validacion(self):
        self.ventanaValidar.hide()

    def ir_administrador(self):
        # Metodo para volver a la ventana del administrador
        self.hide()
        self.ventanaAnterior.escanear_alertas()
        self.ventanaAnterior.notificacion_alertas()
        self.ventanaAnterior.show()