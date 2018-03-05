from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from vistas import ui_agrmodCtaCte
from controladores import controlador


class AgrModCtaCte(QtWidgets.QDialog,
                   ui_agrmodCtaCte.Ui_agrmodCtaCte):
    def __init__(self, sesion, ctacte=None, codigo=None, parent=None):
        super(AgrModCtaCte, self).__init__(parent)
        self.setupUi(self)
        self.sesion = sesion
        self.cargarcboProvincia()
        self.codigo = codigo
        self.ctacte = ctacte
        if ctacte is not None:
            self.txtCodigo.setText(str(self.codigo))
            self.txtNombre.setText(str(self.ctacte[0][0]))
            self.txtDomicilio.setText(str(self.ctacte[0][1]))
            self.txtCuit.setText(str(self.ctacte[0][2]))
            self.txtObs.setText(str(self.ctacte[0][3]))
            self.txtCodpost.setText(str(self.ctacte[0][4]))
            self.cboIvatipo.setCurrentIndex(self.ctacte[0][5])
            self.txtTelefono.setText(str(self.ctacte[0][6]))
            self.dteAlta.setDate(self.ctacte[0][7])
            self.cboProvincia.setCurrentIndex(self.ctacte[0][8])
            self.cboLocalidad.setCurrentIndex(self.ctacte[0][9])
            self.btnAceptar.button(QtWidgets.QDialogButtonBox.Save).setText(
                "&Modificar")
            self.setWindowTitle("Modificar CtaCte")
        else:
            self.txtCuit.setInputMask("00-00000000-0")
            self.groupBox.setTitle('Codigo:' + str(self.codigo))
            self.txtCodigo.setText(str(controlador.obtenerId(self.sesion,
                                                             'ctacte')))
            self.dteAlta.setDate(QDate.currentDate())
            self.btnAceptar.button(QtWidgets.QDialogButtonBox.Save).setText(
                "&Agregar")
            self.setWindowTitle("Agregar CtaCte")

    def cargarcboProvincia(self):
        self.cboProvincia.clear()
        self.cboProvincia.addItem("Provincia")
        lista = controlador.obtenerProvincias(self.sesion, 1)
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

    def validar_cuit(self):
        # validaciones minimas
        cuit = self.txtCuit.text()
        if len(cuit) != 13 or cuit[2] != "-" or cuit[11] != "-":
            return False
        base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        # remuevo las barras
        cuit = cuit.replace("-", "")
        # calculo el digito verificador:
        aux = 0
        for i in range(10):
            aux += int(cuit[i]) * base[i]
            aux = 11 - (aux - (int(aux / 11) * 11))
            if aux == 11:
                aux = 0
            if aux == 10:
                aux = 9

            if (aux == int(cuit[10])) is False:
                return QtWidgets.QMessageBox.information(self, 'Mensaje',
                                                         ''' Cuit Invalido''',
                                                         QtWidgets.QMessageBox
                                                         .Ok)

    def accept(self):
        try:
            ctacteDic = {}
            ctacteDic["nombre"] = str(self.txtNombre.text())
            ctacteDic["domicilio"] = str(self.txtDomicilio.text())
            ctacteDic["cuit"] = str(self.txtCuit.text())
            ctacteDic["obs"] = str(self.txtObs.toPlainText())
            ctacteDic["codpos"] = str(self.txtCodpost.text())
            ctacteDic["ivatipo"] = str(self.cboIvatipo.currentIndex())
            ctacteDic["telefono"] = int(self.txtTelefono.text())
            ctacteDic["falta"] = self.dteAlta.date().toPyDate()
            ctacteDic["provincia"] = self.cboProvincia.currentIndex()
            ctacteDic["localidad"] = self.cboLocalidad.currentIndex()
            data = ({"ctacte": ctacteDic})
            controlador.agrmodCtaCte(self.sesion, data, self.codigo)

        except (ValueError):
            print ("Se produjo un error de valor")

        QtWidgets.QDialog.accept(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
