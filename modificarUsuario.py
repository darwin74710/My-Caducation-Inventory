import math
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QPushButton, QWidget, QLineEdit, QLabel, \
    QVBoxLayout, QHBoxLayout, QGridLayout, QDialog, QDialogButtonBox, QFormLayout, QComboBox, QScrollArea, QButtonGroup

from cliente import Cliente

class ModificarUsuario(QMainWindow):
    def __init__(self, anterior):
        super(ModificarUsuario, self).__init__(anterior)
        # Se crea la ventana principal junto a sus propiedades
        self.ventanaAnteriorC = anterior

        self.colorFondo1 = anterior.colorFondo1
        self.colorFondo2 = anterior.colorFondo2
        self.colorFondo3 = anterior.colorFondo3
        self.colorLetra1 = anterior.colorLetra1
        self.colorLetra2 = anterior.colorLetra2
        self.colorLetra3 = anterior.colorLetra3
        self.colorBotones1 = anterior.colorBotones1
        self.colorBotones2 = anterior.colorBotones2
        self.colorBotones3 = anterior.colorBotones3
        self.colorLogo = anterior.colorLogo

        self.setWindowTitle("Modificar usuario")
        self.setStyleSheet("background-color: " + self.colorFondo1 + ";")

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
        self.tnumero1.setText("MODIFICAR USUARIOS")
        self.tnumero1.setFont(QFont("Arial", 40))
        self.tnumero1.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.tituloHorizontal.addWidget(self.tnumero1)
        self.tituloHorizontal.addStretch()

        self.botonDesconectar = QPushButton()
        self.botonDesconectar.setFixedWidth(50)
        self.botonDesconectar.setFixedHeight(50)
        self.botonDesconectar.setStyleSheet("background-color: " + self.colorBotones1 + ";")
        self.botonDesconectar.setIcon(QtGui.QIcon('Imagenes/iconos/casa.png'))
        self.botonDesconectar.setIconSize(QSize(40, 40))
        self.botonDesconectar.clicked.connect(self.accion_botonatras)

        self.tituloHorizontal.addWidget(self.botonDesconectar)

        self.titulo.setLayout(self.tituloHorizontal)

        self.verticalP.addWidget(self.titulo)

        self.ventanaFondo = QLabel()
        self.horizontalFondo = QHBoxLayout()

        self.ventanaDatos = QLabel()
        self.ventanaDatos.setStyleSheet("background-color: " + self.colorFondo2 + ";")
        self.ventanaDatos.setFixedHeight(400)
        self.ventanaDatos.setFixedWidth(660)
        self.horizontal = QHBoxLayout()

        self.labelIzquierdo = QLabel()
        self.labelIzquierdo.setFixedWidth(300)
        self.ladoIzquierdo = QFormLayout()

        # Se crean los campos para ingresar los datos del usuario

        self.filtro = QComboBox()
        self.filtro.setFixedWidth(250)
        self.filtro.setFixedHeight(20)
        self.filtro.setStyleSheet("background-color: white;")
        self.filtro.setFont(QFont("Arial", 12))
        self.filtro.addItems(["Administrador", "Usuario"])

        self.ladoIzquierdo.addRow(self.filtro)

        self.titulo1 = QLabel("Nombre completo")
        self.titulo1.setFont(QFont("Arial", 12))
        self.titulo1.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.ladoIzquierdo.addRow(self.titulo1)

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setStyleSheet("background-color: white;")
        self.nombreCompleto.setFixedWidth(250)
        self.nombreCompleto.setFont(QFont("Arial", 12))
        self.nombreCompleto.setMaxLength(100)

        self.ladoIzquierdo.addRow(self.nombreCompleto)

        self.titulo2 = QLabel("Nombre de usuario")
        self.titulo2.setFont(QFont("Arial", 12))
        self.titulo2.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.ladoIzquierdo.addRow(self.titulo2)

        self.NombredeUsuario = QLineEdit()
        self.NombredeUsuario.setStyleSheet("background-color: white;")
        self.NombredeUsuario.setFixedWidth(250)
        self.NombredeUsuario.setFont(QFont("Arial", 12))
        self.NombredeUsuario.setMaxLength(20)

        self.ladoIzquierdo.addRow(self.NombredeUsuario)

        self.titulo3 = QLabel("Contraseña")
        self.titulo3.setFont(QFont("Arial", 12))
        self.titulo3.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.ladoIzquierdo.addRow(self.titulo3)

        self.password = QLineEdit()
        self.password.setStyleSheet("background-color: white;")
        self.password.setFixedWidth(250)
        self.password.setFont(QFont("Arial", 12))
        self.password.setMaxLength(20)
        self.password.setEchoMode(QLineEdit.Password)

        self.cambiarContra1 = QPushButton()
        self.cambiarContra1.setFixedWidth(25)
        self.cambiarContra1.setStyleSheet("background-color: " + self.colorBotones2 + ";")
        self.cambiarContra1.clicked.connect(self.alternar_contrasena1)
        self.activacion1 = True
        self.cambiarContra1.setIcon(QtGui.QIcon('Imagenes/iconos/nover.png'))

        self.ladoIzquierdo.addRow(self.password, self.cambiarContra1)

        self.titulo4 = QLabel("Confirmar Contraseña")
        self.titulo4.setFont(QFont("Arial", 12))
        self.titulo4.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.ladoIzquierdo.addRow(self.titulo4)

        self.password2 = QLineEdit()
        self.password2.setStyleSheet("background-color: white;")
        self.password2.setFixedWidth(250)
        self.password2.setFont(QFont("Arial", 12))
        self.password2.setMaxLength(20)
        self.password2.setEchoMode(QLineEdit.Password)

        self.cambiarContra2 = QPushButton()
        self.cambiarContra2.setFixedWidth(25)
        self.cambiarContra2.setStyleSheet("background-color: " + self.colorBotones2 + ";")
        self.cambiarContra2.clicked.connect(self.alternar_contrasena2)
        self.activacion2 = True
        self.cambiarContra2.setIcon(QtGui.QIcon('Imagenes/iconos/nover.png'))

        self.ladoIzquierdo.addRow(self.password2, self.cambiarContra2)

        self.titulo5 = QLabel("Documento de identidad")
        self.titulo5.setFont(QFont("Arial", 12))
        self.titulo5.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.ladoIzquierdo.addRow(self.titulo5)

        self.Documento = QLineEdit()
        self.Documento.setStyleSheet("background-color: white;")
        self.Documento.setFixedWidth(250)
        self.Documento.setFont(QFont("Arial", 12))
        self.Documento.setMaxLength(20)

        self.ladoIzquierdo.addRow(self.Documento)

        self.titulo6 = QLabel("Correo electronico")
        self.titulo6.setFont(QFont("Arial", 12))
        self.titulo6.setStyleSheet("color: " + self.colorLetra1 + ";")

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

        self.espaciado = QLabel()
        self.espaciado.setFixedHeight(20)
        self.ladoDerecho.addRow(self.espaciado)

        # Se construyen los elementos para el ingreso de preguntas
        self.tituloPregunta1 = QLabel("Pregunta de verificacion 1")
        self.tituloPregunta1.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.tituloPregunta1.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.tituloPregunta1)

        self.pregunta1 = QLineEdit()
        self.pregunta1.setStyleSheet("background-color: white;")
        self.pregunta1.setFixedWidth(320)
        self.pregunta1.setFont(QFont("Arial", 12))
        self.pregunta1.setMaxLength(70)

        self.ladoDerecho.addRow(self.pregunta1)

        self.tituloRespuesta1 = QLabel("Respuesta de verificacion 1")
        self.tituloRespuesta1.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.tituloRespuesta1.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.tituloRespuesta1)

        self.respuesta1 = QLineEdit()
        self.respuesta1.setStyleSheet("background-color: white;")
        self.respuesta1.setFixedWidth(320)
        self.respuesta1.setFont(QFont("Arial", 12))
        self.respuesta1.setMaxLength(70)

        self.ladoDerecho.addRow(self.respuesta1)

        self.tituloPregunta2 = QLabel("Pregunta de verificacion 2")
        self.tituloPregunta2.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.tituloPregunta2.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.tituloPregunta2)

        self.pregunta2 = QLineEdit()
        self.pregunta2.setStyleSheet("background-color: white;")
        self.pregunta2.setFixedWidth(320)
        self.pregunta2.setFont(QFont("Arial", 12))
        self.pregunta2.setMaxLength(70)

        self.ladoDerecho.addRow(self.pregunta2)

        self.tituloRespuesta2 = QLabel("Respuesta de verificacion 2")
        self.tituloRespuesta2.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.tituloRespuesta2.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.tituloRespuesta2)

        self.respuesta2 = QLineEdit()
        self.respuesta2.setStyleSheet("background-color: white;")
        self.respuesta2.setFixedWidth(320)
        self.respuesta2.setFont(QFont("Arial", 12))
        self.respuesta2.setMaxLength(70)

        self.ladoDerecho.addRow(self.respuesta2)

        self.tituloPregunta3 = QLabel("Pregunta de verificacion 3")
        self.tituloPregunta3.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.tituloPregunta3.setFont(QFont("Arial", 12))

        self.ladoDerecho.addRow(self.tituloPregunta3)

        self.pregunta3 = QLineEdit()
        self.pregunta3.setStyleSheet("background-color: white;")
        self.pregunta3.setFixedWidth(320)
        self.pregunta3.setFont(QFont("Arial", 12))
        self.pregunta3.setMaxLength(70)

        self.ladoDerecho.addRow(self.pregunta3)

        self.tituloRespuesta3 = QLabel("Respuesta de verificacion 3")
        self.tituloRespuesta3.setStyleSheet("color: " + self.colorLetra1 + ";")
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

        self.horizontalFondo.addWidget(self.ventanaDatos)

        self.usuarios = QScrollArea()
        self.usuarios.setFixedHeight(400)
        self.usuarios.setStyleSheet("background-color: " + self.colorFondo2 + "; border: none;")
        self.usuarios.setWidgetResizable(True)

        self.contenedora = QWidget()
        self.cuadricula = QGridLayout(self.contenedora)
        self.cuadricula.setAlignment(Qt.AlignTop)
        self.usuarios.setWidget(self.contenedora)

        self.horizontalFondo.addWidget(self.usuarios)

        self.ventanaFondo.setLayout(self.horizontalFondo)
        self.verticalP.addWidget(self.ventanaFondo)

        self.cargar_Usuarios()

        # Se crea una ventana para distribuir los botones en la parte inferior
        self.ventanaBotones = QLabel()
        self.ventanaBotones.setFixedHeight(60)
        self.ventanaBotones.setContentsMargins(0, 0, 0, 0)
        self.horizontalB = QHBoxLayout()

        # Creamos el botón para registrar los usuarios
        self.botonModificar = QPushButton("Modificar")
        self.botonModificar.setFixedWidth(100)
        self.botonModificar.setFixedHeight(40)
        self.botonModificar.setFont(QFont("Arial", 12))
        self.botonModificar.setStyleSheet("background-color: " + self.colorBotones1 + ";"
                                          "color: white;")
        self.botonModificar.clicked.connect(self.metodo_accionModificar)

        self.horizontalB.addWidget(self.botonModificar)

        # Creamos el botón para limpiar los campos de texto
        self.botonEliminar = QPushButton("Eliminar")
        self.botonEliminar.setFixedWidth(100)
        self.botonEliminar.setFixedHeight(40)
        self.botonEliminar.setFont(QFont("Arial", 12))
        self.botonEliminar.setStyleSheet("background-color: " + self.colorBotones1 + ";"
                                        "color: white;")
        self.botonEliminar.clicked.connect(self.metodo_accionEliminar)

        self.horizontalB.addStretch()
        self.horizontalB.addWidget(self.botonEliminar)

        self.ventanaBotones.setLayout(self.horizontalB)
        self.verticalP.addWidget(self.ventanaBotones)

        self.fondo.setLayout(self.verticalP)

        self.ventanadeDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.verticalDialogo = QVBoxLayout()
        self.ventanadeDialogo.setWindowIcon(QtGui.QIcon("Imagenes/" + self.colorLogo))
        self.ventanadeDialogo.setStyleSheet("background-color: " + self.colorFondo1 + ";")
        self.ventanadeDialogo.setWindowTitle("Modificar usuario")
        self.ventanadeDialogo.setWindowModality(Qt.ApplicationModal)


        self.mensaje = QLabel("")
        self.mensaje.setFont(QFont("Arial", 12))
        self.mensaje.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.verticalDialogo.addWidget(self.mensaje)

        self.botonesModificar = QLabel()
        self.espacioHorizontal = QHBoxLayout()

        self.botonOk = QPushButton("Ok")
        self.botonOk.setFixedWidth(80)
        self.botonOk.setFixedHeight(25)
        self.botonOk.setFont(QFont("Arial", 12))
        self.botonOk.setStyleSheet("background-color: " + self.colorBotones1 + "; color: white;")
        self.botonOk.clicked.connect(self.cerrar_mensaje)

        self.espacioHorizontal.addStretch()
        self.espacioHorizontal.addWidget(self.botonOk)
        self.botonesModificar.setLayout(self.espacioHorizontal)
        self.verticalDialogo.addWidget(self.botonesModificar)

        self.botonesEliminar = QLabel()
        self.espacioHorizontal = QHBoxLayout()

        self.Si = QPushButton("Si")
        self.Si.setFixedWidth(80)
        self.Si.setFixedHeight(25)
        self.Si.setFont(QFont("Arial", 12))
        self.Si.setStyleSheet("background-color: " + self.colorBotones1 + "; color: white;")
        self.Si.clicked.connect(self.eliminar_usuarios)

        self.No = QPushButton("No")
        self.No.setFixedWidth(80)
        self.No.setFixedHeight(25)
        self.No.setFont(QFont("Arial", 12))
        self.No.setStyleSheet("background-color: " + self.colorBotones1 + "; color: white;")
        self.No.clicked.connect(self.cerrar_mensaje)

        self.espacioHorizontal.addWidget(self.Si)
        self.espacioHorizontal.addStretch()
        self.espacioHorizontal.addWidget(self.No)
        self.botonesEliminar.setLayout(self.espacioHorizontal)
        self.verticalDialogo.addWidget(self.botonesEliminar)

        self.ventanadeDialogo.setLayout(self.verticalDialogo)

        self.datosCorrectos = True

        self.vacio = ""

        self.file = open('datos/usuarios.txt', 'rb')
        self.usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')
            self.posicion = len(self.usuarios) + 1
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
            self.u.posicion = self.posicion

            self.file2 = open('datos/usuarios.txt', 'wb')
            for self.u in self.usuarios:
                self.file2.write(bytes(str(self.u.posicion) + ";"
                                       + self.u.nombreCompleto + ";"
                                       + self.u.usuario + ";"
                                       + self.u.password + ";"
                                       + self.u.documento + ";"
                                       + self.u.correo + ";"
                                       + self.u.pregunta1 + ";"
                                       + self.u.respuesta1 + ";"
                                       + self.u.pregunta2 + ";"
                                       + self.u.respuesta2 + ";"
                                       + self.u.pregunta3 + ";"
                                       + self.u.respuesta3 + ";"
                                       + self.u.validar + ";"
                                       + self.u.vacio, encoding='UTF-8'))
            self.file2.close()
        self.file.close()

        self.posicion = 0

    def cargar_Usuarios(self):
        self.file = open('datos/usuarios.txt', 'rb')
        self.usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')
            self.posicion = len(self.usuarios) + 1
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
            self.u.posicion = self.posicion

        self.numeroUsuarios = len(self.usuarios)
        self.contador = 0
        self.elementosPorColumna = 1

        self.numeroFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) + 1

        self.botones = QButtonGroup()
        self.botones.setExclusive(True)

        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna + 1):
                if self.contador < self.numeroUsuarios:
                    self.ventanaAux = QWidget()

                    self.verticalCuadricula = QVBoxLayout()

                    self.botonAccion = QPushButton(self.usuarios[self.contador].usuario)
                    self.botonAccion.setFont(QFont("Arial", 12))
                    self.botonAccion.setStyleSheet("color: white; background-color: " + self.colorBotones2 + ";")
                    self.botonAccion.setFixedHeight(50)

                    self.verticalCuadricula.addWidget(self.botonAccion)

                    self.botones.addButton(self.botonAccion, int(self.usuarios[self.contador].posicion))

                    self.ventanaAux.setLayout(self.verticalCuadricula)

                    self.cuadricula.addWidget(self.ventanaAux, fila, columna)

                    self.contador += 1
        self.botones.idClicked.connect(self.metodo_accionUsuarios)
        self.posicion = 0

    def metodo_accionUsuarios(self, posicion):
        if self.posicion == 0:
            self.botones.button(posicion).setStyleSheet("color: white; background-color: " + self.colorBotones3 + ";")
        if self.posicion > 0:
            self.botones.button(self.posicion).setStyleSheet("color: white; background-color: " + self.colorBotones2 + ";")
            self.botones.button(posicion).setStyleSheet("color: white; background-color: " + self.colorBotones3 + ";")

        self.posicion = posicion

        self.file = open('datos/usuarios.txt', 'rb')
        usuarios = []

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
            usuarios.append(self.u)
        self.file.close()

        for self.u in usuarios:
            if int(self.u.posicion) == self.posicion:

                if self.u.validar == "Administrador":
                    self.filtro.setCurrentIndex(0)
                if self.u.validar == "Usuario":
                    self.filtro.setCurrentIndex(1)

                self.nombreCompleto.setText(self.u.nombreCompleto)
                self.NombredeUsuario.setText(self.u.usuario)
                self.password.setText(self.u.password)
                self.password2.setText(self.u.password)
                self.Documento.setText(self.u.documento)
                self.correo.setText(self.u.correo)
                self.pregunta1.setText(self.u.pregunta1)
                self.respuesta1.setText(self.u.respuesta1)
                self.pregunta2.setText(self.u.pregunta2)
                self.respuesta2.setText(self.u.respuesta2)
                self.pregunta3.setText(self.u.pregunta3)
                self.respuesta3.setText(self.u.respuesta3)
                break

    def metodo_accionModificar(self):
        self.botonesModificar.show()
        self.botonesEliminar.hide()
        if self.posicion == 0:
            self.ventanadeDialogo.setFixedWidth(260)
            self.ventanadeDialogo.setFixedHeight(100)
            self.mensaje.setText("Debe seleccionar algún usuario.")
            self.ventanadeDialogo.exec_()
        else:
            self.datosCorrectos = True
            if (
                    self.nombreCompleto.text() == ''
                    or self.NombredeUsuario.text() == ''
                    or self.password.text() == ''
                    or self.password2.text() == ''
                    or self.Documento.text() == ''
                    or self.correo.text() == ''
                    or self.pregunta1.text() == ''
                    or self.respuesta1.text() == ''
                    or self.pregunta2.text() == ''
                    or self.respuesta2.text() == ''
                    or self.pregunta3.text() == ''
                    or self.respuesta3.text() == ''
            ):
                self.datosCorrectos = False
                self.ventanadeDialogo.setFixedWidth(260)
                self.ventanadeDialogo.setFixedHeight(100)
                self.mensaje.setText("Debe ingresar todos los campos.")
                self.ventanadeDialogo.exec_()
            else:
                if (self.password.text() != self.password2.text()):
                    self.datosCorrectos = False
                    self.ventanadeDialogo.setFixedWidth(260)
                    self.ventanadeDialogo.setFixedHeight(100)
                    self.mensaje.setText("Las contraseñas no son iguales.")
                    self.ventanadeDialogo.exec_()

                if not self.Documento.text().isdigit():
                    self.datosCorrectos = False
                    self.ventanadeDialogo.setFixedWidth(272)
                    self.ventanadeDialogo.setFixedHeight(100)
                    self.mensaje.setText("El documento debe ser en numeros.")
                    self.ventanadeDialogo.exec_()

            if self.datosCorrectos:
                for self.u in self.usuarios:
                    if int(self.u.posicion) == int(self.posicion):
                        self.u.nombreCompleto = self.nombreCompleto.text()
                        self.u.usuario = self.NombredeUsuario.text()
                        self.u.password = self.password.text()
                        self.u.documento = self.Documento.text()
                        self.u.correo = self.correo.text()
                        self.u.pregunta1 = self.pregunta1.text()
                        self.u.respuesta1 = self.respuesta1.text()
                        self.u.pregunta2 = self.pregunta2.text()
                        self.u.respuesta2 = self.respuesta2.text()
                        self.u.pregunta3 = self.pregunta3.text()
                        self.u.respuesta3 = self.respuesta3.text()

                        if self.filtro.currentIndex() == 0:
                            self.u.validar = "Administrador"
                        if self.filtro.currentIndex() == 1:
                            self.u.validar = "Usuario"
                        break

                self.file2 = open('datos/usuarios.txt', 'wb')
                for self.u in self.usuarios:
                    self.file2.write(bytes(str(self.u.posicion) + ";"
                                           + self.u.nombreCompleto + ";"
                                           + self.u.usuario + ";"
                                           + self.u.password + ";"
                                           + self.u.documento + ";"
                                           + self.u.correo + ";"
                                           + self.u.pregunta1 + ";"
                                           + self.u.respuesta1 + ";"
                                           + self.u.pregunta2 + ";"
                                           + self.u.respuesta2 + ";"
                                           + self.u.pregunta3 + ";"
                                           + self.u.respuesta3 + ";"
                                           + self.u.validar + ";"
                                           + self.u.vacio, encoding='UTF-8'))
                self.file2.close()
                self.ventanadeDialogo.setFixedWidth(340)
                self.ventanadeDialogo.setFixedHeight(100)
                self.mensaje.setText("Se ah modificado el usuario correctamente.")
                self.ventanadeDialogo.show()
                self.metodo_cerrar()
                self.metodo_limpiar()
                self.ventanaAnteriorC.ir_modificar_usuario()

    def metodo_accionEliminar(self):
        if self.posicion == 0:
            self.botonesModificar.show()
            self.botonesEliminar.hide()
            self.ventanadeDialogo.setFixedWidth(260)
            self.ventanadeDialogo.setFixedHeight(100)
            self.mensaje.setText("Debe seleccionar algún usuario.")
            self.ventanadeDialogo.exec_()
        else:
            self.botonesModificar.hide()
            self.botonesEliminar.show()
            self.ventanadeDialogo.setFixedWidth(260)
            self.ventanadeDialogo.setFixedHeight(100)
            self.mensaje.setText("¿Desea eliminar el usuario?")
            self.ventanadeDialogo.exec_()

    def eliminar_usuarios(self):
        for self.u in self.usuarios:
            if int(self.u.posicion) == int(self.posicion):
                self.usuarios.remove(self.u)
                break

        self.file2 = open('datos/usuarios.txt', 'wb')
        for self.u in self.usuarios:
            self.file2.write(bytes(str(self.u.posicion) + ";"
                                   + self.u.nombreCompleto + ";"
                                   + self.u.usuario + ";"
                                   + self.u.password + ";"
                                   + self.u.documento + ";"
                                   + self.u.correo + ";"
                                   + self.u.pregunta1 + ";"
                                   + self.u.respuesta1 + ";"
                                   + self.u.pregunta2 + ";"
                                   + self.u.respuesta2 + ";"
                                   + self.u.pregunta3 + ";"
                                   + self.u.respuesta3 + ";"
                                   + self.u.validar + ";"
                                   + self.u.vacio, encoding='UTF-8'))
        self.file2.close()
        self.botonesModificar.show()
        self.botonesEliminar.hide()
        self.ventanadeDialogo.setFixedWidth(340)
        self.ventanadeDialogo.setFixedHeight(100)
        self.mensaje.setText("Se ah eliminado el usuario correctamente.")
        self.ventanadeDialogo.show()
        self.metodo_cerrar()
        self.metodo_limpiar()
        self.ventanaAnteriorC.ir_modificar_usuario()

    def metodo_limpiar(self):
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

    def metodo_cerrar(self):
        # Metodo para cerrar las subventanas abiertas en las funciones crear, modificar y eliminar
        self.hide()

    def accion_botonatras(self):
        # Metodo para volver a la ventana del administrador
        self.hide()
        self.ventanaAnteriorC.show()