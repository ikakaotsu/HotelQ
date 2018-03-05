import sys
import agrmodPasajero
import agrmodCtaCte
import listaPasajeros
import listaCtaCte
import listaPrecios
import ingresarPasajero
from PyQt5 import Qt, QtWidgets
from vistas.ui_principal import Ui_Hotel
from controladores import controlador


class ppalHotel(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ppalHotel, self).__init__(parent)
        self.sesion = controlador.conectaraBD()
        self.ui = Ui_Hotel()
        self.ui.setupUi(self)
        self.ui.actSalir.triggered.connect(QtWidgets.qApp.quit)
        self.showMaximized()

    def agrPasajero(self):
        form = agrmodPasajero.AgrModPasajero(self.sesion)
        form.exec_()
    """    if(form.exec_()):
            print ("funciona") """

    def modXid(self):
        codigo, ok = QtWidgets.QInputDialog.getInt(self, 'Modificar por Id',
                                                   'Ingrese Codigo:', 1, 1)
        if ok:
            consulta = controlador.consultaPasajero(self.sesion, codigo)
            try:
                form = agrmodPasajero.AgrModPasajero(self.sesion, consulta,
                                                     codigo)
                form.exec_()
            except:
                QtWidgets.QMessageBox.information(self, 'Mensaje',
                                                  'Pasajero no encontrado',
                                                  QtWidgets.QMessageBox.Ok)

    def modXnya(self):
        ayn, ok = QtWidgets.QInputDialog.getText(self, 'Modificar Pasajero',
                                                 'Ingrese Apellido y Nombre:')
        if (ok & (ayn != '')):
            codigo = controlador.consultaXAyN(self.sesion, str(ayn))
            form = listaPasajeros.ListaPasajeros(self.sesion, codigo,
                                                 flag=True)
            form.exec_()

    def consultar(self):
        ayn, ok = QtWidgets.QInputDialog.getText(self, 'Consultar Pasajero',
                                                 'Ingrese Apellido y Nombre:')
        if (ok & (ayn != '')):
            codigo = controlador.consultaXAyN(self.sesion, str(ayn))
            form = listaPasajeros.ListaPasajeros(self.sesion, codigo)
            form.exec_()

    def ingresar(self):
        form = ingresarPasajero.IngresarPasajero(self.sesion)
        if form.exec_():
            fila = int(form.cbonHab.currentText())-1
            codigo = form.txtcPas.text()
            if (self.ui.tblHotel.item(fila, 1) is None):
                ingreso = str(form.dtefIngreso.date().toPyDate())
                hingreso = form.timeEdit_2.time().toPyTime().strftime('%H:'
                                                                      '%M')
                egreso = str(form.dtefEgreso.date().toPyDate())
                hegreso = form.timeEdit.time().toPyTime().strftime('%H:'
                                                                   '%M')
                self.ui.tblHotel.setItem(fila, 0,
                                         QtWidgets.QTableWidgetItem(codigo))
                self.ui.tblHotel.setItem(fila, 1,
                                         QtWidgets.QTableWidgetItem(ingreso))
                self.ui.tblHotel.setItem(fila, 2,
                                         QtWidgets.QTableWidgetItem(str(
                                             hingreso)))
                self.ui.tblHotel.setItem(fila, 3,
                                         QtWidgets.QTableWidgetItem(egreso))
                self.ui.tblHotel.setItem(fila, 4,
                                         QtWidgets.QTableWidgetItem(str(
                                             hegreso)))
                self.ui.tblHotel.setItem(fila, 5,
                                         QtWidgets.QTableWidgetItem(
                                             form.lbl01.text()))
            else:
                mensaje = "Habitacion Ocupada"
                QtWidgets.QMessageBox.information(self, 'Mensaje', mensaje)
        else:
            print ("Cancelado")

    def egresar(self):
        nro, ok = QtWidgets.QInputDialog.getInt(self, 'Egresar Habitacion',
                                                'Ingrese Nro Habitacion:', 1, 1)
        if (ok and nro < 20):
            nro = nro - 1
            self.ui.tblHotel.removeRow(nro)
            self.ui.tblHotel.insertRow(nro)
        else:
            print ('celda ocupada')

    def agrCtaCte(self):
        form = agrmodCtaCte.AgrModCtaCte(self.sesion)
        form.exec_()

    def modCtaCte(self):
        """"""
        codigo, ok = QtWidgets.QInputDialog.getInt(self, 'Modificar por Id',
                                                   'Ingrese Codigo:', 1, 1)
        if ok:
            consulta = controlador.consultaCtaCte(self.sesion, codigo)
            try:
                form = agrmodCtaCte.AgrModCtaCte(self.sesion, consulta,
                                                 codigo)
                form.exec_()
            except:
                QtWidgets.QMessageBox.information(self, 'Mensaje',
                                                  'CtaCte no encontrado',
                                                  QtWidgets.QMessageBox.Ok)

    def elimCtaCte(self):
        """"""

    def listaCtaCte(self):
        """"""
        form = listaCtaCte.ListaCtaCte(self.sesion)
        form.exec_()

    def listaPasajeros(self):
        """"""
        form = listaPasajeros.ListaPasajeros(self.sesion)
        form.exec_()

    def listaPrecios(self):
        """"""
        self.form = listaPrecios.ListaPrecios()
        self.form.setWindowModality(Qt.Qt.ApplicationModal)
        self.form.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = ppalHotel()
    ui.show()
    sys.exit(app.exec_())
