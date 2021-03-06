# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2190, 1080)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        MainWindow.setFont(font)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainFrame.sizePolicy().hasHeightForWidth())
        self.MainFrame.setSizePolicy(sizePolicy)
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.gridLayout.addWidget(self.MainFrame, 2, 0, 1, 1)
        self.menuBar = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuBar.sizePolicy().hasHeightForWidth())
        self.menuBar.setSizePolicy(sizePolicy)
        self.menuBar.setMinimumSize(QtCore.QSize(0, 85))
        self.menuBar.setMaximumSize(QtCore.QSize(16777215, 70))
        self.menuBar.setStyleSheet("background-color: rgb(23, 161, 145);")
        self.menuBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menuBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuBar.setObjectName("menuBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.menuBar)
        self.horizontalLayout.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout.setSpacing(24)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.homeButton = QtWidgets.QPushButton(self.menuBar)
        self.homeButton.setMinimumSize(QtCore.QSize(0, 48))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(False)
        self.homeButton.setFont(font)
        self.homeButton.setAutoFillBackground(False)
        self.homeButton.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(246, 247, 200);\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/../../res/ui icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QtCore.QSize(24, 24))
        self.homeButton.setObjectName("homeButton")
        self.horizontalLayout.addWidget(self.homeButton)
        self.askLepButton = QtWidgets.QPushButton(self.menuBar)
        self.askLepButton.setMinimumSize(QtCore.QSize(0, 48))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.askLepButton.setFont(font)
        self.askLepButton.setAutoFillBackground(False)
        self.askLepButton.setStyleSheet("background-color: rgb(246, 247, 200);\n"
"border-color: rgb(246, 247, 200);\n"
"selection-color:rgb(233, 234, 189);\n"
"selection-background-color: rgb(233, 234, 189);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/../../res/ui icons/ask lep.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.askLepButton.setIcon(icon1)
        self.askLepButton.setIconSize(QtCore.QSize(24, 24))
        self.askLepButton.setObjectName("askLepButton")
        self.horizontalLayout.addWidget(self.askLepButton)
        self.randomQsButton = QtWidgets.QPushButton(self.menuBar)
        self.randomQsButton.setMinimumSize(QtCore.QSize(0, 48))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.randomQsButton.setFont(font)
        self.randomQsButton.setAutoFillBackground(False)
        self.randomQsButton.setStyleSheet("background-color: rgb(246, 247, 200);\n"
"border-color: rgb(246, 247, 200);\n"
"selection-color:rgb(233, 234, 189);\n"
"selection-background-color: rgb(233, 234, 189);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/../../res/ui icons/random q.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.randomQsButton.setIcon(icon2)
        self.randomQsButton.setIconSize(QtCore.QSize(24, 24))
        self.randomQsButton.setObjectName("randomQsButton")
        self.horizontalLayout.addWidget(self.randomQsButton)
        self.newTestButton = QtWidgets.QPushButton(self.menuBar)
        self.newTestButton.setMinimumSize(QtCore.QSize(0, 48))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.newTestButton.setFont(font)
        self.newTestButton.setAutoFillBackground(False)
        self.newTestButton.setStyleSheet("background-color: rgb(246, 247, 200);\n"
"border-color: rgb(246, 247, 200);\n"
"selection-color:rgb(233, 234, 189);\n"
"selection-background-color: rgb(233, 234, 189);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui/../../res/ui icons/new test.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newTestButton.setIcon(icon3)
        self.newTestButton.setIconSize(QtCore.QSize(24, 24))
        self.newTestButton.setObjectName("newTestButton")
        self.horizontalLayout.addWidget(self.newTestButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.userButton = QtWidgets.QPushButton(self.menuBar)
        self.userButton.setMinimumSize(QtCore.QSize(0, 48))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.userButton.setFont(font)
        self.userButton.setAutoFillBackground(False)
        self.userButton.setStyleSheet("background-color: rgb(246, 247, 200);\n"
"border-color: rgb(246, 247, 200);\n"
"selection-color:rgb(233, 234, 189);\n"
"selection-background-color: rgb(233, 234, 189);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui/../../res/ui icons/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userButton.setIcon(icon4)
        self.userButton.setIconSize(QtCore.QSize(24, 24))
        self.userButton.setObjectName("userButton")
        self.horizontalLayout.addWidget(self.userButton)
        self.gridLayout.addWidget(self.menuBar, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Leprogram"))
        self.homeButton.setText(_translate("MainWindow", " Home"))
        self.askLepButton.setText(_translate("MainWindow", " Ask LeP"))
        self.randomQsButton.setText(_translate("MainWindow", " Random Q\'s"))
        self.newTestButton.setText(_translate("MainWindow", " New Test"))
        self.userButton.setText(_translate("MainWindow", " User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
