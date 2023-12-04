from PyQt5 import QtCore, QtGui, QtWidgets


class InfoPage(QtWidgets.QWidget):

    def __init__(self, start_page):
        super().__init__()
        self.start_page = start_page
        self.setupUi()

    def setupUi(self):
        self.setWindowIcon(QtGui.QIcon('img/logo.png'))
        self.setObjectName("Form")
        self.resize(800, 600)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(72, 59, 123, 255), stop:0.481308 rgba(108, 71, 255, 255), stop:1 rgba(72, 59, 123, 255))")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(9, 1, 146, 146))
        self.pushButton.setMinimumSize(QtCore.QSize(146, 146))
        self.pushButton.setMaximumSize(QtCore.QSize(146, 146))
        self.pushButton.setStyleSheet("background: transparent;background-image: url(:/img/img/logo.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(140, 140, 561, 431))
        self.textEdit.setMinimumSize(QtCore.QSize(561, 431))
        self.textEdit.setStyleSheet("background: transparent;font-family: \"Arial\"; font-size: 17px;color:white")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Car_depot"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:17px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Автор:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"><br />Кладка Данило Вікторович студент 3 курсу групи 6.04.122.010.21.1</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.6pt;\">Про программу:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.6pt;\"><br />Ця програма створена для того щоб допомогти робітникам складу швидко знаходити деталі на автоскладі та вести їх облік.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:9.6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.6pt;\">Про її функціонал:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:9.6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.6pt;\">Спочатку вам треба обрати марку та модель авто до якої ви хочете знайти деталі після цього ви обераете тип деталі(двигун, тормозна система та автосвітло) після цього формується табличка в якій будя вся інформація про все що ви вибрали. З правого боку є пошук по якому ви можете знайти запчастину по її назві та її вирбнику, натиснувши на кнопку &quot;Пошук&quot; у вас виведеться всі деталі в яких є такий вирбник чи деталь для тої машини яку ви обрали. Знизу є три кнопки &quot;Додати запчастину&quot;, &quot;Видалити запчастину&quot;, &quot;Оновити запчастину&quot; натиснувши на які ви можете сюдячи з назв кнопок зробити певні дії в відкритих вікнах.</span></p></body></html>"))
import res