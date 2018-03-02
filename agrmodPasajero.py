from PyQt5 import QtWidgets
# from PyQt5.QtCore import pyqtSignature
from views import ui_agrmodPasajero
from controllers import controlador


class AgrModPasajero(QtWidgets.QDialog,
                     ui_agrmodPasajero.Ui_agrmodPasajero):
    def __init__(self, sesion, pasajero=None, codigo=None, parent=None):
        super(AgrModPasajero, self).__init__(parent)
        self.setupUi(self)
        self.sesion = sesion
        self.cboNacionalidad()
        self.codigo = codigo
        self.pasajero = pasajero
        if pasajero is not None:
            self.txtNombre.setText(str(self.pasajero[0][0]))
            self.txtApellido.setText(str(self.pasajero[0][1]))
            self.cboTdoc.setCurrentIndex(self.pasajero[0][2])
            self.txtNumero.setText(str(self.pasajero[0][3]))
            self.cboECivil.setCurrentIndex(self.pasajero[0][4])
            self.txtOcupacion.setText(str(self.pasajero[0][5]))
            self.txtDomicilio.setText(str(self.pasajero[0][6]))
            self.txtTelefono.setText(str(self.pasajero[0][7]))
            self.txtMail.setText(str(self.pasajero[0][8]))
            self.dteFn.setDate(self.pasajero[0][9])
            self.txtObs.setText(str(self.pasajero[0][10]))
            self.cboNacional.setCurrentIndex(self.pasajero[0][11])
            self.cboProvincia.setCurrentIndex(self.pasajero[0][12])
            self.cboLocalidad.setCurrentIndex(self.pasajero[0][13])
            self.btnAceptar.button(QtWidgets.QDialogButtonBox.Save).setText(
                "&Modificar")
            self.setWindowTitle("Modificar Pasajero")
        else:
            self.btnAceptar.button(QtWidgets.QDialogButtonBox.Save).setText(
                "&Agregar")

    def cboNacionalidad(self):
        self.cboNacional.addItem("Nacionalidad")
        lista = controlador.obtenerPaises(self.sesion)
        for i in lista:
            self.cboNacional.addItems(i)

# @pyqtSignature("int")
    def on_cboNacional_currentIndexChanged(self):
        self.cboProvincia.clear()
        self.cboProvincia.addItem("Provincia")
        indice = self.cboNacional.currentIndex()
        print (indice)
        lista = controlador.obtenerProvincias(self.sesion, indice)
        for i in lista:
            self.cboProvincia.addItems(i)

    # @pyqtSignature("int")
    def on_cboProvincia_currentIndexChanged(self):
        self.cboLocalidad.clear()
        self.cboLocalidad.addItem("Localidad")
        indice = self.cboProvincia.currentIndex()
        lista = controlador.obtenerLocalidades(self.sesion, indice)
        for i in lista:
            self.cboLocalidad.addItems(i)

    def accept(self):
        try:
            pasajeroDic = {}
            pasajeroDic["nombre"] = str(self.txtNombre.text())
            pasajeroDic["apellido"] = str(self.txtApellido.text())
            pasajeroDic["doctipo"] = str(self.cboTdoc.currentIndex())
            pasajeroDic["docnumero"] = str(self.txtNumero.text())
            pasajeroDic["ecivil"] = str(self.cboECivil.currentIndex())
            pasajeroDic["ocupacion"] = str(self.txtOcupacion.text())
            pasajeroDic["domicilio"] = str(self.txtDomicilio.text())
            pasajeroDic["telefono"] = int(self.txtTelefono.text())
            pasajeroDic["mail"] = str(self.txtMail.text())
            pasajeroDic["nacimiento"] = self.dteFn.date().toPyDate()
            pasajeroDic["obs"] = str(self.txtObs.toPlainText())
            pasajeroDic["pais"] = self.cboNacional.currentIndex()
            pasajeroDic["provincia"] = self.cboProvincia.\
                currentIndex()
            pasajeroDic["localidad"] = self.cboLocalidad.\
                currentIndex()
            data = ({"pasajero": pasajeroDic})
            controlador.agrmodPasajero(self.sesion, data, self.codigo)

        except ValueError as e:
            print ("Se produjo un Error", e)

        QtWidgets.QDialog.accept(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    form = AgrModPasajero()
    form.show()
    app.exec_()
