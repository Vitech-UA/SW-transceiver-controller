from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
from uart_connector import UartConnector

uart_port = UartConnector()
uart_port.bode_rate = 11520

app = QtWidgets.QApplication([])
ui = uic.loadUi("ui.ui")
ui.setWindowTitle("Serial connector")

serial = QSerialPort()
serial.setBaudRate(115200)
portlist = []
ports = QSerialPortInfo.availablePorts()
for port in ports:
    portlist.append("{}".format(port.portName()))
    ui.ports_combobox.addItems(portlist)


def open_port():
    serial.setPortName(ui.ports_combobox.currentText())
    serial.open(QIODevice.ReadWrite)


def close_port():
    serial.setPortName(ui.ports_combobox.currentText())
    serial.close()


def on_read():
    RX_RAW = serial.readLine()
    RX_STR = str(RX_RAW, "utf-8")
    print(RX_STR.strip())


def led_control():
    if ui.check_box_led.isChecked():
        serial.write("set_led 1\r\n".encode())
    if not ui.check_box_led.isChecked():
        serial.write("set_led 0\r\n".encode())


ui.close_btn.clicked.connect(close_port)
ui.open_btn.clicked.connect(open_port)
ui.check_box_led.stateChanged.connect(led_control)
serial.readyRead.connect(on_read)
ui.show()
app.exec()
