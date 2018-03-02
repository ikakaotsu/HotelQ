import agrmodPasajero
import infoPasajero
from PyQt5 import QtWidgets
from views import ui_listaPasajeros
from controllers import controlador


class ListaPasajeros(QtWidgets.QDialog,
                     ui_listaPasajeros.Ui_dlglistaPasajeros):
    def __init__(self, sesion, codigo=None, flag=False, parent=None):
        super(ListaPasajeros, self).__init__(parent)
        self.setupUi(self)
        self.flag = flag
        self.sesion = sesion
        self.codigo = codigo
        self.cargarPasajeros()
        self.btnlista.button(QtWidgets.QDialogButtonBox.Close).setText(
            "&Salir")
        if self.flag:
            self.btnlista.button(QtWidgets.QDialogButtonBox.Ok).setText(
                "&Modificar")
        else:
            self.btnlista.button(QtWidgets.QDialogButtonBox.Ok).setText(
                "&Ver")

    def cargarPasajeros(self):
        lista = controlador.obtenerPasajeros(self.sesion)
        n = len(lista)
        self.tblista.setRowCount(n)
        for i in range(n):
            if (lista[i][0] == self.codigo):
                self.tblista.selectRow(i)
            item1 = QtWidgets.QTableWidgetItem(str(lista[i][0]))
            item2 = QtWidgets.QTableWidgetItem(lista[i][1])
            item3 = QtWidgets.QTableWidgetItem(lista[i][3] + ' ' + lista[i][2])
            item4 = QtWidgets.QTableWidgetItem(lista[i][4])
            self.tblista.setItem(i, 0, item1)
            self.tblista.setItem(i, 1, item2)
            self.tblista.setItem(i, 2, item3)
            self.tblista.setItem(i, 3, item4)

    def accept(self):
        """"""
        if self.flag:
            fila = self.tblista.currentItem().row()
            codigo = self.tblista.item(fila, 0).text()
            consulta = controlador.consultaPasajero(self.sesion, codigo)
            dlg = agrmodPasajero.AgrModPasajero(self.sesion, consulta, codigo)
            if (dlg.exec_()):
                self.tblista.clearContents()
                self.cargarPasajeros()
        else:
            fila = self.tblista.currentItem().row()
            codigo = self.tblista.item(fila, 0).text()
            consulta = controlador.consultaPasajero(self.sesion, codigo)
            self.frame = infoPasajero.InfoPasajero(self.sesion, consulta)
            self.frame.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = ListaPasajeros()
    form.show()
    app.exec_()
