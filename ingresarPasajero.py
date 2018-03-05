from PyQt5 import QtWidgets
from vistas import ui_ingresarPasajero
from controladores import controlador


class IngresarPasajero(QtWidgets.QDialog,
                       ui_ingresarPasajero.Ui_fmIngresar):
    def __init__(self, sesion, parent=None):
        super(IngresarPasajero, self).__init__(parent)
        self.setupUi(self)
        self.sesion = sesion

    def buscar(self):
        dicECivil = {0: "Soltero", 1: "Casado", 2: "Viudo", 3: "Sepadado"}
        cod = self.txtcPas.text()
        try:
            if cod != "":
                lista = controlador.consultaPasajero(self.sesion, cod)
                self.lbl01.setText(str(lista[0][0]) + ' ' +
                                   str(lista[0][1]))
                self.lbl02.setText(str(lista[0][3]))
                self.lbl03.setText(str(lista[0][5]))
                self.lbl04.setText(controlador.consultaPais(self.sesion,
                                                            int(lista[0][11])))
                self.lbl05.setText(dicECivil[lista[0][4]])
                self.lbl06.setText(str(lista[0][10]))
        except IndexError:
            QtWidgets.QMessageBox.information(self, 'Mensaje',
                                              ''' Pasajero no Encontrado''',
                                              QtWidgets.QMessageBox.Ok)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = IngresarPasajero()
    form.show()
    app.exec_()
