# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 392)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 761, 341))
        self.label.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/Loginpage.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 10, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 50, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.User = QtWidgets.QLabel(self.centralwidget)
        self.User.setGeometry(QtCore.QRect(250, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.User.setFont(font)
        self.User.setObjectName("User")
        self.Pass = QtWidgets.QLabel(self.centralwidget)
        self.Pass.setGeometry(QtCore.QRect(250, 140, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Pass.setFont(font)
        self.Pass.setObjectName("Pass")
        self.Pass_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Pass_2.setGeometry(QtCore.QRect(360, 160, 113, 20))
        self.Pass_2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.Pass_2.setText("")
        self.Pass_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Pass_2.setObjectName("Pass_2")
        self.User_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.User_2.setGeometry(QtCore.QRect(360, 120, 113, 20))
        self.User_2.setObjectName("User_2")
        self.Login = QtWidgets.QPushButton(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(250, 200, 221, 31))
        self.Login.setStyleSheet("")
        self.Login.setObjectName("Login")
        self.FP = QtWidgets.QPushButton(self.centralwidget)
        self.FP.setGeometry(QtCore.QRect(250, 240, 221, 31))
        self.FP.setObjectName("FP")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login_Page"))
        self.label_2.setText(_translate("MainWindow", "Restaurant Billing System "))
        self.label_3.setText(_translate("MainWindow", "ADMIN LOGIN"))
        self.User.setText(_translate("MainWindow", "Username: "))
        self.Pass.setText(_translate("MainWindow", "Password: "))
        self.Login.setText(_translate("MainWindow", "LOGIN"))
        self.FP.setText(_translate("MainWindow", "FORGOT PASSWORD"))
import Login_Page_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())