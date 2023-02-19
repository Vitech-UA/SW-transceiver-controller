from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice

app = QtWidgets.QApplication([])
ui = uic.loadUi("ui.ui")
ui.setWindowTitle("Serial connector")

serial = QSerialPort()
serial.setBaudRate(115200)
portlist = []
ports = QSerialPortInfo.availablePorts()
for port in ports:
    portlist.append(port.portName())
ui.ports_combobox.addItems(portlist)

ui.show()
app.exec()
