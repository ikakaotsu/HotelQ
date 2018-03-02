import sys
from PyQt5 import QtGui, QtCore

rows = "ABCD"
choices = ['apple', 'orange', 'banana']


class Delegate(QtGui.QItemDelegate):
    def __init__(self, owner, items):
        super(Delegate, self).__init__(owner)
        self.items = items

    def createEditor(self, parent, option, index):
        self.editor = QtGui.QComboBox(parent)
        self.editor.addItems(self.items)
        return self.editor

    def paint(self, painter, option, index):
        value = index.data(QtCore.Qt.DisplayRole).toString()
        style = QtGui.QApplication.style()
        opt = QtGui.QStyleOptionComboBox()
        opt.text = str(value)
        opt.rect = option.rect
        style.drawComplexControl(QtGui.QStyle.CC_ComboBox, opt, painter)
        QtGui.QItemDelegate.paint(self, painter, option, index)

    def setEditorData(self, editor, index):
        value = index.data(QtCore.Qt.DisplayRole).toString()
        num = self.items.index(value)
        editor.setCurrentIndex(num)

    def setModelData(self, editor, model, index):
        value = editor.currentText()
        model.setData(index, QtCore.Qt.DisplayRole, QtCore.QVariant(value))

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class Model(QtCore.QAbstractTableModel):
    def __init__(self):
        super(Model, self).__init__()
        self.table = [[row, choices[0]] for row in rows]

    def rowCount(self, index=QtCore.QModelIndex()):
        return len(self.table)

    def columnCount(self, index=QtCore.QModelIndex()):
        return 2

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.table[index.row()][index.column()]

    def setData(self, index, role, value):
        if role == QtCore.Qt.DisplayRole:
            self.table[index.row()][index.column()] = value


class Main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.model = Model()
        self.table = QtGui.QTableView()
        self.table.setModel(self.model)
        self.table.setItemDelegateForColumn(1, Delegate(self, ["apple", "orange", "banana"]))
        self.setCentralWidget(self.table)
        self.setWindowTitle('Delegate Test')
        self.show()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    app.exec_()
