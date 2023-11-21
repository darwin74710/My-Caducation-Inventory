import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QFormLayout, QLabel, QWidget, QLineEdit, \
    QPushButton, QHBoxLayout, QVBoxLayout

from administrador import Administrador
from recuperarUsuario import RecuperarUsuario
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

        # Se establece una ventana de fondo junto a una distribución
        self.fondo = QWidget()
        self.horizontal = QVBoxLayout()
        self.setCentralWidget(self.fondo)

        # Se coloca el logo de la app en el fondo
        self.letero1 = QLabel()
        self.letero1.setFixedWidth(285)
        self.letero1.setFixedHeight(285)
        self.logo = QPixmap("Imagenes/logo.png")
        self.letero1.setPixmap(self.logo)
        self.letero1.setScaledContents(True)
        self.letero1.resize(self.logo.width(), self.logo.height())

        self.horizontal.addWidget(self.letero1)

        self.ventana1 = QWidget()

        # Creamos el ingreso de usuario con titulo y un campo para escribirlo
        self.letrero1 = QLabel("Ingrese su usuario")
        self.formulario = QFormLayout()
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

        # Creamos el ingreso de contraseña con su titulo y un campo para escribirlo
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

        # Creamos un botón para elegir si se ve la contraseña ingresada o no
        self.cambiarContra = QPushButton()
        self.cambiarContra.setIcon(QtGui.QIcon('Imagenes/iconos/nover.png'))
        self.cambiarContra.setFixedWidth(25)
        self.cambiarContra.clicked.connect(self.alternar_contrasena)
        self.activacion = True

        self.formulario.addRow(self.contraseña, self.cambiarContra)

        # Se crea una ventana para distribuir los botones en el fondo
        self.ventana2 = QWidget()
        self.horizontal2 = QHBoxLayout()
        self.ventana2.setFixedWidth(257)
        self.formulario.addRow(self.ventana2)

        self.botonRecuperar = QPushButton("Recuperar\nUsuario")
        self.botonRecuperar.setFixedWidth(100)
        self.botonRecuperar.setFixedHeight(45)
        self.botonRecuperar.setStyleSheet("background-color: #8EA85D; color: white;")
        self.botonRecuperar.setFont(QFont("Arial", 12))
        self.botonRecuperar.clicked.connect(self.accion_botonRecuperar)

        self.horizontal2.addWidget(self.botonRecuperar)

        self.horizontal2.addStretch()

        #Se crea el botón para ingresar a la ventana administrador
        self.botonIngresar = QPushButton("Ingresar")
        self.botonIngresar.setFixedWidth(100)
        self.botonIngresar.setFixedHeight(45)
        self.botonIngresar.setStyleSheet("background-color: #8EA85D; color: white;")
        self.botonIngresar.setFont(QFont("Arial", 12))
        self.botonIngresar.clicked.connect(self.accion_botonIngresar)

        self.horizontal2.addWidget(self.botonIngresar)

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

    def accion_botonRecuperar(self):
        self.hide()
        self.ventanaRec = RecuperarUsuario(self)
        self.ventanaRec.show()

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

