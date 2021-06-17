from PyQt5 import QtWidgets, uic
import sys
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
CS = 18
UD = 23
INC = 24
GPIO.setup(CS, GPIO.OUT)  # CS
GPIO.setup(UD, GPIO.OUT)  # UD
GPIO.setup(INC, GPIO.OUT)  # INC

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ihm.ui', self)
        self.show()

        self.bt_mais = self.findChild(QtWidgets.QPushButton, 'bt_mais')
        self.bt_mais.clicked.connect(self.mais)

        self.bt_menos = self.findChild(QtWidgets.QPushButton, 'bt_menos')
        self.bt_menos.clicked.connect(self.menos)

        self.bt_memoria = self.findChild(QtWidgets.QPushButton, 'bt_memoria')
        self.bt_memoria.clicked.connect(self.memoria)

    def mais(self):
        print("+")
        GPIO.output(CS, GPIO.LOW)
        GPIO.output(UD, GPIO.HIGH)
        GPIO.output(INC, GPIO.HIGH)
        sleep(0.05)
        GPIO.output(INC, GPIO.LOW)

    def menos(self):
        print("-")
        GPIO.output(CS, GPIO.LOW)
        GPIO.output(UD, GPIO.LOW)
        GPIO.output(INC, GPIO.HIGH)
        sleep(0.05)
        GPIO.output(INC, GPIO.LOW)

    def memoria(self):
        print("Gravando... ")
        GPIO.output(INC, GPIO.HIGH)
        GPIO.output(CS, GPIO.HIGH)
        sleep(0.05)
        GPIO.output(CS, GPIO.LOW)
        print("OK!")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
