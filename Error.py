from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Question(object):
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
        self.pushButtonYes = QtWidgets.QPushButton(Dialog)
        self.pushButtonYes.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButtonYes.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButtonYes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonYes.setStyleSheet("background: qlineargradient(spread:pad, x1:0.504673, y1:0, x2:0.519, y2:1, stop:0 rgba(241, 101, 41, 255), stop:1 rgba(112, 0, 255, 255)); color: white; padding: 0 0 0 2px; border-radius: 5px; font-family: \"Arial\"; font-size: 17px;")
        self.pushButtonYes.setObjectName("pushButtonYes")
        self.horizontalLayout.addWidget(self.pushButtonYes)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonNo = QtWidgets.QPushButton(Dialog)
        self.pushButtonNo.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButtonNo.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButtonNo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonNo.setStyleSheet("background: qlineargradient(spread:pad, x1:0.504673, y1:0, x2:0.519, y2:1, stop:0 rgba(241, 101, 41, 255), stop:1 rgba(112, 0, 255, 255)); color: white; padding: 0 0 0 2px; border-radius: 5px; font-family: \"Arial\"; font-size: 17px;")
        self.pushButtonNo.setObjectName("pushButtonNo")
        self.horizontalLayout.addWidget(self.pushButtonNo)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textValue.setText(_translate("Dialog", "Error"))
        self.pushButtonYes.setText(_translate("Dialog", "Так"))
        self.pushButtonNo.setText(_translate("Dialog", "Ні"))
    
    # Відкритя діалогового вікна
    def open(self, text):
        self.dialog = QtWidgets.QDialog()
        self.setupUi(self.dialog)
        self.textValue.setText(text)
        self.result = False
        
        self.pushButtonYes.clicked.connect(self.accept)
        self.pushButtonNo.clicked.connect(self.close)
        self.dialog.show()
        self.dialog.exec_()
        return self.result
    
    def accept(self):
        self.result = True    
        self.dialog.accept()
    
    def close(self):
        self.dialog.close()