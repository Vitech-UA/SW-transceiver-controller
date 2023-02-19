from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
ui = uic.loadUi("ui.ui")
ui.setWindowTitle("Serial connector")
ui.show()

app.exec()
