import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets

DB_HOST = "127.0.0.1"
#DB_HOST = "192.168.1.155"
DB_NAME = "telspr1"
DB_USER = "postgres"
DB_PASS = "sql"


def process_cmd(cmd):
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
    cur = conn.cursor()
    cur.execute(cmd)
    try:
        rows = cur.fetchall()
    except:
        conn.commit()
        conn.close()
        cur.close()
        return True
    conn.commit()
    conn.close()
    cur.close()
    return rows if rows else []


def load_data(table):
    table.setRowCount(0)
    rows = process_cmd(
        '''select uniq_id, f.f_val, n.name, o.otc, s.s_name, bldn, bldn_k, appr, tel   from main c join fam f on c.fam = f.f_id join names n on c.name = n.n_id  join otcs o on c.otc = o.o_id join streets s on c.street = s.s_id ''')
    for row in rows:
        currentRowCount = table.rowCount()
        table.insertRow(currentRowCount)
        for i in range(9):
            table.setItem(currentRowCount, i, QtWidgets.QTableWidgetItem(str(row[i])))


def load_data_fam(table):
    table.setRowCount(0)
    rows = process_cmd('''select f_id, f_val from fam ''')
    for row in rows:
        currentRowCount = table.rowCount()
        table.insertRow(currentRowCount)
        for i in range(2):
            table.setItem(currentRowCount, i, QtWidgets.QTableWidgetItem(str(row[i])))


def load_data_name(table):
    table.setRowCount(0)
    rows = process_cmd('''select * from names ''')
    for row in rows:
        currentRowCount = table.rowCount()
        table.insertRow(currentRowCount)
        for i in range(2):
            table.setItem(currentRowCount, i, QtWidgets.QTableWidgetItem(str(row[i])))


def load_data_patr(table):
    table.setRowCount(0)
    rows = process_cmd('''select * from otcs ''')
    for row in rows:
        currentRowCount = table.rowCount()
        table.insertRow(currentRowCount)
        for i in range(2):
            table.setItem(currentRowCount, i, QtWidgets.QTableWidgetItem(str(row[i])))


def load_data_street(table):
    table.setRowCount(0)
    rows = process_cmd('''select * from streets ''')
    for row in rows:
        currentRowCount = table.rowCount()
        table.insertRow(currentRowCount)
        for i in range(2):
            table.setItem(currentRowCount, i, QtWidgets.QTableWidgetItem(str(row[i])))


