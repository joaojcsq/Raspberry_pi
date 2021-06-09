from PyQt5 import QtWidgets, uic
import variaveis
import sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('tela.ui', self)
        self.show()

        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')  # Find the button
        self.button.clicked.connect(self.gerador)

        self.freq = self.findChild(QtWidgets.QLineEdit, 'lineEdit_freq')
        self.duty = self.findChild(QtWidgets.QLineEdit, 'lineEdit_duty')
        self.gpio = self.findChild(QtWidgets.QLineEdit, 'lineEdit_gpio')

    def gerador(self):
        freq = int(self.freq.text())
        duty = int(self.duty.text())
        porta = int(self.gpio.text())

        GPIO.setup(porta, GPIO.OUT)

        try:
            self.pulso = GPIO.PWM(porta, freq)
            self.pulso.start(0)
        except RuntimeError:
            del self.pulso
            self.pulso = GPIO.PWM(porta, freq)
            self.pulso.start(0)

        if variaveis.status_bt:
            variaveis.status_bt = False
            self.button.setStyleSheet('background-color: rgb(255, 10, 10)')
            self.pulso.ChangeDutyCycle(0)
            self.button.setText("OFF")
        else:
            variaveis.status_bt = True
            self.button.setStyleSheet('background-color : rgb(85, 255, 127)')
            self.button.setText("ON")
            self.pulso.ChangeDutyCycle(duty)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
