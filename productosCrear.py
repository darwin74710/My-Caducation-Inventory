from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QFormLayout, QTextEdit, QVBoxLayout, QHBoxLayout, \
    QLineEdit, QPushButton, QDialog, QComboBox
from productosLista import Lista
from datetime import datetime
import calendar

class ProductosCrear(QMainWindow):
    def __init__(self, anterior):
        super(ProductosCrear, self).__init__(anterior)
        # Se crea la ventana principal junto a sus modificaciones
        self.ventanaAnterior = anterior

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

        self.fechaActual = datetime.today()
        self.calendario = calendar

        self.setWindowTitle("Crear producto")

        self.ancho = 400
        self.alto = 345
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())
        self.setWindowModality(Qt.ApplicationModal)

        self.ventanaDialogo = QLabel()
        self.setCentralWidget(self.ventanaDialogo)
        self.formularioPrin = QFormLayout()
        self.ventanaDialogo.setStyleSheet("background-color: " + self.colorFondo1 + ";")

        self.principal = QLabel()
        self.formularioMensaje = QFormLayout()
        self.principal.setFixedHeight(270)
        self.principal.setStyleSheet("background-color: " + self.colorFondo2 + ";")

        self.titulo0 = QLabel("Nombre: ")
        self.titulo0.setFixedHeight(20)
        self.titulo0.setFont(QFont("Arial", 12))
        self.titulo0.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.nombre = QLineEdit()
        self.nombre.setFixedHeight(20)
        self.nombre.setMaxLength(40)
        self.nombre.setStyleSheet("background-color: white;")
        self.nombre.setFont(QFont("Arial", 12))

        self.formularioMensaje.addRow(self.titulo0, self.nombre)

        self.titulo1 = QLabel("Descripción: ")
        self.titulo1.setFixedHeight(20)
        self.titulo1.setFont(QFont("Arial", 12))
        self.titulo1.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.descripcion = QTextEdit()
        self.descripcion.setFixedHeight(80)
        self.descripcion.setStyleSheet("background-color: white;")
        self.descripcion.setFont(QFont("Arial", 12))

        self.formularioMensaje.addRow(self.titulo1, self.descripcion)

        self.titulo2 = QLabel("Caducidad:")
        self.titulo2.setFixedHeight(50)
        self.titulo2.setFont(QFont("Arial", 12))
        self.titulo2.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.minivertical = QVBoxLayout()
        self.infoCaducidad = QLabel()
        self.infoCaducidad.setFixedHeight(70)

        self.minihorizontal2 = QHBoxLayout()
        self.minititulos = QLabel()
        self.minititulos.setFixedHeight(25)

        self.miniTitulo1 = QLabel("día")
        self.miniTitulo1.setFixedWidth(50)
        self.miniTitulo1.setFixedHeight(20)
        self.miniTitulo1.setFont(QFont("Arial", 12))
        self.miniTitulo1.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.miniTitulo2 = QLabel("mes")
        self.miniTitulo2.setFixedWidth(50)
        self.miniTitulo2.setFixedHeight(20)
        self.miniTitulo2.setFont(QFont("Arial", 12))
        self.miniTitulo2.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.miniTitulo3 = QLabel("año")
        self.miniTitulo3.setFixedWidth(50)
        self.miniTitulo3.setFixedHeight(20)
        self.miniTitulo3.setFont(QFont("Arial", 12))
        self.miniTitulo3.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.minihorizontal2.addWidget(self.miniTitulo1)
        self.minihorizontal2.addStretch()
        self.minihorizontal2.addWidget(self.miniTitulo2)
        self.minihorizontal2.addStretch()
        self.minihorizontal2.addWidget(self.miniTitulo3)

        self.minititulos.setLayout(self.minihorizontal2)
        self.minivertical.addWidget(self.minititulos)

        self.minihorizontal3 = QHBoxLayout()
        self.miniInfo = QLabel()
        self.miniInfo.setFixedHeight(30)

        self.dia = QLineEdit()
        self.dia.setFixedWidth(50)
        self.dia.setFixedHeight(20)
        self.dia.setMaxLength(2)
        self.dia.setStyleSheet("background-color: white;")
        self.dia.setFont(QFont("Arial", 12))

        self.mes = QLineEdit()
        self.mes.setFixedWidth(50)
        self.mes.setFixedHeight(20)
        self.mes.setMaxLength(2)
        self.mes.setStyleSheet("background-color: white;")
        self.mes.setFont(QFont("Arial", 12))

        self.ano = QLineEdit()
        self.ano.setFixedWidth(50)
        self.ano.setFixedHeight(20)
        self.ano.setMaxLength(4)
        self.ano.setStyleSheet("background-color: white;")
        self.ano.setFont(QFont("Arial", 12))

        # Estas barras son simple decoración
        self.barra = QLabel("/")
        self.barra.setFixedWidth(50)
        self.barra.setFixedHeight(20)
        self.barra.setAlignment(Qt.AlignCenter)
        self.barra.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.barra.setFont(QFont("Arial", 12))

        self.barra2 = QLabel("/")
        self.barra2.setFixedWidth(50)
        self.barra2.setFixedHeight(20)
        self.barra2.setAlignment(Qt.AlignCenter)
        self.barra2.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.barra2.setFont(QFont("Arial", 12))

        self.minihorizontal3.addWidget(self.dia)
        self.minihorizontal3.addWidget(self.barra)
        self.minihorizontal3.addWidget(self.mes)
        self.minihorizontal3.addWidget(self.barra2)
        self.minihorizontal3.addWidget(self.ano)

        self.miniInfo.setLayout(self.minihorizontal3)
        self.minivertical.addWidget(self.miniInfo)
        self.infoCaducidad.setLayout(self.minivertical)
        self.formularioMensaje.addRow(self.titulo2, self.infoCaducidad)

        self.vacio = QLabel()
        self.formularioMensaje.addWidget(self.vacio)

        self.titulo3 = QLabel("Cantidad:")
        self.titulo3.setFixedHeight(20)
        self.titulo3.setFont(QFont("Arial", 12))
        self.titulo3.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.cantidad = QLineEdit()
        self.cantidad.setFixedWidth(50)
        self.cantidad.setFixedHeight(20)
        self.cantidad.setStyleSheet("background-color: white;")
        self.cantidad.setFont(QFont("Arial", 12))

        self.formularioMensaje.addRow(self.titulo3, self.cantidad)

        self.titulo4 = QLabel("Filtro:")
        self.titulo4.setFixedHeight(20)
        self.titulo4.setFont(QFont("Arial", 12))
        self.titulo4.setStyleSheet("color: " + self.colorLetra1 + ";")

        self.filtro = QComboBox()
        self.filtro.setFixedHeight(20)
        self.filtro.setStyleSheet("background-color: white;")
        self.filtro.setFont(QFont("Arial", 12))
        self.filtro.addItems(["Granos", "Enlatados", "Lacteos", "Carnicos", "Pescados", "Otros"])

        self.formularioMensaje.addRow(self.titulo4, self.filtro)

        self.principal.setLayout(self.formularioMensaje)
        self.formularioPrin.addRow(self.principal)

        # Se crea ventana establecida en la parte inferior para crear botones en los que se puede cancelar la creación del producto o crearlo
        self.botones2 = QLabel()
        self.botones2.setFixedHeight(37)
        self.minihorizontal4 = QHBoxLayout()

        self.botonCrear = QPushButton("Crear")
        self.botonCrear.setFixedWidth(100)
        self.botonCrear.setFixedHeight(27)
        self.botonCrear.setStyleSheet("background-color: " + self.colorBotones1 + "; color: white;")
        self.botonCrear.setFont(QFont("Arial", 12))
        self.botonCrear.clicked.connect(self.funcion_crear)

        self.botonAtras = QPushButton("Cancelar")
        self.botonAtras.setFixedWidth(100)
        self.botonAtras.setFixedHeight(27)
        self.botonAtras.setStyleSheet("background-color: " + self.colorBotones1 + "; color: white;")
        self.botonAtras.setFont(QFont("Arial", 12))
        self.botonAtras.clicked.connect(self.metodo_cerrar)

        self.minihorizontal4.addWidget(self.botonCrear)
        self.minihorizontal4.addStretch()
        self.minihorizontal4.addWidget(self.botonAtras)

        self.botones2.setLayout(self.minihorizontal4)
        self.formularioPrin.addRow(self.botones2)

        self.ventanaDialogo.setLayout(self.formularioPrin)

        self.ventanaValidar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaValidar.setWindowIcon(QtGui.QIcon("Imagenes/" + self.colorLogo))
        self.ventanaValidar.setFixedWidth(300)
        self.ventanaValidar.setFixedHeight(100)
        self.ventanaValidar.setWindowTitle("Validación")
        self.ventanaValidar.setStyleSheet("background-color: " + self.colorFondo1 + ";")
        self.ventanaValidar.setWindowModality(Qt.ApplicationModal)

        self.verticalValidar = QVBoxLayout()

        self.mensaje = QLabel("")
        self.mensaje.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.mensaje.setFont(QFont("Arial", 12))

        self.verticalValidar.addWidget(self.mensaje)

        self.botones = QLabel()
        self.horizontalValidacion = QHBoxLayout()

        self.horizontalValidacion.addStretch()
        self.Ok = QPushButton("Ok")
        self.Ok.setFixedWidth(80)
        self.Ok.setFixedHeight(25)
        self.Ok.setStyleSheet("background-color: " + self.colorBotones1 + "; color: white;")
        self.Ok.setFont(QFont("Arial", 12))
        self.Ok.clicked.connect(self.metodo_cerrar_validacion)

        self.horizontalValidacion.addWidget(self.Ok)

        self.botones.setLayout(self.horizontalValidacion)
        self.verticalValidar.addWidget(self.botones)
        self.ventanaValidar.setLayout(self.verticalValidar)

        self.datosCorrectos = True

        self.file = open('datos/productos.txt', 'rb')
        self.usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")
            if linea == '':
                break
            u = Lista(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8]
            )
            self.usuarios.append(u)
        self.file.close()

    def funcion_crear(self):
        self.datosCorrectos = True
        self.numeroDia = self.dia.text().replace(" ", "")
        self.numeroMes = self.mes.text().replace(" ", "")
        self.numeroAno = self.ano.text().replace(" ", "")
        self.numeroCantidad = self.cantidad.text().replace(" ", "")
        self.descripcionTexto = self.descripcion.toPlainText().replace("\n", " ")
        self.vacio = " "

        self.diaActual = int(self.fechaActual.day)
        self.mesActual = int(self.fechaActual.month)
        self.anoActual = int(self.fechaActual.year)

        if not self.numeroDia.isdigit() or not self.numeroMes.isdigit() or not self.numeroAno.isdigit() or int(self.numeroMes) > 12:
            self.ventanaValidar.setFixedWidth(440)
            self.ventanaValidar.setFixedHeight(160)
            self.datosCorrectos = False
            self.mensaje.setText("- Debe ingresar los datos correctamente.\n\n- Los datos deben estar actualizados a la fecha: " + str(
                self.diaActual) + "/" + str(self.mesActual) + "/" + str(self.anoActual) + "\n\n- La fecha no se puede modificar.")
            self.ventanaValidar.exec_()
        else:
            self.ultimoDia = self.calendario.monthrange(int(self.numeroAno), int(self.numeroMes))
            self.limiteDia = self.ultimoDia[1]

            self.identificadorFiltro = self.filtro.currentIndex()

            if (int(self.numeroAno) > int(self.anoActual) or (
                    int(self.anoActual) == int(self.numeroAno) and (int(self.numeroMes) > int(self.mesActual)))):
                if ((
                        not self.numeroDia.isdigit() or not self.numeroMes.isdigit() or not self.numeroAno.isdigit() or not self.numeroCantidad.isdigit())
                        or ((self.numeroDia.isnumeric() and (int(self.numeroDia) < 1)))
                        or ((self.numeroMes.isnumeric() and (int(self.numeroMes) < 1)))
                        or not (int(self.numeroDia) <= int(self.limiteDia) and int(self.numeroMes) <= int(12))
                        or ((self.numeroAno.isnumeric() and int(self.numeroAno) < int(self.anoActual)))
                        or ((self.numeroCantidad.isnumeric() and int(self.numeroCantidad) <= 0))
                ):
                    self.ventanaValidar.setFixedWidth(440)
                    self.ventanaValidar.setFixedHeight(160)
                    self.datosCorrectos = False
                    self.mensaje.setText(
                        "- Debe ingresar los datos correctamente.\n\n- Los datos deben estar actualizados a la fecha: " + str(
                            self.diaActual) + "/" + str(self.mesActual) + "/" + str(
                            self.anoActual) + "\n\n- La fecha no se puede modificar.")
                    self.ventanaValidar.exec_()
            if (int(self.anoActual) == int(self.numeroAno) and (int(self.mesActual) == int(self.numeroMes))):
                if ((
                        not self.numeroDia.isdigit() or not self.numeroMes.isdigit() or not self.numeroAno.isdigit() or not self.numeroCantidad.isdigit())
                        or ((self.numeroDia.isnumeric() and (int(self.numeroDia) < int(self.diaActual))))
                        or ((self.numeroMes.isnumeric() and (int(self.numeroMes) < int(self.mesActual))))
                        or not (int(self.numeroDia) <= int(self.limiteDia) and int(self.numeroMes) <= int(12))
                        or ((self.numeroAno.isnumeric() and int(self.numeroAno) < int(self.anoActual)))
                        or ((self.numeroCantidad.isnumeric() and int(self.numeroCantidad) <= 0))
                ):
                    self.ventanaValidar.setFixedWidth(440)
                    self.ventanaValidar.setFixedHeight(160)
                    self.datosCorrectos = False
                    self.mensaje.setText(
                        "- Debe ingresar los datos correctamente.\n\n- Los datos deben estar actualizados a la fecha: " + str(
                            self.diaActual) + "/" + str(self.mesActual) + "/" + str(
                            self.anoActual) + "\n\n- La fecha no se puede modificar.")
                    self.ventanaValidar.exec_()
            if (int(self.numeroAno) < int(self.anoActual)):
                self.ventanaValidar.setFixedWidth(440)
                self.ventanaValidar.setFixedHeight(160)
                self.datosCorrectos = False
                self.mensaje.setText(
                    "- Debe ingresar los datos correctamente.\n\n- Los datos deben estar actualizados a la fecha: " + str(
                        self.diaActual) + "/" + str(self.mesActual) + "/" + str(
                        self.anoActual) + "\n\n- La fecha no se puede modificar.")
                self.ventanaValidar.exec_()
            if (int(self.anoActual) == int(self.numeroAno) and int(self.numeroMes) < int(self.mesActual)):
                self.ventanaValidar.setFixedWidth(440)
                self.ventanaValidar.setFixedHeight(160)
                self.datosCorrectos = False
                self.mensaje.setText(
                    "- Debe ingresar los datos correctamente.\n\n- Los datos deben estar actualizados a la fecha: " + str(
                        self.diaActual) + "/" + str(self.mesActual) + "/" + str(
                        self.anoActual) + "\n\n- La fecha no se puede modificar.")
                self.ventanaValidar.exec_()

        if self.datosCorrectos:
            self.idPosicion = len(self.usuarios) + 1
            self.file = open('datos/productos.txt', 'ab')
            self.file.write(bytes(self.nombre.text() + ";"
                                  + str(self.idPosicion) + ";"
                                  + str(self.identificadorFiltro) + ";"
                                  + self.descripcionTexto + ";"
                                  + self.numeroDia + ";"
                                  + self.numeroMes + ";"
                                  + self.numeroAno + ";"
                                  + self.numeroCantidad + ";"
                                  + self.vacio + "\n", encoding='UTF-8'))
            self.file.close()

            self.ventanaValidar.setFixedWidth(300)
            self.ventanaValidar.setFixedHeight(125)
            self.mensaje.setText("Se a creado exitosamente el producto:\n" +
                                 self.nombre.text())
            self.ventanaValidar.exec_()
            self.ventanaAnterior.ordenar_productos_lista()
            self.ventanaAnterior.limpiar()
            self.hide()

    def metodo_cerrar(self):
        # Metodo para cerrar las subventanas abiertas en las funciones crear, modificar y eliminar
        self.hide()

    def metodo_cerrar_validacion(self):
        self.ventanaValidar.hide()
