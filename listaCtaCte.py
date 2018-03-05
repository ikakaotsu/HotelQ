from PyQt5 import QtWidgets, QtGui, QtCore
from vistas import ui_listaCtaCte
from controladores import controlador


class ListaCtaCte(QtWidgets.QDialog,
                  ui_listaCtaCte.Ui_listaCtaCte):
    def __init__(self, sesion, codigo=None, parent=None):
        super(ListaCtaCte, self).__init__(parent)
        self.setupUi(self)
        self.sesion = sesion
        self.codigo = codigo
        self.cargarCtaCte()
        self.btnAceptar.button(QtWidgets.QDialogButtonBox.Close).setText(
            "&Salir")
        self.btnAceptar.button(QtWidgets.QDialogButtonBox.Ok).setText(
            "&Buscar")

    def cargarCtaCte(self):
        modelo = QtGui.QStandardItemModel(0, 10, self)
        modelo.setHorizontalHeaderItem(0, QtGui.QStandardItem("Codigo"))
        modelo.setHorizontalHeaderItem(1, QtGui.QStandardItem("Nombre"))
        modelo.setHorizontalHeaderItem(2, QtGui.QStandardItem("Domicilio"))
        modelo.setHorizontalHeaderItem(3, QtGui.QStandardItem("Cuit"))
        modelo.setHorizontalHeaderItem(4, QtGui.QStandardItem("Cod Postal"))
        modelo.setHorizontalHeaderItem(5, QtGui.QStandardItem("Tipo de Iva")
                                       )
        modelo.setHorizontalHeaderItem(6, QtGui.QStandardItem("Telefono"))
        modelo.setHorizontalHeaderItem(7, QtGui.QStandardItem("Fecha de Alta"))
        modelo.setHorizontalHeaderItem(8, QtGui.QStandardItem("Provincia"))
        modelo.setHorizontalHeaderItem(9, QtGui.QStandardItem("Localidad"))
        modelo.setHorizontalHeaderItem(10, QtGui.QStandardItem("Observaciones"))
        tiva = ["Res. Inscripto", "Exento", "Consumidor Final",
                "Monotributista"]
        lista = controlador.obtenerCtaCte(self.sesion)
        for i in range(len(lista)):
            vcodigo = QtGui.QStandardItem(str(lista[i].id))
            vnombre = QtGui.QStandardItem(lista[i].nombre)
            vdomicilio = QtGui.QStandardItem(lista[i].domicilio)
            vcuit = QtGui.QStandardItem(lista[i].cuit)
            vobservaciones = QtGui.QStandardItem(lista[i].observaciones)
            vcodigopostal = QtGui.QStandardItem(str(lista[i].codigopostal))
            vivatipo = QtGui.QStandardItem(str(tiva[lista[i].ivatipo]))
            vtelefono = QtGui.QStandardItem(str(lista[i].telefono))
            vfechalta = QtGui.QStandardItem(str(lista[i].fechalta))
            vprovincia = QtGui.QStandardItem(controlador.consultaProvincia(
                                             self.sesion, lista[i].provincia))
            vlocalidad = QtGui.QStandardItem(controlador.consultaLocalidad(
                                             self.sesion, lista[i].localidad))
            modelo.setItem(i, 0, vcodigo)
            modelo.setItem(i, 1, vnombre)
            modelo.setItem(i, 2, vdomicilio)
            modelo.setItem(i, 3, vcuit)
            modelo.setItem(i, 4, vcodigopostal)
            modelo.setItem(i, 5, vivatipo)
            modelo.setItem(i, 6, vtelefono)
            modelo.setItem(i, 7, vfechalta)
            modelo.setItem(i, 8, vprovincia)
            modelo.setItem(i, 9, vlocalidad)
            modelo.setItem(i, 10, vobservaciones)
        self.tviewCtaCte.setModel(modelo)

    def buscar(self):
        """"""
        apeynom, ok = QtWidgets.QInputDialog.getText(self, 'Apellido y Nombre',
                                                     'Apellido y Nombre:')
        if(ok & (apeynom != '')):
            modl = self.tviewCtaCte.model()
            proxy = QtCore.QSortFilterProxyModel()
            proxy.setSourceModel(modl)
            proxy.setFilterKeyColumn(1)
            proxy.setFilterFixedString(apeynom)
            matchingIndex = proxy.mapToSource(proxy.index(0, 0))
            print(matchingIndex)
            if(matchingIndex.isValid()):
                self.tviewCtaCte.scrollTo(matchingIndex,
                                          QtWidgets.QAbstractItemView.
                                          EnsureVisible)
            else:
                QtWidgets.QMessageBox.information(self, 'Mensaje',
                                                  ''' CtaCte no Encontrado''',
                                                  QtWidgets.QMessageBox.Ok)
