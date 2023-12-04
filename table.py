from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from addPage import AddPage
from deletePage import DeletePage
from updatePage import UpdatePage


class TablePage(QtWidgets.QWidget):

    def __init__(self, check, start_page, connectToDB, brand, model, selected_checkboxes):
        super().__init__()
        self.selected_checkboxes = selected_checkboxes
        self.connectToDB = connectToDB
        self.start_page = start_page
        self.check = check
        self.brand = brand
        self.model = model
        self.setupUi()

    def setupUi(self):
        self.setWindowIcon(QtGui.QIcon('img/logo.png'))
        self.setObjectName("Form")
        self.resize(1000, 600)
        self.setMinimumSize(QtCore.QSize(1000, 600))
        self.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(72, 59, 123, 255), stop:0.481308 rgba(108, 71, 255, 255), stop:1 rgba(72, 59, 123, 255))")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.logoHome = QtWidgets.QPushButton(self)
        self.logoHome.setMinimumSize(QtCore.QSize(146, 146))
        self.logoHome.setMaximumSize(QtCore.QSize(146, 146))
        self.logoHome.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logoHome.setStyleSheet("background: transparent;background-image: url(:/img/img/logo.png);")
        self.logoHome.setText("")
        self.logoHome.setObjectName("logoHome")
        self.horizontalLayout_4.addWidget(self.logoHome)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 14, -1, 92)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background: transparent; border: none;background-image: url(:/img/img/back.svg);background-repeat:no-repeat;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.widget = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background: transparent;")
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(480, 326))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setStyleSheet("QTableWidget { background-color: rgba(217, 217, 217, 50%); color: rgb(255, 255, 255);font-family: Arial;font-size: 17px;border-radius: 16px;}QTableWidget QHeaderView {font-family: Arial;font-size: 17px;color: white;background: transparent;}QHeaderView::section {height: 31px;background: transparent;}QTableWidget::item {height: 31px;background: transparent;border-left: 1px solid rgba(0, 0, 0, 0.50);border-top: 1px solid rgba(0, 0, 0, 0);}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Назва", "Тип деталі", "Виробник", "Марка", "Модель", "Кількість", "Ціна за одиницю"])
        self.tableWidget.setColumnWidth(0, 30)  # ID
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(15, -1, -1, 0)
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineTitle = QtWidgets.QLineEdit(self.widget)
        self.lineTitle.setMinimumSize(QtCore.QSize(223, 44))
        self.lineTitle.setMaximumSize(QtCore.QSize(223, 44))
        self.lineTitle.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 15px;")
        self.lineTitle.setObjectName("lineTitle")
        self.verticalLayout.addWidget(self.lineTitle)
        self.lineManufacturer = QtWidgets.QLineEdit(self.widget)
        self.lineManufacturer.setMinimumSize(QtCore.QSize(223, 44))
        self.lineManufacturer.setMaximumSize(QtCore.QSize(223, 44))
        self.lineManufacturer.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 15px;")
        self.lineManufacturer.setObjectName("lineManufacturer")
        self.verticalLayout.addWidget(self.lineManufacturer)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 12, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonSearch = QtWidgets.QPushButton(self.widget)
        self.pushButtonSearch.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButtonSearch.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButtonSearch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonSearch.setStyleSheet("border-radius: 5px;background: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.528037, y2:1, stop:0 rgba(241, 101, 41, 255), stop:1 rgba(112, 0, 255, 255));box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);color: #FFFFFF; font-family: \"Arial\"; font-size: 17px;")
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.horizontalLayout_2.addWidget(self.pushButtonSearch)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.widget)
        self.widget1 = QtWidgets.QWidget(self)
        self.widget1.setStyleSheet("background: transparent;")
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(-1, 30, -1, 20)
        self.horizontalLayout.setSpacing(27)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonAdd = QtWidgets.QPushButton(self.widget1)
        self.pushButtonAdd.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButtonAdd.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButtonAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonAdd.setStyleSheet("background: qlineargradient(spread:pad, x1:0.504673, y1:0, x2:0.519, y2:1, stop:0 rgba(241, 101, 41, 255), stop:1 rgba(112, 0, 255, 255)); color: white; padding: 5px; border-radius: 5px;font-family: \"Arial\"; font-size: 17px;")
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.horizontalLayout.addWidget(self.pushButtonAdd)
        self.pushButtonDelete = QtWidgets.QPushButton(self.widget1)
        self.pushButtonDelete.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButtonDelete.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButtonDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonDelete.setStyleSheet("background: qlineargradient(spread:pad, x1:0.504673, y1:0, x2:0.519, y2:1, stop:0 rgba(241, 101, 41, 255), stop:1 rgba(112, 0, 255, 255)); color: white; padding: 5px; border-radius: 5px;font-family: \"Arial\"; font-size: 17px;")
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout.addWidget(self.pushButtonDelete)
        self.pushButtonUpdate = QtWidgets.QPushButton(self.widget1)
        self.pushButtonUpdate.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButtonUpdate.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButtonUpdate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonUpdate.setStyleSheet("background: qlineargradient(spread:pad, x1:0.504673, y1:0, x2:0.519, y2:1, stop:0 rgba(241, 101, 41, 255), stop:1 rgba(112, 0, 255, 255)); color: white; padding: 5px; border-radius: 5px;font-family: \"Arial\"; font-size: 17px;")
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.horizontalLayout.addWidget(self.pushButtonUpdate)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_3.addWidget(self.widget1)

        print(self.brand, self.model, self.connectToDB, self.selected_checkboxes)
        
        # Виклик методу для заповнення таблиці
        self.full_table()

        # Додавання функціоналу до кнопок
        self.pushButtonAdd.clicked.connect(self.buttonAddRow)
        self.pushButton.clicked.connect(self.go_back)
        self.pushButtonDelete.clicked.connect(self.buttonDeleteRow)
        self.pushButtonUpdate.clicked.connect(self.buttonUpdateRow)
        self.pushButtonSearch.clicked.connect(self.searchDetail)
        self.logoHome.clicked.connect(self.go_back_start_page)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Car_depot"))
        self.lineTitle.setPlaceholderText(_translate("Form", "Назва"))
        self.lineManufacturer.setPlaceholderText(_translate("Form", "Виробник"))
        self.pushButtonSearch.setText(_translate("Form", "Пошук"))
        self.pushButtonAdd.setText(_translate("Form", "Додати запчастину"))
        self.pushButtonDelete.setText(_translate("Form", "Видалення запчастини"))
        self.pushButtonUpdate.setText(_translate("Form", "Оновити запчастину"))

    # Повернення до попередньої сторніки(check.py)
    def go_back(self):
        self.close()
        self.check.show()
    
    # Повернення на початкову сторінку
    def go_back_start_page(self):
        self.close()
        self.start_page.cleanCheck()
        self.start_page.comboBoxMark.addItem("Виберіть марку")
        self.start_page.comboBoxMark.setCurrentText("Виберіть марку")
        self.start_page.comboBoxModel.addItem("Виберіть модель")
        self.start_page.comboBoxModel.setCurrentText("Виберіть модель")
        self.start_page.GetCars()
        self.start_page.show()

    # Відкриваємо вікно для додавання нової запчастини та передаємо параметри
    def buttonAddRow(self):
        # Створення об'єкта та передаємо наші параметри
        self.add_page = AddPage(self, self.connectToDB, self.brand, self.model, self.selected_checkboxes)
        self.add_page.show()
        # З'єднуємо подію з натисканням на кнопку
        self.add_page.pushButtonAdd.clicked.connect(self.add_page.addRow)

    # Відкриваємо вікно для видалення запчастини та передаємо параметри
    def buttonDeleteRow(self):
        self.delete_page = DeletePage(self, self.connectToDB, self.brand, self.model, self.selected_checkboxes)
        self.delete_page.show()
        # self.full_table()
        self.delete_page.pushButtonDelete.clicked.connect(self.delete_page.delete_Row)
        
    #Відкриваємо вікно для оновлення запчастини та передаємо параметри
    def buttonUpdateRow(self):
        self.update_page = UpdatePage(self, self.connectToDB, self.brand, self.model, self.selected_checkboxes)
        self.update_page.show()
        self.update_page.pushButtonUpdate.clicked.connect(self.update_page.updateRow)    
    
    # Отримання інформації з БД та відображення її в таблиці
    def full_table(self):
        # Створення курсора для роботи з базою даних
        self.cursor = self.connectToDB.cursor()

        # Отримання даних з бази днаих відповідно до обраних чекбоксів
        match len(self.selected_checkboxes):
            case 1:
                self.cursor.execute(f"SELECT * FROM details WHERE brand = '{self.brand}' AND model = '{self.model}' AND detailType = '{self.selected_checkboxes[0]}'")
            case 2:
                self.cursor.execute(f"SELECT * FROM details WHERE brand = '{self.brand}' AND model = '{self.model}' AND detailType IN ('{self.selected_checkboxes[0]}', '{self.selected_checkboxes[1]}')")
            case _:
                checkboxes_str = ', '.join([f"'{checkbox}'" for checkbox in self.selected_checkboxes])
                self.cursor.execute(f"SELECT * FROM details WHERE brand = '{self.brand}' AND model = '{self.model}' AND detailType IN ({checkboxes_str})")
        
        # Отримання результатів запиту
        result = self.cursor.fetchall()

        # Встановлення кількості рядків у таблиці
        count_row = len(result)
        self.tableWidget.setRowCount(count_row)

        # Заповнення таблиці даними
        for row_i, row_data in enumerate(result):
            for colomn_j, colomn_data in enumerate(row_data):
                items = QtWidgets.QTableWidgetItem(str(colomn_data))
                self.tableWidget.setItem(row_i, colomn_j, items)

        self.cursor.close()

    # Пошук запчастини
    def searchDetail(self):
        # Отримання назви та виробника які ми ввели
        title = self.lineTitle.text()
        manufacturer = self.lineManufacturer.text()

        cursor = self.connectToDB.cursor()

        # Створюємо список для збереження умов пошуку
        conditions = []

        #Додаємо умови пошуку якщо вони задані
        if self.brand:
            conditions.append(f"brand = '{self.brand}'")

        if self.model:
            conditions.append(f"model = '{self.model}'")
    
        if self.selected_checkboxes:
            checkboxes_str = ', '.join([f"'{checkbox}'" for checkbox in self.selected_checkboxes])
            conditions.append(f"detailType IN ({checkboxes_str})")

        if title:
            conditions.append(f"title LIKE '%{title}%'")

        if manufacturer:
            conditions.append(f"manufacturer LIKE '%{manufacturer}%'")

        if conditions:
            where_clause = " AND ".join(conditions)
            query = f"SELECT * FROM details WHERE {where_clause}"
            cursor.execute(query)

            result = cursor.fetchall()
            self.tableWidget.setRowCount(len(result))

            for row_i, row_data in enumerate(result):
                for colomn_j, colomn_data in enumerate(row_data):
                    items = QtWidgets.QTableWidgetItem(str(colomn_data))
                    self.tableWidget.setItem(row_i, colomn_j, items)
        else:
            self.tableWidget.setRowCount(0)  # No conditions, so clear the table

        cursor.close()
    
import res
