import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QFormLayout, QLabel, QWidget, QLineEdit, \
    QPushButton, QHBoxLayout, QVBoxLayout, QDialog

from administrador import Administrador
from recuperarUsuario import RecuperarUsuario
from cliente import Cliente
class Ingreso(QMainWindow):
    def __init__(self, parent=None):
        super(Ingreso, self).__init__(parent=parent)

        self.esAdministrador = True
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

        # Creamos el ingreso de contraseña con su título y un campo para escribirlo
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
        self.cambiarContra.setStyleSheet("background-color: #8EA85D;")
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

        self.file = open('datos/usuarios.txt', 'rb')
        self.usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")
            if linea == '':
                break

            self.u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10],
                lista[11],
                lista[12],
                lista[13]
            )

            self.usuarios.append(self.u)

        self.file.close()

        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaDialogo.setWindowIcon(QtGui.QIcon("Imagenes/logo sin fondo.png"))
        self.ventanaDialogo.setWindowTitle("Ingreso")
        self.ventanaDialogo.setStyleSheet("background-color: #9AC069;")
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)
        self.vertical = QVBoxLayout()

        self.mensaje = QLabel("")
        self.mensaje.setFont(QFont("Arial", 12))
        self.mensaje.setStyleSheet("color: white;")
        self.vertical.addWidget(self.mensaje)

        self.cajaBoton = QLabel()
        self.cajaBH = QHBoxLayout()
        self.cajaBH.addStretch()

        self.botonOk = QPushButton("Ok")
        self.botonOk.setFixedWidth(70)
        self.botonOk.setFixedHeight(25)
        self.botonOk.setStyleSheet("background-color: #8EA85D; color: white;")
        self.botonOk.setFont(QFont("Arial", 12))
        self.botonOk.clicked.connect(self.accion_botonOk)

        self.cajaBH.addWidget(self.botonOk)
        self.cajaBoton.setLayout(self.cajaBH)
        self.vertical.addWidget(self.cajaBoton)
        self.ventanaDialogo.setLayout(self.vertical)

    def accion_botonIngresar(self):

        self.file = open('datos/usuarios.txt', 'rb')
        self.usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")
            if linea == '':
                break

            self.u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10],
                lista[11],
                lista[12],
                lista[13]
            )

            self.usuarios.append(self.u)

        self.file.close()

        datosCorrectos = False
        for self.u in self.usuarios:
            if self.u.usuario == self.usuario.text():
                if self.u.password == self.contraseña.text():
                    datosCorrectos = True
                    if self.u.validar == "Administrador":
                        self.esAdministrador = True
                    if self.u.validar == "Usuario":
                        self.esAdministrador = False
                    break
                else:
                    datosCorrectos = False
            else:
                datosCorrectos = False

        if not self.usuario.text() == "":
            if not self.contraseña.text() == "":
                if datosCorrectos == False:
                    self.ventanaDialogo.setFixedWidth(320)
                    self.ventanaDialogo.setFixedHeight(100)
                    self.mensaje.setText("El usuario o la contraseña son incorrectos.")
                    self.ventanaDialogo.exec_()
                else:
                    # Aquí se ingresa.
                    self.ventanaDialogo.setFixedWidth(240)
                    self.ventanaDialogo.setFixedHeight(100)
                    self.mensaje.setText("Ah ingresado correctamente.")
                    self.ventanaDialogo.exec_()

                    self.hide()
                    self.usuario.setText('')
                    self.contraseña.setText('')

                    self.ventanaA = Administrador(self)
                    self.ventanaA.show()
            elif self.contraseña.text() == "" and not self.usuario.text() == "":
                self.ventanaDialogo.setFixedWidth(300)
                self.ventanaDialogo.setFixedHeight(100)
                self.mensaje.setText("Ingrese una contraseña para continuar.")
                self.ventanaDialogo.exec_()
        elif self.usuario.text() == "" and not self.contraseña.text() == "":
            self.ventanaDialogo.setFixedWidth(270)
            self.ventanaDialogo.setFixedHeight(100)
            self.mensaje.setText("Ingrese un usuario para continuar.")
            self.ventanaDialogo.exec_()
        elif self.usuario.text() == "" and self.contraseña.text() == "":
            self.ventanaDialogo.setFixedWidth(350)
            self.ventanaDialogo.setFixedHeight(100)
            self.mensaje.setText("Ingrese un usuario y contraseña para continuar.")
            self.ventanaDialogo.exec_()

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

    def accion_botonOk(self):
        self.ventanaDialogo.hide()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana = Ingreso()

    ventana.show()

    sys.exit(app.exec_())

