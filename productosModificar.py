from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QFormLayout, QTextEdit, QVBoxLayout, QHBoxLayout, \
    QLineEdit, QPushButton, QComboBox, QDialog


class ProductosModificar(QMainWindow):
    def __init__(self, anterior):
        super(ProductosModificar, self).__init__(anterior)
        # Se crea la ventana principal junto a sus modificaciones
        self.ventanaAnterior = anterior

        self.setWindowTitle("Modificar producto")

        self.ancho = 400
        self.alto = 345
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())
        self.setWindowModality(Qt.ApplicationModal)

        self.ventanaDialogo = QLabel()
        self.setCentralWidget(self.ventanaDialogo)
        self.formularioPrin = QFormLayout()
        self.ventanaDialogo.setStyleSheet("background-color: #9AC069;")

        self.principal = QLabel()
        self.formularioMensaje = QFormLayout()
        self.principal.setFixedHeight(270)
        self.principal.setStyleSheet("background-color: #8EA85D;")

        self.titulo0 = QLabel("Nombre: ")
        self.titulo0.setFixedHeight(20)
        self.titulo0.setFont(QFont("Arial", 12))
        self.titulo0.setStyleSheet("color: white;")

        self.nombre = QLineEdit()
        self.nombre.setFixedHeight(20)
        self.nombre.setMaxLength(40)
        self.nombre.setStyleSheet("background-color: white;")
        self.nombre.setFont(QFont("Arial", 12))

        self.formularioMensaje.addRow(self.titulo0, self.nombre)

        self.titulo1 = QLabel("Descripción: ")
        self.titulo1.setFixedHeight(20)
        self.titulo1.setFont(QFont("Arial", 12))
        self.titulo1.setStyleSheet("color: white;")

        self.descripcion = QTextEdit()
        self.descripcion.setFixedHeight(80)
        self.descripcion.setStyleSheet("background-color: white;")
        self.descripcion.setFont(QFont("Arial", 12))

        self.formularioMensaje.addRow(self.titulo1, self.descripcion)

        self.titulo2 = QLabel("Caducidad:")
        self.titulo2.setFixedHeight(50)
        self.titulo2.setFont(QFont("Arial", 12))
        self.titulo2.setStyleSheet("color: white;")

        self.minivertical = QVBoxLayout()
        self.infoCaducidad = QLabel()
        self.infoCaducidad.setFixedHeight(70)

        self.minihorizontal2 = QHBoxLayout()
        self.minititulos = QLabel()
        self.minititulos.setFixedHeight(25)

        self.miniTitulo1 = QLabel("día")
        self.miniTitulo1.setFixedWidth(50)
        self.miniTitulo1.setFixedHeight(20)
        self.miniTitulo1.setFont(QFont("Arial", 12))
        self.miniTitulo1.setStyleSheet("color: white;")

        self.miniTitulo2 = QLabel("mes")
        self.miniTitulo2.setFixedWidth(50)
        self.miniTitulo2.setFixedHeight(20)
        self.miniTitulo2.setFont(QFont("Arial", 12))
        self.miniTitulo2.setStyleSheet("color: white;")

        self.miniTitulo3 = QLabel("año")
        self.miniTitulo3.setFixedWidth(50)
        self.miniTitulo3.setFixedHeight(20)
        self.miniTitulo3.setFont(QFont("Arial", 12))
        self.miniTitulo3.setStyleSheet("color: white;")

        self.minihorizontal2.addWidget(self.miniTitulo1)
        self.minihorizontal2.addStretch()
        self.minihorizontal2.addWidget(self.miniTitulo2)
        self.minihorizontal2.addStretch()
        self.minihorizontal2.addWidget(self.miniTitulo3)

        self.minititulos.setLayout(self.minihorizontal2)
        self.minivertical.addWidget(self.minititulos)

        self.minihorizontal3 = QHBoxLayout()
        self.miniInfo = QLabel()
        self.miniInfo.setFixedHeight(30)

        self.dia = QLineEdit()
        self.dia.setFixedWidth(50)
        self.dia.setFixedHeight(20)
        self.dia.setMaxLength(2)
        self.dia.setStyleSheet("background-color: white;")
        self.dia.setFont(QFont("Arial", 12))

        self.mes = QLineEdit()
        self.mes.setFixedWidth(50)
        self.mes.setFixedHeight(20)
        self.mes.setMaxLength(2)
        self.mes.setStyleSheet("background-color: white;")
        self.mes.setFont(QFont("Arial", 12))

        self.ano = QLineEdit()
        self.ano.setFixedWidth(50)
        self.ano.setFixedHeight(20)
        self.ano.setMaxLength(4)
        self.ano.setStyleSheet("background-color: white;")
        self.ano.setFont(QFont("Arial", 12))

        # Estas barras son simple decoración
        self.barra = QLabel("/")
        self.barra.setFixedWidth(50)
        self.barra.setFixedHeight(20)
        self.barra.setAlignment(Qt.AlignCenter)
        self.barra.setStyleSheet("color: white;")
        self.barra.setFont(QFont("Arial", 12))

        self.barra2 = QLabel("/")
        self.barra2.setFixedWidth(50)
        self.barra2.setFixedHeight(20)
        self.barra2.setAlignment(Qt.AlignCenter)
        self.barra2.setStyleSheet("color: white;")
        self.barra2.setFont(QFont("Arial", 12))

        self.minihorizontal3.addWidget(self.dia)
        self.minihorizontal3.addWidget(self.barra)
        self.minihorizontal3.addWidget(self.mes)
        self.minihorizontal3.addWidget(self.barra2)
        self.minihorizontal3.addWidget(self.ano)

        self.miniInfo.setLayout(self.minihorizontal3)
        self.minivertical.addWidget(self.miniInfo)
        self.infoCaducidad.setLayout(self.minivertical)
        self.formularioMensaje.addRow(self.titulo2, self.infoCaducidad)

        self.vacio = QLabel()
        self.formularioMensaje.addWidget(self.vacio)

        self.titulo3 = QLabel("Cantidad:")
        self.titulo3.setFixedHeight(20)
        self.titulo3.setFont(QFont("Arial", 12))
        self.titulo3.setStyleSheet("color: white;")

        self.cantidad = QLineEdit()
        self.cantidad.setFixedWidth(50)
        self.cantidad.setFixedHeight(20)
        self.cantidad.setStyleSheet("background-color: white;")
        self.cantidad.setFont(QFont("Arial", 12))

        self.formularioMensaje.addRow(self.titulo3, self.cantidad)

        self.titulo4 = QLabel("Filtro:")
        self.titulo4.setFixedHeight(20)
        self.titulo4.setFont(QFont("Arial", 12))
        self.titulo4.setStyleSheet("color: white;")

        self.filtro = QComboBox()
        self.filtro.setFixedHeight(20)
        self.filtro.setStyleSheet("background-color: white;")
        self.filtro.setFont(QFont("Arial", 12))
        self.filtro.addItems(["Granos", "Enlatados", "Parva", "Lacteos", "Carnicos", "Pescados"])

        self.formularioMensaje.addRow(self.titulo4, self.filtro)

        self.principal.setLayout(self.formularioMensaje)
        self.formularioPrin.addRow(self.principal)

        # Se crea ventana establecida en la parte inferior para crear botones en los que se puede cancelar la creación del producto o crearlo
        self.botones2 = QLabel()
        self.botones2.setFixedHeight(37)
        self.minihorizontal4 = QHBoxLayout()

        self.botonModificar = QPushButton("Modificar")
        self.botonModificar.setFixedWidth(100)
        self.botonModificar.setFixedHeight(27)
        self.botonModificar.setStyleSheet("background-color: #8EA85D; color: white;")
        self.botonModificar.setFont(QFont("Arial", 12))
        self.botonModificar.clicked.connect(self.funcion_modificar)

        self.botonAtras = QPushButton("Cancelar")
        self.botonAtras.setFixedWidth(100)
        self.botonAtras.setFixedHeight(27)
        self.botonAtras.setStyleSheet("background-color: #8EA85D; color: white;")
        self.botonAtras.setFont(QFont("Arial", 12))
        self.botonAtras.clicked.connect(self.metodo_cerrar)

        self.minihorizontal4.addWidget(self.botonModificar)
        self.minihorizontal4.addStretch()
        self.minihorizontal4.addWidget(self.botonAtras)

        self.botones2.setLayout(self.minihorizontal4)
        self.formularioPrin.addRow(self.botones2)

        self.ventanaDialogo.setLayout(self.formularioPrin)

        self.ventanaValidar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaValidar.setWindowIcon(QtGui.QIcon("Imagenes/logo sin fondo.png"))
        self.ventanaValidar.setFixedWidth(300)
        self.ventanaValidar.setFixedHeight(100)
        self.ventanaValidar.setWindowTitle("Validación")
        self.ventanaValidar.setStyleSheet("background-color: #9AC069;")
        self.ventanaValidar.setWindowModality(Qt.ApplicationModal)

        self.verticalValidar = QVBoxLayout()

        self.mensaje = QLabel("")
        self.mensaje.setStyleSheet("color: white;")
        self.mensaje.setFont(QFont("Arial", 12))

        self.verticalValidar.addWidget(self.mensaje)

        self.botones = QLabel()
        self.horizontalValidacion = QHBoxLayout()

        self.horizontalValidacion.addStretch()
        self.Ok = QPushButton("Ok")
        self.Ok.setFixedWidth(80)
        self.Ok.setFixedHeight(25)
        self.Ok.setStyleSheet("background-color: #8EA85D; color: white;")
        self.Ok.setFont(QFont("Arial", 12))
        self.Ok.clicked.connect(self.metodo_cerrar_validacion)

        self.horizontalValidacion.addWidget(self.Ok)

        self.botones.setLayout(self.horizontalValidacion)
        self.verticalValidar.addWidget(self.botones)
        self.ventanaValidar.setLayout(self.verticalValidar)

        self.datosCorrectos = True

    def funcion_modificar(self):
        # Metodo para crear el producto y guardar la información
        print("Modifica producto")

    def metodo_cerrar(self):
        # Metodo para cerrar las subventanas abiertas en las funciones crear, modificar y eliminar
        self.hide()

    def metodo_cerrar_validacion(self):
        self.ventanaValidar.hide()