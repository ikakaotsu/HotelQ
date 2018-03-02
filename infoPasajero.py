from PyQt5 import QtWidgets
from PyQt5 import QtCore
from views import ui_infoPasajero
from controllers import controlador
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsScene


class InfoPasajero(QtWidgets.QFrame,
                   ui_infoPasajero.Ui_infoPasajero):
    def __init__(self, sesion, pasajero=None, parent=None):
        super(InfoPasajero, self).__init__(parent)
        self.setupUi(self)
        self.sesion = sesion
        self.centerOnScreen()
        dicECivil = {0: "Soltero", 1: "Casado", 2: "Viudo", 3: "Separado"}
        if pasajero is not None:
            scene = QGraphicsScene()
            pixmap = QPixmap('2486.jpg')
            pixmap_resized = pixmap.scaled(500, 370, QtCore.Qt.KeepAspectRatio)
            scene.addPixmap(pixmap_resized)
            self.graphicsView.setScene(scene)
            n = controlador.consultaPais(self.sesion,
                                         int(pasajero[0][11]))
            p = controlador.consultaProvincia(self.sesion,
                                              int(pasajero[0][12]))
            lc = controlador.consultaLocalidad(self.sesion,
                                               int(pasajero[0][13]))
            self.lbl01.setText(str(pasajero[0][3]))
            self.lbl02.setText(str(pasajero[0][0] +
                               " " + pasajero[0][1]))
            self.lbl03.setText(str(pasajero[0][6]))
            self.lbl04.setText(str(pasajero[0][9]))
            self.lbl05.setText(n)
            self.lbl06.setText(p)
            self.lbl07.setText(lc)
            self.lbl08.setText(dicECivil[pasajero[0][4]])
            self.lbl09.setText(str(pasajero[0][7]))
            self.lbl10.setText(str(pasajero[0][5]))
            self.lbl11.setText(str(pasajero[0][8]))
            self.lbl12.setText(str(pasajero[0][10]))

    def mousePressEvent(self, QMouseEvent):
        self.close()

    def centerOnScreen(self):
        '''Centers the window on the screen.'''
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frame = InfoPasajero()
    frame.show()
    app.exec_()
