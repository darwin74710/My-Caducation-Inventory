import sys

from PyQt5 import QtCore
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
                             "\nen el formulario. Los campos marcados con un"
                             "\nasterisco (*) son obligatorios.")

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

        #----- LAYOUT DERECHO -----
        self.ladoDerecho = QFormLayout()

        self.ladoDerecho.setContentsMargins(50, 0, 0, 0)

        self.letreroD = QLabel()

        self.letreroD.setText("Recuperar contraseña")

        self.letreroD.setFont(QFont("arial", 20))

        self.letreroD.setStyleSheet("color: white;")

        self.ladoDerecho.addRow(self.letreroD)

        self.letreroD2 = QLabel()

        self.letreroD2.setFixedWidth(340)

        self.letreroD2.setText("Ingrese la informacion para recuperar"
                               "\nla contraseña. los campos marcados"
                               "\ncon asterisco (*) son obligatorios.")

        self.letreroD2.setFont(QFont("arial", 10))

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

        self.ladoDerecho.addRow(self.labelPregunta1)

        self.pregunta1 = QLineEdit()
        self.pregunta1.setStyleSheet("background-color: white;")
        self.pregunta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta1)

        #-----respuesta pregunta de validacion 1
        self.labelRespuesta1 = QLabel("Respuesta de verificacion 1*")

        self.ladoDerecho.addRow(self.labelRespuesta1)


        self.respuesta1 = QLineEdit()
        self.respuesta1.setStyleSheet("background-color: white;")
        self.respuesta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta1)

        #----- Segunda Pregunta de verificacion
        self.labelPregunta2 = QLabel("Pregunta de verificacion 2*")

        self.ladoDerecho.addRow(self.labelPregunta2)

        self.pregunta2 = QLineEdit()
        self.pregunta2.setStyleSheet("background-color: white;")
        self.pregunta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta2)

        # -----respuesta pregunta de validacion 2
        self.labelRespuesta2 = QLabel("Respuesta de verificacion 2*")

        self.ladoDerecho.addRow(self.labelRespuesta2)

        self.respuesta2 = QLineEdit()
        self.respuesta2.setStyleSheet("background-color: white;")
        self.respuesta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta2)

        #-----Tercera pregunta de verificacion
        self.labelPregunta3 = QLabel("Pregunta de verificacion 3*")

        self.ladoDerecho.addRow(self.labelPregunta3)

        self.pregunta3 = QLineEdit()
        self.pregunta3.setStyleSheet("background-color: white;")
        self.pregunta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta3)

        # -----respuesta pregunta de validacion 3
        self.labelRespuesta3 = QLabel("Respuesta de verificacion 3*")

        self.ladoDerecho.addRow(self.labelRespuesta3)

        self.respuesta3 = QLineEdit()
        self.respuesta3.setStyleSheet("background-color: white;")
        self.respuesta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta3)

        #----- se crea boton para buscarlas preguntas
        self.botonBuscar = QPushButton("Buscar")

        self.botonBuscar.setFixedWidth(90)

        self.botonBuscar.setStyleSheet("background-color: #9AC069;"
                                        "color: white;"
                                        "padding: 10px;"
                                        "margin-top: 40px;"
                                       )

        #-----Boton recuperar contraseña
        self.botonRecuperar = QPushButton("Recuperar")

        self.botonRecuperar.setFixedWidth(90)

        self.botonRecuperar.setStyleSheet("background-color: #9AC069;"
                                       "color: white;"
                                       "padding: 10px;"
                                       "margin-top: 40px;"
                                       )

        self.ladoDerecho.addRow(self.botonBuscar, self.botonRecuperar)

        self.horizontal.addLayout(self.ladoDerecho)

        #----- SE COLOCA LA FINAL -----
        self.fondo.setLayout(self.horizontal)

    def accion_botonRegistrar(self):

        self.ventanadeDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        self.ventanadeDialogo.resize(300, 150)

        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanadeDialogo.accept)

        self.ventanadeDialogo.setWindowTitle("Formulario de registro")

        self.ventanadeDialogo.setWindowModality(Qt.ApplicationModal)

        self.vertical = QVBoxLayout()

        self.mensaje = QLabel("")

        self.mensaje.setStyleSheet("background-color: #9AC069 ; color: white ; padding: 10px;")

        self.vertical.addWidget(self.mensaje)

        self.vertical.addWidget(self.opciones)

        self.ventanadeDialogo.setLayout(self.vertical)

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



