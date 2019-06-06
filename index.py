from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import sqlite3

from PyQt5.uic import loadUiType

ui,_=loadUiType('library.ui')

class MainApp(QMainWindow,ui):
    def __init__(self):
        QMainWindow.__init__(self)
        #self.setWindowFlags(Qt.CustomizeWindowHint)    //Makes the window borderless
        self.setupUi(self)
        self.handle_buttons()
        self.handle_transitions()
        self.publs_showal()
        self.catgs_showal()
        self.auths_showal()
        self.books_showal()
        self.publs_combos()
        self.catgs_combos()
        self.auths_combos()

    def handle_buttons(self):
        self.btn_opers.clicked.connect(self.act_opers)
        self.btn_books.clicked.connect(self.act_books)
        self.btn_users.clicked.connect(self.act_users)
        self.btn_thems.clicked.connect(self.act_thems)
        self.btn_mesgs.clicked.connect(self.act_mesgs)
        self.btn_stats.clicked.connect(self.act_stats)
        self.btn_catgs.clicked.connect(self.act_catgs)
        self.btn_auths.clicked.connect(self.act_auths)
        self.btn_publs.clicked.connect(self.act_publs)
        self.btn_hdocs.clicked.connect(self.act_hdocs)
        self.add_catgs.clicked.connect(self.catgs_addnew)
        self.add_auths.clicked.connect(self.auths_addnew)
        self.add_publs.clicked.connect(self.publs_addnew)
        self.add_books.clicked.connect(self.books_addnew)

    def handle_transitions(self):
        self.MainMenu.tabBar().setVisible(False)

########### MAIN UI TABS ###########

    def act_opers(self):
        self.MainMenu.setCurrentIndex(0)

    def act_books(self):
        self.MainMenu.setCurrentIndex(1)
        pass

    def act_users(self):
        self.MainMenu.setCurrentIndex(2)
        pass

    def act_catgs(self):
        self.MainMenu.setCurrentIndex(3)
        pass

    def act_auths(self):
        self.MainMenu.setCurrentIndex(4)
        pass

    def act_publs(self):
        self.MainMenu.setCurrentIndex(5)
        pass

    def act_mesgs(self):
        self.MainMenu.setCurrentIndex(6)
        pass

    def act_stats(self):
        self.MainMenu.setCurrentIndex(7)
        pass

    def act_thems(self):
        self.MainMenu.setCurrentIndex(8)
        pass

    def act_hdocs(self):
        self.MainMenu.setCurrentIndex(9)
        pass

########### MAIN UI TABS ###########

########### <BOOKS MENU> ###########

    def books_addnew(self):
        rental_rate=0
        self.db = sqlite3.connect('database/main.db')
        self.cur = self.db.cursor()
        book_name = self.book_add_name.text()
        book_accn = self.book_add_accn.text()
        book_cost = self.book_add_cost.text()
        book_rent = self.book_add_rent.text()
        book_catg = self.book_add_catg.currentIndex()
        book_publ = self.book_add_publ.currentIndex()
        book_auth = self.book_add_auth.currentIndex()
        book_desc = self.book_add_desc.toPlainText()
        try:
            if int(book_rent)<1 or int(book_rent)>5:
                self.book_add_rent.clear()
                self.statusBar().showMessage("Invalid archive rental value!", msecs=5000)
            else:
                print("insert into books(book_accn, book_name, book_desc, book_catg, book_publ, book_auth, book_cost, book_rent) values ("+str(book_accn)+", '"+str(book_name)+"', '"+str(book_desc)+"', "+str(book_catg)+", "+str(book_publ)+", "+str(book_auth)+", "+str(book_cost)+", "+str(book_rent)+")")
                self.cur.execute("insert into books(book_accn, book_name, book_desc, book_catg, book_publ, book_auth, book_cost, book_rent) values ("+str(book_accn)+", '"+str(book_name)+"', '"+str(book_desc)+"', "+str(book_catg)+", "+str(book_publ)+", "+str(book_auth)+", "+str(book_cost)+", "+str(book_rent)+")")
                self.db.commit()
                self.book_add_name.clear()
                self.book_add_accn.clear()
                self.book_add_cost.clear()
                self.book_add_rent.clear()
                self.book_add_catg.setCurrentIndex(0)
                self.book_add_publ.setCurrentIndex(0)
                self.book_add_auth.setCurrentIndex(0)
                self.book_add_desc.clear()
                self.books_showal()
                self.statusBar().showMessage("New archive has been added successfully!", msecs=5000)
        except Exception as e:
            print(e)
            error_mesg="Adding new category has failed due to "+str(e)
            self.statusBar().showMessage(error_mesg,msecs=5000)
        pass

    def books_showal(self):
        self.db = sqlite3.connect('database/main.db')
        self.cur = self.db.cursor()
        self.cur.execute("select * from books")
        data=self.cur.fetchall()
        if data:
            self.show_all_books.setRowCount(0)
            self.show_all_books.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.show_all_books.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.show_all_books.rowCount()
                self.show_all_books.insertRow(row_position)
        pass

    def books_search(self):
        pass

    def books_mkedit(self):
        pass

    def books_delete(self):
        pass

########### <BOOKS MENU> ###########

########### <USERS MENU> ###########

    def users_addnew(self):
        pass

    def users_login(self):
        pass

    def users_mkedit(self):
        pass

########### <USERS MENU> ###########

