import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QFormLayout, QLabel, QWidget, QLineEdit, \
    QPushButton, QHBoxLayout, QVBoxLayout

from administrador import Administrador

class Ingreso(QMainWindow):
    def __init__(self, parent=None):
        super(Ingreso, self).__init__(parent=parent)
        # Se crea la ventana principal junto a sus modificaciones
        self.setWindowTitle("Login")
        self.setWindowIcon(QtGui.QIcon("Imagenes/logo sin fondo.png"))
        self.setStyleSheet("background-color: #9AC069;")

        self.ancho = 285
        self.alto = 510

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Se empieza a trabajar en la construcción de la ventana
        self.fondo = QWidget()
        self.setCentralWidget(self.fondo)

        self.horizontal = QVBoxLayout()
        self.formulario = QFormLayout()

        # Se establece el logo de la aplicación
        self.letero1 = QLabel()
        self.letero1.setFixedWidth(285)
        self.letero1.setFixedHeight(285)
        self.logo = QPixmap("Imagenes/logo.png")
        self.letero1.setPixmap(self.logo)
        self.letero1.setScaledContents(True)
        self.letero1.resize(self.logo.width(), self.logo.height())
        # agregamos espacio para separar el titulo
        self.horizontal.addWidget(self.letero1)

        self.ventana1 = QWidget()

        # Se crea el ingreso del usuario
        self.letrero1 = QLabel("Ingrese su usuario")
        self.letrero1.setFixedHeight(30)
        self.letrero1.setStyleSheet("color: white;")
        self.letrero1.setFont(QFont("Arial", 12))
        self.formulario.addRow(self.letrero1)

        self.usuario = QLineEdit()
        self.usuario.setStyleSheet("background-color: white;")
        self.usuario.setFixedWidth(250)
        self.usuario.setFont(QFont("Arial", 12))
        self.usuario.setMaxLength(14)
        self.formulario.addRow(self.usuario)

        # Se crea el ingreso de la contraseña
        self.letrero2 = QLabel("Ingrese su contraseña")
        self.letrero2.setFixedHeight(30)
        self.letrero2.setStyleSheet("color: white;")
        self.letrero2.setFont(QFont("Arial", 12))
        self.formulario.addRow(self.letrero2)

        self.contraseña = QLineEdit()
        self.contraseña.setStyleSheet("background-color: white;")
        self.contraseña.setFixedWidth(217)
        self.contraseña.setFont(QFont("Arial", 12))
        self.contraseña.setMaxLength(14)
        self.contraseña.setEchoMode(QLineEdit.Password)

        # Se crea botón para alternar entre poder ver y no ver la contraseña
        self.cambiarContra = QPushButton()
        self.cambiarContra.setIcon(QtGui.QIcon('Imagenes/iconos/nover.png'))
        self.cambiarContra.setFixedWidth(25)
        self.cambiarContra.clicked.connect(self.alternar_contrasena)
        self.activacion = True

        self.formulario.addRow(self.contraseña, self.cambiarContra)

        # Se crean los botones para el ingreso de usuario o la creación de uno
        self.ventana2 = QWidget()
        self.ventana2.setFixedWidth(257)
        self.horizontal2 = QHBoxLayout()
        self.formulario.addRow(self.ventana2)

        self.espacio = QLabel()
        self.horizontal2.addWidget(self.espacio)
        self.horizontal2.addStretch()

        self.botonIngresar = QPushButton("Ingresar")
        self.botonIngresar.setFixedWidth(100)
        self.botonIngresar.setFixedHeight(35)
        self.botonIngresar.setStyleSheet("background-color: #8EA85D; color: white;")
        self.botonIngresar.setFont(QFont("Arial", 12))


        self.horizontal2.addWidget(self.botonIngresar)

        self.botonIngresar.clicked.connect(self.accion_botonIngresar)

        self.horizontal.addWidget(self.ventana1)

        self.ventana2.setLayout(self.horizontal2)
        self.ventana1.setLayout(self.formulario)
        self.fondo.setLayout(self.horizontal)

    def accion_botonIngresar(self):
        # Metodo para iniciar sesión e ir a la ventana Administrador
        self.hide()
        self.usuario.setText('')
        self.contraseña.setText('')

        self.ventanaA = Administrador(self)
        self.ventanaA.show()

    def alternar_contrasena(self):
        # Metodo para poder ver o no ver la contraseña ingresada
        if self.activacion == True:
            self.activacion = False
            self.contraseña.setEchoMode(QLineEdit.Normal)
            self.cambiarContra.setIcon(QtGui.QIcon('Imagenes/iconos/ver.png'))
        elif self.activacion == False:
            self.activacion = True
            self.contraseña.setEchoMode(QLineEdit.Password)
            self.cambiarContra.setIcon(QtGui.QIcon('Imagenes/iconos/nover.png'))



if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana = Ingreso()

    ventana.show()

    sys.exit(app.exec_())

