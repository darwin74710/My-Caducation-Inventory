import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QPushButton, QWidget, QLineEdit, QLabel, \
    QVBoxLayout, QHBoxLayout, QGridLayout, QDialog, QDialogButtonBox, QFormLayout

class CrearUsuario(QMainWindow):
    def __init__(self, anteriorC):
        super(CrearUsuario, self).__init__(anteriorC)
        # Se crea la ventana principal junto a sus propiedades
        self.ventanaAnteriorC = anteriorC

        self.setWindowTitle("Creación de usuario")
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
        self.tnumero1.setText("REGISTRAR USUARIOS")
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
        self.titulo1 = QLabel("Nombre completo")
        self.titulo1.setFont(QFont("Arial", 12))
        self.titulo1.setStyleSheet("color: white;")

        self.ladoIzquierdo.addRow(self.titulo1)

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setStyleSheet("background-color: white;")
        self.nombreCompleto.setFixedWidth(250)
        self.nombreCompleto.setFont(QFont("Arial", 12))
        self.nombreCompleto.setMaxLength(100)

        self.ladoIzquierdo.addRow(self.nombreCompleto)

        self.titulo2 = QLabel("Nombre de usuario")
        self.titulo2.setFont(QFont("Arial", 12))
        self.titulo2.setStyleSheet("color: white;")

        self.ladoIzquierdo.addRow(self.titulo2)

        self.NombredeUsuario = QLineEdit()
        self.NombredeUsuario.setStyleSheet("background-color: white;")
        self.NombredeUsuario.setFixedWidth(250)
        self.NombredeUsuario.setFont(QFont("Arial", 12))
        self.NombredeUsuario.setMaxLength(30)

        self.ladoIzquierdo.addRow(self.NombredeUsuario)

        self.titulo3 = QLabel("Contraseña")
        self.titulo3.setFont(QFont("Arial", 12))
        self.titulo3.setStyleSheet("color: white;")

        self.ladoIzquierdo.addRow(self.titulo3)

        self.password = QLineEdit()
        self.password.setStyleSheet("background-color: white;")
        self.password.setFixedWidth(250)
        self.password.setFont(QFont("Arial", 12))
        self.password.setMaxLength(20)
        self.password.setEchoMode(QLineEdit.Password)

        self.cambiarContra1 = QPushButton()
        self.cambiarContra1.setFixedWidth(25)
        self.cambiarContra1.clicked.connect(self.alternar_contrasena1)
        self.activacion1 = True
        self.cambiarContra1.setIcon(QtGui.QIcon('Imagenes/iconos/nover.png'))

        self.ladoIzquierdo.addRow(self.password, self.cambiarContra1)

        self.titulo4 = QLabel("Confirmar Contraseña")
        self.titulo4.setFont(QFont("Arial", 12))
        self.titulo4.setStyleSheet("color: white;")

        self.ladoIzquierdo.addRow(self.titulo4)

        self.password2 = QLineEdit()
        self.password2.setStyleSheet("background-color: white;")
        self.password2.setFixedWidth(250)
        self.password2.setFont(QFont("Arial", 12))
        self.password2.setMaxLength(20)
        self.password2.setEchoMode(QLineEdit.Password)

        self.cambiarContra2 = QPushButton()
        self.cambiarContra2.setFixedWidth(25)
        self.cambiarContra2.clicked.connect(self.alternar_contrasena2)
        self.activacion2 = True
        self.cambiarContra2.setIcon(QtGui.QIcon('Imagenes/iconos/nover.png'))

        self.ladoIzquierdo.addRow(self.password2, self.cambiarContra2)

        self.titulo5 = QLabel("Documento de identidad")
        self.titulo5.setFont(QFont("Arial", 12))
        self.titulo5.setStyleSheet("color: white;")

        self.ladoIzquierdo.addRow(self.titulo5)

        self.Documento = QLineEdit()
        self.Documento.setStyleSheet("background-color: white;")
        self.Documento.setFixedWidth(250)
        self.Documento.setFont(QFont("Arial", 12))
        self.Documento.setMaxLength(20)

        self.ladoIzquierdo.addRow(self.Documento)

        self.titulo6 = QLabel("Correo electronico")
        self.titulo6.setFont(QFont("Arial", 12))
        self.titulo6.setStyleSheet("color: white;")

        self.ladoIzquierdo.addRow(self.titulo6)

        self.correo = QLineEdit()
        self.correo.setStyleSheet("background-color: white;")
        self.correo.setFixedWidth(250)
        self.correo.setFont(QFont("Arial", 12))
        self.correo.setMaxLength(100)

        self.ladoIzquierdo.addRow(self.correo)

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
        self.ventanaBotones.setContentsMargins(0, 0, 0, 0)
        self.horizontalB = QHBoxLayout()

        # Creamos el botón para registrar los usuarios
        self.botonRegistrar = QPushButton("Registrar")
        self.botonRegistrar.setFixedWidth(100)
        self.botonRegistrar.setFixedHeight(40)
        self.botonRegistrar.setFont(QFont("Arial", 12))
        self.botonRegistrar.setStyleSheet("background-color: #8EA85D;"
                                          "color: white;")
        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        self.horizontalB.addStretch()
        self.horizontalB.addWidget(self.botonRegistrar)

        # Creamos el botón para limpiar los campos de texto
        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(100)
        self.botonLimpiar.setFixedHeight(40)
        self.botonLimpiar.setFont(QFont("Arial", 12))
        self.botonLimpiar.setStyleSheet("background-color: #8EA85D;"
                                        "color: white;")
        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.horizontalB.addStretch()
        self.horizontalB.addWidget(self.botonLimpiar)
        self.horizontalB.addStretch()

        self.ventanaBotones.setLayout(self.horizontalB)
        self.verticalP.addWidget(self.ventanaBotones)

        self.fondo.setLayout(self.verticalP)

    def accion_botonRegistrar(self):
        # Metodo para guardar el usuario en un archivo plano
        # Se crea la ventana de validación
        self.ventanadeDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.formulario = QFormLayout()
        self.ventanadeDialogo.setWindowIcon(QtGui.QIcon("Imagenes/logo sin fondo.png"))
        self.ventanadeDialogo.setFixedWidth(300)
        self.ventanadeDialogo.setFixedHeight(90)
        self.ventanadeDialogo.setStyleSheet("background-color: #9AC069;")
        self.ventanadeDialogo.setWindowTitle("Formulario de registro")
        self.ventanadeDialogo.setWindowModality(Qt.ApplicationModal)

        # Se crean los elementos a mostrar
        self.espacio2 = QLabel()
        self.espacio2.setFixedHeight(5)
        self.formulario.addRow(self.espacio2)

        self.mensaje = QLabel("")
        self.mensaje.setFont(QFont("Arial", 12))
        self.mensaje.setStyleSheet("color: white;")

        self.formulario.addRow(self.mensaje)
        self.formulario.addRow(self.espacio2)

        self.espacio = QLabel()
        self.espacio.setFixedWidth(190)

        self.atras = QPushButton("Atrás")
        self.atras.setFixedWidth(80)
        self.atras.setFixedHeight(25)
        self.atras.setFont(QFont("Arial", 12))
        self.atras.setStyleSheet("background-color: #8EA85D; color: white;")
        self.atras.clicked.connect(self.cerrar_mensaje)

        self.formulario.addRow(self.espacio, self.atras)

        self.ventanadeDialogo.setLayout(self.formulario)

        self.datosCorrectos = True

        # Validación para no repetir la contraseña
        if (
            self.password.text() != self.password2.text()
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Las contraseñas no son iguales")

            self.ventanadeDialogo.exec_()

        # Validación para evitar campos vacios
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

        # Sl ingresar datos correctos
        if self.datosCorrectos:
            # Se abre el archivo plano y se añade la información en binario decodificandola en formato occidental
            # El ab se establece para guardar información
            self.file = open('datos/usuarios.txt', 'ab')

            self.file.write(bytes(self.nombreCompleto.text() + ";"
                                  + self.NombredeUsuario.text() + ";"
                                  + self.password.text() + ";"
                                    #Se eliminó la función de guardar la contraseña número 2
                                    #para no tener problema con la función
                                    #recuperar usuario.
                                  #+ self.password2.text() + ";"
                                  + self.Documento.text() + ";"
                                  + self.correo.text() + ";"
                                  + self.pregunta1.text() + ";"
                                  + self.respuesta1.text() + ";"
                                  + self.pregunta2.text() + ";"
                                  + self.respuesta2.text() + ";"
                                  + self.pregunta3.text() + ";"
                                  + self.respuesta3.text() + "\n", encoding='UTF-8'))
            self.file.close()

            # Se abre el archivo plano en modo lectura y se muestra la inforamción de el
            # El rb se establece para leer información
            self.file = open('datos/usuarios.txt', 'rb')
            #se recorre el archivo linea por linea
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()

    def accion_botonLimpiar(self):
        # Metodo para vaciar los campos de información
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
        # Metodo para ver y no ver la contraseña
        if self.activacion1 == True:
            self.activacion1 = False
            self.password.setEchoMode(QLineEdit.Normal)
            self.cambiarContra1.setIcon(QtGui.QIcon('Imagenes/iconos/ver.png'))
        elif self.activacion1 == False:
            self.activacion1 = True
            self.password.setEchoMode(QLineEdit.Password)
            self.cambiarContra1.setIcon(QtGui.QIcon('Imagenes/iconos/nover.png'))

    def alternar_contrasena2(self):
        # Metodo para ver y no ver la contraseña 2
        # Toca separarlos en diferentes metodos para evitar errores
        if self.activacion2 == True:
            self.activacion2 = False
            self.password2.setEchoMode(QLineEdit.Normal)
            self.cambiarContra2.setIcon(QtGui.QIcon('Imagenes/iconos/ver.png'))
        elif self.activacion2 == False:
            self.activacion2 = True
            self.password2.setEchoMode(QLineEdit.Password)
            self.cambiarContra2.setIcon(QtGui.QIcon('Imagenes/iconos/nover.png'))

    def cerrar_mensaje(self):
        # Metodo para cerrar la ventana de validación
        self.ventanadeDialogo.hide()

    def accion_botonatras(self):
        # Metodo para volver a la ventana del administrador
        self.hide()
        self.ventanaAnteriorC.show()