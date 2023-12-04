from PyQt5 import QtCore, QtGui, QtWidgets
from table import TablePage
import mysql.connector

class CheckPage(QtWidgets.QWidget):

    def __init__(self, start_page, connectToDB, brand, model):
        super().__init__()
        self.start_page = start_page
        self.connectToDB = connectToDB
        self.brand = brand
        self.model = model
        self.setupUi()

    def setupUi(self):
        self.setWindowIcon(QtGui.QIcon('img/logo.png'))
        self.setObjectName("Form")
        self.resize(800, 600)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(72, 59, 123, 255), stop:0.481308 rgba(108, 71, 255, 255), stop:1 rgba(72, 59, 123, 255))")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 15, 19, 12)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background: transparent; border: none;background-image: url(:/img/img/back.svg);background-repeat:no-repeat;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logoHome = QtWidgets.QPushButton(self)
        self.logoHome.setMinimumSize(QtCore.QSize(146, 146))
        self.logoHome.setMaximumSize(QtCore.QSize(146, 146))
        self.logoHome.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logoHome.setStyleSheet("background: transparent;background-image: url(:/img/img/logo.png);")
        self.logoHome.setText("")
        self.logoHome.setObjectName("logoHome")
        self.horizontalLayout_3.addWidget(self.logoHome)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 73, -1, 55)
        self.horizontalLayout.setSpacing(27)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.checkBoxEngine = QtWidgets.QCheckBox(self)
        self.checkBoxEngine.setMinimumSize(QtCore.QSize(223, 44))
        self.checkBoxEngine.setMaximumSize(QtCore.QSize(223, 44))
        self.checkBoxEngine.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBoxEngine.setStyleSheet("background: rgb(255, 255, 255); border-radius:10px; padding: 0 0 0 10px; font-family: \"Arial\"; font-size: 17px;")
        self.checkBoxEngine.setObjectName("checkBoxEngine")
        self.horizontalLayout.addWidget(self.checkBoxEngine)
        self.checkBoxBreaks = QtWidgets.QCheckBox(self)
        self.checkBoxBreaks.setMinimumSize(QtCore.QSize(223, 44))
        self.checkBoxBreaks.setMaximumSize(QtCore.QSize(223, 44))
        self.checkBoxBreaks.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBoxBreaks.setStyleSheet("background: rgb(255, 255, 255); border-radius:10px; padding: 0 0 0 10px; font-family: \"Arial\"; font-size: 17px;")
        self.checkBoxBreaks.setObjectName("checkBoxBreaks")
        self.horizontalLayout.addWidget(self.checkBoxBreaks)
        self.checkBoxLights = QtWidgets.QCheckBox(self)
        self.checkBoxLights.setMinimumSize(QtCore.QSize(223, 44))
        self.checkBoxLights.setMaximumSize(QtCore.QSize(223, 44))
        self.checkBoxLights.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBoxLights.setStyleSheet("background: rgb(255, 255, 255); border-radius:10px; padding: 0 0 0 10px; font-family: \"Arial\"; font-size: 17px;")
        self.checkBoxLights.setObjectName("checkBoxLights")
        self.horizontalLayout.addWidget(self.checkBoxLights)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonContinue = QtWidgets.QPushButton(self)
        self.pushButtonContinue.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButtonContinue.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButtonContinue.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonContinue.setStyleSheet("border-radius: 5px;background: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.528037, y2:1, stop:0 rgba(241, 101, 41, 255), stop:1 rgba(112, 0, 255, 255));box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);color: #FFFFFF; font-family: \"Arial\"; font-size: 17px;")
        self.pushButtonContinue.setObjectName("pushButtonContinue")
        self.horizontalLayout_2.addWidget(self.pushButtonContinue)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)

        # Додавання функціоналу до кнопок
        self.pushButtonContinue.clicked.connect(self.checkCheckBoxes)
        self.pushButton.clicked.connect(self.go_back)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Car_depot"))
        self.checkBoxEngine.setText(_translate("Form", "Двигун"))
        self.checkBoxBreaks.setText(_translate("Form", "Тормозна система"))
        self.checkBoxLights.setText(_translate("Form", "Автосвітло"))
        self.pushButtonContinue.setText(_translate("Form", "Пошук"))
    
    # Перевірка та вибір типу деталі
    def checkCheckBoxes(self):
        # Створюємо массив для збереження обраних checkBox
        selected_checkboxes = []

        # Перевіряємо кожен checkBox на наявність галочки
        if self.checkBoxEngine.isChecked():
            selected_checkboxes.append("Двигун")

        if self.checkBoxBreaks.isChecked():
            selected_checkboxes.append("Тормозна система")

        if self.checkBoxLights.isChecked():
            selected_checkboxes.append("Автосвітло")

        # Если ни один чекбокс не выбран, выводим сообщение в консоль Якщо ж ми не вибрали не одного із checkBox то їх края будуть червоними
        if not selected_checkboxes:
            self.checkBoxEngine.setStyleSheet("border: 2px solid red;background: rgb(255, 255, 255); border-radius:10px; padding: 0 0 0 10px; font-family: \"Arial\"; font-size: 17px;")
            self.checkBoxBreaks.setStyleSheet("border: 2px solid red;background: rgb(255, 255, 255); border-radius:10px; padding: 0 0 0 10px; font-family: \"Arial\"; font-size: 17px;")
            self.checkBoxLights.setStyleSheet("border: 2px solid red;background: rgb(255, 255, 255); border-radius:10px; padding: 0 0 0 10px; font-family: \"Arial\"; font-size: 17px;")
        else:
            #Якщо ми пройшли перевірку та обрали хоча б один checkBox то зберігаємо наш вибір та передаємо до наступної сторінки
            self.table_page = TablePage(self, self.start_page, self.connectToDB, self.brand, self.model, selected_checkboxes)
            self.table_page.show()
            self.close()
    
    #Повернення назад
    def go_back(self):
        self.close()
        self.start_page.show()
import res
