# -*- coding: utf-8 -*-
# @Time : 2021/6/27 16:08
# @Author : Toutoutoutouer
# @Email : wes0018@aliyun.com
import pymysql
import pyodbc
import sys

import qdarkstyle
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from add import Ui_Dialog4
from addbooks import Ui_Dialog12
from addborrow import Ui_Dialog11
from addreader import Ui_Dialog10
from ok import Ui_Dialog2
from qttext.dele import Ui_Dialog6
from qttext.delebooks import Ui_query18
from qttext.deleborrow import Ui_query17
from qttext.delereader import Ui_query16
from qttext.update import Ui_Dialog5
from qttext.updatebooks import Ui_Dialog15
from qttext.updateborrow import Ui_Dialog14
from query import Ui_Dialog3
from querybooks import Ui_query3
from queryborrow import Ui_query2
from queryreader import Ui_query
from untitled import Ui_Dialog
from updatreader import Ui_Dialog13


class Methods(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(Methods, self).__init__()
        self.setupUi(self)

    # -----------*登录函数*-----------
    def login(self):
        conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
        cursor = conn.cursor()
        sql = "SELECT * FROM login WHERE username='{}' ".format(self.lineEdit.text())
        cursor.execute(sql)
        loginpassword = cursor.fetchall()
        if loginpassword:
            if self.lineEdit_2.text() == loginpassword[0][1]:
                window.pushButton.clicked.connect(lambda: {window.close(), window2.show()})
                conn.close()
            else:
                QMessageBox.warning(self, "错误", "密码错误,请重新输入!", QMessageBox.Ok)
                conn.close()
        else:
            QMessageBox.warning(self, "错误", "找不到账号,请重新输入!", QMessageBox.Ok)
            conn.close()

    # -----------*退出函数*-----------
    def appquit(self):
        sys.exit(app.exec_())


# 主菜单界面
class Methods2(QtWidgets.QMainWindow, Ui_Dialog2):
    def __init__(self):
        super(Methods2, self).__init__()
        self.setupUi(self)

    def query(self):
        window2.pushButton.clicked.connect(lambda: {window2.close(), window3.show()})

    def add(self):
        window2.pushButton_2.clicked.connect(lambda: {window2.close(), window4.show()})

    def update(self):
        window2.pushButton_3.clicked.connect(lambda: {window2.close(), window5.show()})

    def dele(self):
        window2.pushButton_4.clicked.connect(lambda: {window2.close(), window6.show()})

    def menu(self):
        window2.pushButton_4.clicked.connect(lambda: {window2.close(), window.show()})


# 查询选择界面
class Methods3(QtWidgets.QMainWindow, Ui_Dialog3):
    def __init__(self):
        super(Methods3, self).__init__()
        self.setupUi(self)

    def queryreader(self):
        window3.pushButton.clicked.connect(lambda: {window3.close(), window7.show()})

    def queryborrow(self):
        window3.pushButton_2.clicked.connect(lambda: {window3.close(), window8.show()})

    def querybooks(self):
        window3.pushButton_3.clicked.connect(lambda: {window3.close(), window9.show()})

    def menu(self):
        window3.pushButton_4.clicked.connect(lambda: {window3.close(), window2.show()})


# 添加选择界面
class Methods4(QtWidgets.QMainWindow, Ui_Dialog4):
    def __init__(self):
        super(Methods4, self).__init__()
        self.setupUi(self)

    def addreader(self):
        window4.pushButton.clicked.connect(lambda: {window4.close(), window10.show()})

    def addborrow(self):
        window4.pushButton_2.clicked.connect(lambda: {window4.close(), window11.show()})

    def addbooks(self):
        window4.pushButton_3.clicked.connect(lambda: {window4.close(), window12.show()})

    def menu(self):
        window4.pushButton_4.clicked.connect(lambda: {window4.close(), window2.show()})


# 修改选择界面
class Methods5(QtWidgets.QMainWindow, Ui_Dialog5):
    def __init__(self):
        super(Methods5, self).__init__()
        self.setupUi(self)

    def updatereader(self):
        window5.pushButton.clicked.connect(lambda: {window5.close(), window13.show()})

    def updateborrow(self):
        window5.pushButton_2.clicked.connect(lambda: {window5.close(), window14.show()})

    def updatebooks(self):
        window5.pushButton_3.clicked.connect(lambda: {window5.close(), window15.show()})

    def menu(self):
        window5.pushButton_4.clicked.connect(lambda: {window5.close(), window2.show()})


# 删除选择界面
class Methods6(QtWidgets.QMainWindow, Ui_Dialog6):
    def __init__(self):
        super(Methods6, self).__init__()
        self.setupUi(self)

    def delereader(self):
        window6.pushButton.clicked.connect(lambda: {window6.close(), window16.show()})

    def deleborrow(self):
        window6.pushButton_2.clicked.connect(lambda: {window6.close(), window17.show()})

    def delebooks(self):
        window6.pushButton_3.clicked.connect(lambda: {window6.close(), window18.show()})

    def menu(self):
        window6.pushButton_4.clicked.connect(lambda: {window6.close(), window2.show()})


###查询按钮实现功能
class Methods7(QtWidgets.QMainWindow, Ui_query):
    def __init__(self):
        super(Methods7, self).__init__()
        self.setupUi(self)

    def query(self):
        conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
        cursor = conn.cursor()
        sql = "SELECT * FROM 读者信息 WHERE 借阅证号='{}' ".format(self.lineEdit.text())
        cursor.execute(sql)
        text = cursor.fetchall()
        if text:
            if self.lineEdit.text() == text[0][0]:
                QMessageBox.information(self, "结果", "{}".format(text), QMessageBox.Ok)
                if QMessageBox.Ok:
                    window7.close()
                    window3.show()
                conn.close()
            else:
                QMessageBox.warning(self, "错误", "密码错误,请重新输入!", QMessageBox.Ok)
                conn.close()
        else:
            QMessageBox.warning(self, "错误", "无此读者信息!", QMessageBox.Ok)
            conn.close()
            if QMessageBox.Ok:
                window7.close()
                window3.show()


class Methods8(QtWidgets.QMainWindow, Ui_query2):
    def __init__(self):
        super(Methods8, self).__init__()
        self.setupUi(self)

    def query(self):
        conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
        cursor = conn.cursor()
        sql = "SELECT * FROM 借阅信息 WHERE 借阅证号='{}' ".format(self.lineEdit.text())
        cursor.execute(sql)
        text = cursor.fetchall()
        if text:
            if self.lineEdit.text() == text[0][0]:
                QMessageBox.information(self, "结果", "{}".format(text), QMessageBox.Ok)
                if QMessageBox.Ok:
                    window8.close()
                    window3.show()
                conn.close()
            else:
                QMessageBox.warning(self, "错误", "密码错误,请重新输入!", QMessageBox.Ok)
                conn.close()
        else:
            QMessageBox.warning(self, "错误", "无此借阅信息!", QMessageBox.Ok)
            conn.close()


class Methods9(QtWidgets.QMainWindow, Ui_query3):
    def __init__(self):
        super(Methods9, self).__init__()
        self.setupUi(self)

    def query(self):
        conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
        cursor = conn.cursor()
        sql = "SELECT * FROM 图书信息 WHERE 图书编号='{}' ".format(self.lineEdit.text())
        cursor.execute(sql)
        text = cursor.fetchall()
        if text:
            if self.lineEdit.text() == text[0][0]:
                QMessageBox.information(self, "结果", "{}".format(text), QMessageBox.Ok)
                if QMessageBox.Ok:
                    window9.close()
                    window3.show()
                conn.close()
            else:
                QMessageBox.warning(self, "错误", "密码错误,请重新输入!", QMessageBox.Ok)
                conn.close()
        else:
            QMessageBox.warning(self, "错误", "无此图书信息!", QMessageBox.Ok)
            conn.close()


# 添加按钮实现功能
class Methods10(QtWidgets.QMainWindow, Ui_Dialog10):
    def __init__(self):
        super(Methods10, self).__init__()
        self.setupUi(self)

    def addreader(self):
        conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
        cursor = conn.cursor()
        sql = "SELECT * FROM 读者信息 WHERE 借阅证号='{}' ".format(self.lineEdit.text())
        cursor.execute(sql)
        stu = cursor.fetchone()
        if stu:
            QMessageBox.warning(self, "错误", "此读者已存在!", QMessageBox.Ok)
            conn.close()
            if QMessageBox.Ok:
                window12.close()
                window2.show()
        elif self.lineEdit.text():
            sql = "insert 读者信息(借阅证号,姓名,性别,单位) values('{}','{}','{}','{}')".format(self.lineEdit.text(),
                                                                                  self.lineEdit_2.text(),
                                                                                  self.lineEdit_3.text(),
                                                                                  self.lineEdit_4.text())
            cursor.execute(sql)  # 把单个学生添加到总列表中
            # 向数据库提交
            conn.commit()
            # 关闭连接
            conn.close()
            QMessageBox.information(self, "结果", "添加成功", QMessageBox.Ok)
            if QMessageBox.Ok:
                window10.close()
                window2.show()
        # 关闭连接


class Methods11(QtWidgets.QMainWindow, Ui_Dialog11):
    def __init__(self):
        super(Methods11, self).__init__()
        self.setupUi(self)

    def addborrow(self):
        conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
        cursor = conn.cursor()
        sql = "SELECT * FROM 图书信息 WHERE 图书编号='{}' ".format(self.lineEdit_2.text())
        cursor.execute(sql)
        stu = cursor.fetchone()
        if stu:
            if self.lineEdit_2.text():
                sql = "insert 借阅信息(借阅证号,图书编号) values('{}','{}')".format(self.lineEdit.text(), self.lineEdit_2.text())
                cursor.execute(sql)
                conn.commit()
                conn.close()
                QMessageBox.information(self, "结果", "添加成功", QMessageBox.Ok)
                if QMessageBox.Ok:
                    window11.close()
                    window2.show()
            else:
                QMessageBox.warning(self, "错误", "图书编号不能为空", QMessageBox.Ok)
                if QMessageBox.Ok:
                    window11.close()
                    window2.show()
                conn.close()

        else:
            QMessageBox.warning(self, "错误", "图书中无此本书", QMessageBox.Ok)
            if QMessageBox.Ok:
                window11.close()
                window2.show()
            conn.close()


class Methods12(QtWidgets.QMainWindow, Ui_Dialog12):
    def __init__(self):
        super(Methods12, self).__init__()
        self.setupUi(self)

    def addbooks(self):
        conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
        cursor = conn.cursor()
        sql = "SELECT * FROM 图书信息 WHERE 图书编号='{}' ".format(self.lineEdit.text())
        cursor.execute(sql)
        stu = cursor.fetchone()
        if stu:
            QMessageBox.warning(self, "错误", "此图书已存在!", QMessageBox.Ok)
            conn.close()
            if QMessageBox.Ok:
                window12.close()
                window2.show()
        elif self.lineEdit.text():
            sql = "insert 图书信息(图书编号,书名,作者,出版单位) values('{}','{}','{}','{}')".format(self.lineEdit.text(),
                                                                                    self.lineEdit_2.text(),
                                                                                    self.lineEdit_3.text(),
                                                                                    self.lineEdit_4.text())
            cursor.execute(sql)  # 把单个学生添加到总列表中
            # 向数据库提交
            conn.commit()
            # 关闭连接
            conn.close()
            QMessageBox.information(self, "结果", "添加成功", QMessageBox.Ok)
            if QMessageBox.Ok:
                window12.close()
                window2.show()


# 修改按钮实现功能
class Methods13(QtWidgets.QMainWindow, Ui_Dialog13):
    def __init__(self):
        super(Methods13, self).__init__()
        self.setupUi(self)

    def updatereader(self):
        conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
        cursor = conn.cursor()
        sql = "select * from 读者信息 where 借阅证号='{}'".format(self.lineEdit.text())
        cursor.execute(sql)
        stu = cursor.fetchone()
        if stu:
            sql = "update 读者信息 set 姓名='{}',性别='{}',单位='{}' where 借阅证号='{}'".format(self.lineEdit_2.text(),
                                                                                   self.lineEdit_3.text(),
                                                                                   self.lineEdit_4.text(),
                                                                                   self.lineEdit.text())
            try:
                cursor.execute(sql)
                conn.commit()
                conn.close()
                QMessageBox.information(self, "结果", "修改成功", QMessageBox.Ok)
                if QMessageBox.Ok:
                    window13.close()
                    window3.show()
            except Exception as e1:
                # 发生错误时回滚
                conn.rollback()
                conn.close()
                QMessageBox.warning(self, "错误", "修改失败!", QMessageBox.Ok)
                QMessageBox.warning(self, "错误", "{}".format(e1), QMessageBox.Ok)
            return
        QMessageBox.warning(self, "错误", "此记录不存在", QMessageBox.Ok)


class Methods14(QtWidgets.QMainWindow, Ui_Dialog14):
    def __init__(self):
        super(Methods14, self).__init__()
        self.setupUi(self)

    def updateborrow(self):
        conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
        cursor = conn.cursor()
        sql = "select * from 借阅信息 where 借阅证号='{}'".format(self.lineEdit.text())
        cursor.execute(sql)
        stu = cursor.fetchone()
        if stu:
            sql = "update 借阅信息 set 图书编号='{}' where 借阅证号='{}'".format(self.lineEdit_2.text(), self.lineEdit.text())
            try:
                cursor.execute(sql)
                conn.commit()
                conn.close()
                QMessageBox.information(self, "结果", "修改成功", QMessageBox.Ok)
                if QMessageBox.Ok:
                    window14.close()
                    window3.show()
            except Exception as e1:
                # 发生错误时回滚
                conn.rollback()
                conn.close()
                QMessageBox.warning(self, "错误", "修改失败!", QMessageBox.Ok)
                QMessageBox.warning(self, "错误", "{}".format(e1), QMessageBox.Ok)
            return
        QMessageBox.warning(self, "错误", "此记录不存在", QMessageBox.Ok)


class Methods15(QtWidgets.QMainWindow, Ui_Dialog15):
    def __init__(self):
        super(Methods15, self).__init__()
        self.setupUi(self)

    def updatebooks(self):
        conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
        cursor = conn.cursor()
        sql = "select * from 图书信息 where 图书编号='{}'".format(self.lineEdit.text())
        cursor.execute(sql)
        stu = cursor.fetchone()
        if stu:
            sql = "update 图书信息 set 书名='{}',作者='{}',出版单位='{}' where 图书编号='{}'".format(self.lineEdit_2.text(),
                                                                                     self.lineEdit_3.text(),
                                                                                     self.lineEdit_4.text(),
                                                                                     self.lineEdit.text())
            try:
                cursor.execute(sql)
                conn.commit()
                conn.close()
                QMessageBox.information(self, "结果", "修改成功", QMessageBox.Ok)
                if QMessageBox.Ok:
                    window15.close()
                    window3.show()
            except Exception as e1:
                # 发生错误时回滚
                conn.rollback()
                conn.close()
                QMessageBox.warning(self, "错误", "修改失败!", QMessageBox.Ok)
                QMessageBox.warning(self, "错误", "{}".format(e1), QMessageBox.Ok)
            return
        QMessageBox.warning(self, "错误", "此记录不存在", QMessageBox.Ok)


# 删除按钮实现功能
class Methods16(QtWidgets.QMainWindow, Ui_query16):
    def __init__(self):
        super(Methods16, self).__init__()
        self.setupUi(self)

    def delereader(self):
        conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM 读者信息 WHERE 借阅证号='{}' ".format(self.lineEdit.text()))
        stu = cursor.fetchone()
        if stu:
            cursor.execute("delete from 读者信息 where 借阅证号='{}'".format(self.lineEdit.text()))
            QMessageBox.information(self, "结果", "删除成功", QMessageBox.Ok)
            conn.commit()
            conn.close()
            if QMessageBox.Ok:
                window16.close()
                window6.show()
        else:
            QMessageBox.warning(self, "错误", "此记录不存在存在!", QMessageBox.Ok)
            if QMessageBox.Ok:
                window16.close()
                window6.show()


class Methods17(QtWidgets.QMainWindow, Ui_query17):
    def __init__(self):
        super(Methods17, self).__init__()
        self.setupUi(self)

    def deleborrow(self):
        conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM 借阅信息 WHERE 借阅证号='{}' ".format(self.lineEdit.text()))
        stu = cursor.fetchone()
        if stu:
            cursor.execute("delete from 借阅信息 where 借阅证号='{}'".format(self.lineEdit.text()))
            QMessageBox.information(self, "结果", "删除成功", QMessageBox.Ok)
            conn.commit()
            conn.close()
            if QMessageBox.Ok:
                window17.close()
                window6.show()
        else:
            QMessageBox.warning(self, "错误", "此记录不存在存在!", QMessageBox.Ok)
            if QMessageBox.Ok:
                window17.close()
                window6.show()


class Methods18(QtWidgets.QMainWindow, Ui_query18):
    def __init__(self):
        super(Methods18, self).__init__()
        self.setupUi(self)

    def delebooks(self):
        conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM 图书信息 WHERE 图书编号='{}' ".format(self.lineEdit.text()))
        stu = cursor.fetchone()
        if stu:
            cursor.execute("delete from 图书信息 where 图书编号='{}'".format(self.lineEdit.text()))
            QMessageBox.information(self, "结果", "删除成功", QMessageBox.Ok)
            conn.commit()
            conn.close()
            if QMessageBox.Ok:
                window18.close()
                window6.show()
        else:
            QMessageBox.warning(self, "错误", "此记录不存在存在!", QMessageBox.Ok)
            if QMessageBox.Ok:
                window18.close()
                window6.show()


app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet())
window = Methods()
window2 = Methods2()
window3 = Methods3()
window4 = Methods4()
window5 = Methods5()
window6 = Methods6()
window7 = Methods7()
window8 = Methods8()
window9 = Methods9()
window10 = Methods10()
window11 = Methods11()
window12 = Methods12()
window13 = Methods13()
window14 = Methods14()
window15 = Methods15()
window16 = Methods16()
window17 = Methods17()
window18 = Methods18()
window.show()
sys.exit(app.exec_())
