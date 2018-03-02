# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listaPasajeros.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlglistaPasajeros(object):
    def setupUi(self, dlglistaPasajeros):
        dlglistaPasajeros.setObjectName("dlglistaPasajeros")
        dlglistaPasajeros.resize(718, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/freeicons24x24/alien.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlglistaPasajeros.setWindowIcon(icon)
        dlglistaPasajeros.setSizeGripEnabled(False)
        dlglistaPasajeros.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(dlglistaPasajeros)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tblista = QtWidgets.QTableWidget(dlglistaPasajeros)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblista.sizePolicy().hasHeightForWidth())
        self.tblista.setSizePolicy(sizePolicy)
        self.tblista.setAlternatingRowColors(True)
        self.tblista.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblista.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblista.setCornerButtonEnabled(False)
        self.tblista.setObjectName("tblista")
        self.tblista.setColumnCount(4)
        self.tblista.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblista.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblista.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblista.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblista.setHorizontalHeaderItem(3, item)
        self.tblista.horizontalHeader().setCascadingSectionResizes(False)
        self.tblista.horizontalHeader().setDefaultSectionSize(150)
        self.tblista.horizontalHeader().setSortIndicatorShown(True)
        self.tblista.horizontalHeader().setStretchLastSection(True)
        self.tblista.verticalHeader().setVisible(False)
        self.tblista.verticalHeader().setCascadingSectionResizes(False)
        self.tblista.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tblista)
        self.btnlista = QtWidgets.QDialogButtonBox(dlglistaPasajeros)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnlista.sizePolicy().hasHeightForWidth())
        self.btnlista.setSizePolicy(sizePolicy)
        self.btnlista.setAcceptDrops(False)
        self.btnlista.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnlista.setAutoFillBackground(False)
        self.btnlista.setOrientation(QtCore.Qt.Horizontal)
        self.btnlista.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.btnlista.setCenterButtons(True)
        self.btnlista.setObjectName("btnlista")
        self.verticalLayout.addWidget(self.btnlista)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(dlglistaPasajeros)
        self.btnlista.rejected.connect(dlglistaPasajeros.reject)
        self.btnlista.accepted.connect(dlglistaPasajeros.accept)
        QtCore.QMetaObject.connectSlotsByName(dlglistaPasajeros)

    def retranslateUi(self, dlglistaPasajeros):
        _translate = QtCore.QCoreApplication.translate
        dlglistaPasajeros.setWindowTitle(_translate("dlglistaPasajeros", "Lista Pasajeros"))
        item = self.tblista.horizontalHeaderItem(0)
        item.setText(_translate("dlglistaPasajeros", "Codigo"))
        item = self.tblista.horizontalHeaderItem(1)
        item.setText(_translate("dlglistaPasajeros", "Documento Nº"))
        item = self.tblista.horizontalHeaderItem(2)
        item.setText(_translate("dlglistaPasajeros", "Nombre y Apellido"))
        item = self.tblista.horizontalHeaderItem(3)
        item.setText(_translate("dlglistaPasajeros", "Observaciones"))

from . import iconosQ
