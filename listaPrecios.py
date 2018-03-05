from PyQt5 import QtWidgets
from vistas import ui_listaPrecios


class ListaPrecios(QtWidgets.QMainWindow,
                   ui_listaPrecios.Ui_listaPrecios):
    def __init__(self, parent=None):
        super(ListaPrecios, self).__init__(parent)
        self.setupUi(self)
        self.fmAgregar.hide()

    def nuevo(self):
        """"""
        self.fmAgregar.show()

    def guardar(self):
        """"""

    def modificar(self):
        """"""

    def eliminar(self):
        """"""

    def buscar(self):
        """"""

    def imprimir(self):
        """"""

    def agregar(self):
        """"""
        rubro = QtWidgets.QTableWidgetItem(self.txtrubro.text())
        articulo = QtWidgets.QTableWidgetItem(self.txtarticulo.text())
        stock = QtWidgets.QTableWidgetItem(str(self.sbstock.value()))
        precio = QtWidgets.QTableWidgetItem(self.txtprecio.text())
        descripcion = QtWidgets.QTableWidgetItem(self.txtdescripcion.text())
        print(stock)
        posicionfila = self.tableWidget.rowCount()
        self.tableWidget.insertRow(posicionfila)
        self.tableWidget.setItem(posicionfila, 1, rubro)
        self.tableWidget.setItem(posicionfila, 2, articulo)
        self.tableWidget.setItem(posicionfila, 3, stock)
        self.tableWidget.setItem(posicionfila, 4, precio)
        self.tableWidget.setItem(posicionfila, 5, descripcion)
        self.fmAgregar.hide()
        print("Boton Presionado")
