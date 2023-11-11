import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QLabel, QFormLayout, QComboBox, QPushButton

class Pruebas(QMainWindow):
    def __init__(self, parent=None):
        super(Pruebas, self).__init__(parent=parent)

        self.ancho = 400
        self.alto = 400
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

        self.filtro = QComboBox()
        self.filtro.addItems(["1", "2", "3"])

        self.formularioPrin.addRow(self.filtro)

        self.boton = QPushButton("validar")
        self.boton.clicked.connect(self.validaciones)

        self.formularioPrin.addRow(self.boton)

        self.ventanaDialogo.setLayout(self.formularioPrin)
    def validaciones(self):
        if self.filtro.currentIndex() == 0:
            print("el numero es 1")
        if self.filtro.currentIndex() == 1:
            print("el numero es 2")
        if self.filtro.currentIndex() == 2:
            print("el numero es 3")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana = Pruebas()

    ventana.show()

    sys.exit(app.exec_())