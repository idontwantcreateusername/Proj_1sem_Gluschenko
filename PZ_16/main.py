import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#ff00ff', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="BD/11.png")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить клиента', command=self.open_dialog, bg='#5da130', bd=0,
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="BD/12.png")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="BD/13.png")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.del_rec, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="BD/14.png")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="BD/15.png")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#5da130',
                                bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('user_id', 'sn', 'nm', 'fn', 'ppay', 'ppy', 'lod', 'crd', 'ttl'),
                                 height=15, show='headings')

        self.tree.column('user_id', width=50, anchor=tk.CENTER)
        self.tree.column('sn', width=180, anchor=tk.CENTER)
        self.tree.column('nm', width=180, anchor=tk.CENTER)
        self.tree.column('fn', width=180, anchor=tk.CENTER)
        self.tree.column('ppay', width=70, anchor=tk.CENTER)
        self.tree.column('ppy', width=70, anchor=tk.CENTER)
        self.tree.column('lod', width=120, anchor=tk.CENTER)
        self.tree.column('crd', width=70, anchor=tk.CENTER)
        self.tree.column('ttl', width=70, anchor=tk.CENTER)

        self.tree.heading('user_id', text='Код клиента')
        self.tree.heading('sn', text='Фамилия')
        self.tree.heading('nm', text='Имя')
        self.tree.heading('fn', text='Отчество')
        self.tree.heading('ppay', text='Периодический платёж')
        self.tree.heading('ppy', text='Годовой %')
        self.tree.heading('lod', text='Срок вклада')
        self.tree.heading('crd', text='Пластиковая карта')
        self.tree.heading('ttl', text='Конечная сумма')

        self.tree.pack()

    def records(self, user_id, sn, nm, fn, ppay, ppy, lod, crd, ttl):
        self.db.insert_data(user_id, sn, nm, fn, ppay, ppy, lod, crd, ttl)
        self.view_records()

    def update_record(self, user_id, sn, nm, fn, ppay, ppy, lod, crd, ttl):
        self.db.cur.execute(
            """UPDATE users SET sn=?, nm=?, fn=?, ppay=?, ppy=?, lod=?, crd=?, ttl=? WHERE user_id=?""",
            (sn, nm, fn, ppay, ppy, lod, crd, ttl, user_id))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self, uid):
        self.db.cur.execute("""DELETE FROM users WHERE user_id=?""", uid)
        self.db.con.commit()
        self.view_records()

    # def search_records(self, user_id):
    #     user_id = ("%" + user_id + "%",)
    #     self.db.cur.execute("""SELECT * FROM users WHERE name LIKE ?""", user_id)
    #     [self.tree.delete(i) for i in self.tree.get_children()]
    #     [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def search_records(self, score):
        score = (score, )
        self.db.cur.execute("""SELECT * FROM users WHERE sn=?""", score)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def del_rec(self):
        DelRec()

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить клиентта')
        self.geometry('400x300+400+300')
        self.resizable(False, False)

        label_id = tk.Label(self, text='Номер')
        label_id.place(x=50, y=25)
        self.entry_id = ttk.Entry(self)
        self.entry_id.place(x=200, y=25)

        label_sn = tk.Label(self, text='Фамилия')
        label_sn.place(x=50, y=50)
        self.entry_sn = ttk.Entry(self)
        self.entry_sn.place(x=200, y=50)

        label_name = tk.Label(self, text='Имя')
        label_name.place(x=50, y=75)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=75)

        label_fn = tk.Label(self, text='Отчество')
        label_fn.place(x=50, y=100)
        self.entry_fn = ttk.Entry(self)
        self.entry_fn.place(x=200, y=100)

        label_ppay = tk.Label(self, text='Периодический платёж')
        label_ppay.place(x=50, y=125)
        self.entry_ppay = ttk.Entry(self)
        self.entry_ppay.place(x=200, y=125)

        label_ppy = tk.Label(self, text='Годовой %')
        label_ppy.place(x=50, y=150)
        self.entry_ppy = ttk.Entry(self)
        self.entry_ppy.place(x=200, y=150)

        label_lod = tk.Label(self, text='Срок вклада')
        label_lod.place(x=50, y=175)
        self.entry_lod = ttk.Entry(self)
        self.entry_lod.place(x=200, y=175)

        label_crd = tk.Label(self, text='Есть карта?')
        label_crd.place(x=50, y=200)
        self.combobox = ttk.Combobox(self, values=[u'Есть', u'Нет'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=200)

        label_ttl = tk.Label(self, text='Итог')
        label_ttl.place(x=50, y=225)
        self.entry_ttl = ttk.Entry(self)
        self.entry_ttl.place(x=200, y=225)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=260)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=260)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_id.get(),
                                                                       self.entry_sn.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_fn.get(),
                                                                       self.entry_ppay.get(),
                                                                       self.entry_ppy.get(),
                                                                       self.entry_lod.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_ttl.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=260)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_id.get(),
                                                                          self.entry_sn.get(),
                                                                          self.entry_name.get(),
                                                                          self.entry_fn.get(),
                                                                          self.entry_ppay.get(),
                                                                          self.entry_ppy.get(),
                                                                          self.entry_lod.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_ttl.get()))
        self.btn_ok.destroy()


class DelRec(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_del()
        self.view = app

    def init_del(self):
        self.title("Удаление")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="удалить")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.delete_records(self.entry_search.get()))


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        with sq.connect('BD/saper.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                sn TEXT NOT NULL,
                nm TEXT NOT NULL,
                fn TEXT NOT NULL,
                ppay REAL NOT NULL DEFAULT 1,
                ppy REAL,
                lod TEXT,
                crd INTEGER,
                ttl INTEGER
                )""")

    def insert_data(self, user_id, sn, nm, fn, ppay, ppy, lod, crd, ttl):
        self.cur.execute(
            """INSERT INTO users(user_id, sn, nm, fn, ppay, ppy, lod, crd, ttl) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (user_id, sn, nm, fn, ppay, ppy, lod, crd, ttl))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Финтех на минималках")
    root.geometry("995x450+300+200")
    root.resizable(False, False)
    root.mainloop()
