import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QPushButton, QWidget, QLineEdit, QLabel, \
    QVBoxLayout, QHBoxLayout, QGridLayout, QDialog, QDialogButtonBox, QFormLayout


class CrearUsuario(QMainWindow):
    def __init__(self, anteriorC):
        super(CrearUsuario, self).__init__(anteriorC)

        self.ventanaAnteriorC = anteriorC

        self.setWindowTitle("Creación de usuario")
        self.setStyleSheet("background-color: #9AC069;")

        self.ancho = 800
        self.alto = 600

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

        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # ----- lAYOUT IZQUIERDO -----
        self.ladoIzquierdo = QFormLayout()

        self.letreroI = QLabel()

        self.letreroI.setText("Registar Usuario")

        self.letreroI.setFont(QFont("arial", 20))

        self.letreroI.setStyleSheet("color: white;")

        self.ladoIzquierdo.addRow(self.letreroI)

        self.letreroI2 = QLabel()

        self.letreroI2.setFixedWidth(340)

        self.letreroI2.setText("Ingrese la informacion que se esta solicitando"
                             "\nen el formulario. Los campos que tienen un *"
                             "\nson obligatorios.")

        self.letreroI2.setFont(QFont("arial", 10))

        self.letreroI2.setStyleSheet("color: white; margin-bottom: 40px;"
                                     "margin-top: 20px;"
                                     "padding-bottom: 10px;"
                                     "border: 2px solid white;"
                                     "border-left: none;"
                                     "border-right: none;"
                                     "border-top: none;")

        self.ladoIzquierdo.addRow(self.letreroI2)

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setStyleSheet("background-color: white;")
        self.nombreCompleto.setFixedWidth(250)
        self.nombreCompleto.setMaxLength(70)

        self.ladoIzquierdo.addRow("Nombre completo*", self.nombreCompleto)

        self.NombredeUsuario = QLineEdit()
        self.NombredeUsuario.setStyleSheet("background-color: white;")
        self.NombredeUsuario.setFixedWidth(250)
        self.NombredeUsuario.setMaxLength(14)

        self.ladoIzquierdo.addRow("Nombre de usuario*", self.NombredeUsuario)

        self.password = QLineEdit()
        self.password.setStyleSheet("background-color: white;")
        self.password.setFixedWidth(250)
        self.password.setMaxLength(14)
        self.password.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Contraseña*", self.password)

        self.password2 = QLineEdit()
        self.password2.setStyleSheet("background-color: white;")
        self.password2.setFixedWidth(250)
        self.password2.setMaxLength(14)
        self.password2.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Confirmar Contraseña*", self.password2)

        self.Documento = QLineEdit()
        self.Documento.setStyleSheet("background-color: white;")
        self.Documento.setFixedWidth(250)
        self.Documento.setMaxLength(14)

        self.ladoIzquierdo.addRow("Documento de identidad*", self.Documento)

        self.correo = QLineEdit()
        self.correo.setStyleSheet("background-color: white;")
        self.correo.setFixedWidth(250)
        self.correo.setMaxLength(14)

        self.ladoIzquierdo.addRow("Correo electronico*", self.correo)

        self.botonRegistrar = QPushButton("Registrar")
        self.botonRegistrar.setFixedWidth(90)


        self.botonRegistrar.setStyleSheet("background-color: #9AC069;"
                                          "color: white;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(90)

        self.botonLimpiar.setStyleSheet("background-color: #9AC069;"
                                          "color: white;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        self.horizontal.addLayout(self.ladoIzquierdo)

        #----- SE COLOCA LA FINAL -----
        self.fondo.setLayout(self.horizontal)

        '''
        self.espacio = QLabel()
        # consultar tipos de letras del sistema
        # for p in QFontDatabase().families():
        # print(p)
        # creamos letrero
        self.ventana1 = QWidget()
        self.login = QLabel("CREACIÓN DE USUARIO")
        self.login.setFont(QFont("Arial", 30))
        self.login.setStyleSheet("color: white;")
        self.login.setAlignment(Qt.AlignCenter)
        self.formulario.addWidget(self.login)

        self.formulario.addStretch()

        self.ventanaU = QWidget()
        self.Cuadricula = QGridLayout()
        self.ventanaU.setLayout(self.Cuadricula)
        # hacemos letrero de primer numero
        self.letrero1 = QLabel("Ingrese su usuario")
        self.letrero1.setFont(QFont("Arial", 17))
        self.letrero1.setStyleSheet("color: white;")
        self.Cuadricula.addWidget(self.letrero1, 0, 1)

        # hacemos campo para ingresar el usuario
        self.usuario = QLineEdit()
        self.usuario.setStyleSheet("background-color: white;")
        # definimos el ancho del campo 80px
        self.usuario.setFixedWidth(250)
        self.usuario.setFont(QFont("Arial", 20))
        # estabelcemos que solo ingrese numero de 12 caracteres
        self.usuario.setMaxLength(14)
        # ponemos el letero y ponemos el campo del primer numero en la segunda fila
        self.Cuadricula.addWidget(self.usuario, 1, 1)

        self.instruc = QLabel("- Usuario y contraseña de maximo\n14 caracteres")
        self.instruc.setFont(QFont("Arial", 13))
        self.instruc.setStyleSheet("color: white;")
        self.Cuadricula.addWidget(self.instruc, 0, 0)
        self.instruc2 = QLabel("- No ingrese caracteres especiales")
        self.instruc2.setFont(QFont("Arial", 13))
        self.instruc2.setStyleSheet("color: white;")
        self.Cuadricula.addWidget(self.instruc2, 1, 0)
        self.instruc4 = QLabel("")
        self.instruc4.setFont(QFont("Arial", 30))
        self.instruc4.setStyleSheet("color: white;")
        self.Cuadricula.addWidget(self.instruc4, 3, 0)


        # hacemos el campo para ingresar contraseña
        self.letrero2 = QLabel("Ingrese su contraseña")
        self.letrero2.setFont(QFont("Arial", 17))
        self.letrero2.setStyleSheet("color: white;")
        self.Cuadricula.addWidget(self.letrero2, 4, 0)

        self.contraseña = QLineEdit()
        self.contraseña.setStyleSheet("background-color: white;")
        self.contraseña.setFixedWidth(250)
        self.contraseña.setFont(QFont("Arial", 20))
        self.contraseña.setMaxLength(14)
        self.Cuadricula.addWidget(self.contraseña, 5, 0)

        self.letrero3 = QLabel("Reingrese su contraseña")
        self.letrero3.setFont(QFont("Arial", 17))
        self.letrero3.setStyleSheet("color: white;")
        self.Cuadricula.addWidget(self.letrero3, 4, 1)

        self.contraseña2 = QLineEdit()
        self.contraseña2.setStyleSheet("background-color: white;")
        self.contraseña2.setFixedWidth(250)
        self.contraseña2.setFont(QFont("Arial", 20))
        self.contraseña2.setMaxLength(14)
        self.Cuadricula.addWidget(self.contraseña2, 5, 1)

        self.formulario.addWidget(self.ventanaU)

        self.formulario.addStretch()

        self.ventana2 = QWidget()
        self.formulario.addWidget(self.ventana2)

        self.horizontal2.addStretch()

        self.botonCrear = QPushButton("Crear")
        self.botonCrear.setFixedWidth(150)
        self.botonCrear.setFixedHeight(30)
        self.botonCrear.setStyleSheet("background-color: white; color: #9AC069;")
        self.botonCrear.setFont(QFont("Arial", 14))

        self.botonCrear.clicked.connect(self.crear_usuario)

        self.horizontal2.addWidget(self.botonCrear)
        self.horizontal.addWidget(self.ventana1)
        self.ventana2.setLayout(self.horizontal2)
        self.ventana1.setLayout(self.formulario)
        self.fondo.setLayout(self.horizontal)
        '''

    def accion_botonRegistrar(self):
        pass

    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.NombredeUsuario.setText('')
        self.password.setText('')
        self.password2.setText('')
        self.Documento.setText('')
        self.correo.setText('')
        '''
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')
        '''


        '''
        self.ventanaDialogo = QDialog()
        self.ventanaDialogo.resize(300, 150)
        self.ventanaDialogo.setStyleSheet("background-color: #9AC069;")

        self.botonAceptar = QDialogButtonBox.Ok

        self.opcionesBotones = QDialogButtonBox(self.botonAceptar)
        self.opcionesBotones.setStyleSheet("background-color: white; color: #9AC069;")
        self.opcionesBotones.accepted.connect(self.ventanaDialogo.accept)

        self.ventanaDialogo.setWindowTitle("Validación")
        # Bloquear la ventana anterior para no poder interactuar con ella.
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        self.vertical5 = QVBoxLayout()

        self.mensaje = QLabel("")

        self.vertical5.addWidget(self.mensaje)
        self.vertical5.addWidget(self.opcionesBotones)

        self.ventanaDialogo.setLayout(self.vertical5)

        self.mensaje.setText("Ah creado su usuario correctamente.")
        self.mensaje.setStyleSheet("color: white;")
        self.mensaje.setFont(QFont("Arial", 14))

        self.ventanaDialogo.exec_()

        self.hide()
        self.ventanaAnteriorC.show()
        '''