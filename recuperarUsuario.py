import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QPushButton, QWidget, QLineEdit, QLabel, \
    QVBoxLayout, QHBoxLayout, QGridLayout, QDialog, QDialogButtonBox, QFormLayout

from cliente import Cliente

class RecuperarUsuario(QMainWindow):
    def __init__(self, anteriorC):
        super(RecuperarUsuario, self).__init__(anteriorC)
        # Se crea la ventana principal junto a sus propiedades
        self.ventanaAnteriorC = anteriorC

        self.setWindowTitle("Recuperar Usuario")
        self.setStyleSheet("background-color: #9AC069;")

        self.ancho = 800
        self.alto = 640
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Se crea una ventana para establecer la información y los botones de forma vertical
        self.fondo = QLabel()
        self.verticalP = QVBoxLayout()
        self.setCentralWidget(self.fondo)

        # Se crea una ventana para establecer la información de forma horizontal
        self.ventanaDatos = QLabel()
        self.horizontal = QHBoxLayout()

        self.txtnumero1 = QLabel()
        self.txtnumero1.setText(" <b>Recuperar Usuario</b>")
        self.txtnumero1.setFont(QFont("arial", 24))
        self.txtnumero1.setFixedHeight(100)
        self.txtnumero1.setStyleSheet("color: white; margin-bottom: 30px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid white;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        self.verticalP.addWidget(self.txtnumero1)

        self.dialogo1 = QLabel()
        #self.textnum1.setFixedWidth(340)
        self.dialogo1.setFixedHeight(130)
        self.dialogo1.setText("Bienvenido a My Caducation Inventory."
                              "\nPor favor, ingrese su documento y prosiga con las "
                              "instrucciones dadas en el formulario.")
        self.dialogo1.setFont(QFont("arial", 12))
        self.dialogo1.setStyleSheet("color: white; margin-bottom: 40px;"
                                     "margin-top: 20px;"
                                     "padding-bottom: 15px;"
                                     "border: 2px solid white;"
                                     "border-left: none;"
                                     "border-right: none;"
                                     "border-top: none;")

        self.verticalP.addWidget(self.dialogo1)
        # Desde aquí se trabaja el lado izquierdo de la ventana en donde se puede crear el usuario
        self.ladoIzquierdo = QFormLayout()



        self.titulo5 = QLabel("Documento de identidad*")
        self.titulo5.setFont(QFont("Arial", 12))
        self.titulo5.setStyleSheet("color: white;")

        self.ladoIzquierdo.addRow(self.titulo5)

        self.Documento = QLineEdit()
        self.Documento.setStyleSheet("background-color: white;")
        self.Documento.setFixedWidth(250)
        self.Documento.setFont(QFont("Arial", 12))
        self.Documento.setMaxLength(14)

        self.ladoIzquierdo.addRow(self.Documento)

        self.dialogo2 = QLabel()
        self.dialogo2.setFixedHeight(130)
        self.dialogo2.setText("1. Ingrese su documento y presione ''Buscar''."
                              "\n2. Ingrese las respuestas de las"
                              "preguntas de \nseguridad.")

        self.dialogo2.setFont(QFont("arial", 12))
        self.dialogo2.setStyleSheet("color: white;")

        self.ladoIzquierdo.addRow(self.dialogo2)

        self.horizontal.addLayout(self.ladoIzquierdo)

        # Desde aquí se trabaja el lado derecho de la ventana en donde se crean y responden las preguntas de recuperación de usuario
        self.ladoDerecho = QFormLayout()

        # Se construyen los elementos para el ingreso de preguntas
        self.tituloPregunta1 = QLabel("Pregunta de verificacion 1*")
        self.tituloPregunta1.setStyleSheet("color: white;")
        self.tituloPregunta1.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.tituloPregunta1)

        self.pregunta1 = QLineEdit()
        self.pregunta1.setStyleSheet("background-color: white;")
        self.pregunta1.setFixedWidth(320)
        self.pregunta1.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.pregunta1)

        self.tituloRespuesta1 = QLabel("Respuesta de verificacion 1*")
        self.tituloRespuesta1.setStyleSheet("color: white;")
        self.tituloRespuesta1.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.tituloRespuesta1)

        self.respuesta1 = QLineEdit()
        self.respuesta1.setStyleSheet("background-color: white;")
        self.respuesta1.setFixedWidth(320)
        self.respuesta1.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.respuesta1)

        self.tituloPregunta2 = QLabel("Pregunta de verificacion 2*")
        self.tituloPregunta2.setStyleSheet("color: white;")
        self.tituloPregunta2.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.tituloPregunta2)

        self.pregunta2 = QLineEdit()
        self.pregunta2.setStyleSheet("background-color: white;")
        self.pregunta2.setFixedWidth(320)
        self.pregunta2.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.pregunta2)

        self.tituloRespuesta2 = QLabel("Respuesta de verificacion 2*")
        self.tituloRespuesta2.setStyleSheet("color: white;")
        self.tituloRespuesta2.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.tituloRespuesta2)

        self.respuesta2 = QLineEdit()
        self.respuesta2.setStyleSheet("background-color: white;")
        self.respuesta2.setFixedWidth(320)
        self.respuesta2.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.respuesta2)

        self.tituloPregunta3 = QLabel("Pregunta de verificacion 3*")
        self.tituloPregunta3.setStyleSheet("color: white;")
        self.tituloPregunta3.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.tituloPregunta3)

        self.pregunta3 = QLineEdit()
        self.pregunta3.setStyleSheet("background-color: white;")
        self.pregunta3.setFixedWidth(320)
        self.pregunta3.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.pregunta3)

        self.tituloRespuesta3 = QLabel("Respuesta de verificacion 3*")
        self.tituloRespuesta3.setStyleSheet("color: white;")
        self.tituloRespuesta3.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.tituloRespuesta3)

        self.respuesta3 = QLineEdit()
        self.respuesta3.setStyleSheet("background-color: white;")
        self.respuesta3.setFixedWidth(320)
        self.respuesta3.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.respuesta3)

        self.horizontal.addLayout(self.ladoDerecho)
        self.ventanaDatos.setLayout(self.horizontal)
        self.verticalP.addWidget(self.ventanaDatos)

        # Se crea una ventana para distribuir los botones en la parte inferior
        self.ventanaBotones = QLabel()
        self.ventanaBotones.setFixedHeight(100)
        self.horizontalB = QHBoxLayout()

        self.botonBuscar = QPushButton("Buscar")
        self.botonBuscar.setFixedWidth(100)
        self.botonBuscar.setFont(QFont("Arial", 12))
        self.botonBuscar.setStyleSheet("background-color: #8EA85D;"
                                          "color: white;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonBuscar.clicked.connect(self.accion_botonBuscar)
        #ESPACIO PARA CONECTAR EL BOTÓN A UNA FUNCIÓN
        self.horizontalB.addWidget(self.botonBuscar)


        # Creamos el botón para registrar los usuarios
        self.botonRecuperar = QPushButton("Recuperar")
        self.botonRecuperar.setFixedWidth(100)
        self.botonRecuperar.setFont(QFont("Arial", 12))
        self.botonRecuperar.setStyleSheet("background-color: #8EA85D;"
                                          "color: white;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonRecuperar.clicked.connect(self.accion_botonRecuperar)

        self.horizontalB.addWidget(self.botonRecuperar)

        # Creamos el botón para limpiar los campos de texto
        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(100)
        self.botonLimpiar.setFont(QFont("Arial", 12))
        self.botonLimpiar.setStyleSheet("background-color: #8EA85D;"
                                        "color: white;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")
        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.horizontalB.addWidget(self.botonLimpiar)
        self.horizontalB.addStretch()

        # Creamos el botón para retroceder a la pestaña administrador
        self.botonAtras = QPushButton("Atras")
        self.botonAtras.setFixedWidth(100)
        self.botonAtras.setFont(QFont("Arial", 12))
        self.botonAtras.setStyleSheet("background-color: #8EA85D;"
                                       "color: white;"
                                       "padding: 10px;"
                                       "margin-top: 40px;"
                                       )
        self.botonAtras.clicked.connect(self.accion_botonatras)

        self.horizontalB.addWidget(self.botonAtras)

        self.ventanaBotones.setLayout(self.horizontalB)
        self.verticalP.addWidget(self.ventanaBotones)

        self.fondo.setLayout(self.verticalP)


        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        self.ventanaDialogo.resize(300, 150)
        self.ventanaDialogo.setWindowTitle("Formulario de registro")
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        self.vertical = QVBoxLayout()

        self.mensaje = QLabel("")
        self.mensaje.setStyleSheet("background-color: ; color: black; padding: 10px;")

        self.vertical.addWidget(self.mensaje)

        self.cajaBoton = QLabel()
        self.cajaBH = QHBoxLayout()
        self.cajaBH.addStretch()

        self.botonOk = QPushButton("Ok")
        self.botonOk.setFixedWidth(50)
        self.botonOk.setFixedHeight(25)
        self.botonOk.setStyleSheet("background-color: #8EA85D; color: white;")
        self.botonOk.setFont(QFont("Arial", 12))
        self.botonOk.clicked.connect(self.accion_botonOk)

        self.cajaBH.addWidget(self.botonOk)
        self.cajaBoton.setLayout(self.cajaBH)








        self.vertical.addWidget(self.cajaBoton)

        self.ventanaDialogo.setLayout(self.vertical)


        self.datosCorrectos = True




    def accion_botonLimpiar(self):
        # Metodo para vaciar los campos de información
        self.Documento.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')

    def botonBuscar(self):
        pass

    def cerrar_mensaje(self):
        # Metodo para cerrar la ventana de validación
        self.ventanadeDialogo.hide()

    def accion_botonRecuperar(self):

        self.datosCorrectos = True

        self.ventanaDialogo.setWindowTitle("Recuperar usuario")
        self.ventanaDialogo.setWindowIcon(QtGui.QIcon("Imagenes/logo sin fondo.png"))
        self.ventanaDialogo.setStyleSheet("background-color: #9AC069;")
        self.mensaje.setStyleSheet("color: white;")

        if (
            self.pregunta1.text() == '' or
            self.pregunta2.text() == '' or
            self.pregunta3.text() == ''
        ):

            self.datosCorrectos = False

            self.mensaje.setText("Para recuperar tú contraseña primero"
                                 "\ndebes buscar el número de documento "
                                 "\ncon el que fué registrada la cuenta.")

            self.ventanaDialogo.exec_()

        if(
            self.pregunta1.text() != '' and
            self.respuesta1.text() == '' and
            self.pregunta2.text() != '' and
            self.respuesta2.text() == '' and
            self.pregunta3.text() != '' and
            self.respuesta3.text() == ''
        ):

            self.datosCorrectos = False

            self.mensaje.setText("Para recuperar la contraseña debe"
                                 "\ningresar la respuesta a cada pregunta.")

            self.ventanaDialogo.exec_()


        if (
            self.datosCorrectos
        ):

            self.file = open('datos/usuarios.txt', 'rb')

            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                lista = linea.split(";")

                if linea == '':
                    break

                u= Cliente(
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
                    lista[10]
                    )

                usuarios.append(u)

            self.file.close()

            existeDocumento = False

            resp1 = ''
            resp2 = ''
            resp3 = ''
            passw = ''

            for u in usuarios:

                if u.documento == self.Documento.text():

                    existeDocumento = True

                    resp1 = u.respuesta1
                    resp2 = u.respuesta2
                    resp3 = u.respuesta3
                    passw = u.password

                    break

            if(
                self.respuesta1.text().lower().strip() == resp1.lower().strip() and
                self.respuesta2.text().lower().strip() == resp2.lower().strip() and
                self.respuesta3.text().lower().strip() == resp3.lower().strip()
            ):

                self.accion_botonLimpiar()

                self.mensaje.setText("Contraseña: " + passw)

                self.ventanaDialogo.exec_()

            else:

                self.mensaje.setText("Las respuestas son incorrectas para éstas"
                                     "\npreguntas de recuperación."
                                     "\nVuelva a intentarlo.")

                self.ventanaDialogo.exec_()





    def accion_botonBuscar(self):

        self.ventanaDialogo.setWindowTitle("Buscar documento.")
        self.ventanaDialogo.setWindowIcon(QtGui.QIcon("Imagenes/logo sin fondo.png"))
        self.ventanaDialogo.setStyleSheet("background-color: #9AC069;")
        self.mensaje.setStyleSheet("color: white;")

        self.datosCorrectos = True

        if (
                self.Documento.text() == ''
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Si va a buscar las preguntas"
                                 "para recuperar la contraseña"
                                 "\ndebe primero, ingresar el documento.")

            self.ventanaDialogo.exec_()

        if (
                not self.Documento.text().isnumeric()
        ):
            self.datosCorrectos = False

            self.mensaje.setText("El documento debe ser numérico."
                                 "\nno ingrese letras"
                                 " ni carácteres especiales.")

            self.ventanaDialogo.exec_()

            self.Documento.setText('')

        if (
                self.datosCorrectos
        ):
            self.file = open('datos/usuarios.txt', 'rb')

            # Lista vacía para guardar usuarios.

            usuarios = []

            while self.file:

                linea = self.file.readline().decode('UTF-8')

                lista = linea.split(";")

                if linea == '':
                    break

                u = Cliente(
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
                )

                usuarios.append(u)
                print(u)


            self.file.close()

            existeDocumento = False

            for u in usuarios:

                if u.documento == self.Documento.text():
                    self.pregunta1.setText(u.pregunta1)
                    self.pregunta2.setText(u.pregunta2)
                    self.pregunta3.setText(u.pregunta3)

                    existeDocumento = True

                    break

            if(
                 existeDocumento == False
            ):
                self.mensaje.setText("No existe un usuario con este documento:\n"
                                     + self.Documento.text())

                self.ventanaDialogo.exec_()

    def accion_botonatras(self):
        # Metodo para volver a la ventana del administrador
        self.hide()
        self.ventanaAnteriorC.show()


    def accion_botonOk(self):


        self.ventanaDialogo.hide()


