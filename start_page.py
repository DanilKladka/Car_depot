from PyQt5 import QtCore, QtGui, QtWidgets
from check import CheckPage
from info import InfoPage
import mysql.connector


class StartPage(QtWidgets.QWidget):

    def __init__(self, connectToDB):
        super().__init__()
        self.connectToDB = connectToDB
        self.setupUi()
    # Налаштування інтерфейсу
    def setupUi(self):
        self.setWindowIcon(QtGui.QIcon('img/logo.png'))
        self.setObjectName("Form")
        self.resize(800, 637)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(72, 59, 123, 255), stop:0.481308 rgba(108, 71, 255, 255), stop:1 rgba(72, 59, 123, 255))")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_main = QtWidgets.QVBoxLayout()
        self.verticalLayout_main.setContentsMargins(-1, 20, -1, 20)
        self.verticalLayout_main.setSpacing(60)
        self.verticalLayout_main.setObjectName("verticalLayout_main")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(20, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setMinimumSize(QtCore.QSize(90, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(90, 40))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius: 5px;background: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.528037, y2:1, stop:0 rgba(241, 101, 41, 255), stop:1 rgba(112, 0, 255, 255));box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);color: #FFFFFF; font-family: \"Arial\"; font-size: 17px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_main.addLayout(self.horizontalLayout_4)
        self.horizontalLayoutLogo = QtWidgets.QHBoxLayout()
        self.horizontalLayoutLogo.setSpacing(0)
        self.horizontalLayoutLogo.setObjectName("horizontalLayoutLogo")
        self.logo = QtWidgets.QLabel(self)
        self.logo.setMinimumSize(QtCore.QSize(146, 146))
        self.logo.setMaximumSize(QtCore.QSize(146, 146))
        self.logo.setStyleSheet("background: transparent;background-image: url(:/img/img/logo.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.horizontalLayoutLogo.addWidget(self.logo)
        self.verticalLayout_main.addLayout(self.horizontalLayoutLogo)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(36)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setMinimumSize(QtCore.QSize(50, 15))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_2.setStyleSheet("background: transparent;color:white; font-family: \"Arial\"; font-size: 17px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.comboBoxMark = QtWidgets.QComboBox(self)
        self.comboBoxMark.setMinimumSize(QtCore.QSize(223, 44))
        self.comboBoxMark.setMaximumSize(QtCore.QSize(223, 44))
        self.comboBoxMark.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxMark.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 15px; placeholder: \"Марка\"")
        self.comboBoxMark.setObjectName("comboBoxMark")
        self.verticalLayout_3.addWidget(self.comboBoxMark)
        self.label = QtWidgets.QLabel(self)
        self.label.setMinimumSize(QtCore.QSize(50, 40))
        self.label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label.setStyleSheet("background: transparent;color:white; font-family: \"Arial\"; font-size: 17px;")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.comboBoxModel = QtWidgets.QComboBox(self)
        self.comboBoxModel.setMinimumSize(QtCore.QSize(223, 44))
        self.comboBoxModel.setMaximumSize(QtCore.QSize(223, 44))
        self.comboBoxModel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxModel.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 15px;")
        self.comboBoxModel.setObjectName("comboBoxModel")
        self.verticalLayout_3.addWidget(self.comboBoxModel)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonNext = QtWidgets.QPushButton(self)
        self.pushButtonNext.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButtonNext.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButtonNext.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonNext.setStyleSheet("border-radius: 5px;background: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.528037, y2:1, stop:0 rgba(241, 101, 41, 255), stop:1 rgba(112, 0, 255, 255));box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);color: #FFFFFF; font-size: 16px;font-family: Arial;")
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout.addWidget(self.pushButtonNext)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_main.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_main.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_main)
        
        #Додавання елемента в comboBoxMark по замовчуванню
        self.comboBoxMark.addItem("Виберіть марку")
        self.comboBoxMark.setCurrentText("Виберіть марку")
        #Додавання елемента в comboBoxModel по замовчуванню
        self.comboBoxModel.addItem("Виберіть модель")
        self.comboBoxModel.setCurrentText("Виберіть модель")
        # Виклик метода для отримання марки та моделі авто з БД
        self.GetCars()
        # Додавання функціоналу до кнопок
        self.pushButton.clicked.connect(self.open_info_page)
        self.pushButtonNext.clicked.connect(self.checking_and_opening_next_page)
        
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Car_depot"))
        self.pushButton.setText(_translate("Form", "Інфо"))
        self.label_2.setText(_translate("Form", "Марка"))
        self.label.setText(_translate("Form", "Модель"))
        self.pushButtonNext.setText(_translate("Form", "Продовжити"))

    # Перевірка перед переходом до check
    def checking_and_opening_next_page(self):
        # Перевіряємо чи обрали значення в comboBoxMark
        # Якщо не обрали значення в comboBoxMark та comboBoxModel то їх края будуть червоними
        if self.comboBoxMark.currentIndex() == 0:
            self.comboBoxMark.setStyleSheet("border: 2px solid red;border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 15px;")
            self.comboBoxModel.setStyleSheet("border: 2px solid red;border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 15px;")
        else:
            # Скидання стилів
            self.comboBoxMark.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 15px;")
            self.comboBoxModel.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 15px;")
        
        # Якщо ми обрали значення в цих comboBox то зберігаємо підключення до БД та наші значення що ми обрали в comboBox та переходимо до наступної сторінки
        if self.comboBoxMark.currentIndex() != 0:
            self.brand = self.comboBoxMark.currentText()
            self.model = self.comboBoxModel.currentText()
            self.check_page = CheckPage(self, self.connectToDB, self.brand, self.model)
            self.check_page.show()
            self.hide()
    
    # Отримання марки та моделі
    def GetCars(self):

        self.cursor = self.connectToDB.cursor()
        query = "SELECT brand, model FROM details" # Створюємо змінну для запиту до БД
        self.cursor.execute(query) # Виконуємо цей запит

        result = self.cursor.fetchall() # Отримання цього результату

        self.car_dict = {} # Створення словника для авто
        for brand, model in result: # Заповнюємо наш словник марками та моделями
            if brand in self.car_dict:
                if model not in self.car_dict[brand]:
                    self.car_dict[brand].append(model)
            else:
                self.car_dict[brand] = [model]

        # Додаємо марки до comboBoxMark
        self.comboBoxMark.addItems(self.car_dict.keys())
        # З'єднуємо марку з її моделю, якщо марка змінюється то вміст списку моделей до цієї марки оновлюється
        self.comboBoxMark.currentIndexChanged.connect(self.updateComboBoxModel)
    
    # Метод для оновлення змісту comboBoxModel на основі обраної марки
    def updateComboBoxModel(self):

        self.comboBoxModel.clear()

        selected_mark = self.comboBoxMark.currentText()
        # Перевірка на те чи існує така марка в нашому словнику
        if selected_mark in self.car_dict:
            # Додаємо моделі до ComboBoxModel
            self.comboBoxModel.addItems(self.car_dict[selected_mark])

    # Відкриття інформаційного вікна
    def open_info_page(self):
        self.info_page = InfoPage(self)
        self.info_page.show()
    
    # Метод для очищення вмісту по замовчуванню
    def cleanCheck(self):
        self.comboBoxMark.clear()
        self.comboBoxModel.clear()
import res