import psycopg2
import tkinter as tk
from tkinter import ttk

from psycopg2 import Error


def main():
    attributes = ('fam', 'nam', 'otc', 'street')
    fams = []
    nams = []
    otcs = []
    streets = []

    # DB connect
    try:
        conn = psycopg2.connect(
            dbname="main",
            user="postgres",
            password="User2114",
            host="localhost"
        )
        if not conn.closed:
            print("Мы в системе, пора навести марафет)")
            print("Успешное подключение к базе данных PostgreSQL!")
            cur = conn.cursor()
            conn.autocommit = True
            for i in range(4):
                cur.execute(f"""select {attributes[i]} from {attributes[i]}""")
                elements = cur.fetchall()
                cur.execute(f"""select {attributes[i]}_id from {attributes[i]}""")
                ids = cur.fetchall()
                for elem in range(len(elements)):
                    elements[elem] = (elements[elem][0]).strip()
                for id in range(len(ids)):
                    ids[id] = ids[id][0]
                match i:
                    case 0:
                        for m in range(len(elements)):
                            fams.append([elements[m], ids[m]])
                    case 1:
                        for m in range(len(elements)):
                            nams.append([elements[m], ids[m]])
                    case 2:
                        for m in range(len(elements)):
                            otcs.append([elements[m], ids[m]])
                    case 3:
                        for m in range(len(elements)):
                            streets.append([elements[m], ids[m]])
        else:
            print("Не удалось установить соединение с базой данных.")
    except Error as e:
        print("Ошибка при подключении к базе данных PostgreSQL:", e)

    # Initialize window
    def init():
        window = tk.Tk()
        window.geometry("1660x480")
        window.title("DB Client")

        # Get data from TKinter entry poles
        def get_entry_data():
            data = []
            data.append(entry_fam.get())
            data.append(entry_nam.get())
            data.append(entry_otc.get())
            data.append(entry_street.get())
            data.append(entry_building.get())
            data.append(entry_apartment.get())
            data.append(entry_phone.get())
            return data

        # Insert function
        def insert_data():
            data = get_entry_data()
            flag = True
            print()
            for elem in data:
                if not elem: flag = False
            if not flag:
                print("Not all data inserted, enter all data!")
            else:
                if data[0] not in fams:
                    cur.execute(f"""insert into fam values(default, '{data[0]}')""")
                    cur.execute(f"""select fam_id from fam where fam = '{data[0]}'""")
                    fam_id = cur.fetchone()[0]
                    fams.append([data[0], fam_id])
                else:
                    cur.execute(f"""select fam_id from fam where fam = '{data[0]}'""")
                    fam_id = cur.fetchone()[0]
                print(fam_id)
                if data[1] not in nams:
                    cur.execute(f"""insert into nam values(default, '{data[1]}')""")
                    cur.execute(f"""select nam_id from nam where nam = '{data[1]}'""")
                    nam_id = cur.fetchone()[0]
                    nams.append([data[1], nam_id])
                else:
                    cur.execute(f"""select nam_id from nam where nam = '{data[1]}'""")
                    nam_id = cur.fetchone()[0]

                if data[2] not in otcs:
                    cur.execute(f"""insert into otc values(default, '{data[2]}')""")
                    cur.execute(f"""select otc_id from otc where otc = '{data[2]}'""")
                    otc_id = cur.fetchone()[0]
                    otcs.append([data[2], otc_id])
                else:
                    cur.execute(f"""select otc_id from otc where otc = '{data[2]}'""")
                    otc_id = cur.fetchone()[0]

                if data[3] not in streets:
                    cur.execute(f"""insert into street values(default, '{data[3]}')""")
                    cur.execute(f"""select street_id from street where street = '{data[3]}'""")
                    street_id = cur.fetchone()[0]
                    streets.append([data[3], street_id])
                else:
                    cur.execute(f"""select street_id from street where street = '{data[3]}'""")
                    street_id = cur.fetchone()[0]

                cur.execute(
                    f"""insert into main values(default, {fam_id}, {nam_id}, {otc_id}, {street_id}, '{data[4]}', {data[5]}, '{data[6]}')""")
                print('Succesful insert')

        # Change function
        def change_data():
            change_id = int(entry_change_id.get())
            if not change_id:
                print("Insert ID for string you want to change!")
            data = get_entry_data()
            flag = True
            print()
            for elem in data:
                if not elem: flag = False
            if not flag:
                print("Not all data inserted, enter all data!")
            else:
                if data[0] not in fams:
                    cur.execute(f"""insert into fam values(default, '{data[0]}')""")
                    cur.execute(f"""select fam_id from fam where fam = '{data[0]}'""")
                    fam_id = cur.fetchone()[0]
                    fams.append([data[0], fam_id])
                else:
                    cur.execute(f"""select fam_id from fam where fam = '{data[0]}'""")
                    fam_id = cur.fetchone()[0]
                print(fam_id)
                if data[1] not in nams:
                    cur.execute(f"""insert into nam values(default, '{data[1]}')""")
                    cur.execute(f"""select nam_id from nam where nam = '{data[1]}'""")
                    nam_id = cur.fetchone()[0]
                    nams.append([data[1], nam_id])
                else:
                    cur.execute(f"""select nam_id from nam where nam = '{data[1]}'""")
                    nam_id = cur.fetchone()[0]

                if data[2] not in otcs:
                    cur.execute(f"""insert into otc values(default, '{data[2]}')""")
                    cur.execute(f"""select otc_id from otc where otc = '{data[2]}'""")
                    otc_id = cur.fetchone()[0]
                    otcs.append([data[2], otc_id])
                else:
                    cur.execute(f"""select otc_id from otc where otc = '{data[2]}'""")
                    otc_id = cur.fetchone()[0]

                if data[3] not in streets:
                    cur.execute(f"""insert into street values(default, '{data[3]}')""")
                    cur.execute(f"""select street_id from street where street = '{data[3]}'""")
                    street_id = cur.fetchone()[0]
                    streets.append([data[3], street_id])
                else:
                    cur.execute(f"""select street_id from street where street = '{data[3]}'""")
                    street_id = cur.fetchone()[0]

                cur.execute(
                    f"""update main set fam = {fam_id}, nam = {nam_id}, otc = {otc_id}, street = {street_id}, building = '{data[4]}', appartment = {data[5]}, phone = '{data[6]}' where u_id = {change_id}""")
                print("Succesful data change")

        # Delete function
        def delete_data():
            delete_id = int(entry_delete_id.get())
            if not delete_id:
                print("Insert ID for string you want to delete!")
            cur.execute(f"""delete from main where u_id = {delete_id}""")

            print("Succesful deletion")

        # Show data function
        def get_table_data():
            print(1)
            data = []
            cur.execute("""select u_id, fam.fam, nam.nam, otc.otc,
                    street.street, building, appartment, phone from main
                    join fam on main.fam = fam_id
                    join nam on main.nam = nam_id
                    join otc on main.otc = otc_id
                    join street on main.street = street_id;""")
            rows = cur.fetchall()
            for row in rows:
                cleaned_row = [str(item).strip() for item in row]
                data.append(cleaned_row)
            print("Succesful show")
            return data

        # Show table
        def show_table():
            data = get_table_data()
            #table_window = tk.Toplevel()
            #table_window.geometry("800x600")
            #table_window.title("Data Table")

            columns = ('id', 'fam', 'nam', 'otc', 'street', 'building', 'appartment', 'phone')
            tree = ttk.Treeview(window, columns=columns, show='headings')
            #tree = ttk.Treeview(table_window, columns=columns, show='headings')
            # tree["columns"] = ("ID", "Фамилия", "Имя", "Отчество", "Улица", "Здание", "Квартира", "Телефон")

            tree.heading("id", text="ID")
            tree.heading("fam", text="Фамилия")
            tree.heading("nam", text="Имя")
            tree.heading("otc", text="Отчество")
            tree.heading("street", text="Улица")
            tree.heading("building", text="Здание")
            tree.heading("appartment", text="Квартира")
            tree.heading("phone", text="Телефон")

            #i = 0
            #for wid in (10, 70, 50, 70, 120, 30, 20, 100):
            #    tree.column(tree["columns"][i], width=wid)
            #    i += 1

            for row in data:
                tree.insert("", 'end', values=row)

            tree.pack(expand=True, fill="both")

            tree.place(x=10, y=70, width=1640, height=400)

        # Функциональные поля для ввода данных
        height = 20
        width = 100

        label_fam = tk.Label(window, text="Фамилия:")
        label_fam.pack()
        label_fam.place(x=10, y=10, width=width, height=height)
        entry_fam = tk.Entry(window)
        entry_fam.pack()
        entry_fam.place(x=10, y=30, width=width, height=height)

        label_nam = tk.Label(window, text="Имя:")
        label_nam.pack()
        label_nam.place(x=130, y=10, width=width, height=height)
        entry_nam = tk.Entry(window)
        entry_nam.pack()
        entry_nam.place(x=130, y=30, width=width, height=height)

        label_otc = tk.Label(window, text="Отчество:")
        label_otc.pack()
        label_otc.place(x=250, y=10, width=width, height=height)
        entry_otc = tk.Entry(window)
        entry_otc.pack()
        entry_otc.place(x=250, y=30, width=width, height=height)

        label_street = tk.Label(window, text="Street:")
        label_street.pack()
        label_street.place(x=370, y=10, width=width, height=height)
        entry_street = tk.Entry(window)
        entry_street.pack()
        entry_street.place(x=370, y=30, width=width, height=height)

        label_building = tk.Label(window, text="House:")
        label_building.pack()
        label_building.place(x=490, y=10, width=width, height=height)
        entry_building = tk.Entry(window)
        entry_building.pack()
        entry_building.place(x=490, y=30, width=width, height=height)

        label_apartment = tk.Label(window, text="Квартира:")
        label_apartment.pack()
        label_apartment.place(x=610, y=10, width=width, height=height)
        entry_apartment = tk.Entry(window)
        entry_apartment.pack()
        entry_apartment.place(x=610, y=30, width=width, height=height)

        label_phone = tk.Label(window, text="Телефон:")
        label_phone.pack()
        label_phone.place(x=730, y=10, width=width, height=height)
        entry_phone = tk.Entry(window)
        entry_phone.pack()
        entry_phone.place(x=730, y=30, width=width, height=height)

        # Кнопка для добавления данных в БД
        button_insert = tk.Button(window, text="Add data", command=insert_data)
        button_insert.pack()
        button_insert.place(x=850, y=30, width=width, height=height)

        # Кнопка для обновления данных в БД
        # Entry for ID to change
        label_change_id = tk.Label(window, text="ID для изменения:")
        label_change_id.pack()
        label_change_id.place(x=1020, y=10, width=width, height=height)
        entry_change_id = tk.Entry(window)
        entry_change_id.pack()
        entry_change_id.place(x=1020, y=30, width=width, height=height)

        button_change = tk.Button(window, text="Изменить данные", command=change_data)
        button_change.pack()
        button_change.place(x=1140, y=30, width=width, height=height)

        # Кнопка для удаления данных БД
        label_delete_id = tk.Label(window, text="ID для удаления:")
        label_delete_id.pack()
        label_delete_id.place(x=1310, y=10, width=width, height=height)
        entry_delete_id = tk.Entry(window)
        entry_delete_id.pack()
        entry_delete_id.place(x=1310, y=30, width=width, height=height)

        button_delete = tk.Button(window, text="Удалить данные", command=delete_data)
        button_delete.pack()
        button_delete.place(x=1430, y=30, width=width, height=height)

        # Кнопка для показа данных БД
        button_show = tk.Button(window, text="Обновить данные", command=show_table)
        button_show.pack()
        button_show.place(x=1550, y=30, width=width, height=height)

        window.mainloop()

    init()


if __name__ == "__main__":
    main()
