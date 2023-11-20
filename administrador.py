from PyQt5 import QtGui
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QFont, QMovie
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QLabel, \
    QFormLayout, QPushButton, QHBoxLayout
from datetime import date

from crearUsuario import CrearUsuario
from manual import Manual
from alertas import Alertas
from productosActualizador import Actualizador
from productosLista import Lista
import calendar

class Administrador(QMainWindow):
    def __init__(self, anterior):
        super(Administrador, self).__init__(anterior)
        # Se crea la ventana principal junto a sus modificaciones
        self.ventanaAnterior = anterior
        self.actualizador = Actualizador
        self.actualizadorFiltros = 6
        self.fechaActual = date.today()
        self.calendario = calendar

        self.setWindowTitle("Administrador")

        self.ancho = 1000
        self.alto = 563
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Creamos un label vacio para usarlo como espacios y estructurar mejor los labels
        self.vacio = QLabel("")
        # Se establece una ventana de fondo para distribuir elementos en ella
        self.Principal = QWidget()
        self.vertical = QVBoxLayout()
        self.Principal.setStyleSheet("background-color: #9AC069;")
        self.setCentralWidget(self.Principal)

        # Se crea una ventana para almacenar el titulo y los botones de crear usuario o desconexión
        self.ventana = QLabel()
        self.horizontal = QHBoxLayout()
        self.ventana.setFixedHeight(60)

        # Creamos label para poner el titulo
        self.titulo1 = QLabel("ADMINISTRADOR")
        self.titulo1.setFont(QFont("Arial", 40))
        self.titulo1.setStyleSheet("color: white;")
        self.titulo1.setAlignment(Qt.AlignCenter)

        self.horizontal.addWidget(self.titulo1)
        self.horizontal.addStretch()

        # Creamos botón para ir a la ventana CrearUsuario
        self.botonCrearUsuario = QPushButton()
        self.botonCrearUsuario.setFixedWidth(50)
        self.botonCrearUsuario.setFixedHeight(50)
        self.botonCrearUsuario.setStyleSheet("background-color: #8EA85D;")
        self.botonCrearUsuario.setIcon(QtGui.QIcon('Imagenes/iconos/usuario.png'))
        self.botonCrearUsuario.setIconSize(QSize(40, 40))
        self.botonCrearUsuario.clicked.connect(self.ir_crear_usuario)

        self.horizontal.addWidget(self.botonCrearUsuario)

        # Creamos botón para desconectar la sesión
        self.botonDesconectar = QPushButton()
        self.botonDesconectar.setFixedWidth(50)
        self.botonDesconectar.setFixedHeight(50)
        self.botonDesconectar.setStyleSheet("background-color: #8EA85D;")
        self.botonDesconectar.setIcon(QtGui.QIcon('Imagenes/iconos/computador.png'))
        self.botonDesconectar.setIconSize(QSize(50, 50))
        self.botonDesconectar.clicked.connect(self.desconectar)

        self.horizontal.addWidget(self.botonDesconectar)

        self.ventana.setLayout(self.horizontal)
        self.vertical.addWidget(self.ventana)

        self.vertical.addStretch()

        # Se crea una ventana para colocar la información y botones para ir a las demás ventanas
        self.Fondo = QLabel()
        self.Horizontal = QHBoxLayout()
        self.Fondo.setStyleSheet("background-color: white;")
        self.Fondo.setFixedHeight(480)

        # Se crea una ventana para colocar la información del lado izquierdo
        self.ventanai = QLabel()
        self.Formulario = QFormLayout()
        self.ventanai.setFixedWidth(600)

        # Creamos un texto que explica cosas basicas de la aplicación
        self.explicacion = QLabel()
        self.explicacion.setFixedHeight(125)
        self.explicacion.setText("Bienvenid@ a My Caducation Inventory, desde aquí podras navegar a las diferentes\n"
                                 "pestañas, si quieres volver a este lugar dale click al botón arriba a la derecha\n"
                                 "con un icono de casa que aparece en las otras pestañas.\n\n"
                                 "Puedes crear un usuario o desconectarte con los botones que se encuentran arriba\n"
                                 "a la derecha de esta ventana.\n")
        self.explicacion.setFont(QFont("arial", 12))

        self.Formulario.addRow(self.explicacion)
        # Se agrega el label vacio del inicio para hacer un espacio con el layout formulario
        self.Formulario.addRow(self.vacio)

        # Creamos el titulo de productos
        self.Titulo2 = QLabel()
        self.Titulo2.setText("Productos: ")
        self.Titulo2.setFont(QFont("arial", 15))
        self.Titulo2.setStyleSheet("color: #9AC069;")

        # Creamos la explicación de los productos
        self.descripcion2 = QLabel("En esta pestaña encontraras todos los productos que\n"
                                   "tengas almacenados, puedes crear, eliminar, modificar,\n"
                                   "actualizar y visualizar cada producto registrado.")
        self.descripcion2.setFont(QFont("arial", 12))

        self.Formulario.addRow(self.Titulo2, self.descripcion2)
        self.Formulario.addRow(self.vacio)

        # Creamos el titulo de manual
        self.Titulo3 = QLabel()
        self.Titulo3.setText("Manual: ")
        self.Titulo3.setFont(QFont("arial", 15))
        self.Titulo3.setStyleSheet("color: #9AC069;")

        # Creamos la explicación del manual
        self.descripcion3 = QLabel("En esta pestaña encontraras el manual en dónde podras\n"
                                   "leer acerca de información adicional que te podria ayudar.")
        self.descripcion3.setFont(QFont("arial", 12))

        self.Formulario.addRow(self.Titulo3, self.descripcion3)
        self.Formulario.addRow(self.vacio)

        # Creamos el titulo de alertas
        self.Titulo4 = QLabel()
        self.Titulo4.setText("Alertas: ")
        self.Titulo4.setFont(QFont("arial", 15))
        self.Titulo4.setStyleSheet("color: #9AC069;")

        # Creamos la explicación de alertas
        self.descripcion4 = QLabel("En esta pestaña recibiras notificaciones acerca de\n"
                                   "productos que se encuentren pronto a caducar.")
        self.descripcion4.setFont(QFont("arial", 12))

        self.Formulario.addRow(self.Titulo4, self.descripcion4)
        self.Formulario.addRow(self.vacio)

        # Creamos una ventana para poner los botones al lado izquierdo y distribuirlos horizontalmente
        self.pestañas = QLabel()
        self.horizontalP = QHBoxLayout()
        self.pestañas.setFixedWidth(560)
        self.pestañas.setFixedHeight(100)
        self.pestañas.setFont(QFont("arial", 15))
        self.pestañas.setStyleSheet("color: #9AC069; border: 2px solid #9AC069;")

        # Botón para ir a productos
        self.productos = QPushButton()
        self.productos.setFixedWidth(175)
        self.productos.setFixedHeight(70)
        self.productos.setStyleSheet("background-color: #8EA85D; color: white;")
        self.productos.setIcon(QtGui.QIcon('Imagenes/iconos/Productos.png'))
        self.productos.setIconSize(QSize(150, 60))
        self.productos.clicked.connect(self.ir_productos)

        self.horizontalP.addWidget(self.productos)

        # Botón para ir a manual
        self.manual = QPushButton()
        self.manual.setFixedWidth(175)
        self.manual.setFixedHeight(70)
        self.manual.setStyleSheet("background-color: #8EA85D; color: white;")
        self.manual.setIcon(QtGui.QIcon('Imagenes/iconos/Manual.png'))
        self.manual.setIconSize(QSize(150, 60))
        self.manual.clicked.connect(self.ir_manual)

        self.horizontalP.addWidget(self.manual)

        # Botón para ir a alertas
        self.fondoAlertas = QLabel()
        self.fondoAlertas.setStyleSheet("background-color: #8EA85D; padding: 0px;")
        self.fondoAlertas.setContentsMargins(0, 0, 0, 0)
        self.imagenAlertasVacia = QMovie("Imagenes/iconos/Alertas.gif")
        self.imagenAlertasPerpetua = QMovie("Imagenes/iconos/AlertasGif.gif")
        self.fondoAlertas.setMovie(self.imagenAlertasVacia)
        self.imagenAlertasVacia.start()
        self.fondoAlertas.setFixedWidth(175)
        self.fondoAlertas.setFixedHeight(70)
        self.fondoAlertas.setScaledContents(True)
        self.verticalAlertas = QHBoxLayout()
        self.verticalAlertas.setContentsMargins(0, 0, 0, 0)

        self.Alertas = QPushButton()
        self.Alertas.setFixedWidth(175)
        self.Alertas.setFixedHeight(70)
        self.Alertas.setStyleSheet("background-color: none; color: none; border: 2px none;")
        self.Alertas.clicked.connect(self.ir_alertas)

        self.verticalAlertas.addWidget(self.Alertas)
        self.fondoAlertas.setLayout(self.verticalAlertas)

        self.horizontalP.addWidget(self.fondoAlertas)
        self.pestañas.setLayout(self.horizontalP)
        self.Formulario.addRow(self.pestañas)

        self.ventanai.setLayout(self.Formulario)
        self.Horizontal.addWidget(self.ventanai)

        # Se crea una ventana para colocar la imagen de la aplicación del lado derecho
        self.ventanad = QLabel()
        self.imagenD = QPixmap("Imagenes/logo blanco.png")
        self.ventanad.setPixmap(self.imagenD)
        self.ventanad.setScaledContents(True)
        self.ventanad.setFixedHeight(350)
        self.ventanad.setFixedWidth(350)

        self.Horizontal.addWidget(self.ventanad)
        self.vertical.addWidget(self.Fondo)
        self.Fondo.setLayout(self.Horizontal)
        self.Principal.setLayout(self.vertical)

        # Sistema para detectar productos aproximados a 10 días
        self.escanear_alertas()
        self.notificacion_alertas()

    def escanear_alertas(self):
        self.alertasCaducidad = False
        self.alertas = 0
        self.file = open('datos/productos.txt', 'rb')
        self.usuarios = []

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
            self.usuarios.append(self.u)
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

            if (self.alertasCaducidad == True):
                self.alertas += 1
        self.file.close()

    def notificacion_alertas(self):
        if self.alertas >= 1:
            self.fondoAlertas.setMovie(self.imagenAlertasPerpetua)
            self.imagenAlertasPerpetua.start()
            self.imagenAlertasVacia.stop()
        if self.alertas == 0:
            self.fondoAlertas.setMovie(self.imagenAlertasVacia)
            self.imagenAlertasVacia.start()
            self.imagenAlertasPerpetua.stop()
    def ir_productos(self):
        # Metodo para ir a la ventana productos
        self.hide()
        self.actualizador.actualizar(self)

    def ir_manual(self):
        # Metodo para ir a la ventana manual
        self.ver_manual = Manual(self)
        self.hide()
        self.ver_manual.show()

    def ir_alertas(self):
        # Metodo para ir a la ventana alertas
        self.ver_alertas = Alertas(self)
        self.hide()
        self.ver_alertas.show()

    def ir_crear_usuario(self):
        # Metodo para ir a la ventana crear usuario
        self.crear_usuario = CrearUsuario(self)
        self.hide()
        self.crear_usuario.show()

    def desconectar(self):
        # Metodo para cerar la sesion
        self.hide()
        self.ventanaAnterior.show()