def get_combo(cmd):
    rows = process_cmd(cmd)
    rows = [row[0].strip() for row in rows]
    return rows


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 520)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
#        self.centralwidget.setStyleSheet("background-color: #FFDAB9;")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 220, 851, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(
            ['Код', 'Фамилия', 'Имя', 'Отчество', 'Улица', 'Дом', 'Корпус', 'Квартира', 'Телефон'])
        load_data(self.tableWidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 75, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(190, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 20, 75, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(605, 20, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(690, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(800, 20, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 110, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_house = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_house.setGeometry(QtCore.QRect(590, 60, 61, 20))
        self.lineEdit_house.setText("")
        self.lineEdit_house.setObjectName("lineEdit_house")
        self.comboBox_surname = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_surname.addItems([''] + get_combo('select f_val from fam'))
        self.comboBox_surname.setGeometry(QtCore.QRect(40, 60, 91, 22))
        self.comboBox_surname.setObjectName("comboBox_surname")
        self.comboBox_name = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_name.addItems([''] + get_combo('select name from names'))
        self.comboBox_name.setGeometry(QtCore.QRect(175, 60, 91, 22))
        self.comboBox_name.setObjectName("comboBox_name")
        self.comboBox_patr = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_patr.addItems([''] + get_combo('select otc from otcs'))
        self.comboBox_patr.setGeometry(QtCore.QRect(300, 60, 91, 22))
        self.comboBox_patr.setObjectName("comboBox_patr")
        self.comboBox_street = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_street.addItems([''] + get_combo('select s_name from streets'))
        self.comboBox_street.setGeometry(QtCore.QRect(440, 60, 91, 22))
        self.comboBox_street.setObjectName("comboBox_street")
        self.lineEdit_korpus = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_korpus.setGeometry(QtCore.QRect(690, 60, 61, 20))
        self.lineEdit_korpus.setText("")
        self.lineEdit_korpus.setObjectName("lineEdit_korpus")
        self.lineEdit_flat = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_flat.setGeometry(QtCore.QRect(810, 60, 61, 20))
        self.lineEdit_flat.setText("")
        self.lineEdit_flat.setObjectName("lineEdit_flat")
        self.lineEdit_tel = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tel.setGeometry(QtCore.QRect(40, 150, 131, 20))
        self.lineEdit_tel.setText("")
        self.lineEdit_tel.setObjectName("lineEdit_tel")
        self.toolButton_surname = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_surname.setGeometry(QtCore.QRect(130, 60, 25, 19))
        self.toolButton_surname.setObjectName("toolButton_surname")
        self.toolButton_surname.clicked.connect(self.openDialog)
        self.toolButton_name = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_name.setGeometry(QtCore.QRect(265, 60, 25, 19))
        self.toolButton_name.setObjectName("toolButton_name")
        self.toolButton_name.clicked.connect(self.openDialog_name)
        self.toolButton_patr = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_patr.setGeometry(QtCore.QRect(390, 60, 25, 19))
        self.toolButton_patr.setObjectName("toolButton_patr")
        self.toolButton_patr.clicked.connect(self.openDialog_patr)
        self.toolButton_street = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_street.setGeometry(QtCore.QRect(530, 60, 25, 19))
        self.toolButton_street.setObjectName("toolButton_street")
        self.toolButton_street.clicked.connect(self.openDialog_street)
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setGeometry(QtCore.QRect(250, 150, 125, 40))
        self.pushButton_search.setFont(font)
        self.pushButton_search.setObjectName("pushButton")
        self.pushButton_search.clicked.connect(self.search_main)
        self.pushButton_insert = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_insert.setGeometry(QtCore.QRect(400, 150, 125, 40))
        self.pushButton_insert.setFont(font)
        self.pushButton_insert.setObjectName("pushButton_2")
        self.pushButton_insert.clicked.connect(self.insert_main)
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(550, 150, 125, 40))
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setObjectName("pushButton_3")
        self.pushButton_delete.clicked.connect(self.delete_main)
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_update.setGeometry(QtCore.QRect(700, 150, 125, 40))
        self.pushButton_update.setFont(font)
        self.pushButton_update.setObjectName("pushButton_4")
        self.pushButton_update.clicked.connect(self.update_main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 892, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openDialog(self):
        dialog = ClssDialog(self)
        dialog.exec_()

    def openDialog_name(self):
        dialog = ClssDialog_name(self)
        dialog.exec_()

    def openDialog_patr(self):
        dialog = ClssDialog_patr(self)
        dialog.exec_()

    def openDialog_street(self):
        dialog = ClssDialog_street(self)
        dialog.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#        self.label.setText(_translate("MainWindow", "Код"))
        self.label_1.setText(_translate("MainWindow", "Имя"))
        self.label_2.setText(_translate("MainWindow", "Фамилия"))
        self.label_3.setText(_translate("MainWindow", "Отчество"))
        self.label_4.setText(_translate("MainWindow", "Улица"))
        self.label_5.setText(_translate("MainWindow", "Дом"))
        self.label_6.setText(_translate("MainWindow", "Корпус"))
        self.label_7.setText(_translate("MainWindow", "Квартира"))
        self.label_8.setText(_translate("MainWindow", "Телефон"))
        self.toolButton_name.setText(_translate("MainWindow", "..."))
        self.toolButton_surname.setText(_translate("MainWindow", "..."))
        self.toolButton_patr.setText(_translate("MainWindow", "..."))
        self.toolButton_street.setText(_translate("MainWindow", "..."))
        self.pushButton_search.setText(_translate("MainWindow", "Поиск"))
        self.pushButton_insert.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_delete.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_update.setText(_translate("MainWindow", "Изменить"))

    def insert_main(self):
        cmd_fam="select f.f_id from fam f where f.f_val = '{}' ".format(self.comboBox_surname.currentText())
        row = process_cmd(cmd_fam)
        print(row)
        print(row[0][0])
#        street = "and s.s_name = '{}' ".format(street)

        from PyQt5.QtWidgets import QMessageBox
        alert = QMessageBox()
        alert.setText(str(row[0]))
        alert.exec_()

        cmd = f'''insert into main values (default, (select f.f_id from fam f where f.f_val = '{self.comboBox_surname.currentText()}'),
            (select n.n_id from names n where n.name = '{self.comboBox_name.currentText()}'), (select o.o_id from otcs o where o.otc = '{self.comboBox_patr.currentText()}'),
            (select s.s_id from streets s where s.s_name = '{self.comboBox_street.currentText()}'), '{self.lineEdit_house.text()}',
            '{self.lineEdit_korpus.text()}', '{self.lineEdit_flat.text()}', '{self.lineEdit_tel.text()}')'''
        process_cmd(cmd)
        load_data(self.tableWidget)

    def search_main(self):
        fam=self.comboBox_surname.currentText()
        if fam :
             fam="and f.f_val ='{}' ".format(fam)
        else:
            fam=''

        name=self.comboBox_name.currentText()
        if name :
             name="and n.name ='{}' ".format(name)
        else:
            name=''

        patr =self.comboBox_patr.currentText()
        if patr :
             patr="and o.otc ='{}' ".format(patr)
        else:
            patr=''

        street = self.comboBox_street.currentText()
        if street:
            street="and s.s_name = '{}' ".format(street)
        else:
            street=''

        house  = self.lineEdit_house.text()
        if house:
            house="and c.bldn= '{}' ".format(house)
        else:
            house=''

        korpus  = self.lineEdit_korpus.text()
        if korpus :
            korpus= "and c.bldn_k= '{}' ".format(korpus)
        else :
            korpus=''

        flat  = self.lineEdit_flat.text()
        if flat :
            flat="and c.appr = {} ".format(flat)
        else :
            flat=''

        tel  = self.lineEdit_tel.text()
        if tel:
            tel= "and c.tel LIKE '{}'".format(tel)
        else :
            tel=''

        from PyQt5.QtWidgets import QMessageBox
        alert = QMessageBox()
#        alert.setText(fam)
#        alert.exec_()

#        fam = f"and f.f_val = '{self.comboBox_surname.currentText()}'" if self.comboBox_surname.currentText() else ''
#        name = f"and n.name = '{self.comboBox_name.currentText()}'" if self.comboBox_name.currentText() else ''
#        patr = f"and o.otc = '{self.comboBox_patr.currentText()}'" if self.comboBox_patr.currentText() else ''
#        street = f"and s.s_name = '{self.comboBox_street.currentText()}'" if self.comboBox_street.currentText() else ''
#        house = f"and c.bldn = '{self.lineEdit_house.text()}'" if self.lineEdit_house.text() else ''
#        korpus = f"and c.bldn_k = '{self.lineEdit_korpus.text()}'" if self.lineEdit_korpus.text() else ''
#        flat = f"and c.appr = '{self.lineEdit_flat.text()}'" if self.lineEdit_flat.text() else ''
#        tel = f"and c.tel = '{self.lineEdit_tel.text()}'" if self.lineEdit_tel.text() else ''
#        filters = (fam + name + patr + street + house + korpus + flat + tel).strip('and')
        filters = (fam + name + patr + street + house + korpus + flat + tel)

        alert.setText(filters)
        alert.exec_()

        filters = filters.replace("and", "", 1)

        if fam or name or patr or street or house or korpus or flat or tel:
            cmd = '''select uniq_id, f.f_val, n.name, o.otc, s.s_name, bldn, bldn_k, appr, tel  from main c join fam f on c.fam = f.f_id join names n on c.name = n.n_id 
                     join otcs o on c.otc = o.o_id join streets s on c.street = s.s_id where ''' + filters

            alert = QMessageBox()
            alert.setText(cmd)
            alert.exec_()

            rows = process_cmd(cmd)
 #           print(rows)
            self.tableWidget.setRowCount(0)
            for row in rows:
                currentRowCount = self.tableWidget.rowCount()
                self.tableWidget.insertRow(currentRowCount)
                for i in range(9):
                    if i == 7 or i == 0:
                        self.tableWidget.setItem(currentRowCount, i, QtWidgets.QTableWidgetItem(str(row[i])))
                    else:
#                        print(row[i],str(row[i]))
                        self.tableWidget.setItem(currentRowCount, i, QtWidgets.QTableWidgetItem(row[i]))

        else:
            load_data(self.tableWidget)

    def cell_clicked(self): #определение номера столбца и строки для ячейки
        global costsz,totalz,descriptionz,row,col
        row = self.table.currentItem().row() #Номер строки корректируемой ячейки
        col = self.table.currentItem().column() #Номер столбца корректируемой ячейки
        idz = int(self.table.item(row,0).text()) #Запоминание значений полей
        descriptionz= self.table.item(row,1).text() #корректируемой строки
        costsz= self.table.item(row,2).text()
        totalz= self.table.item(row,3).text()

    def update_main(self):
        #        temp=self.tableWidget.currentRow()
        row = self.tableWidget.currentItem().row()  # Номер строки корректируемой ячейки
        #        print(row)
        #        idz = int(self.tableWidget.item(row,0).text()) #Запоминание значений полей
        #           Поля записи
        record_id = self.tableWidget.item(row, 0).text()  # Запоминание значений полей
        wrk_fam = self.tableWidget.item(row, 1).text()
        wrk_name = self.tableWidget.item(row, 2).text()
        wrk_otc = self.tableWidget.item(row, 3).text()
        print(record_id, wrk_fam, wrk_name, wrk_otc)

    def delete_main(self):
#        temp=self.tableWidget.currentRow()
        row = self.tableWidget.currentItem().row()  # Номер строки корректируемой ячейки
#        print(row)
#        idz = int(self.tableWidget.item(row,0).text()) #Запоминание значений полей
#           Поля записи
        record_id = self.tableWidget.item(row,0).text() #Запоминание значений полей
        from PyQt5.QtWidgets import QMessageBox
        alert = QMessageBox()
        alert.setText(record_id)
        alert.exec_()

 #       print (temp)
        cmd = f'''delete from main where uniq_id = {record_id}'''
        process_cmd(cmd)
        load_data(self.tableWidget)


class ClssDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog, self).__init__(parent)
        self.resize(550, 350)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 280, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'Фамилия'])
        load_data_fam(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.setWindowTitle("Dialog")
        self.lineEdit_input = QtWidgets.QLineEdit(self)
        self.lineEdit_input.setGeometry(QtCore.QRect(310, 50, 230, 25))
        self.lineEdit_input.setText("")
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.pushButton_search = QtWidgets.QPushButton(self)
        self.pushButton_search.setGeometry(QtCore.QRect(360, 100, 100, 30))
        self.pushButton_search.setObjectName("pushButton")
        self.pushButton_search.clicked.connect(self.search_fams)
        self.pushButton_insert = QtWidgets.QPushButton(self)
        self.pushButton_insert.setGeometry(QtCore.QRect(360, 150, 100, 30))
        self.pushButton_insert.setObjectName("pushButton_2")
        self.pushButton_insert.clicked.connect(self.insert_fams)
        self.pushButton_delete = QtWidgets.QPushButton(self)
        self.pushButton_delete.setGeometry(QtCore.QRect(360, 200, 100, 30))
        self.pushButton_delete.setObjectName("pushButton_3")
        self.pushButton_delete.clicked.connect(self.delete_fams)
        self.pushButton_search.setText("Поиск")
        self.pushButton_insert.setText("Добавить")
        self.pushButton_delete.setText("Удалить")

    def btnClosed(self):
        self.close()

    def insert_fams(self):
        if self.lineEdit_input.text():
            cmd = f'''insert into fams values (default, '{self.lineEdit_input.text()}')'''
            print(cmd)
            process_cmd(cmd)
            load_data_fam(self.tableWidget)
            ui.comboBox_surname.clear()
            ui.comboBox_surname.addItems([''] + get_combo('select f_val from fam'))

    def search_fams(self):
        if self.lineEdit_input.text():
            cmd = f"select * from fam where f_val = '{self.lineEdit_input.text()}'"
            print(cmd)
            rows = process_cmd(cmd)
            self.tableWidget.setRowCount(0)
            for row in rows:
                currentRowCount = self.tableWidget.rowCount()
                self.tableWidget.insertRow(currentRowCount)
                for i in range(2):
                    self.tableWidget.setItem(currentRowCount, i, QtWidgets.QTableWidgetItem(str(row[i])))
        else:
            load_data_fam(self.tableWidget)

    # def delete_fams(self):
    #     cmd = f"delete  from fams  where f_val = '{self.lineEdit_input.text()}'"
    #     process_cmd(cmd)
    #     load_data_fam(self.tableWidget)
    #     ui.comboBox_surname.clear()
    #     ui.comboBox_surname.addItems([''] + get_combo('select f_val from fams'))

    def delete_fams(self):  ###
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            cmd = f"delete  from fams  where f_val = '{self.lineEdit_input.text()}'"
            process_cmd(cmd)
            load_data_fam(self.tableWidget)
            ui.comboBox_surname.clear()
            ui.comboBox_surname.addItems([''] + get_combo('select f_val from fam'))
        else:
            print('Отмена')


class ClssDialog_name(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog_name, self).__init__(parent)
        self.resize(550, 350)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 280, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'Имя'])
        load_data_name(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.setWindowTitle("Dialog")
        self.lineEdit_input = QtWidgets.QLineEdit(self)
        self.lineEdit_input.setGeometry(QtCore.QRect(310, 50, 230, 25))
        self.lineEdit_input.setText("")
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.pushButton_search = QtWidgets.QPushButton(self)
        self.pushButton_search.setGeometry(QtCore.QRect(360, 100, 100, 30))
        self.pushButton_search.setObjectName("pushButton")
        self.pushButton_search.clicked.connect(self.search_fams)
        self.pushButton_insert = QtWidgets.QPushButton(self)
        self.pushButton_insert.setGeometry(QtCore.QRect(360, 150, 100, 30))
        self.pushButton_insert.setObjectName("pushButton_2")
        self.pushButton_insert.clicked.connect(self.insert_fams)
        self.pushButton_delete = QtWidgets.QPushButton(self)
        self.pushButton_delete.setGeometry(QtCore.QRect(360, 200, 100, 30))
        self.pushButton_delete.setObjectName("pushButton_3")
        self.pushButton_delete.clicked.connect(self.delete_fams)
        self.pushButton_search.setText("Поиск")
        self.pushButton_insert.setText("Добавить")
        self.pushButton_delete.setText("Удалить")

    def btnClosed(self):
        self.close()

    def insert_fams(self):
        if self.lineEdit_input.text():
            cmd = f'''insert into names values (default, '{self.lineEdit_input.text()}')'''
            print(cmd)
            process_cmd(cmd)
            load_data_name(self.tableWidget)
            ui.comboBox_name.clear()
            ui.comboBox_name.addItems([''] + get_combo('select name from names'))

    def search_fams(self):
        if self.lineEdit_input.text():
            cmd = f"select * from names where name = '{self.lineEdit_input.text()}'"
            print(cmd)
            rows = process_cmd(cmd)
            self.tableWidget.setRowCount(0)
            for row in rows:
                currentRowCount = self.tableWidget.rowCount()
                self.tableWidget.insertRow(currentRowCount)
                for i in range(2):
                    self.tableWidget.setItem(currentRowCount, i, QtWidgets.QTableWidgetItem(str(row[i])))
        else:
            load_data_name(self.tableWidget)

    def delete_fams(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            cmd = f"delete  from names  where name = '{self.lineEdit_input.text()}'"
            process_cmd(cmd)
            load_data_name(self.tableWidget)
            ui.comboBox_name.clear()
            ui.comboBox_name.addItems([''] + get_combo('select name from names'))
        else:
            print('Отмена')


class ClssDialog_patr(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog_patr, self).__init__(parent)
        self.resize(550, 350)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 280, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'Отчество'])
        load_data_patr(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.setWindowTitle("Dialog")
        self.lineEdit_input = QtWidgets.QLineEdit(self)
        self.lineEdit_input.setGeometry(QtCore.QRect(310, 50, 230, 25))
        self.lineEdit_input.setText("")
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.pushButton_search = QtWidgets.QPushButton(self)
        self.pushButton_search.setGeometry(QtCore.QRect(360, 100, 100, 30))
        self.pushButton_search.setObjectName("pushButton")
        self.pushButton_search.clicked.connect(self.search_fams)
        self.pushButton_insert = QtWidgets.QPushButton(self)
        self.pushButton_insert.setGeometry(QtCore.QRect(360, 150, 100, 30))
        self.pushButton_insert.setObjectName("pushButton_2")
        self.pushButton_insert.clicked.connect(self.insert_fams)
        self.pushButton_delete = QtWidgets.QPushButton(self)
        self.pushButton_delete.setGeometry(QtCore.QRect(360, 200, 100, 30))
        self.pushButton_delete.setObjectName("pushButton_3")
        self.pushButton_delete.clicked.connect(self.delete_fams)
        self.pushButton_search.setText("Поиск")
        self.pushButton_insert.setText("Добавить")
        self.pushButton_delete.setText("Удалить")

    def btnClosed(self):
        self.close()

    def insert_fams(self):
        if self.lineEdit_input.text():
            cmd = f'''insert into otcs values (default, '{self.lineEdit_input.text()}')'''
            print(cmd)
            process_cmd(cmd)
            load_data_patr(self.tableWidget)
            ui.comboBox_patr.clear()
            ui.comboBox_patr.addItems([''] + get_combo('select otc from otcs'))

    def search_fams(self):
        if self.lineEdit_input.text():
            cmd = f"select * from otcs where otc = '{self.lineEdit_input.text()}'"
            print(cmd)
            rows = process_cmd(cmd)
            self.tableWidget.setRowCount(0)
            for row in rows:
                currentRowCount = self.tableWidget.rowCount()
                self.tableWidget.insertRow(currentRowCount)
                for i in range(2):
                    self.tableWidget.setItem(currentRowCount, i, QtWidgets.QTableWidgetItem(str(row[i])))
        else:
            load_data_patr(self.tableWidget)

    def delete_fams(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            cmd = f"delete  from otcs  where otc = '{self.lineEdit_input.text()}'"
            process_cmd(cmd)
            load_data_patr(self.tableWidget)
            ui.comboBox_patr.clear()
            ui.comboBox_patr.addItems([''] + get_combo('select otc from otcs'))
        else:
            print('Отмена')


class ClssDialog_street(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog_street, self).__init__(parent)
        self.resize(550, 350)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 280, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'Улица'])
        load_data_street(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.setWindowTitle("Dialog")
        self.lineEdit_input = QtWidgets.QLineEdit(self)
        self.lineEdit_input.setGeometry(QtCore.QRect(310, 50, 230, 25))
        self.lineEdit_input.setText("")
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.pushButton_search = QtWidgets.QPushButton(self)
        self.pushButton_search.setGeometry(QtCore.QRect(360, 100, 100, 30))
        self.pushButton_search.setObjectName("pushButton")
        self.pushButton_search.clicked.connect(self.search_fams)
        self.pushButton_insert = QtWidgets.QPushButton(self)
        self.pushButton_insert.setGeometry(QtCore.QRect(360, 150, 100, 30))
        self.pushButton_insert.setObjectName("pushButton_2")
        self.pushButton_insert.clicked.connect(self.insert_fams)
        self.pushButton_delete = QtWidgets.QPushButton(self)
        self.pushButton_delete.setGeometry(QtCore.QRect(360, 200, 100, 30))
        self.pushButton_delete.setObjectName("pushButton_3")
        self.pushButton_delete.clicked.connect(self.delete_fams)
        self.pushButton_search.setText("Поиск")
        self.pushButton_insert.setText("Добавить")
        self.pushButton_delete.setText("Удалить")

    def btnClosed(self):
        self.close()

    def insert_fams(self):
        if self.lineEdit_input.text():
            cmd = f'''insert into streets values (default, '{self.lineEdit_input.text()}')'''
            print(cmd)
            process_cmd(cmd)
            load_data_street(self.tableWidget)
            ui.comboBox_street.clear()
            ui.comboBox_street.addItems([''] + get_combo('select s_name from streets'))

    def search_fams(self):
        if self.lineEdit_input.text():
            cmd = f"select * from streets where s_name = '{self.lineEdit_input.text()}'"
            print(cmd)
            rows = process_cmd(cmd)
            self.tableWidget.setRowCount(0)
            for row in rows:
                currentRowCount = self.tableWidget.rowCount()
                self.tableWidget.insertRow(currentRowCount)
                for i in range(2):
                    self.tableWidget.setItem(currentRowCount, i, QtWidgets.QTableWidgetItem(str(row[i])))
        else:
            load_data_street(self.tableWidget)

    def delete_fams(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            cmd = f"delete  from streets  where s_name = '{self.lineEdit_input.text()}'"
            process_cmd(cmd)
            load_data_street(self.tableWidget)
            ui.comboBox_street.clear()
            ui.comboBox_street.addItems([''] + get_combo('select s_name from streets'))
        else:
            print('Отмена')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
