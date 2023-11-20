from PyQt5.QtWidgets import QMainWindow
from productos import Productos
class Actualizador(QMainWindow):
    def __init__(self, anterior):
        super(Actualizador, self).__init__(anterior)
        self.setFixedHeight(0)
        self.setFixedWidth(0)
        self.ventanaAnterior = anterior
        self.actualizar()


    def actualizar(self):
        self.hide()
        self.productos = Productos(self)
        self.productos.show()