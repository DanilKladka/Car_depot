from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Message(object):
    
    def setupUi(self, Dialog):
        Dialog.setWindowIcon(QtGui.QIcon('img/logo.png'))
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 250)
        Dialog.setMinimumSize(QtCore.QSize(400, 250))
        Dialog.setMaximumSize(QtCore.QSize(400, 250))
        Dialog.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(72, 59, 123, 255), stop:0.481308 rgba(108, 71, 255, 255), stop:1 rgba(72, 59, 123, 255))")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(30, 60, 30, 30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textValue = QtWidgets.QLabel(Dialog)
        self.textValue.setMinimumSize(QtCore.QSize(0, 60))
        self.textValue.setMaximumSize(QtCore.QSize(16777215, 60))
        self.textValue.setStyleSheet("background: none; font-family: \"Arial\"; font-size: 20px; color: white")
        self.textValue.setObjectName("textValue")
        self.verticalLayout.addWidget(self.textValue)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonOK = QtWidgets.QPushButton(Dialog)
        self.pushButtonOK.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButtonOK.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButtonOK.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonOK.setStyleSheet("background: qlineargradient(spread:pad, x1:0.504673, y1:0, x2:0.519, y2:1, stop:0 rgba(241, 101, 41, 255), stop:1 rgba(112, 0, 255, 255)); color: white; padding: 0 0 0 2px; border-radius: 5px; font-family: \"Arial\"; font-size: 17px;")
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.horizontalLayout.addWidget(self.pushButtonOK)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textValue.setText(_translate("Dialog", "Привет"))
        self.pushButtonOK.setText(_translate("Dialog", "Ok"))
    
    # Відкритя діалогового вікна
    def open(self, text):
        self.dialog = QtWidgets.QDialog()
        self.setupUi(self.dialog)
        self.textValue.setText(text)
        
        self.pushButtonOK.clicked.connect(self.accept)
        
        self.dialog.show()
        self.dialog.exec_()

    def accept(self): 
        self.dialog.accept()