import sys

from PyQt5 import QtCore, QtGui
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
        self.alto = 640

        self.resize(self.ancho, self.alto)

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.fondo = QLabel()
        self.setCentralWidget(self.fondo)

        self.verticalP = QVBoxLayout()

        self.ventanaDatos = QLabel()

        self.horizontal = QHBoxLayout()

        # ----- lAYOUT IZQUIERDO -----
        self.ladoIzquierdo = QFormLayout()
        self.letreroI = QLabel()
        self.letreroI.setText("Registar Usuario")
        self.letreroI.setFont(QFont("arial", 24))
        self.letreroI.setStyleSheet("color: white;")

        self.ladoIzquierdo.addRow(self.letreroI)

        self.letreroI2 = QLabel()
        self.letreroI2.setFixedWidth(340)
        self.letreroI2.setFixedHeight(130)
        self.letreroI2.setText("Ingrese la informacion que se esta solicitando"
                             "\nen el formulario. Los campos marcados con un"
                             "\nasterisco (*) son obligatorios.")
        self.letreroI2.setFont(QFont("arial", 12))
        self.letreroI2.setStyleSheet("color: white; margin-bottom: 40px;"
                                     "margin-top: 20px;"
                                     "padding-bottom: 10px;"
                                     "border: 2px solid white;"
                                     "border-left: none;"
                                     "border-right: none;"
                                     "border-top: none;")

        self.ladoIzquierdo.addRow(self.letreroI2)


        self.titulo1 = QLabel("Nombre completo*")
        self.titulo1.setFont(QFont("Arial", 12))
        self.titulo1.setStyleSheet("color: white;")

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setStyleSheet("background-color: white;")
        self.nombreCompleto.setFixedWidth(250)
        self.nombreCompleto.setFont(QFont("Arial", 12))
        self.nombreCompleto.setMaxLength(70)

        self.ladoIzquierdo.addRow(self.titulo1)
        self.ladoIzquierdo.addRow(self.nombreCompleto)

        self.titulo2 = QLabel("Nombre de usuario*")
        self.titulo2.setFont(QFont("Arial", 12))
        self.titulo2.setStyleSheet("color: white;")

        self.NombredeUsuario = QLineEdit()
        self.NombredeUsuario.setStyleSheet("background-color: white;")
        self.NombredeUsuario.setFixedWidth(250)
        self.NombredeUsuario.setFont(QFont("Arial", 12))
        self.NombredeUsuario.setMaxLength(14)

        self.ladoIzquierdo.addRow(self.titulo2)
        self.ladoIzquierdo.addRow(self.NombredeUsuario)

        self.titulo3 = QLabel("Contraseña*")
        self.titulo3.setFont(QFont("Arial", 12))
        self.titulo3.setStyleSheet("color: white;")

        self.password = QLineEdit()
        self.password.setStyleSheet("background-color: white;")
        self.password.setFixedWidth(250)
        self.password.setFont(QFont("Arial", 12))
        self.password.setMaxLength(14)
        self.password.setEchoMode(QLineEdit.Password)

        self.cambiarContra1 = QPushButton()
        self.cambiarContra1.setFixedWidth(25)
        self.cambiarContra1.clicked.connect(self.alternar_contrasena1)
        self.activacion1 = True
        self.cambiarContra1.setIcon(QtGui.QIcon('Imagenes/iconos/nover.png'))

        self.ladoIzquierdo.addRow(self.titulo3)
        self.ladoIzquierdo.addRow(self.password, self.cambiarContra1)

        self.titulo4 = QLabel("Confirmar Contraseña*")
        self.titulo4.setFont(QFont("Arial", 12))
        self.titulo4.setStyleSheet("color: white;")

        self.password2 = QLineEdit()
        self.password2.setStyleSheet("background-color: white;")
        self.password2.setFixedWidth(250)
        self.password2.setFont(QFont("Arial", 12))
        self.password2.setMaxLength(14)
        self.password2.setEchoMode(QLineEdit.Password)

        self.cambiarContra2 = QPushButton()
        self.cambiarContra2.setFixedWidth(25)
        self.cambiarContra2.clicked.connect(self.alternar_contrasena2)
        self.activacion2 = True
        self.cambiarContra2.setIcon(QtGui.QIcon('Imagenes/iconos/nover.png'))

        self.ladoIzquierdo.addRow(self.titulo4)
        self.ladoIzquierdo.addRow(self.password2, self.cambiarContra2)

        self.titulo5 = QLabel("Documento de identidad*")
        self.titulo5.setFont(QFont("Arial", 12))
        self.titulo5.setStyleSheet("color: white;")

        self.Documento = QLineEdit()
        self.Documento.setStyleSheet("background-color: white;")
        self.Documento.setFixedWidth(250)
        self.Documento.setFont(QFont("Arial", 12))
        self.Documento.setMaxLength(14)

        self.ladoIzquierdo.addRow(self.titulo5)
        self.ladoIzquierdo.addRow(self.Documento)

        self.titulo6 = QLabel("Correo electronico*")
        self.titulo6.setFont(QFont("Arial", 12))
        self.titulo6.setStyleSheet("color: white;")

        self.correo = QLineEdit()
        self.correo.setStyleSheet("background-color: white;")
        self.correo.setFixedWidth(250)
        self.correo.setFont(QFont("Arial", 12))
        self.correo.setMaxLength(14)

        self.ladoIzquierdo.addRow(self.titulo6)
        self.ladoIzquierdo.addRow(self.correo)

        self.horizontal.addLayout(self.ladoIzquierdo)

        #----- LAYOUT DERECHO -----
        self.ladoDerecho = QFormLayout()

        self.letreroD = QLabel()
        self.letreroD.setText("Recuperar contraseña")
        self.letreroD.setFont(QFont("arial", 24))
        self.letreroD.setStyleSheet("color: white;")

        self.ladoDerecho.addRow(self.letreroD)

        self.letreroD2 = QLabel()
        self.letreroD2.setFixedWidth(340)
        self.letreroD2.setFixedHeight(130)
        self.letreroD2.setText("Ingrese la informacion para recuperar"
                               "\nla contraseña. los campos marcados"
                               "\ncon asterisco (*) son obligatorios.")
        self.letreroD2.setFont(QFont("arial", 12))
        self.letreroD2.setStyleSheet("color: white; margin-bottom: 40px;"
                                     "margin-top: 20px;"
                                     "padding-bottom: 10px;"
                                     "border: 2px solid white;"
                                     "border-left: none;"
                                     "border-right: none;"
                                     "border-top: none;")
        self.ladoDerecho.addRow(self.letreroD2)

        #-----primera pregunta de validacion
        self.labelPregunta1 = QLabel("Pregunta de verificacion 1*")
        self.labelPregunta1.setStyleSheet("color: white;")
        self.labelPregunta1.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.labelPregunta1)

        self.pregunta1 = QLineEdit()
        self.pregunta1.setStyleSheet("background-color: white;")
        self.pregunta1.setFixedWidth(320)
        self.pregunta1.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.pregunta1)

        #-----respuesta pregunta de validacion 1
        self.labelRespuesta1 = QLabel("Respuesta de verificacion 1*")
        self.labelRespuesta1.setStyleSheet("color: white;")
        self.labelRespuesta1.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.labelRespuesta1)


        self.respuesta1 = QLineEdit()
        self.respuesta1.setStyleSheet("background-color: white;")
        self.respuesta1.setFixedWidth(320)
        self.respuesta1.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.respuesta1)

        #----- Segunda Pregunta de verificacion
        self.labelPregunta2 = QLabel("Pregunta de verificacion 2*")
        self.labelPregunta2.setStyleSheet("color: white;")
        self.labelPregunta2.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.labelPregunta2)

        self.pregunta2 = QLineEdit()
        self.pregunta2.setStyleSheet("background-color: white;")
        self.pregunta2.setFixedWidth(320)
        self.pregunta2.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.pregunta2)

        # -----respuesta pregunta de validacion 2
        self.labelRespuesta2 = QLabel("Respuesta de verificacion 2*")
        self.labelRespuesta2.setStyleSheet("color: white;")
        self.labelRespuesta2.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.labelRespuesta2)

        self.respuesta2 = QLineEdit()
        self.respuesta2.setStyleSheet("background-color: white;")
        self.respuesta2.setFixedWidth(320)
        self.respuesta2.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.respuesta2)

        #-----Tercera pregunta de verificacion
        self.labelPregunta3 = QLabel("Pregunta de verificacion 3*")
        self.labelPregunta3.setStyleSheet("color: white;")
        self.labelPregunta3.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.labelPregunta3)

        self.pregunta3 = QLineEdit()
        self.pregunta3.setStyleSheet("background-color: white;")
        self.pregunta3.setFixedWidth(320)
        self.pregunta3.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.pregunta3)

        # -----respuesta pregunta de validacion 3
        self.labelRespuesta3 = QLabel("Respuesta de verificacion 3*")
        self.labelRespuesta3.setStyleSheet("color: white;")
        self.labelRespuesta3.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.labelRespuesta3)

        self.respuesta3 = QLineEdit()
        self.respuesta3.setStyleSheet("background-color: white;")
        self.respuesta3.setFixedWidth(320)
        self.respuesta3.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.respuesta3)

        self.horizontal.addLayout(self.ladoDerecho)
        self.ventanaDatos.setLayout(self.horizontal)
        self.verticalP.addWidget(self.ventanaDatos)

        self.ventanaBotones = QLabel()
        self.ventanaBotones.setFixedHeight(100)
        self.horizontalB = QHBoxLayout()

        self.botonRegistrar = QPushButton("Registrar")
        self.botonRegistrar.setFixedWidth(100)
        self.botonRegistrar.setFont(QFont("Arial", 12))
        self.botonRegistrar.setStyleSheet("background-color: #8EA85D;"
                                          "color: white;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(100)
        self.botonLimpiar.setFont(QFont("Arial", 12))
        self.botonLimpiar.setStyleSheet("background-color: #8EA85D;"
                                        "color: white;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")
        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.botonAtras = QPushButton("Atras")
        self.botonAtras.setFixedWidth(100)
        self.botonAtras.setFont(QFont("Arial", 12))
        self.botonAtras.setStyleSheet("background-color: #8EA85D;"
                                       "color: white;"
                                       "padding: 10px;"
                                       "margin-top: 40px;"
                                       )
        self.botonAtras.clicked.connect(self.accion_botonatras)

        self.botonBuscar = QPushButton("Buscar")
        self.botonBuscar.setFixedWidth(100)
        self.botonBuscar.setFont(QFont("Arial", 12))
        self.botonBuscar.setStyleSheet("background-color: #8EA85D;"
                                       "color: white;"
                                       "padding: 10px;"
                                       "margin-top: 40px;"
                                       )

        # -----Boton recuperar contraseña
        self.botonRecuperar = QPushButton("Recuperar")
        self.botonRecuperar.setFixedWidth(100)
        self.botonRecuperar.setFont(QFont("Arial", 12))
        self.botonRecuperar.setStyleSheet("background-color: #8EA85D;"
                                          "color: white;"
                                          "padding: 10px;"
                                          "margin-top: 40px;"
                                          )

        self.horizontalB.addWidget(self.botonRegistrar)
        self.horizontalB.addWidget(self.botonLimpiar)
        self.horizontalB.addStretch()
        self.horizontalB.addWidget(self.botonAtras)
        self.horizontalB.addStretch()
        self.horizontalB.addWidget(self.botonBuscar)
        self.horizontalB.addWidget(self.botonRecuperar)

        self.ventanaBotones.setLayout(self.horizontalB)
        self.verticalP.addWidget(self.ventanaBotones)
        #----- SE COLOCA LA FINAL -----
        self.fondo.setLayout(self.verticalP)


    def accion_botonRegistrar(self):
        self.ventanadeDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanadeDialogo.setWindowIcon(QtGui.QIcon("Imagenes/logo sin fondo.png"))
        self.ventanadeDialogo.setFixedWidth(300)
        self.ventanadeDialogo.setFixedHeight(90)
        self.ventanadeDialogo.setStyleSheet("background-color: #9AC069;")
        self.ventanadeDialogo.setWindowTitle("Formulario de registro")
        self.ventanadeDialogo.setWindowModality(Qt.ApplicationModal)

        self.formulario = QFormLayout()

        self.espacio2 = QLabel()
        self.espacio2.setFixedHeight(5)
        self.formulario.addRow(self.espacio2)

        self.mensaje = QLabel("")
        self.mensaje.setFont(QFont("Arial", 12))
        self.mensaje.setStyleSheet("color: white;")

        self.espacio = QLabel()
        self.espacio.setFixedWidth(190)

        self.atras = QPushButton("Atrás")
        self.atras.setFixedWidth(80)
        self.atras.setFixedHeight(25)
        self.atras.setFont(QFont("Arial", 12))
        self.atras.setStyleSheet("background-color: #8EA85D; color: white;")
        self.atras.clicked.connect(self.cerrar_mensaje)

        self.formulario.addRow(self.mensaje)
        self.formulario.addRow(self.espacio2)
        self.formulario.addRow(self.espacio, self.atras)

        self.ventanadeDialogo.setLayout(self.formulario)

        self.datosCorrectos = True

        if (
            self.password.text() != self.password2.text()
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Las contraseñas no son iguales")

            self.ventanadeDialogo.exec_()

        if (
                self.nombreCompleto.text() == ''
                or self.NombredeUsuario.text() == ''
                or self.password.text() == ''
                or self.password2.text() == ''
                or self.Documento.setText == ''
                or self.correo.setText == ''
                or self.pregunta1.setText == ''
                or self.respuesta1.setText == ''
                or self.pregunta2.setText == ''
                or self.respuesta2.setText == ''
                or self.pregunta3.setText == ''
                or self.respuesta3.setText == ''
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Debe ingresar todos los campos")

            self.ventanadeDialogo.exec_()

        if self.datosCorrectos:

            self.file = open('datos/clientes.txt', 'ab')

            self.file.write(bytes(self.nombreCompleto.text() + ";"
                                  + self.NombredeUsuario.text() + ";"
                                  + self.password.text() + ";"
                                  + self.password2.text() + ";"
                                  + self.Documento.text() + ";"
                                  + self.correo.text() + ";"
                                  + self.pregunta1.text() + ";"
                                  + self.respuesta1.text() + ";"
                                  + self.pregunta2.text() + ";"
                                  + self.respuesta2.text() + ";"
                                  + self.pregunta3.text() + ";"
                                  + self.respuesta3.text() + "\n", encoding='UTF-8'))
            #---se cierra el archivo
            self.file.close()

            #se abre el modo lectura de los datos
            self.file = open('datos/clientes.txt', 'rb')
            #se recorre el archivo linea por linea
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()

    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.NombredeUsuario.setText('')
        self.password.setText('')
        self.password2.setText('')
        self.Documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')

    def alternar_contrasena1(self):
        if self.activacion1 == True:
            self.activacion1 = False
            self.password.setEchoMode(QLineEdit.Normal)
            self.cambiarContra1.setIcon(QtGui.QIcon('Imagenes/iconos/ver.png'))
        elif self.activacion1 == False:
            self.activacion1 = True
            self.password.setEchoMode(QLineEdit.Password)
            self.cambiarContra1.setIcon(QtGui.QIcon('Imagenes/iconos/nover.png'))

    def alternar_contrasena2(self):
        if self.activacion2 == True:
            self.activacion2 = False
            self.password2.setEchoMode(QLineEdit.Normal)
            self.cambiarContra2.setIcon(QtGui.QIcon('Imagenes/iconos/ver.png'))
        elif self.activacion2 == False:
            self.activacion2 = True
            self.password2.setEchoMode(QLineEdit.Password)
            self.cambiarContra2.setIcon(QtGui.QIcon('Imagenes/iconos/nover.png'))

    def cerrar_mensaje(self):
        self.ventanadeDialogo.hide()

    def accion_botonatras(self):
        self.hide()
        self.ventanaAnteriorC.show()