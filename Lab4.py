# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
# from PyQt5.QtCore import pyqtSlot
#
# class App(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.title = 'PyQt5 wybieranie kolorów'
#         self.left = 10
#         self.top = 10
#         self.width = 320
#         self.height = 200
#         self.initUI()
#
#     def initUI(self):
#      self.setWindowTitle(self.title)
#      self.setGeometry(self.left, self.top, self.width, self.height)
#
#      button = QPushButton('Open color dialog', self)
#      button.setToolTip('Opens color dialog')
#      button.move(10, 10)
#      button.clicked.connect(self.on_click)
#      self.show()
#
#     @pyqtSlot()
#     def on_click(self):
#         openColorDialog(self)
#
# def openColorDialog(self):
#     color = QColorDialog.getColor()
#
#     if color.isValid():
#      print(color.name())
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
# ex = App()
# sys.exit(app.exec_())

# from PyQt5.QtWidgets import QWidget, QApplication
# from PyQt5.QtGui import QPainter, QColor
#
# class Kolory(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         self.interfejs()
#
#     def interfejs(self):
#
#         self.resize(400, 100)
#         self.setWindowTitle("Colors")
#         self.show()
#
#     def paintEvent(self, e):
#         qp = QPainter()
#         qp.begin(self)
#         self.drawRectangles(qp)
#         qp.end()
#
#     def drawRectangles(self, qp):
#         col = QColor(0, 0, 0)
#         col.setNamedColor('#d4d4d4')
#         qp.setPen(col)
#
#         qp.setBrush(QColor('red'))
#         qp.drawRect(10, 15, 90, 60)
#
#         qp.setBrush(QColor('orange'))
#         qp.drawRect(150, 15, 90, 60)
#
#         qp.setBrush(QColor('dark blue'))
#         qp.drawRect(300, 15, 90, 60)
#
# if __name__ == '__main__':
#     import sys
#
#     app = QApplication(sys.argv)
#     okno = Kolory()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication,QAction
# from PyQt5.QtGui import QIcon
#
# class App(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.title = 'PyQt5 menu'
#         self.left = 10
#         self.top = 10
#         self.width = 640
#         self.height = 400
#         self.initUI()
#
#     def initUI(self):
#      self.setWindowTitle(self.title)
#      self.setGeometry(self.left, self.top, self.width, self.height)
#
#      mainMenu = self.menuBar()
#      fileMenu = mainMenu.addMenu('Plik')
#      editMenu = mainMenu.addMenu('Edycja')
#      viewMenu = mainMenu.addMenu('Widok')
#      searchMenu = mainMenu.addMenu('Szukaj')
#      toolsMenu = mainMenu.addMenu('Narzędzia')
#      helpMenu = mainMenu.addMenu('Pomoc')
#      exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
#      exitButton.setShortcut('Ctrl+Q')
#      exitButton.setStatusTip('Exit application')
#      exitButton.triggered.connect(self.close)
#      fileMenu.addAction(exitButton)
#      self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
# ex = App()
# sys.exit(app.exec_())

import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

