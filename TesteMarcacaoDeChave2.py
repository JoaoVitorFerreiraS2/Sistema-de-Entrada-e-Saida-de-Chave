

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QCheckBox,  QFrame, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget, QRadioButton)

#Aqui é onde fica o desenho do sistema, o designe.

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 357)
        MainWindow.setMinimumSize(850, 357)
        MainWindow.setMaximumSize(850, 357)


        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setGeometry(QRect(0, 0, 321, 321))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)

        self.matricula_label = QLabel(self.left_container)
        self.matricula_label.setObjectName(u"matricula_label")
        self.matricula_label.setGeometry(QRect(10, 20, 61, 16))

        self.acao_label = QLabel(self.left_container)
        self.acao_label.setObjectName(u"acao_label")
        self.acao_label.setGeometry(QRect(10, 50, 41, 21))

        self.pushButton = QPushButton(self.left_container)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 120, 81, 31))

        self.atualizar = QPushButton(self.left_container)
        self.atualizar.setObjectName(u"atualizar")
        self.atualizar.setGeometry(QRect(100, 120, 81, 31))

        self.matricula_entry = QLineEdit(self.left_container)
        self.matricula_entry.setObjectName(u"matricula_entry")
        self.matricula_entry.setGeometry(QRect(90, 20, 150, 20))
        self.matricula_entry.setPlaceholderText("Digite sua matrícula...")

        self.acao_label = QLabel(self.left_container)
        self.acao_label.setObjectName(u"acao_label")
        self.acao_label.setGeometry(QRect(10, 50, 41, 21))

        # Substitua a entrada de lista por caixas de seleção
        
        self.saida_radio = QRadioButton("Saída", self.left_container)
        self.saida_radio.setGeometry(QRect(70, 50, 80, 20))
        self.entrada_radio = QRadioButton("Entrada", self.left_container)
        self.entrada_radio.setGeometry(QRect(160, 50, 80, 20))

        
        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setGeometry(QRect(319, 119, 600, 231))
        self.main_container.setMaximumSize(QSize(600, 16777215))
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        
        self.registros_table = QTableWidget(self.main_container)
        if (self.registros_table.columnCount() < 5):
            self.registros_table.setColumnCount(5)

        __qtablewidgetitem = QTableWidgetItem()
        self.registros_table.setHorizontalHeaderItem(0, __qtablewidgetitem)

        __qtablewidgetitem1 = QTableWidgetItem()
        self.registros_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)

        __qtablewidgetitem2 = QTableWidgetItem()
        self.registros_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)

        __qtablewidgetitem3 = QTableWidgetItem()
        self.registros_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)

        __qtablewidgetitem4 = QTableWidgetItem()
        self.registros_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)


        self.registros_table.setObjectName(u"registros_table")
        self.registros_table.setGeometry(QRect(2, 1, 600, 431))

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(320, 0, 600, 121))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.matricula_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Matricula:</span></p></body></html>", None))
        self.acao_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">A\u00e7\u00e3o:</span></p></body></html>", None))
        
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.atualizar.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))

        ___qtablewidgetitem = self.registros_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Matrícula", None));
        ___qtablewidgetitem1 = self.registros_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"A\u00e7\u00e3o", None));
        ___qtablewidgetitem2 = self.registros_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Bloco", None));
        ___qtablewidgetitem3 = self.registros_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Hora", None));
        ___qtablewidgetitem3 = self.registros_table.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Data", None));
    # retranslateUi

