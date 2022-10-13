# Zayn Severance, last updated 10/13/2022
# Frontend.py
# Handles the frontend completley in PyQt5, be sure to use this and not PyQt6!
# Yes, this is what you get when a backend guy makes a frontend.

import sys
import ctypes
myappid = 'gitgud.contxt.ver1.0' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    ANDS = ""
    ORS = ""
    NOTS = ""
    num1 = 0
    num2 = 0
    num3 = 0

    def __init__(self, window2=None):
        super(Ui_MainWindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon('Icon.png'))
        self.setObjectName("contxt")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 160, 131, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 210, 131, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 260, 131, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(300, 160, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(300, 210, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(300, 260, 42, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 320, 211, 28))
        self.pushButton.setObjectName("pushButton")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.setWindowTitle("contxt")
        self.pushButton.setText("Search")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 801, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("contxt.")

        QtCore.QMetaObject.connectSlotsByName(self)

        # lines for handling added manually
        self.pushButton.clicked.connect(self.button_clicked)
        self._window2 = window2


    # button handle
    def button_clicked(self):
        print("click")
        ANDS = self.lineEdit.text()
        ORS  = self.lineEdit_2.text()
        NOTS = self.lineEdit_3.text()
        num1 = int(self.spinBox.text())
        num2 = int(self.spinBox_2.text())
        num3 = int(self.spinBox_3.text())
        print("query:", ANDS, "range", num1, ORS, "range", num2, NOTS, "range", num3)
        self.hide()
        if self._window2 is None:
            self._window2 = Ui_Results(self)
        # I would expect your function for grabbing data to be somewhere around here
        self._window2.setText()
        self._window2.show()


class Ui_Results(QtWidgets.QMainWindow):
    def __init__(self, window1=None):
        super(Ui_Results, self).__init__()

        gridLayout = QtWidgets.QGridLayout()

        self.setWindowIcon(QtGui.QIcon('Icon.png'))
        self.setObjectName("contxt")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(10)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton('pushButton')
        self.pushButton.setObjectName("pushButton")
        self.setCentralWidget(self.centralwidget)

        self.pushButton.setText("Modify Search")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 801, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.setWindowTitle("contxt")
        self.centralwidget.setLayout(gridLayout)
        gridLayout.addWidget(self.label, 0, 0, 1, 3)
        gridLayout.addWidget(self.pushButton, 0, 4, 1, 1)
        gridLayout.addWidget(self.tableWidget, 1, 0, 4, 4)

        # added code for button handle
        self.pushButton.clicked.connect(self.button_clicked)
        self._window1 = window1
        print("Made window 2")

        self.populateTable()

    # return to other menu
    def button_clicked(self):
        self.hide()
        if self._window1 is None:
            self._window1 = Ui_MainWindow(self)
        self._window1.show()

    # this is where you would put your data to fill the result table
    # Yes, this is for you Matt!
    def populateTable(self):
        # grab data from the backend to populate this table
        # use the table population function to fill it in
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(10)

    # This class updates the search text label
    def setText(self):
        text = "Results for ANDS " + self._window1.lineEdit.text() + " DIST " + self._window1.spinBox.text() + \
               ", ORS " + self._window1.lineEdit_2.text() + " DIST " + self._window1.spinBox_2.text() + \
               " NOTS " + self._window1.lineEdit_3.text() + " DIST " + self._window1.spinBox_3.text()
        self.label.setText(text)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    sys.exit(app.exec())