class Kalkulator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        etykieta1 = QLabel("Liczba 1:", self)
        etykieta2 = QLabel("Liczba 2:", self)
        etykieta3 = QLabel("Wynik:", self)

        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 0, 1)
        ukladT.addWidget(etykieta3, 0, 2)

        self.liczba1Edt = QLineEdit()
        self.liczba2Edt = QLineEdit()
        self.wynikEdt = QLineEdit()

        self.wynikEdt.readonly = True
        self.wynikEdt.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')

        ukladT.addWidget(self.liczba1Edt, 1, 0)
        ukladT.addWidget(self.liczba2Edt, 1, 1)
        ukladT.addWidget(self.wynikEdt, 1, 2)

        dodajBtn = QPushButton("&Dodaj", self)
        odejmijBtn = QPushButton("&Odejmij", self)
        dzielBtn = QPushButton("&Mnóż", self)
        mnozBtn = QPushButton("&Dziel", self)
        pierwBtn = QPushButton("&Pierwiastkuj", self)
        kwadratBtn = QPushButton("&Kwadratuj", self)
        odwrotBtn = QPushButton("&WOdwrotna", self)
        procenttBtn = QPushButton("&Procent", self)
        koniecBtn = QPushButton("&Koniec", self)
        koniecBtn.resize(koniecBtn.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajBtn)
        ukladH.addWidget(odejmijBtn)
        ukladH.addWidget(dzielBtn)
        ukladH.addWidget(pierwBtn)
        ukladH.addWidget(kwadratBtn)
        ukladH.addWidget(mnozBtn)
        ukladH.addWidget(odwrotBtn)
        ukladH.addWidget(procenttBtn)

        ukladT.addLayout(ukladH, 2, 0, 1, 3)
        ukladT.addWidget(koniecBtn, 3, 0, 1, 3)

        self.setLayout(ukladT)

        koniecBtn.clicked.connect(self.koniec)
        dodajBtn.clicked.connect(self.dzialanie)
        odejmijBtn.clicked.connect(self.dzialanie)
        mnozBtn.clicked.connect(self.dzialanie)
        pierwBtn.clicked.connect(self.dzialanie2)
        kwadratBtn.clicked.connect(self.dzialanie2)
        odwrotBtn.clicked.connect(self.dzialanie2)
        procenttBtn.clicked.connect(self.dzialanie)
        dzielBtn.clicked.connect(self.dzialanie)

        self.liczba1Edt.setFocus()
        self.setGeometry(20, 20, 300, 100)
        self.setWindowIcon(QIcon('kalkulator.png'))
        self.setWindowTitle("Prosty kalkulator")
        self.show()

    def koniec(self):
        self.close()

    def closeEvent(self, event):

        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno koniec?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def dzialanie(self):

        nadawca = self.sender()

        try:
            liczba1 = float(self.liczba1Edt.text())
            liczba2 = float(self.liczba2Edt.text())
            wynik = ""

            if nadawca.text() == "&Dodaj":
                wynik = liczba1 + liczba2
            elif nadawca.text() == "&Odejmij":
                wynik = liczba1 - liczba2
            elif nadawca.text() == "&Mnóż":
                wynik = liczba1 * liczba2
            elif nadawca.text() == "&Procent":
                wynik = 100 * float(liczba2) / float(liczba1)
            elif nadawca.text() == "&Dziel":
                try:
                    wynik = round(liczba1 / liczba2, 9)
                except ZeroDivisionError:
                    QMessageBox.critical(
                        self, "Błąd", "Nie można dzielić przez zero!")
                    return
            self.wynikEdt.setText(str(wynik))

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)

    def dzialanie2(self):

        nadawca = self.sender()

        try:
            liczba = float(self.liczba1Edt.text())
            wynik = ""

            if nadawca.text() == "&Kwadratuj":
                wynik = liczba * liczba
            elif nadawca.text() == "&WOdwrotna":
                wynik = 1 / liczba
            elif nadawca.text() == "&Pierwiastkuj":
                try:
                    wynik = math.sqrt(liczba)
                    if liczba < 0:
                        raise Exception
                except Exception:
                    QMessageBox.critical(
                        self, "Błąd", "Liczba musi byc wieksza od zera")
                    return
            self.wynikEdt.setText(str(wynik))
        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec_())

