# Импортирование необходимых модулей
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
import sys
import psycopg2

# Подключение к базе данных PostgreSQL
connection = psycopg2.connect(
  database="telspr",
  user="postgres",
  password="sql",
  host="127.0.0.1"
)

cursor = connection.cursor()

# Подключение GUI
app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("MyForm111.ui")
window.show()
children = window.children()
############################

#Заполняем комбобоксы
combosurname = children[18]
comboname = children[19]
combopatronymic = children[20]

combosurname.clear()
start_query = 'SELECT DISTINCT f_val FROM fam'
cursor.execute(start_query)
surnamerecords = cursor.fetchall()
for rec in surnamerecords:
    combosurname.addItem(rec[0])

comboname.clear()
start_query = 'SELECT DISTINCT n_val FROM nam'
cursor.execute(start_query)
namerecords = cursor.fetchall()
for rec in namerecords:
    comboname.addItem(rec[0])

combopatronymic.clear()
start_query = 'SELECT DISTINCT o_val FROM otc'
cursor.execute(start_query)
patronymicrecords = cursor.fetchall()
for rec in patronymicrecords:
    combopatronymic.addItem(rec[0])
####################################

# Инициализация кнопок
buttonFind = children[13]
buttonAdd = children[14]
buttonSave = children[15]
buttonDelete = children[16]
####################################

#Инициализация таблицы
table = children[17]
table.setColumnCount(9)
table.setHorizontalHeaderLabels(["Id", "surname", "name", "patronymic", "street", "house", "frame", "apartment", "telephone"])

# Функция обработки кнопки Поиск


def on_find_click():

    table.clear()
    table.setRowCount(0)

    surname = children[18].currentText()
    name = children[19].currentText()
    patronymic = children[20].currentText()

    #Перевод из текста в значения дочерной таблицы
    work_query = "SELECT fam_id FROM public.fam WHERE fam_val = %s "
    cursor.execute(work_query, (surname,))
    connection.commit()
    records = cursor.fetchall()
    surname = records[0][0]

    work_query = 'SELECT name_id FROM name WHERE name_val=%s'
    cursor.execute(work_query, (name, ))
    connection.commit()
    records = cursor.fetchall()
    name = records[0][0]

    work_query = 'SELECT otc_id FROM otchestvo WHERE otc_val=%s'
    cursor.execute(work_query, (patronymic, ))
    records = cursor.fetchall()
    patronymic = records[0][0]
    #############################################

    data = (surname, name, patronymic)

    find_query = 'SELECT * FROM main WHERE fam = %s AND name = %s AND otc = %s'

    cursor.execute(find_query, data)
    connection.commit()
    records = cursor.fetchall()

    for row in records:
        # Перевод из значений дочерной таблицы в текст
        work_query = "SELECT fam_val FROM public.fam WHERE fam_id = %s "
        cursor.execute(work_query, (row[1],))
        connection.commit()
        records = cursor.fetchall()
        s = records[0][0]

        work_query = 'SELECT name_val FROM name WHERE name_id=%s'
        cursor.execute(work_query, (row[2],))
        connection.commit()
        records = cursor.fetchall()
        n = records[0][0]

        work_query = 'SELECT otc_val FROM otchestvo WHERE otc_id=%s'
        cursor.execute(work_query, (row[3],))
        connection.commit()
        records = cursor.fetchall()
        t = records[0][0]

        work_query = 'SELECT str_val FROM street WHERE str_id=%s'
        cursor.execute(work_query, (row[4],))
        connection.commit()
        records = cursor.fetchall()
        st = records[0][0]
        #############################################

        rowPosition = table.rowCount()
        table.insertRow(rowPosition)

        table.setItem(rowPosition, 0, QTableWidgetItem(str(row[0])))
        table.setItem(rowPosition, 1, QTableWidgetItem(str(s)))
        table.setItem(rowPosition, 2, QTableWidgetItem(str(n)))
        table.setItem(rowPosition, 3, QTableWidgetItem(str(t)))
        table.setItem(rowPosition, 4, QTableWidgetItem(str(st)))
        table.setItem(rowPosition, 5, QTableWidgetItem(str(row[5])))
        table.setItem(rowPosition, 6, QTableWidgetItem(str(row[6])))
        table.setItem(rowPosition, 7, QTableWidgetItem(str(row[7])))
        table.setItem(rowPosition, 8, QTableWidgetItem(str(row[8])))
        table.setHorizontalHeaderLabels(["Id", "surname", "name", "patronymic", "street", "house", "frame", "apartment", "telephone"])


