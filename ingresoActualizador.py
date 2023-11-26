import sys

from PyQt5.QtWidgets import QApplication, QWidget
from ingreso import Ingreso
class Actualizador(QWidget):
    def __init__(self, parent=None):
        super(Actualizador, self).__init__(parent=parent)
        self.actualizar()
    def actualizar(self):
        self.ingreso = Ingreso(self)
        self.ingreso.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana = Actualizador()

    sys.exit(app.exec_())