########### <CATGS MENU> ###########

    def catgs_addnew(self):
        self.db = sqlite3.connect('database/main.db')
        self.cur = self.db.cursor()
        catg_idno=self.catg_add_idno.text()
        print(catg_idno)
        catg_name=self.catg_add_name.text()
        print(catg_name)
        catg_desc=self.catg_add_desc.toPlainText()
        print(catg_desc)
        try:
            self.cur.execute("insert into categories (catg_idno,catg_name,catg_desc) values ("+str(catg_idno)+", '"+catg_name+"', '"+catg_desc+"')")
            self.db.commit()
            print("Command Executed!")
            print("insert into categories (catg_idno,catg_name,catg_desc) values ("+str(catg_idno)+", '"+catg_name+"', '"+catg_desc+"')")
            self.statusBar().showMessage("New category has been added successfully!",msecs=5000)
            self.catg_add_idno.clear()
            self.catg_add_name.clear()
            self.catg_add_desc.clear()
            self.catgs_showal()
            self.catgs_combos()
        except Exception as e:
            print(e)
            error_mesg="Adding new category has failed due to "+str(e)
            self.statusBar().showMessage(error_mesg,msecs=5000)
        pass

    def catgs_showal(self):
        self.db = sqlite3.connect('database/main.db')
        self.cur = self.db.cursor()
        self.cur.execute("select * from categories")
        data=self.cur.fetchall()
        if data:
            self.show_all_catgs.setRowCount(0)
            self.show_all_catgs.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.show_all_catgs.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.show_all_catgs.rowCount()
                self.show_all_catgs.insertRow(row_position)
        pass

    def catgs_combos(self):
        self.db = sqlite3.connect('database/main.db')
        self.cur = self.db.cursor()
        self.cur.execute("select catg_name from categories")
        data=self.cur.fetchall()
        self.book_add_catg.clear()
        for item in data:
            #print(item[0])
            self.book_add_catg.addItem(item[0])
        pass

    def catgs_modify(self):
        pass

    def catgs_remove(self):
        pass

########### <CATGS MENU> ###########

########### <AUTHS MENU> ###########

    def auths_addnew(self):
        self.db = sqlite3.connect('database/main.db')
        self.cur = self.db.cursor()
        auth_idno=self.auth_add_idno.text()
        auth_name=self.auth_add_name.text()
        auth_desc=self.auth_add_desc.toPlainText()
        try:
            self.cur.execute("insert into authors (auth_idno,auth_name,auth_desc) values ("+str(auth_idno)+", '"+auth_name+"', '"+auth_desc+"')")
            self.db.commit()
            print("Command Executed!")
            print("insert into authors (auth_idno,auth_name,auth_desc) values ("+str(auth_idno)+", '"+auth_name+"', '"+auth_desc+"')")
            self.statusBar().showMessage("New author data has been added successfully!",msecs=5000)
            self.auth_add_idno.clear()
            self.auth_add_name.clear()
            self.auth_add_desc.clear()
            self.auths_showal()
            self.auths_combos()
        except Exception as e:
            print(e)
            error_mesg="Adding new author data has failed due to "+str(e)
            self.statusBar().showMessage(error_mesg,msecs=5000)
        pass

    def auths_showal(self):
        self.db = sqlite3.connect('database/main.db')
        self.cur = self.db.cursor()
        self.cur.execute("select * from authors")
        data=self.cur.fetchall()
        if data:
            self.show_all_auths.setRowCount(0)
            self.show_all_auths.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.show_all_auths.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.show_all_auths.rowCount()
                self.show_all_auths.insertRow(row_position)
        pass

    def auths_combos(self):
        self.db = sqlite3.connect('database/main.db')
        self.cur = self.db.cursor()
        self.cur.execute("select auth_name from authors")
        data=self.cur.fetchall()
        self.book_add_auth.clear()
        for item in data:
            #print(item[0])
            self.book_add_auth.addItem(item[0])
        pass

    def auths_modify(self):
        pass

    def auths_remove(self):
        pass

########### <AUTHS MENU> ###########

########### <PUBLS MENU> ###########

    def publs_addnew(self):
        self.db = sqlite3.connect('database/main.db')
        self.cur = self.db.cursor()
        publ_idno=self.publ_add_idno.text()
        publ_name=self.publ_add_name.text()
        publ_desc=self.publ_add_desc.toPlainText()
        try:
            self.cur.execute("insert into publishers (publ_idno,publ_name,publ_desc) values ("+str(publ_idno)+", '"+publ_name+"', '"+publ_desc+"')")
            self.db.commit()
            print("Command Executed!")
            print("insert into publishers (publ_idno,publ_name,publ_desc) values ("+str(publ_idno)+", '"+publ_name+"', '"+publ_desc+"')")
            self.statusBar().showMessage("New publisher data has been added successfully!",msecs=5000)
            self.publ_add_idno.clear()
            self.publ_add_name.clear()
            self.publ_add_desc.clear()
            self.publs_showal()
            self.publs_combos()
        except Exception as e:
            print(e)
            error_mesg="Adding new publisher data has failed due to "+str(e)
            self.statusBar().showMessage(error_mesg,msecs=5000)
        pass

    def publs_showal(self):
        self.db = sqlite3.connect('database/main.db')
        self.cur = self.db.cursor()
        self.cur.execute("select * from publishers")
        data=self.cur.fetchall()
        if data:
            self.show_all_publs.setRowCount(0)
            self.show_all_publs.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.show_all_publs.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.show_all_publs.rowCount()
                self.show_all_publs.insertRow(row_position)
        pass

    def publs_combos(self):
        self.db = sqlite3.connect('database/main.db')
        self.cur = self.db.cursor()
        self.cur.execute("select publ_name from publishers")
        data=self.cur.fetchall()
        self.book_add_publ.clear()
        for item in data:
            #print(item[0])
            self.book_add_publ.addItem(item[0])
        pass

    def publs_modify(self):
        pass

    def publs_remove(self):
        pass

########### <PUBLS MENU> ###########

def main():
    app=QApplication(sys.argv)
    window=MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()