# Функция обработки кнопки Добавить

def on_add_click():
    print("clicked!")

    surname = children[21].text()
    name = children[22].text()
    patronymic = children[23].text()
    street = children[4].text()
    house = children[6].text()
    frame = children[8].text()
    apartment = children[9].text()
    telephone = children[12].text()

    #Перевод из текста в значения дочерних таблиц
    work_query = 'SELECT fam_val FROM public.fam'
    cursor.execute(work_query, (surname,))
    surnamerecords = cursor.fetchall()
    flag = 0
    for sur in surnamerecords:
        if surname == sur[0].rstrip():
            flag = 1

    if flag==1:
        work_query = 'SELECT fam_id FROM public.fam WHERE fam_val=%s'
        cursor.execute(work_query, (surname,))
        surnamerecords = cursor.fetchall()
        surname = surnamerecords[0][0]

    if flag == 0:
        maxid_query = "SELECT fam_id FROM public.fam ORDER BY fam_id DESC LIMIT 1"
        cursor.execute(maxid_query)
        max_id_add = cursor.fetchone()
        max_id_add = max_id_add[0]

        add_query = "INSERT INTO public.fam (fam_id,fam_val) VALUES(%s, %s)"
        data = (max_id_add + 1, (surname,))
        cursor.execute(add_query, data)
        connection.commit()

        surname = max_id_add + 1



    work_query = 'SELECT name_val FROM public.name'
    cursor.execute(work_query, (name,))
    namerecords = cursor.fetchall()
    flag = 0
    for nam in namerecords:
        if name == nam[0].rstrip():
            flag = 1

    if flag==1:
        work_query = 'SELECT name_id FROM public.name WHERE name_val=%s'
        cursor.execute(work_query, (name,))
        namerecords = cursor.fetchall()
        name = namerecords[0][0]

    if flag == 0:
        maxid_query = "SELECT name_id FROM public.name ORDER BY name_id DESC LIMIT 1"
        cursor.execute(maxid_query)
        max_id_add = cursor.fetchone()
        max_id_add = max_id_add[0]

        add_query = "INSERT INTO public.name (name_id, name_val) VALUES(%s, %s)"
        data = (max_id_add + 1, (name,))
        cursor.execute(add_query, data)
        connection.commit()

        name = max_id_add + 1



    work_query = 'SELECT otc_val FROM public.otchestvo'
    cursor.execute(work_query, (patronymic,))
    patronymicrecords = cursor.fetchall()
    flag = 0
    for otc in patronymicrecords:
        if patronymic == otc[0].rstrip():
            flag = 1

    if flag==1:
        work_query = 'SELECT otc_id FROM public.otchestvo WHERE otc_val=%s'
        cursor.execute(work_query, (patronymic,))
        otcrecords = cursor.fetchall()
        patronymic = otcrecords[0][0]

    if flag == 0:
        maxid_query = "SELECT otc_id FROM public.otchestvo ORDER BY otc_id DESC LIMIT 1"
        cursor.execute(maxid_query)
        max_id_add = cursor.fetchone()
        max_id_add = max_id_add[0]

        add_query = "INSERT INTO public.otchestvo (otc_id, otc_val) VALUES(%s, %s)"
        data = (max_id_add + 1, (patronymic,))
        cursor.execute(add_query, data)
        connection.commit()

        patronymic = max_id_add + 1


    work_query = 'SELECT str_val FROM public.street'
    cursor.execute(work_query, (street,))
    strrecords = cursor.fetchall()
    flag = 0
    for st in strrecords:
        if street == st[0].rstrip():
            flag = 1

    if flag==1:
        work_query = 'SELECT str_id FROM public.street WHERE str_val=%s'
        cursor.execute(work_query, (street,))
        strrecords = cursor.fetchall()
        street = strrecords[0][0]

    if flag == 0:
        maxid_query = "SELECT str_id FROM public.street ORDER BY str_id DESC LIMIT 1"
        cursor.execute(maxid_query)
        max_id_add = cursor.fetchone()
        max_id_add = max_id_add[0]

        add_query = "INSERT INTO public.street (str_id, str_val) VALUES(%s, %s)"
        data = (max_id_add + 1, (street,))
        cursor.execute(add_query, data)
        connection.commit()

        street = max_id_add + 1

    #########################################

    maxid_query = "SELECT u_id FROM public.main ORDER BY u_id DESC LIMIT 1"
    cursor.execute(maxid_query)
    max_id = cursor.fetchone()
    max=max_id[0]

    data = (max+1, surname, name, patronymic, street, house, frame, apartment, telephone)

    insert_query = "INSERT INTO main(u_id, fam, name, otc, str, bldn, bldn_k, appr, telef) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    cursor.execute(insert_query, data)
    connection.commit()

    #Обновление бокса
    combosurname.clear()
    start_query = 'SELECT DISTINCT fam_val FROM public.fam'
    cursor.execute(start_query)
    surnamerecords = cursor.fetchall()
    for rec in surnamerecords:
        combosurname.addItem(rec[0])

    comboname.clear()
    start_query = 'SELECT DISTINCT name_val FROM public.name'
    cursor.execute(start_query)
    namerecords = cursor.fetchall()
    for rec in namerecords:
        comboname.addItem(rec[0])

    combopatronymic.clear()
    start_query = 'SELECT DISTINCT otc_val FROM public.otchestvo'
    cursor.execute(start_query)
    patronymicrecords = cursor.fetchall()
    for rec in patronymicrecords:
        combopatronymic.addItem(rec[0])
    ##############################

    print("Done!")

