# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddModPasajero.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_agrmodPasajero(object):
    def setupUi(self, agrmodPasajero):
        agrmodPasajero.setObjectName("agrmodPasajero")
        agrmodPasajero.resize(630, 465)
        agrmodPasajero.setMaximumSize(QtCore.QSize(630, 465))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/freeicons24x24/alien.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        agrmodPasajero.setWindowIcon(icon)
        agrmodPasajero.setStyleSheet("")
        self.groupBox = QtWidgets.QGroupBox(agrmodPasajero)
        self.groupBox.setGeometry(QtCore.QRect(0, 3, 630, 461))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 601, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txtOcupacion = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtOcupacion.setObjectName("txtOcupacion")
        self.gridLayout.addWidget(self.txtOcupacion, 5, 5, 1, 3)
        self.txtApellido = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtApellido.setObjectName("txtApellido")
        self.gridLayout.addWidget(self.txtApellido, 1, 1, 1, 3)
        self.lblNombre = QtWidgets.QLabel(self.layoutWidget)
        self.lblNombre.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNombre.setObjectName("lblNombre")
        self.gridLayout.addWidget(self.lblNombre, 1, 4, 1, 1)
        self.cboProvincia = QtWidgets.QComboBox(self.layoutWidget)
        self.cboProvincia.setObjectName("cboProvincia")
        self.gridLayout.addWidget(self.cboProvincia, 4, 1, 1, 3)
        self.lblFn = QtWidgets.QLabel(self.layoutWidget)
        self.lblFn.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFn.setObjectName("lblFn")
        self.gridLayout.addWidget(self.lblFn, 3, 0, 1, 1)
        self.lblLocalidad = QtWidgets.QLabel(self.layoutWidget)
        self.lblLocalidad.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLocalidad.setObjectName("lblLocalidad")
        self.gridLayout.addWidget(self.lblLocalidad, 4, 4, 1, 1)
        self.lblCivil = QtWidgets.QLabel(self.layoutWidget)
        self.lblCivil.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCivil.setObjectName("lblCivil")
        self.gridLayout.addWidget(self.lblCivil, 5, 0, 1, 1)
        self.lblApellido = QtWidgets.QLabel(self.layoutWidget)
        self.lblApellido.setAlignment(QtCore.Qt.AlignCenter)
        self.lblApellido.setObjectName("lblApellido")
        self.gridLayout.addWidget(self.lblApellido, 1, 0, 1, 1)
        self.cboECivil = QtWidgets.QComboBox(self.layoutWidget)
        self.cboECivil.setObjectName("cboECivil")
        self.cboECivil.addItem("")
        self.cboECivil.addItem("")
        self.cboECivil.addItem("")
        self.cboECivil.addItem("")
        self.gridLayout.addWidget(self.cboECivil, 5, 1, 1, 3)
        self.lblObs = QtWidgets.QLabel(self.layoutWidget)
        self.lblObs.setAlignment(QtCore.Qt.AlignCenter)
        self.lblObs.setObjectName("lblObs")
        self.gridLayout.addWidget(self.lblObs, 7, 0, 1, 1)
        self.txtNombre = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtNombre.setObjectName("txtNombre")
        self.gridLayout.addWidget(self.txtNombre, 1, 5, 1, 3)
        self.cboLocalidad = QtWidgets.QComboBox(self.layoutWidget)
        self.cboLocalidad.setObjectName("cboLocalidad")
        self.gridLayout.addWidget(self.cboLocalidad, 4, 5, 1, 3)
        self.lblTdoc = QtWidgets.QLabel(self.layoutWidget)
        self.lblTdoc.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTdoc.setObjectName("lblTdoc")
        self.gridLayout.addWidget(self.lblTdoc, 0, 0, 1, 1)
        self.lblDomicilio = QtWidgets.QLabel(self.layoutWidget)
        self.lblDomicilio.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDomicilio.setObjectName("lblDomicilio")
        self.gridLayout.addWidget(self.lblDomicilio, 2, 0, 1, 1)
        self.lblNumero = QtWidgets.QLabel(self.layoutWidget)
        self.lblNumero.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNumero.setObjectName("lblNumero")
        self.gridLayout.addWidget(self.lblNumero, 0, 4, 1, 1)
        self.lblOcupacion = QtWidgets.QLabel(self.layoutWidget)
        self.lblOcupacion.setAlignment(QtCore.Qt.AlignCenter)
        self.lblOcupacion.setObjectName("lblOcupacion")
        self.gridLayout.addWidget(self.lblOcupacion, 5, 4, 1, 1)
        self.lblNacinalidad = QtWidgets.QLabel(self.layoutWidget)
        self.lblNacinalidad.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNacinalidad.setObjectName("lblNacinalidad")
        self.gridLayout.addWidget(self.lblNacinalidad, 3, 4, 1, 1)
        self.lblProvincia = QtWidgets.QLabel(self.layoutWidget)
        self.lblProvincia.setAlignment(QtCore.Qt.AlignCenter)
        self.lblProvincia.setObjectName("lblProvincia")
        self.gridLayout.addWidget(self.lblProvincia, 4, 0, 1, 1)
        self.txtNumero = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtNumero.setObjectName("txtNumero")
        self.gridLayout.addWidget(self.txtNumero, 0, 5, 1, 3)
        self.txtDomicilio = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtDomicilio.setObjectName("txtDomicilio")
        self.gridLayout.addWidget(self.txtDomicilio, 2, 1, 1, 7)
        self.cboNacional = QtWidgets.QComboBox(self.layoutWidget)
        self.cboNacional.setObjectName("cboNacional")
        self.gridLayout.addWidget(self.cboNacional, 3, 5, 1, 3)
        self.lblTelefono = QtWidgets.QLabel(self.layoutWidget)
        self.lblTelefono.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTelefono.setObjectName("lblTelefono")
        self.gridLayout.addWidget(self.lblTelefono, 6, 0, 1, 1)
        self.txtObs = QtWidgets.QTextEdit(self.layoutWidget)
        self.txtObs.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.txtObs.setObjectName("txtObs")
        self.gridLayout.addWidget(self.txtObs, 7, 1, 1, 7)
        self.lblMail = QtWidgets.QLabel(self.layoutWidget)
        self.lblMail.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMail.setObjectName("lblMail")
        self.gridLayout.addWidget(self.lblMail, 6, 4, 1, 1)
        self.txtMail = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtMail.setObjectName("txtMail")
        self.gridLayout.addWidget(self.txtMail, 6, 5, 1, 3)
        self.txtTelefono = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtTelefono.setObjectName("txtTelefono")
        self.gridLayout.addWidget(self.txtTelefono, 6, 1, 1, 3)
        self.dteFn = QtWidgets.QDateEdit(self.layoutWidget)
        self.dteFn.setCalendarPopup(False)
        self.dteFn.setDate(QtCore.QDate(1984, 1, 2))
        self.dteFn.setObjectName("dteFn")
        self.gridLayout.addWidget(self.dteFn, 3, 1, 1, 3)
        self.cboTdoc = QtWidgets.QComboBox(self.layoutWidget)
        self.cboTdoc.setObjectName("cboTdoc")
        self.cboTdoc.addItem("")
        self.cboTdoc.addItem("")
        self.cboTdoc.addItem("")
        self.cboTdoc.addItem("")
        self.cboTdoc.addItem("")
        self.gridLayout.addWidget(self.cboTdoc, 0, 1, 1, 3)
        self.btnAceptar = QtWidgets.QDialogButtonBox(self.groupBox)
        self.btnAceptar.setGeometry(QtCore.QRect(80, 423, 541, 32))
        self.btnAceptar.setMinimumSize(QtCore.QSize(0, 0))
        self.btnAceptar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnAceptar.setAutoFillBackground(False)
        self.btnAceptar.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Argentina))
        self.btnAceptar.setOrientation(QtCore.Qt.Horizontal)
        self.btnAceptar.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.btnAceptar.setCenterButtons(False)
        self.btnAceptar.setObjectName("btnAceptar")
        self.lblNumero.setBuddy(self.txtNumero)

        self.retranslateUi(agrmodPasajero)
        self.cboNacional.currentIndexChanged['int'].connect(self.cboProvincia.setFocus)
        self.cboProvincia.currentIndexChanged['int'].connect(self.cboLocalidad.setFocus)
        self.btnAceptar.accepted.connect(agrmodPasajero.accept)
        self.btnAceptar.rejected.connect(agrmodPasajero.reject)
        self.cboTdoc.currentIndexChanged['QString'].connect(self.txtNumero.update)
        QtCore.QMetaObject.connectSlotsByName(agrmodPasajero)
        agrmodPasajero.setTabOrder(self.cboTdoc, self.txtNumero)
        agrmodPasajero.setTabOrder(self.txtNumero, self.txtApellido)
        agrmodPasajero.setTabOrder(self.txtApellido, self.txtNombre)
        agrmodPasajero.setTabOrder(self.txtNombre, self.txtDomicilio)
        agrmodPasajero.setTabOrder(self.txtDomicilio, self.dteFn)
        agrmodPasajero.setTabOrder(self.dteFn, self.cboNacional)
        agrmodPasajero.setTabOrder(self.cboNacional, self.cboProvincia)
        agrmodPasajero.setTabOrder(self.cboProvincia, self.cboLocalidad)
        agrmodPasajero.setTabOrder(self.cboLocalidad, self.cboECivil)
        agrmodPasajero.setTabOrder(self.cboECivil, self.txtOcupacion)
        agrmodPasajero.setTabOrder(self.txtOcupacion, self.txtTelefono)
        agrmodPasajero.setTabOrder(self.txtTelefono, self.txtMail)
        agrmodPasajero.setTabOrder(self.txtMail, self.txtObs)
        agrmodPasajero.setTabOrder(self.txtObs, self.btnAceptar)

    def retranslateUi(self, agrmodPasajero):
        _translate = QtCore.QCoreApplication.translate
        agrmodPasajero.setWindowTitle(_translate("agrmodPasajero", "Agregar Pasajero"))
        self.lblNombre.setText(_translate("agrmodPasajero", "Nombre:"))
        self.lblFn.setText(_translate("agrmodPasajero", "Fecha de Nacimiento:"))
        self.lblLocalidad.setText(_translate("agrmodPasajero", "Localidad:"))
        self.lblCivil.setText(_translate("agrmodPasajero", "Estado Civil:"))
        self.lblApellido.setText(_translate("agrmodPasajero", "Apellido:"))
        self.cboECivil.setItemText(0, _translate("agrmodPasajero", "Soltero"))
        self.cboECivil.setItemText(1, _translate("agrmodPasajero", "Casado"))
        self.cboECivil.setItemText(2, _translate("agrmodPasajero", "Viudo"))
        self.cboECivil.setItemText(3, _translate("agrmodPasajero", "Separado"))
        self.lblObs.setText(_translate("agrmodPasajero", "Observaciones"))
        self.lblTdoc.setText(_translate("agrmodPasajero", "Tipo de Documento:"))
        self.lblDomicilio.setText(_translate("agrmodPasajero", "Domicilio:"))
        self.lblNumero.setText(_translate("agrmodPasajero", " N&umero:"))
        self.lblOcupacion.setText(_translate("agrmodPasajero", "Ocupacion:"))
        self.lblNacinalidad.setText(_translate("agrmodPasajero", "Nacionalidad:"))
        self.lblProvincia.setText(_translate("agrmodPasajero", "Provincia:"))
        self.lblTelefono.setText(_translate("agrmodPasajero", "Telefono"))
        self.lblMail.setText(_translate("agrmodPasajero", "Mail"))
        self.dteFn.setDisplayFormat(_translate("agrmodPasajero", "yyyy-MM-dd"))
        self.cboTdoc.setItemText(0, _translate("agrmodPasajero", "DNI"))
        self.cboTdoc.setItemText(1, _translate("agrmodPasajero", "Pasaporte"))
        self.cboTdoc.setItemText(2, _translate("agrmodPasajero", "Carné de Identidad"))
        self.cboTdoc.setItemText(3, _translate("agrmodPasajero", "Libreta de Enrrolamiento"))
        self.cboTdoc.setItemText(4, _translate("agrmodPasajero", "Libreta Civica"))

from . import iconosQ
