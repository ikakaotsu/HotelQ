# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListaCtaCte.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_listaCtaCte(object):
    def setupUi(self, listaCtaCte):
        listaCtaCte.setObjectName("listaCtaCte")
        listaCtaCte.resize(615, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/freeicons24x24/alien.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        listaCtaCte.setWindowIcon(icon)
        listaCtaCte.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(listaCtaCte)
        self.gridLayout.setObjectName("gridLayout")
        self.tviewCtaCte = QtWidgets.QTableView(listaCtaCte)
        self.tviewCtaCte.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tviewCtaCte.setCornerButtonEnabled(False)
        self.tviewCtaCte.setObjectName("tviewCtaCte")
        self.tviewCtaCte.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tviewCtaCte, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.btnAceptar = QtWidgets.QDialogButtonBox(listaCtaCte)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAceptar.sizePolicy().hasHeightForWidth())
        self.btnAceptar.setSizePolicy(sizePolicy)
        self.btnAceptar.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btnAceptar.setFont(font)
        self.btnAceptar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnAceptar.setAutoFillBackground(False)
        self.btnAceptar.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.btnAceptar.setCenterButtons(True)
        self.btnAceptar.setObjectName("btnAceptar")
        self.gridLayout.addWidget(self.btnAceptar, 1, 0, 1, 1)

        self.retranslateUi(listaCtaCte)
        self.btnAceptar.accepted.connect(listaCtaCte.buscar)
        self.btnAceptar.rejected.connect(listaCtaCte.reject)
        QtCore.QMetaObject.connectSlotsByName(listaCtaCte)

    def retranslateUi(self, listaCtaCte):
        _translate = QtCore.QCoreApplication.translate
        listaCtaCte.setWindowTitle(_translate("listaCtaCte", "Lista CtaCte"))

from . import iconosQ