# Функция обработки кнопки Сохранить


def on_save_click():
    print("clicked!")

    surname = children[18].currentText()
    name = children[19].currentText()
    patronymic = children[20].currentText()
    street = children[4].text()
    house = children[6].text()
    frame = children[8].text()
    apartment = children[9].text()
    telephone = children[12].text()

    #Перевод из текста в значения дочерной таблицы
    work_query = 'SELECT str_val FROM public.street'
    cursor.execute(work_query, (street,))
    strrecords = cursor.fetchall()
    flag = 0
    for st in strrecords:
        if street == st[0].rstrip():
            flag = 1

    if flag == 1:
        work_query = 'SELECT str_id FROM public.street WHERE str_val=%s'
        cursor.execute(work_query, (street,))
        strrecords = cursor.fetchall()
        street = strrecords[0][0]

    if flag == 0:
        maxid_query = "SELECT str_id FROM public.street ORDER BY str_id DESC LIMIT 1"
        cursor.execute(maxid_query)
        max_id_add = cursor.fetchone()
        max_id_add = max_id_add[0]

        add_query = "INSERT INTO public.street (str_id, str_val) VALUES(%s, %s)"
        data = (max_id_add + 1, (street,))
        cursor.execute(add_query, data)
        connection.commit()

        street = max_id_add + 1


    work_query = "SELECT fam_id FROM public.fam WHERE fam_val = %s "
    cursor.execute(work_query, (surname,))
    connection.commit()
    records = cursor.fetchall()
    surname = records[0][0]

    work_query = 'SELECT name_id FROM name WHERE name_val=%s'
    cursor.execute(work_query, (name, ))
    connection.commit()
    records = cursor.fetchall()
    name = records[0][0]

    work_query = 'SELECT otc_id FROM otchestvo WHERE otc_val=%s'
    cursor.execute(work_query, (patronymic, ))
    records = cursor.fetchall()
    patronymic = records[0][0]
    #############################################

    data = (street, house, frame, apartment, telephone, surname, name, patronymic)

    save_query = "UPDATE main SET str=%s, bldn=%s, bldn_k=%s, appr=%s, telef=%s WHERE fam = %s AND name = %s AND otc = %s"
    cursor.execute(save_query, data)
    connection.commit()

    print("Done!")

