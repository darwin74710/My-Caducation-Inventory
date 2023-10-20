import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QFormLayout, QLabel, QWidget, QLineEdit, \
    QPushButton, QHBoxLayout, QVBoxLayout

from administrador import Administrador

from crearUsuario import CrearUsuario

class Ingreso(QMainWindow):
    def __init__(self, parent=None):
        super(Ingreso, self).__init__(parent=parent)

        self.setWindowTitle("Login")
        self.setStyleSheet("background-color: #739f6e;")

        self.ancho = 700
        self.alto = 400

        self.resize(self.ancho, self.alto)

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())


        self.fondo = QWidget()

        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()
        self.formulario = QVBoxLayout()
        self.horizontal2 = QHBoxLayout()

        # consultar tipos de letras del sistema
        #for p in QFontDatabase().families():
            #print(p)
        # creamos letrero
        self.letero1 = QLabel()

        self.logo = QPixmap("Imagenes/logo.png")
        self.letero1.setPixmap(self.logo)
        self.letero1.setStyleSheet("border: 4px solid black;")
        self.letero1.setScaledContents(True)
        self.resize(self.logo.width(), self.logo.height())
        # agregamos espacio para separar el titulo
        self.horizontal.addWidget(self.letero1)

        self.ventana1 = QWidget()
        self.login = QLabel("LOGIN")
        self.login.setFont(QFont("Arial", 80))
        self.login.setStyleSheet("color: #e86868;")
        self.login.setAlignment(Qt.AlignCenter)
        self.formulario.addWidget(self.login)

        # hacemos letrero de primer numero
        self.letrero1 = QLabel("Ingrese su usuario")
        self.letrero1.setFont(QFont("Arial", 17))
        self.formulario.addWidget(self.letrero1)

        # hacemos campo para ingresar el usuario
        self.usuario = QLineEdit()
        self.usuario.setStyleSheet("background-color: white;")
        # definimos el ancho del campo 80px
        self.usuario.setFixedWidth(250)
        self.usuario.setFont(QFont("Arial", 20))
        # estabelcemos que solo ingrese numero de 12 caracteres
        self.usuario.setMaxLength(14)
        # ponemos el letero y ponemos el campo del primer numero en la segunda fila
        self.formulario.addWidget(self.usuario)

        # hacemos el campo para ingresar contraseña
        self.letrero2 = QLabel("Ingrese su contraseña")
        self.letrero2.setFont(QFont("Arial", 17))
        self.formulario.addWidget(self.letrero2)

        self.contraseña = QLineEdit()
        self.contraseña.setStyleSheet("background-color: white;")
        self.contraseña.setFixedWidth(250)
        self.contraseña.setFont(QFont("Arial", 20))
        self.contraseña.setMaxLength(14)
        self.formulario.addWidget(self.contraseña)

        self.formulario.addStretch()


        self.ventana2 = QWidget()
        self.formulario.addWidget(self.ventana2)

        self.botonCrear = QPushButton("Crear Usuario")
        self.botonCrear.setFixedWidth(150)
        self.botonCrear.setFixedHeight(30)
        self.botonCrear.setStyleSheet("background-color: #e86868; color: white;")
        self.botonCrear.setFont(QFont("Arial", 14))

        self.botonCrear.clicked.connect(self.crear_usuario)

        self.horizontal2.addWidget(self.botonCrear)

        # hacemos boton para hacer ingresar
        self.botonIngresar = QPushButton("Ingresar")
        self.botonIngresar.setFixedWidth(150)
        self.botonIngresar.setFixedHeight(30)
        self.botonIngresar.setStyleSheet("background-color: #e86868; color: white;")
        self.botonIngresar.setFont(QFont("Arial", 14))


        self.horizontal2.addWidget(self.botonIngresar)

        self.botonIngresar.clicked.connect(self.accion_botonIngresar)

        self.horizontal.addWidget(self.ventana1)

        self.ventana2.setLayout(self.horizontal2)
        self.ventana1.setLayout(self.formulario)
        self.fondo.setLayout(self.horizontal)
    def accion_botonIngresar(self):
        self.hide()

        self.ventanaA = Administrador(self)
        self.ventanaA.show()

    def crear_usuario(self):
        self.hide()

        self.ventanaB = CrearUsuario(self)
        self.ventanaB.show()



if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana = Ingreso()

    ventana.show()

    sys.exit(app.exec_())

