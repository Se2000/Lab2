# Zadanie 1

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

# Zadanie 2a

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor


class Kolory(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):
        self.resize(400, 100)
        self.setWindowTitle("Colors")
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        qp.setBrush(QColor('red'))
        qp.drawRect(10, 15, 90, 60)

        qp.setBrush(QColor('orange'))
        qp.drawRect(150, 15, 90, 60)

        qp.setBrush(QColor('dark blue'))
        qp.drawRect(300, 15, 90, 60)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Kolory()
    sys.exit(app.exec_())

# Zadanie 2b

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
from PyQt5.QtGui import QIcon


class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 menu'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('Plik')
        editMenu = mainMenu.addMenu('Edycja')
        viewMenu = mainMenu.addMenu('Widok')
        searchMenu = mainMenu.addMenu('Szukaj')
        toolsMenu = mainMenu.addMenu('Narzędzia')
        helpMenu = mainMenu.addMenu('Pomoc')
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())

# Zadanie 3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt5.QtCore import pyqtSlot


class App(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 wybieranie kolorów'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Open color dialog', self)
        button.setToolTip('Opens color dialog')
        button.move(10, 10)
        button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        openColorDialog(self)


def openColorDialog(self):
    color = QColorDialog.getColor()

    if color.isValid():
        print(color.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())