# import sys
# from math import sqrt
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
#
# num = 0.0
# newNum = 0.0
# sumIt = 0.0
# sumAll = 0.0
# operator = ""
#
# opVar = False
#
# class Calc(QMainWindow):
#
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.initUI()
#
#     def initUI(self):
#         self.line = QLineEdit(self)
#         self.line.move(5, 5)
#         self.line.setReadOnly(True)
#         self.line.setAlignment(Qt.AlignRight)
#         font = self.line.font()
#         font.setPointSize(40)
#         self.line.setFont(font)
#         self.line.resize(266, 70)
#
#         zero = QPushButton("0", self)
#         zero.move(5, 265)
#         zero.resize(45, 40)
#
#         one = QPushButton("1", self)
#         one.move(5, 215)
#         one.resize(45, 40)
#
#         two = QPushButton("2", self)
#         two.move(60, 215)
#         two.resize(45, 40)
#
#         three = QPushButton("3", self)
#         three.move(115, 215)
#         three.resize(45, 40)
#
#         four = QPushButton("4", self)
#         four.move(5, 165)
#         four.resize(45, 40)
#
#         five = QPushButton("5", self)
#         five.move(60, 165)
#         five.resize(45, 40)
#
#         six = QPushButton("6", self)
#         six.move(115, 165)
#         six.resize(45, 40)
#
#         seven = QPushButton("7", self)
#         seven.move(5, 115)
#         seven.resize(45, 40)
#
#         eight = QPushButton("8", self)
#         eight.move(60, 115)
#         eight.resize(45, 40)
#
#         nine = QPushButton("9", self)
#         nine.move(115, 115)
#         nine.resize(45, 40)
#
#         switch = QPushButton("+/-", self)
#         switch.move(60, 265)
#         switch.resize(45, 40)
#         switch.clicked.connect(self.Switch)
#
#         point = QPushButton(".", self)
#         point.move(115, 265)
#         point.resize(45, 40)
#         point.clicked.connect(self.Point)
#
#         plus = QPushButton("+", self)
#         plus.move(170, 265)
#         plus.resize(45, 40)
#
#         minus = QPushButton("-", self)
#         minus.move(170, 215)
#         minus.resize(45, 40)
#
#         multiply = QPushButton("*", self)
#         multiply.move(170, 165)
#         multiply.resize(45, 40)
#
#         divide = QPushButton("/", self)
#         divide.move(170, 115)
#         divide.resize(45, 40)
#
#         equals = QPushButton("=", self)
#         equals.move(225, 215)
#         equals.resize(45, 90)
#         equals.clicked.connect(self.Equal)
#
#         squared = QPushButton("x²", self)
#         squared.move(225, 165)
#         squared.resize(45, 40)
#         squared.clicked.connect(self.Squared)
#
#         root = QPushButton("√", self)
#         root.move(225, 115)
#         root.resize(45, 40)
#         root.clicked.connect(self.Root)
#
#         ce = QPushButton("CE", self)
#         ce.move(54, 75)
#         ce.resize(112, 40)
#         ce.clicked.connect(self.CE)
#
#         c = QPushButton("C", self)
#         c.move(164, 75)
#         c.resize(112, 40)
#         c.clicked.connect(self.C)
#
#
#         nums = [zero, one, two, three, four, five, six, seven, eight, nine]
#
#         operators = [ce, c, plus, minus, multiply, divide, equals]
#
#         others = [switch, squared, root, point]
#
#         for i in nums:
#             i.setStyleSheet("color:blue;")
#             i.clicked.connect(self.Num)
#
#         for i in operators:
#             i.setStyleSheet("color:red;")
#         for i in operators[2:]:
#             i.clicked.connect(self.operator)
#         for i in others:
#             i.setStyleSheet("color:red;")
#
#         # Window Settings
#
#         self.setGeometry(300, 300, 600, 400)
#         self.setWindowTitle("Kalkulator")
#         self.setFixedSize(600, 400)
#         self.show()
#
#     def Num(self):
#         global num
#         global newNum
#         global opVar
#
#         sender = self.sender()
#
#         newNum = int(sender.text())
#         setNum = str(newNum)
#
#         if opVar == False:
#             self.line.setText(self.line.text() + setNum)
#         else:
#             self.line.setText(setNum)
#             opVar = False
#
#     def operator(self):
#         global sumIt
#         global num
#         global opVar
#         global operator
#
#         sumIt += 1
#
#         if sumIt > 1:
#             self.Equal()
#
#         num = self.line.text()
#         sender = self.sender()
#         operator = sender.text()
#
#         opVar = True
#
#     def Equal(self):
#         global sumIt
#         global sumAll
#         global num
#         global newNum
#         global operator
#         global opVar
#
#         sumIt = 0
#
#         newNum = self.line.text()
#
#         if operator == "+":
#             sumAll = float(num) + float(newNum)
#         elif operator == "-":
#             sumAll = float(num) - float(newNum)
#         elif operator == "*":
#             sumAll = float(num) * float(newNum)
#         elif operator == "/":
#             sumAll = float(num) / float(newNum)
#
#         self.line.setText(str(sumAll))
#         opVar = True
#
#     def Root(self):
#         global num
#
#         num = float(self.line.text())
#         num = sqrt(num)
#         self.line.setText(str(num))
#
#     def Squared(self):
#         global num
#
#         num = float(self.line.text())
#         num = num**2
#         self.line.setText(str(num))
#
#     def Point(self):
#
#         if "." not in self.line.text():
#             self.line.setText(self.line.text() + ".")
#
#     def Switch(self):
#         global num
#
#         num = float(self.line.text())
#         num = -num
#         self.line.setText(str(num))
#
#     def CE(self):
#         self.line.backspace()
#
#     def C(self):
#         global num
#         global newNum
#         global sumAll
#         global operator
#
#         self.line.clear()
#
#         num = 0.0
#         newNum = 0.0
#         sumAll = 0.0
#         operator = ""
#
# def main():
#     app = QApplication(sys.argv)
#     main = Calc()
#     main.show()
#     sys.exit(app.exec_())
#
# if __name__ == "__main__":
#     main()