# Функция обработки кнопки Удалить


def on_delete_click():
    print("clicked!")

    surname = children[18].currentText()
    name = children[19].currentText()
    patronymic = children[20].currentText()
    street = children[4].text()

    #Перевод из текста в значения дочерной таблицы
    work_query = "SELECT fam_id FROM public.fam WHERE fam_val = %s "
    cursor.execute(work_query, (surname,))
    connection.commit()
    records = cursor.fetchall()
    surname = records[0][0]

    work_query = 'SELECT name_id FROM name WHERE name_val=%s'
    cursor.execute(work_query, (name, ))
    connection.commit()
    records = cursor.fetchall()
    name = records[0][0]

    work_query = 'SELECT otc_id FROM otchestvo WHERE otc_val=%s'
    cursor.execute(work_query, (patronymic, ))
    records = cursor.fetchall()
    patronymic = records[0][0]

    work_query = "SELECT str_id FROM public.street WHERE str_val = %s "
    cursor.execute(work_query, (street,))
    connection.commit()
    records = cursor.fetchall()
    street = records[0][0]
    #############################################

    data = (surname, name, patronymic)

    delete_query = "DELETE FROM main WHERE fam = %s AND name = %s AND otc = %s"
    cursor.execute(delete_query, data)
    connection.commit()

    work_query = 'SELECT DISTINCT fam FROM main'
    cursor.execute(work_query)
    records = cursor.fetchall()
    flag = 0
    for r in records:
        if surname == r[0]:
            flag = 1

    if flag == 0:
        delete_query = "DELETE FROM fam WHERE fam_id = %s"
        cursor.execute(delete_query, (surname,))
        connection.commit()

    work_query = 'SELECT DISTINCT name FROM public.main'
    cursor.execute(work_query)
    records = cursor.fetchall()
    flag = 0
    for r in records:
        if name == r[0]:
            flag = 1

    if flag == 0:
        delete_query = "DELETE FROM name WHERE name_id = %s"
        cursor.execute(delete_query, (name,))
        connection.commit()

    work_query = 'SELECT DISTINCT otc FROM public.main'
    cursor.execute(work_query)
    records = cursor.fetchall()
    flag = 0
    for r in records:
        if patronymic == r[0]:
            flag = 1

    if flag == 0:
        delete_query = "DELETE FROM otchestvo WHERE otc_id = %s"
        cursor.execute(delete_query, (patronymic,))
        connection.commit()

    work_query = 'SELECT DISTINCT str FROM public.main'
    cursor.execute(work_query)
    records = cursor.fetchall()
    flag = 0
    for r in records:
        if street == r[0]:
            flag = 1

    if flag == 0:
        delete_query = "DELETE FROM street WHERE str_id = %s"
        cursor.execute(delete_query, (street,))
        connection.commit()

    #Обновление бокса
    combosurname.clear()
    start_query = 'SELECT DISTINCT fam_val FROM public.fam'
    cursor.execute(start_query)
    surnamerecords = cursor.fetchall()
    for rec in surnamerecords:
        combosurname.addItem(rec[0])

    comboname.clear()
    start_query = 'SELECT DISTINCT name_val FROM public.name'
    cursor.execute(start_query)
    namerecords = cursor.fetchall()
    for rec in namerecords:
        comboname.addItem(rec[0])

    combopatronymic.clear()
    start_query = 'SELECT DISTINCT otc_val FROM public.otchestvo'
    cursor.execute(start_query)
    patronymicrecords = cursor.fetchall()
    for rec in patronymicrecords:
        combopatronymic.addItem(rec[0])
    ##############################

    print("Done!")

# Привязка кнопок к функциям обработки


buttonFind.clicked.connect(on_find_click)
buttonAdd.clicked.connect(on_add_click)
buttonSave.clicked.connect(on_save_click)
buttonDelete.clicked.connect(on_delete_click)
sys.exit(app.exec_())
