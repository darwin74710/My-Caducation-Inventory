import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QSize
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

        self.ancho = 1000
        self.alto = 563
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Se crea una ventana para establecer la información y los botones de forma vertical
        self.fondo = QLabel()
        self.fondo.setFixedHeight(575)
        self.verticalP = QVBoxLayout()
        self.setCentralWidget(self.fondo)

        self.titulo = QLabel()
        self.tituloHorizontal = QHBoxLayout()
        self.titulo.setFixedHeight(60)

        self.tnumero1 = QLabel()
        self.tnumero1.setText("RECUPERAR USUARIOS")
        self.tnumero1.setFont(QFont("Arial", 40))
        self.tnumero1.setStyleSheet("color: white;")

        self.tituloHorizontal.addWidget(self.tnumero1)
        self.tituloHorizontal.addStretch()

        self.botonDesconectar = QPushButton()
        self.botonDesconectar.setFixedWidth(50)
        self.botonDesconectar.setFixedHeight(50)
        self.botonDesconectar.setStyleSheet("background-color: #8EA85D;")
        self.botonDesconectar.setIcon(QtGui.QIcon('Imagenes/iconos/casa.png'))
        self.botonDesconectar.setIconSize(QSize(40, 40))
        self.botonDesconectar.clicked.connect(self.accion_botonatras)

        self.tituloHorizontal.addWidget(self.botonDesconectar)

        self.titulo.setLayout(self.tituloHorizontal)

        self.verticalP.addWidget(self.titulo)

        # Desde aquí se trabaja el lado izquierdo de la ventana en donde se puede crear el usuario
        # Se pueden crear layouts y almacenarlos dentro de otros sin crear ventanas
        # Pero las ventanas se crean primero para poder establecer su tamaño al gusto junto al layout
        self.ventanaDatos = QLabel()
        self.ventanaDatos.setStyleSheet("background-color: #8EA85D;")
        self.ventanaDatos.setFixedHeight(400)
        self.horizontal = QHBoxLayout()

        self.labelIzquierdo = QLabel()
        self.ladoIzquierdo = QFormLayout()

        # Se crean los campos para ingresar los datos del usuario
        self.tituloD = QLabel("Documento de identidad")
        self.tituloD.setFixedHeight(100)
        self.tituloD.setAlignment(Qt.AlignBottom)
        self.tituloD.setFont(QFont("Arial", 12))
        self.tituloD.setStyleSheet("color: white;")

        self.ladoIzquierdo.addRow(self.tituloD)

        self.Documento = QLineEdit()
        self.Documento.setStyleSheet("background-color: white;")
        self.Documento.setFixedWidth(250)
        self.Documento.setFont(QFont("Arial", 12))
        self.Documento.setMaxLength(20)

        self.ladoIzquierdo.addRow(self.Documento)

        self.dialogo2 = QLabel()
        self.dialogo2.setFixedHeight(60)
        self.dialogo2.setText("1. Ingrese su documento y presione ''Buscar''."
                              "\n2. Ingrese las respuestas de las "
                              "preguntas de \nseguridad.")
        self.dialogo2.setFont(QFont("arial", 12))
        self.dialogo2.setStyleSheet("color: white;")

        self.ladoIzquierdo.addRow(self.dialogo2)

        self.labelIzquierdo.setLayout(self.ladoIzquierdo)
        self.horizontal.addWidget(self.labelIzquierdo)

        # Desde aquí se trabaja el lado derecho de la ventana en donde se crean y responden las preguntas de recuperación de usuario
        self.labelDerecho = QLabel()
        self.ladoDerecho = QFormLayout()

        # Se construyen los elementos para el ingreso de preguntas
        self.tituloPregunta1 = QLabel("Pregunta de verificacion 1")
        self.tituloPregunta1.setStyleSheet("color: white;")
        self.tituloPregunta1.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.tituloPregunta1)

        self.pregunta1 = QLineEdit()
        self.pregunta1.setContextMenuPolicy(Qt.NoContextMenu)
        self.pregunta1.setReadOnly(True)
        self.pregunta1.setStyleSheet("background-color: white;")
        self.pregunta1.setFixedWidth(320)
        self.pregunta1.setFont(QFont("Arial", 12))
        self.pregunta1.setMaxLength(70)

        self.ladoDerecho.addRow(self.pregunta1)

        self.tituloRespuesta1 = QLabel("Respuesta de verificacion 1")
        self.tituloRespuesta1.setStyleSheet("color: white;")
        self.tituloRespuesta1.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.tituloRespuesta1)

        self.respuesta1 = QLineEdit()
        self.respuesta1.setStyleSheet("background-color: white;")
        self.respuesta1.setFixedWidth(320)
        self.respuesta1.setFont(QFont("Arial", 12))
        self.respuesta1.setMaxLength(70)

        self.ladoDerecho.addRow(self.respuesta1)

        self.tituloPregunta2 = QLabel("Pregunta de verificacion 2")
        self.tituloPregunta2.setStyleSheet("color: white;")
        self.tituloPregunta2.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.tituloPregunta2)

        self.pregunta2 = QLineEdit()
        self.pregunta2.setContextMenuPolicy(Qt.NoContextMenu)
        self.pregunta2.setReadOnly(True)
        self.pregunta2.setStyleSheet("background-color: white;")
        self.pregunta2.setFixedWidth(320)
        self.pregunta2.setFont(QFont("Arial", 12))
        self.pregunta2.setMaxLength(70)

        self.ladoDerecho.addRow(self.pregunta2)

        self.tituloRespuesta2 = QLabel("Respuesta de verificacion 2")
        self.tituloRespuesta2.setStyleSheet("color: white;")
        self.tituloRespuesta2.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.tituloRespuesta2)

        self.respuesta2 = QLineEdit()
        self.respuesta2.setStyleSheet("background-color: white;")
        self.respuesta2.setFixedWidth(320)
        self.respuesta2.setFont(QFont("Arial", 12))
        self.respuesta2.setMaxLength(70)

        self.ladoDerecho.addRow(self.respuesta2)

        self.tituloPregunta3 = QLabel("Pregunta de verificacion 3")
        self.tituloPregunta3.setStyleSheet("color: white;")
        self.tituloPregunta3.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.tituloPregunta3)

        self.pregunta3 = QLineEdit()
        self.pregunta3.setContextMenuPolicy(Qt.NoContextMenu)
        self.pregunta3.setReadOnly(True)
        self.pregunta3.setStyleSheet("background-color: white;")
        self.pregunta3.setFixedWidth(320)
        self.pregunta3.setFont(QFont("Arial", 12))
        self.pregunta3.setMaxLength(70)

        self.ladoDerecho.addRow(self.pregunta3)

        self.tituloRespuesta3 = QLabel("Respuesta de verificacion 3")
        self.tituloRespuesta3.setStyleSheet("color: white;")
        self.tituloRespuesta3.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.tituloRespuesta3)

        self.respuesta3 = QLineEdit()
        self.respuesta3.setStyleSheet("background-color: white;")
        self.respuesta3.setFixedWidth(320)
        self.respuesta3.setFont(QFont("Arial", 12))
        self.respuesta3.setMaxLength(70)

        self.ladoDerecho.addRow(self.respuesta3)

        self.labelDerecho.setLayout(self.ladoDerecho)
        self.horizontal.addWidget(self.labelDerecho)
        self.ventanaDatos.setLayout(self.horizontal)
        self.verticalP.addWidget(self.ventanaDatos)

        # Se crea una ventana para distribuir los botones en la parte inferior
        self.ventanaBotones = QLabel()
        self.ventanaBotones.setFixedHeight(60)
        self.horizontalB = QHBoxLayout()

        self.botonBuscar = QPushButton("Buscar")
        self.botonBuscar.setFixedWidth(100)
        self.botonBuscar.setFixedHeight(40)
        self.botonBuscar.setFont(QFont("Arial", 12))
        self.botonBuscar.setStyleSheet("background-color: #8EA85D; color: white;")
        self.botonBuscar.clicked.connect(self.accion_botonBuscar)
        #ESPACIO PARA CONECTAR EL BOTÓN A UNA FUNCIÓN
        self.horizontalB.addWidget(self.botonBuscar)
        self.horizontalB.addStretch()

        # Creamos el botón para limpiar los campos de texto
        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(100)
        self.botonLimpiar.setFixedHeight(40)
        self.botonLimpiar.setFont(QFont("Arial", 12))
        self.botonLimpiar.setStyleSheet("background-color: #8EA85D; color: white;")
        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.horizontalB.addWidget(self.botonLimpiar)
        self.horizontalB.addStretch()

        # Creamos el botón para registrar los usuarios
        self.botonRecuperar = QPushButton("Recuperar")
        self.botonRecuperar.setFixedWidth(100)
        self.botonRecuperar.setFixedHeight(40)
        self.botonRecuperar.setFont(QFont("Arial", 12))
        self.botonRecuperar.setStyleSheet("background-color: #8EA85D; color: white;")
        self.botonRecuperar.clicked.connect(self.accion_botonRecuperar)

        self.horizontalB.addWidget(self.botonRecuperar)


        self.ventanaBotones.setLayout(self.horizontalB)
        self.verticalP.addWidget(self.ventanaBotones)

        self.fondo.setLayout(self.verticalP)

        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaDialogo.setFixedWidth(430)
        self.ventanaDialogo.setFixedHeight(100)
        self.ventanaDialogo.setWindowTitle("Formulario de registro")
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

    def accion_botonRecuperar(self):
        self.datosCorrectos = True

        self.ventanaDialogo.setWindowTitle("Recuperar usuario")
        self.ventanaDialogo.setWindowIcon(QtGui.QIcon("Imagenes/logo sin fondo.png"))
        self.ventanaDialogo.setStyleSheet("background-color: #9AC069;")
        self.mensaje.setStyleSheet("color: white;")

        if (self.pregunta1.text() == '' or self.pregunta2.text() == '' or self.pregunta3.text() == ''):
            self.datosCorrectos = False
            self.ventanaDialogo.setFixedWidth(300)
            self.ventanaDialogo.setFixedHeight(120)
            self.mensaje.setText("Para recuperar tú contraseña primero"
                                 "\ndebes buscar el número de documento "
                                 "\ncon el que fué registrada la cuenta.")
            self.ventanaDialogo.exec_()

        if(self.pregunta1.text() != '' and
            self.respuesta1.text() == '' and
            self.pregunta2.text() != '' and
            self.respuesta2.text() == '' and
            self.pregunta3.text() != '' and
            self.respuesta3.text() == ''):
            self.datosCorrectos = False

            self.ventanaDialogo.setFixedWidth(300)
            self.ventanaDialogo.setFixedHeight(100)
            self.mensaje.setText("Para recuperar la contraseña debe"
                                 "\ningresar la respuesta a cada pregunta.")
            self.ventanaDialogo.exec_()


        if (self.datosCorrectos):
            self.file = open('datos/usuarios.txt', 'rb')
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
                    lista[11],
                    lista[12],
                    lista[13]
                    )

                usuarios.append(u)

            self.file.close()
            existeDocumento = False

            resp1 = ''
            resp2 = ''
            resp3 = ''
            passw = ''
            name = ''

            for u in usuarios:
                if u.documento == self.Documento.text():
                    existeDocumento = True

                    resp1 = u.respuesta1
                    resp2 = u.respuesta2
                    resp3 = u.respuesta3
                    passw = u.password
                    name = u.usuario
                    break

            if(self.respuesta1.text().lower().strip() == resp1.lower().strip() and
                self.respuesta2.text().lower().strip() == resp2.lower().strip() and
                self.respuesta3.text().lower().strip() == resp3.lower().strip()):

                self.ventanaDialogo.setFixedWidth(320)
                self.ventanaDialogo.setFixedHeight(100)
                self.accion_botonLimpiar()
                self.mensaje.setText("Usuario: " + name +
                                    "\nContraseña: " + passw)
                self.ventanaDialogo.exec_()

            else:
                self.ventanaDialogo.setFixedWidth(320)
                self.ventanaDialogo.setFixedHeight(120)
                self.mensaje.setText("Las respuestas son incorrectas para éstas"
                                     "\npreguntas de recuperación."
                                     "\nVuelva a intentarlo.")
                self.ventanaDialogo.exec_()

    def accion_botonBuscar(self):
        self.ventanaDialogo.setWindowTitle("Recuperar usuario")
        self.ventanaDialogo.setWindowIcon(QtGui.QIcon("Imagenes/logo sin fondo.png"))
        self.ventanaDialogo.setStyleSheet("background-color: #9AC069;")
        self.mensaje.setStyleSheet("color: white;")

        self.datosCorrectos = True

        if (self.Documento.text() == ''):
            self.datosCorrectos = False
            self.ventanaDialogo.setFixedWidth(430)
            self.ventanaDialogo.setFixedHeight(100)
            self.mensaje.setText("Si va a buscar las preguntas para recuperar la contraseña"
                                 "\nprimero debe ingresar el documento.")
            self.ventanaDialogo.exec_()
        else:
            if (not self.Documento.text().isdigit()):
                self.datosCorrectos = False
                self.ventanaDialogo.setFixedWidth(350)
                self.ventanaDialogo.setFixedHeight(100)
                self.mensaje.setText("El documento debe ser numérico."
                                     "\nNo ingrese letras ni carácteres especiales.")

                self.ventanaDialogo.exec_()

        if (self.datosCorrectos):
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
                    lista[11],
                    lista[12],
                    lista[13]
                )
                usuarios.append(u)

            self.file.close()
            existeDocumento = False

            for u in usuarios:
                if u.documento == self.Documento.text():
                    self.pregunta1.setText(u.pregunta1)
                    self.pregunta2.setText(u.pregunta2)
                    self.pregunta3.setText(u.pregunta3)

                    existeDocumento = True
                    break

            if (existeDocumento == False):
                self.ventanaDialogo.setFixedWidth(320)
                self.ventanaDialogo.setFixedHeight(100)
                self.mensaje.setText("No existe un usuario con este documento:\n"
                                     + self.Documento.text())

                self.ventanaDialogo.exec_()

    def accion_botonatras(self):
        # Metodo para volver a la ventana del administrador
        self.hide()
        self.ventanaAnteriorC.show()

    def accion_botonOk(self):
        self.ventanaDialogo.hide()