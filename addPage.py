from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from Message import Ui_Message

class AddPage(QtWidgets.QWidget):

    def __init__(self, table_page, connectToDB, brand, model, selected_checkboxes):
        super().__init__()
        self.table_page = table_page
        self.connectToDB = connectToDB
        self.brand = brand
        self.model = model
        self.selected_checkboxes = selected_checkboxes
        # Виклик методу який налаштовує інтерфейс
        self.setupUi()

    def setupUi(self):
        self.setWindowIcon(QtGui.QIcon('img/logo.png'))
        self.setObjectName("Form")
        self.resize(400, 650)
        self.setMinimumSize(QtCore.QSize(400, 650))
        self.setMaximumSize(QtCore.QSize(400, 650))
        self.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(72, 59, 123, 255), stop:0.481308 rgba(108, 71, 255, 255), stop:1 rgba(72, 59, 123, 255))")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(105, 10, 187, 50))
        self.label.setStyleSheet("background: qlineargradient(spread:pad, x1:0.504673, y1:0, x2:0.519, y2:1, stop:0 rgba(241, 101, 41, 255), stop:1 rgba(112, 0, 255, 255)); color: white; padding: 0 0 0 2px; border-radius: 5px; font-family: \"Arial\"; font-size: 17px;")
        self.label.setObjectName("label")
        self.lineQuantity = QtWidgets.QLineEdit(self)
        self.lineQuantity.setGeometry(QtCore.QRect(90, 440, 223, 44))
        self.lineQuantity.setMinimumSize(QtCore.QSize(223, 44))
        self.lineQuantity.setMaximumSize(QtCore.QSize(223, 44))
        self.lineQuantity.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 10px;font-family: \"Arial\"; font-size: 17px;")
        self.lineQuantity.setObjectName("lineQuantity")
        self.lineName = QtWidgets.QLineEdit(self)
        self.lineName.setGeometry(QtCore.QRect(90, 140, 223, 44))
        self.lineName.setMinimumSize(QtCore.QSize(223, 44))
        self.lineName.setMaximumSize(QtCore.QSize(223, 44))
        self.lineName.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 10px;font-family: \"Arial\"; font-size: 17px;")
        self.lineName.setObjectName("lineName")
        self.lineID = QtWidgets.QLineEdit(self)
        self.lineID.setGeometry(QtCore.QRect(90, 80, 223, 44))
        self.lineID.setMinimumSize(QtCore.QSize(223, 44))
        self.lineID.setMaximumSize(QtCore.QSize(223, 44))
        self.lineID.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 10px;font-family: \"Arial\"; font-size: 17px;")
        self.lineID.setObjectName("lineID")
        self.linePrice = QtWidgets.QLineEdit(self)
        self.linePrice.setGeometry(QtCore.QRect(90, 500, 223, 44))
        self.linePrice.setMinimumSize(QtCore.QSize(223, 44))
        self.linePrice.setMaximumSize(QtCore.QSize(223, 44))
        self.linePrice.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 10px;font-family: \"Arial\"; font-size: 17px;")
        self.linePrice.setObjectName("linePrice")
        self.pushButtonClean = QtWidgets.QPushButton(self)
        self.pushButtonClean.setGeometry(QtCore.QRect(230, 560, 61, 61))
        self.pushButtonClean.setMinimumSize(QtCore.QSize(61, 61))
        self.pushButtonClean.setMaximumSize(QtCore.QSize(61, 61))
        self.pushButtonClean.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonClean.setStyleSheet("background:qlineargradient(spread:pad, x1:0.505, y1:0, x2:0.509, y2:1, stop:0 rgba(255, 107, 0, 255), stop:0.509346 rgba(34, 34, 34, 255), stop:1 rgba(31, 12, 255, 255));background-image:url(:/img/img/clean.svg);border: none; background-repeat: no-repeat; border-radius: 30px; background-position: center")
        self.pushButtonClean.setText("")
        self.pushButtonClean.setObjectName("pushButtonClean")
        self.pushButtonAdd = QtWidgets.QPushButton(self)
        self.pushButtonAdd.setGeometry(QtCore.QRect(110, 560, 61, 61))
        self.pushButtonAdd.setMinimumSize(QtCore.QSize(61, 61))
        self.pushButtonAdd.setMaximumSize(QtCore.QSize(61, 61))
        self.pushButtonAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonAdd.setStyleSheet("background:qlineargradient(spread:pad, x1:0.505, y1:0, x2:0.509, y2:1, stop:0 rgba(255, 107, 0, 255), stop:0.509346 rgba(34, 34, 34, 255), stop:1 rgba(31, 12, 255, 255));background-image:url(:/img/img/plus.svg);border: none; background-repeat: no-repeat; border-radius: 30px; background-position: center")
        self.pushButtonAdd.setText("")
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.comboBoxTypeDetail = QtWidgets.QComboBox(self)
        self.comboBoxTypeDetail.setGeometry(QtCore.QRect(90, 200, 223, 44))
        self.comboBoxTypeDetail.setMinimumSize(QtCore.QSize(223, 44))
        self.comboBoxTypeDetail.setMaximumSize(QtCore.QSize(223, 44))
        self.comboBoxTypeDetail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxTypeDetail.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 15px; ")
        self.comboBoxTypeDetail.setObjectName("comboBoxTypeDetail")
        self.lineMark = QtWidgets.QLineEdit(self)
        self.lineMark.setGeometry(QtCore.QRect(90, 320, 223, 44))
        self.lineMark.setMinimumSize(QtCore.QSize(223, 44))
        self.lineMark.setMaximumSize(QtCore.QSize(223, 44))
        self.lineMark.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 10px;font-family: \"Arial\"; font-size: 17px;")
        self.lineMark.setObjectName("lineMark")
        self.lineModel = QtWidgets.QLineEdit(self)
        self.lineModel.setGeometry(QtCore.QRect(90, 380, 223, 44))
        self.lineModel.setMinimumSize(QtCore.QSize(223, 44))
        self.lineModel.setMaximumSize(QtCore.QSize(223, 44))
        self.lineModel.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 10px;font-family: \"Arial\"; font-size: 17px;")
        self.lineModel.setObjectName("lineModel")
        self.lineManufacturer = QtWidgets.QLineEdit(self)
        self.lineManufacturer.setGeometry(QtCore.QRect(90, 260, 223, 44))
        self.lineManufacturer.setMinimumSize(QtCore.QSize(223, 44))
        self.lineManufacturer.setMaximumSize(QtCore.QSize(223, 44))
        self.lineManufacturer.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 10px;font-family: \"Arial\"; font-size: 17px;")
        self.lineManufacturer.setObjectName("lineManufacturer")

        self.comboBoxTypeDetail.addItem("Виберіть тип деталі")
        self.comboBoxTypeDetail.setCurrentText("Виберіть тип деталі")
        self.pushButtonClean.clicked.connect(self.clean_all_Filds)

        for i in range(len(self.selected_checkboxes)):
            self.comboBoxTypeDetail.addItem(str(self.selected_checkboxes[i]))
        
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add Parts"))
        self.label.setText(_translate("Form", "Додавання запчастини"))
        self.lineQuantity.setPlaceholderText(_translate("Form", "Кількість"))
        self.lineName.setPlaceholderText(_translate("Form", "Назва"))
        self.lineID.setPlaceholderText(_translate("Form", "ID"))
        self.linePrice.setPlaceholderText(_translate("Form", "Вартість"))
        self.lineMark.setPlaceholderText(_translate("Form", "Марка"))
        self.lineModel.setPlaceholderText(_translate("Form", "Модель"))
        self.lineManufacturer.setPlaceholderText(_translate("Form", "Виробник"))
    
    # Метод для очищення усіх значень в усіх полях
    def clean_all_Filds(self):
        self.lineID.setText("")
        self.lineName.setText("")
        self.lineManufacturer.setText("")
        self.lineMark.setText("")
        self.lineModel.setText("")
        self.lineQuantity.setText("")
        self.linePrice.setText("")
    
    # Метод для додавання нового запису
    def addRow(self):
        allFields = False
        self.valuesID = False
        
        checkLine = [self.lineID, self.lineName, self.lineManufacturer, self.lineMark, self.lineModel, self.lineQuantity, self.linePrice]
        # Перевірка всіх полів
        for line in checkLine:
            if line.text() == "":
                allFields = False
                line.setStyleSheet("border: 2px solid red;border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 10px;font-family: \"Arial\"; font-size: 17px;")
            else:
                allFields = True
                line.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 10px;font-family: \"Arial\"; font-size: 17px;")
        
        valluesQuantity = self.checkValuesNumber(self.lineQuantity)
        valluesPrice= self.checkValuesNumber(self.linePrice)

        # Перевірка чи ID унікальний
        if self.checkValuesNumber(self.lineID):
            cursor = self.connectToDB.cursor()
            #Виконуємо SQL-запит для вилучення стовпця ID
            cursor.execute('SELECT id FROM details')
            id_values = [row[0] for row in cursor.fetchall()]
            cursor.close()

            for i in id_values:
                if str(i) == self.lineID.text():
                    self.lineID.setStyleSheet("border: 2px solid red;border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 10px;font-family: \"Arial\"; font-size: 17px;")
                    self.valuesID = False
                    break
                else:
                    self.valuesID = True
                    self.lineID.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 10px;font-family: \"Arial\"; font-size: 17px;")
        
        # Перевірка чи всі перевірки ми пройшли для додавання нового запису
        if allFields and valluesQuantity and valluesPrice and self.comboBoxTypeDetail.currentIndex() != 0:
            print("Все поля прошли проверку")
            query = f"INSERT INTO `cardepot`.`details` (`id`, `title`, `detailType`, `manufacturer`, `brand`, `model`, `quantity`, `price`) VALUES ({int(self.lineID.text())}, '{self.lineName.text()}', '{self.comboBoxTypeDetail.currentText()}', '{self.lineManufacturer.text()}', '{self.lineMark.text()}', '{self.lineModel.text()}', {int(self.lineQuantity.text())}, {float(self.linePrice.text())});"
            cursor = self.connectToDB.cursor()
            
            try:
                cursor.execute(query)
                self.connectToDB.commit()
                self.table_page.full_table()
                self.messageOk = Ui_Message()
                self.messageOk.open("Запис успішно додано")
                self.close()

            except mysql.connector.Error as err:
                print(f"Error: {err}")
            finally:
                cursor.close()
    
    # Перевірка на чи є такий ID чи ні
    def checkValuesNumber(self, field):
        try:
            field_values = float(field.text())
            if float(field.text()) < 0:
                return False
            field.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 10px;font-family: \"Arial\"; font-size: 17px;")
            return True
        except ValueError:
            field.setStyleSheet("border: 2px solid red;border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 10px;font-family: \"Arial\"; font-size: 17px;")
            return False
import res
