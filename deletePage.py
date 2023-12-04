from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from Error import Ui_Question

class DeletePage(QtWidgets.QWidget):
    
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
        self.resize(400, 300)
        self.setMinimumSize(QtCore.QSize(400, 300))
        self.setMaximumSize(QtCore.QSize(400, 300))
        self.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(72, 59, 123, 255), stop:0.481308 rgba(108, 71, 255, 255), stop:1 rgba(72, 59, 123, 255))")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(105, 30, 187, 50))
        self.label.setStyleSheet("background: qlineargradient(spread:pad, x1:0.504673, y1:0, x2:0.519, y2:1, stop:0 rgba(241, 101, 41, 255), stop:1 rgba(112, 0, 255, 255)); color: white; padding: 0 0 0 2px; border-radius: 5px; font-family: \"Arial\"; font-size: 17px;")
        self.label.setObjectName("label")
        self.lineID = QtWidgets.QLineEdit(self)
        self.lineID.setGeometry(QtCore.QRect(90, 120, 223, 44))
        self.lineID.setMinimumSize(QtCore.QSize(223, 44))
        self.lineID.setMaximumSize(QtCore.QSize(223, 44))
        self.lineID.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 10px;font-family: \"Arial\"; font-size: 17px;")
        self.lineID.setObjectName("lineID")
        self.pushButtonClean = QtWidgets.QPushButton(self)
        self.pushButtonClean.setGeometry(QtCore.QRect(230, 200, 61, 61))
        self.pushButtonClean.setMinimumSize(QtCore.QSize(61, 61))
        self.pushButtonClean.setMaximumSize(QtCore.QSize(61, 61))
        self.pushButtonClean.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonClean.setStyleSheet("background:qlineargradient(spread:pad, x1:0.505, y1:0, x2:0.509, y2:1, stop:0 rgba(255, 107, 0, 255), stop:0.509346 rgba(34, 34, 34, 255), stop:1 rgba(31, 12, 255, 255));background-image:url(:/img/img/clean.svg);border: none; background-repeat: no-repeat; border-radius: 30px; background-position: center")
        self.pushButtonClean.setText("")
        self.pushButtonClean.setObjectName("pushButtonClean")
        self.pushButtonDelete = QtWidgets.QPushButton(self)
        self.pushButtonDelete.setGeometry(QtCore.QRect(110, 200, 61, 61))
        self.pushButtonDelete.setMinimumSize(QtCore.QSize(61, 61))
        self.pushButtonDelete.setMaximumSize(QtCore.QSize(61, 61))
        self.pushButtonDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonDelete.setStyleSheet("background:qlineargradient(spread:pad, x1:0.505, y1:0, x2:0.509, y2:1, stop:0 rgba(255, 107, 0, 255), stop:0.509346 rgba(34, 34, 34, 255), stop:1 rgba(31, 12, 255, 255));background-image:url(:/img/img/delete.svg);border: none; background-repeat: no-repeat; border-radius: 30px; background-position: center")
        self.pushButtonDelete.setText("")
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        
        # Додавання функціоналу до кнопок
        self.pushButtonClean.clicked.connect(self.clean_ID)
        
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Delete Parts"))
        self.label.setText(_translate("Form", "Видалення запчастини"))
        self.lineID.setPlaceholderText(_translate("Form", "ID"))
    
    # Метод для очищення усіх значень в усіх полях
    def clean_ID(self):
        self.lineID.setText("")
    
    # Видалення відповідного ID
    def delete_Row(self):
        cursor = self.connectToDB.cursor()

        try:
            checkboxes_str = ', '.join([f"'{checkbox}'" for checkbox in self.selected_checkboxes])
            query_select_id = f"SELECT ID FROM details WHERE brand = '{self.brand}' AND model = '{self.model}' AND detailType IN ({checkboxes_str})"
            cursor.execute(query_select_id)
            Id_List = [str(row[0]) for row in cursor.fetchall()]

            if self.lineID.text() in Id_List:

                query_delete_id = f"DELETE FROM details WHERE id = {self.lineID.text()}"
                result = False
                self.ui_question = Ui_Question()
                result = self.ui_question.open("Ви дійсно хочете видалити запис?")
                if result == True:
                    cursor.execute(query_delete_id)
                    self.connectToDB.commit()
                    self.table_page.full_table()
                    self.close()
                    print("Успешно удалено")
                
                self.lineID.setStyleSheet("border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 10px;font-family: \"Arial\"; font-size: 17px;")
            else:
                print("ID не найден")
                self.lineID.setStyleSheet("border: 2px solid red;border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 10px;font-family: \"Arial\"; font-size: 17px;")
        
        except mysql.connector.Error as error:
            print(f"Ошибка: {error}")
            self.lineID.setStyleSheet("border: 2px solid red;border-radius: 10px;background: #FEFEFE;box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); padding: 0px 15px 0px 10px;font-family: \"Arial\"; font-size: 17px.")
        finally:
            cursor.close()
            self.table_page.full_table()
        
import res
