from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QDialog, QFormLayout, QLabel, QHBoxLayout, QPushButton, QDesktopWidget, \
    QVBoxLayout
from productosLista import Lista
class ProductosEliminar(QMainWindow):
    def __init__(self, anterior):
        super(ProductosEliminar, self).__init__(anterior)
        # Se crea la ventana principal junto a sus modificaciones
        self.ventanaAnterior = anterior
        self.idPosicionEliminar = anterior.idPosicion

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

        self.setWindowTitle("Eliminar Producto")
        self.setWindowIcon(QtGui.QIcon("Imagenes/" + self.colorFondo2))

        self.ancho = 300
        self.alto = 100
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

        self.mensaje = QLabel("¿Desea eliminar este producto?")
        self.mensaje.setFixedHeight(45)
        self.mensaje.setStyleSheet("color: " + self.colorLetra1 + ";")
        self.mensaje.setFont(QFont("Arial", 12))

        self.formularioPrin.addRow(self.mensaje)

        # Se crea ventana establecida en la parte inferior para crear botones en los que se puede cancelar la creación del producto o crearlo
        self.botones2 = QLabel()
        self.botones2.setFixedHeight(37)
        self.minihorizontal4 = QHBoxLayout()

        self.botonSi = QPushButton("Si")
        self.botonSi.setFixedWidth(80)
        self.botonSi.setFixedHeight(25)
        self.botonSi.setStyleSheet("background-color: " + self.colorBotones1 + "; color: white;")
        self.botonSi.setFont(QFont("Arial", 12))
        self.botonSi.clicked.connect(self.funcion_eliminar)

        self.botonNo = QPushButton("No")
        self.botonNo.setFixedWidth(80)
        self.botonNo.setFixedHeight(25)
        self.botonNo.setStyleSheet("background-color: " + self.colorBotones1 + "; color: white;")
        self.botonNo.setFont(QFont("Arial", 12))
        self.botonNo.clicked.connect(self.salir)

        self.minihorizontal4.addWidget(self.botonSi)
        self.minihorizontal4.addStretch()
        self.minihorizontal4.addWidget(self.botonNo)

        self.botones2.setLayout(self.minihorizontal4)
        self.formularioPrin.addRow(self.botones2)

        self.ventanaDialogo.setLayout(self.formularioPrin)


    def funcion_eliminar(self):
        # Metodo para eliminar el producto seleccionado
        self.file = open("datos/productos.txt", 'rb')

        usuarios = []

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
            usuarios.append(u)
        self.file.close()

        for u in usuarios:
            if int(u.idPosicion) == self.idPosicionEliminar:
                usuarios.remove(u)
                break

        self.file = open("datos/productos.txt", 'wb')

        for u in usuarios:
            self.file.write(bytes(u.nombre + ";"
                                  + u.idPosicion + ";"
                                  + u.identificadorFiltro + ";"
                                  + u.descripcion + ";"
                                  + u.numeroDia + ";"
                                  + u.numeroMes + ";"
                                  + u.numeroAno + ";"
                                  + u.numeroCantidad + ";"
                                  + u.espacio, encoding='UTF-8'))
        self.file.close()
        self.ventanaAnterior.hide()
        self.ventanaAnterior.ventanaAnterior.ir_productos()
        self.ventanaAnterior.limpiar()
        self.metodo_cerrar()

    def metodo_cerrar(self):
        self.hide()
        # Metodo para cerrar las subventanas abiertas en las funciones crear, modificar y eliminar
        self.ventanaValidar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaValidar.setWindowIcon(QtGui.QIcon("Imagenes/" + self.colorLogo))
        self.ventanaValidar.setFixedWidth(300)
        self.ventanaValidar.setFixedHeight(100)
        self.ventanaValidar.setWindowTitle("Validación")
        self.ventanaValidar.setStyleSheet("background-color: " + self.colorFondo1 + ";")
        self.ventanaValidar.setWindowModality(Qt.ApplicationModal)

        self.verticalValidar = QVBoxLayout()

        self.ventanaValidar.setFixedWidth(330)
        self.mensaje = QLabel("Se ah eliminado el producto correctamente.")
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

        self.ventanaValidar.exec_()

    def metodo_cerrar_validacion(self):
        self.ventanaValidar.hide()

    def salir(self):
        self.hide()